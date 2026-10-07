# -*- coding: utf-8 -*-
"""Placa informativă publicitară pentru sediul GAL (Anexa la contract „Materiale și activități publicitare” V3, A-(2)).

Pornește de la modelul oficial AFIR „A.2 – Placă FEADR LEADER” V3 (70 × 50 cm) și scoate doar liniile punctate ale
câmpurilor de completat; restul modelului rămâne neatins („nu se aplică soluții creative”).

Fișierul final e un PowerPoint de 70 × 50 cm: modelul curățat ca fundal (vectorial, SVG, cu PNG de rezervă) și textele
proiectului în **Calibri**, cum cere anexa: negru pe fond alb, alb în casetele albastre. Calibri e un font Microsoft, licențiat,
care nu există în acest mediu; PDF-ul de tipar se exportă din PowerPoint, unde Calibri este instalat odată cu Office.
Calculele de lățime se fac cu Carlito, echivalentul metric al lui Calibri (lățimi identice), deci rândurile și centrările sunt
aceleași. Previzualizarea PNG e randată tot cu Carlito."""
import json, os, pathlib, shutil, subprocess, zipfile
import pymupdf

ROOT = pathlib.Path(__file__).resolve().parent.parent            # interventia5/comunicare
SRC = ROOT / 'src'
MODEL = ROOT.parent / 'surse' / 'afir_modele' / 'A.2-ModelAFIR_PLACA_FEADR_LEADER_v3.pdf'
FONTS = ROOT / 'assets' / 'fonts'
OUT = ROOT / 'placa'
BUILD = SRC / '_build'

NEGRU, ALB = (0, 0, 0), (1, 1, 1)

# ---------------------------------------------------------------- datele proiectului
DATE = dict(
    titlu='EDUCAȚIE PENTRU MEDIU ÎN TERITORIUL GAL NAPOCA POROLISSUM – MICRO-GRANTURI PENTRU MEDIU',   # ca în contract
    cod='F36010804713061304413',                    # codul cererii de finanțare atribuit de AFIR (confirmat de GAL, 07.10.2026)
    judet='Cluj',
    localitate='Gilău, Aghireșu, Beliș, Călățele, Căpușu Mare, Huedin, Izvoru Crișului, Măguri-Răcătău, Mănăstireni, '
               'Mărgău, Mărișel, Râșca, Săcuieu, Sâncraiu',   # Gilău primul: ponderea cea mai mare în CF (9%)
    beneficiar='ASOCIAȚIA GRUPUL DE ACȚIUNE LOCALĂ NAPOCA POROLISSUM',
    valoare='138.643,00',
    nerambursabil='138.643,00',
    proiectant='Nu este cazul',
    executant='ASOCIAȚIA GRUPUL DE ACȚIUNE LOCALĂ NAPOCA POROLISSUM',
    demarare=('08', '09', '2026'),                  # data semnării contractului
    finalizare=('08', '06', '2028'),                # 21 de luni de la 08.09.2026 (termen pe luni: ziua corespunzătoare)
)

# ---------------------------------------------------------------- geometria câmpurilor din model (puncte PDF, origine stânga-sus)
CAMPURI = dict(
    titlu=(78, 1126, [614, 668]),        # 2 rânduri, sub eticheta de deasupra (rândurile punctate acoperă 575–680)
    cod=(276, 1111, [761]),
    judet=(172, 512, [839]),
    localitate=(715, 1126, [839]),
    beneficiar=(277, 1119, [941, 1001]),
    proiectant=(1413, 1938, [977, 1022]),
    executant=(1412, 1938, [1070, 1115]),
    valoare=(723, 1043, [1130]),
    nerambursabil=(723, 1043, [1244]),
    demarare=[(1449, 1552), (1587, 1725), (1760, 1900)],
    finalizare=[(1450, 1553), (1588, 1726), (1761, 1901)],
)
DATE_Y = dict(demarare=1178, finalizare=1250)

F_BOLD = pymupdf.Font(fontfile=str(FONTS / 'Carlito-Bold.ttf'))     # metric identic cu Calibri Bold
F_REG = pymupdf.Font(fontfile=str(FONTS / 'Carlito-Regular.ttf'))   # metric identic cu Calibri


def zone_puncte(page):
    """Dreptunghiurile care acoperă exact segmentele de puncte (fiecare punct ≈ 6,5 × 6,8 pt), fără etichetele dintre ele."""
    rows = {}
    for g in page.get_drawings():
        r = g['rect']
        if r.height < 12 and r.width < 14:
            rows.setdefault(round(r.y1 / 3) * 3, []).append(r)
    zones = []
    for y, rs in rows.items():
        if len(rs) < 20:
            continue
        rs.sort(key=lambda r: r.x0)
        seg = [rs[0]]
        for r in rs[1:] + [None]:
            if r is not None and r.x0 - seg[-1].x1 < 15:
                seg.append(r); continue
            if len(seg) >= 5:
                zones.append(pymupdf.Rect(min(q.x0 for q in seg) - 1, min(q.y0 for q in seg) - 1,
                                          max(q.x1 for q in seg) + 1, max(q.y1 for q in seg) + 1))
            if r is not None: seg = [r]
    return zones


def rupe(font, text, size, width):
    lines, cur = [], ''
    for w in text.split(' '):
        t = (cur + ' ' + w).strip()
        if font.text_length(t, fontsize=size) <= width or not cur:
            cur = t
        else:
            lines.append(cur); cur = w
    lines.append(cur)
    return lines


