# -*- coding: utf-8 -*-
"""Placa informativă publicitară pentru sediul GAL (Anexa la contract „Materiale și activități publicitare” V3, A-(2)).

Pornește de la modelul oficial AFIR „A.2 – Placă FEADR LEADER” V3 (70 × 50 cm), scoate doar liniile punctate ale câmpurilor
de completat și scrie în locul lor datele proiectului, cu fontul Carlito (echivalentul metric liber al lui Calibri):
negru pe fond alb, alb în casetele albastre. Restul modelului rămâne neatins („nu se aplică soluții creative”)."""
import pathlib, shutil
import pymupdf

ROOT = pathlib.Path(__file__).resolve().parent.parent            # interventia5/comunicare
MODEL = ROOT.parent / 'surse' / 'afir_modele' / 'A.2-ModelAFIR_PLACA_FEADR_LEADER_v3.pdf'
FONTS = ROOT / 'assets' / 'fonts'
OUT = ROOT / 'placa'

NEGRU, ALB = (0, 0, 0), (1, 1, 1)

# ---------------------------------------------------------------- datele proiectului (din contract și CF)
DATE = dict(
    titlu='EDUCAȚIE PENTRU MEDIU ÎN TERITORIUL GAL NAPOCA POROLISSUM – MICRO-GRANTURI PENTRU MEDIU',
    cod='C36010804713061304413',
    judet='Cluj',
    localitate='Gilău, Aghireșu, Beliș, Călățele, Căpușu Mare, Huedin, Izvoru Crișului, Măguri-Răcătău, Mănăstireni, '
               'Mărgău, Mărișel, Râșca, Săcuieu, Sâncraiu',
    beneficiar='ASOCIAȚIA GRUPUL DE ACȚIUNE LOCALĂ NAPOCA POROLISSUM',
    valoare='138.643,00',
    nerambursabil='138.643,00',
    proiectant='Nu este cazul',
    executant='ASOCIAȚIA GRUPUL DE ACȚIUNE LOCALĂ NAPOCA POROLISSUM',
    demarare=('08', '09', '2026'),
    finalizare=('07', '06', '2028'),
)

# ---------------------------------------------------------------- geometria câmpurilor din model (puncte PDF, origine stânga-sus)
# fiecare câmp: (x0, x1, liste de baseline-uri ale rândurilor punctate)
CAMPURI = dict(
    titlu=(78, 1126, [614, 668]),        # 2 rânduri, sub eticheta de deasupra (cele 3 rânduri punctate acoperă 575–680)
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
DEM_Y, FIN_Y = 1178, 1250


def zone_puncte(page):
    """Dreptunghiurile care acoperă exact rândurile de puncte (fiecare punct ≈ 6,5 × 6,8 pt)."""
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
        for r in rs[1:] + [None]:                     # segmente separate acolo unde e o etichetă între puncte
            if r is not None and r.x0 - seg[-1].x1 < 15:
                seg.append(r); continue
            if len(seg) >= 5:
                zones.append(pymupdf.Rect(min(q.x0 for q in seg) - 1, min(q.y0 for q in seg) - 1,
                                          max(q.x1 for q in seg) + 1, max(q.y1 for q in seg) + 1))
            if r is not None: seg = [r]
    return zones


def rupe(font, text, size, width):
    """Împarte textul pe rânduri care încap în lățimea dată."""
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


def build():
    OUT.mkdir(parents=True, exist_ok=True)
    doc = pymupdf.open(MODEL)
    page = doc[0]

    # 1) scoatem doar liniile punctate (desenele acoperite complet); casetele, etichetele și barele oblice rămân
    for z in zone_puncte(page):
        page.add_redact_annot(z)
    page.apply_redactions(images=pymupdf.PDF_REDACT_IMAGE_NONE,
                          graphics=pymupdf.PDF_REDACT_LINE_ART_REMOVE_IF_COVERED,
                          text=pymupdf.PDF_REDACT_TEXT_NONE)

    # 2) fonturi
    page.insert_font(fontname='CarlitoB', fontfile=str(FONTS / 'Carlito-Bold.ttf'))
    page.insert_font(fontname='CarlitoR', fontfile=str(FONTS / 'Carlito-Regular.ttf'))
    fB = pymupdf.Font(fontfile=str(FONTS / 'Carlito-Bold.ttf'))
    fR = pymupdf.Font(fontfile=str(FONTS / 'Carlito-Regular.ttf'))

    def scrie(camp, text, color, max_size, font='B', max_lines=None, center=False, line_gap=None):
        x0, x1, ys = CAMPURI[camp]
        f = fB if font == 'B' else fR
        n = max_lines or len(ys)
        size, lines = potriveste(f, text, x1 - x0 - 4, n, max_size)
        if line_gap:                                   # rânduri proprii (câmp cu un singur rând punctat)
            base = ys[-1]
            ys = [base - line_gap * (len(lines) - 1 - i) for i in range(len(lines))]
        for y, l in zip(ys, lines):
            x = x0 + 2 if not center else x0 + (x1 - x0 - f.text_length(l, fontsize=size)) / 2
            page.insert_text((x, y), l, fontname='Carlito' + font, fontsize=size, color=color)
        return size, lines

    rap = {}
    rap['titlu'] = scrie('titlu', DATE['titlu'], NEGRU, 46, max_lines=2)
    rap['cod'] = scrie('cod', DATE['cod'], ALB, 46)
    rap['judet'] = scrie('judet', DATE['judet'], NEGRU, 42)
    # localitățile: Gilău primul (ponderea cea mai mare în CF), apoi celelalte; până la 3 rânduri în spațiul câmpului
    rap['localitate'] = scrie('localitate', DATE['localitate'], NEGRU, 42, font='R', max_lines=3, line_gap=21)
    rap['beneficiar'] = scrie('beneficiar', DATE['beneficiar'], NEGRU, 44)
    rap['proiectant'] = scrie('proiectant', DATE['proiectant'], NEGRU, 38)
    rap['executant'] = scrie('executant', DATE['executant'], NEGRU, 38)
    rap['valoare'] = scrie('valoare', DATE['valoare'], ALB, 50, center=True)
    rap['nerambursabil'] = scrie('nerambursabil', DATE['nerambursabil'], ALB, 50, center=True)
    for camp, y in (('demarare', DEM_Y), ('finalizare', FIN_Y)):
        for (x0, x1), part in zip(CAMPURI[camp], DATE[camp]):
            w = fB.text_length(part, fontsize=46)
            page.insert_text((x0 + (x1 - x0 - w) / 2, y), part, fontname='CarlitoB', fontsize=46, color=ALB)

    pdf = OUT / 'Placa_informativa_sediu_GAL_70x50cm.pdf'
    doc.save(pdf, garbage=3, deflate=True)
    d2 = pymupdf.open(pdf)
    d2[0].get_pixmap(dpi=100).save(OUT / 'Placa_informativa_sediu_GAL_previzualizare.png')
    return pdf, rap


if __name__ == '__main__':
    pdf, rap = build()
    print(pdf)
    for k, (s, ls) in rap.items():
        print(f'{k:14s} {s:5.1f} pt  {ls}')