def potriveste(font, text, width, max_lines, max_size, min_size=12):
    s = max_size
    while s >= min_size:
        ls = rupe(font, text, s, width)
        if len(ls) <= max_lines and all(font.text_length(l, fontsize=s) <= width for l in ls):
            return s, ls
        s -= 0.5
    raise ValueError(f'Textul nu încape: {text[:40]}')


def layout():
    """Lista rândurilor de text: poziția stânga, linia de bază, corpul literei, culoarea, grosimea."""
    items = []

    def camp(nume, max_size, bold=True, culoare=NEGRU, max_lines=None, center=False, line_gap=None):
        x0, x1, ys = CAMPURI[nume]
        f = F_BOLD if bold else F_REG
        size, lines = potriveste(f, DATE[nume], x1 - x0 - 4, max_lines or len(ys), max_size)
        if line_gap:
            ys = [ys[-1] - line_gap * (len(lines) - 1 - i) for i in range(len(lines))]
        for y, l in zip(ys, lines):
            w = f.text_length(l, fontsize=size)
            x = x0 + (x1 - x0 - w) / 2 if center else x0 + 2
            items.append(dict(camp=nume, text=l, x=round(x, 2), y=y, w=round(w, 2), size=size, bold=bold, color=culoare))

    camp('titlu', 46, max_lines=2)
    camp('cod', 46, culoare=ALB)
    camp('judet', 42)
    camp('localitate', 42, bold=False, max_lines=3, line_gap=21)
    camp('beneficiar', 44)
    camp('proiectant', 38)
    camp('executant', 38)
    camp('valoare', 50, culoare=ALB, center=True)
    camp('nerambursabil', 50, culoare=ALB, center=True)
    for nume in ('demarare', 'finalizare'):
        for (x0, x1), part in zip(CAMPURI[nume], DATE[nume]):
            w = F_BOLD.text_length(part, fontsize=46)
            items.append(dict(camp=nume, text=part, x=round(x0 + (x1 - x0 - w) / 2, 2), y=DATE_Y[nume], w=round(w, 2),
                              size=46, bold=True, color=ALB))
    return items


def fundal():
    """Modelul AFIR fără liniile punctate: PDF, SVG (vectorial, pentru PowerPoint) și PNG 200 dpi (rezervă)."""
    BUILD.mkdir(parents=True, exist_ok=True)
    doc = pymupdf.open(MODEL)
    page = doc[0]
    for z in zone_puncte(page):
        page.add_redact_annot(z)
    page.apply_redactions(images=pymupdf.PDF_REDACT_IMAGE_NONE,
                          graphics=pymupdf.PDF_REDACT_LINE_ART_REMOVE_IF_COVERED,
                          text=pymupdf.PDF_REDACT_TEXT_NONE)
    pdf = BUILD / 'placa_fundal.pdf'
    doc.save(pdf, garbage=3, deflate=True)
    d = pymupdf.open(pdf)
    (BUILD / 'placa_fundal.svg').write_text(d[0].get_svg_image(text_as_path=True), encoding='utf-8')
    d[0].get_pixmap(dpi=200).save(BUILD / 'placa_fundal.png')
    return pdf, d[0].rect


def previzualizare(fundal_pdf, items):
    doc = pymupdf.open(fundal_pdf); page = doc[0]
    page.insert_font(fontname='CB', fontfile=str(FONTS / 'Carlito-Bold.ttf'))
    page.insert_font(fontname='CR', fontfile=str(FONTS / 'Carlito-Regular.ttf'))
    for it in items:
        page.insert_text((it['x'], it['y']), it['text'], fontname='CB' if it['bold'] else 'CR', fontsize=it['size'], color=it['color'])
    qa = BUILD / 'placa_previzualizare_carlito.pdf'
    doc.save(qa, garbage=3, deflate=True)
    pymupdf.open(qa)[0].get_pixmap(dpi=100).save(OUT / 'Placa_informativa_sediu_GAL_previzualizare.png')
    return qa


def pptx(items, rect):
    spec = dict(width_pt=rect.width, height_pt=rect.height,
                svg=str(BUILD / 'placa_fundal.svg'), png=str(BUILD / 'placa_fundal.png'),
                out=str(OUT / 'Placa_informativa_sediu_GAL_70x50cm_Calibri.pptx'), items=items)
    (BUILD / 'placa_layout.json').write_text(json.dumps(spec, ensure_ascii=False, indent=1), encoding='utf-8')
    env = dict(os.environ)
    subprocess.run(['node', str(SRC / 'placa_pptx.js'), str(BUILD / 'placa_layout.json')], check=True, env=env)
    # pptxgenjs pune un PNG gol ca rezervă pentru SVG; îl înlocuim cu fundalul randat (pentru PowerPoint fără suport SVG)
    out = pathlib.Path(spec['out']); tmp = out.with_suffix('.tmp')
    with zipfile.ZipFile(out) as zin, zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as zout:
        for n in zin.namelist():
            data = zin.read(n)
            if n.startswith('ppt/media/') and n.endswith('.png'):
                data = pathlib.Path(spec['png']).read_bytes()
            zout.writestr(zin.getinfo(n), data)
    tmp.replace(out)
    return out


def build():
    OUT.mkdir(parents=True, exist_ok=True)
    fpdf, rect = fundal()
    items = layout()
    previzualizare(fpdf, items)
    out = pptx(items, rect)
    vechi = OUT / 'Placa_informativa_sediu_GAL_70x50cm.pdf'      # versiunea cu Carlito nu mai e fișier de tipar
    if vechi.exists(): vechi.unlink()
    return out, items


if __name__ == '__main__':
    out, items = build()
    print(out)
    for it in items:
        print(f"{it['camp']:13s} {it['size']:5.1f}pt  y={it['y']}  {it['text']}")
