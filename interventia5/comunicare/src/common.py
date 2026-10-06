# -*- coding: utf-8 -*-
"""Elemente comune pentru materialele de comunicare ale proiectului
„Educație pentru mediu în teritoriul GAL Napoca Porolissum – micro-granturi pentru mediu”.

Randare: HTML/SVG -> PDF cu Chromium headless -> PNG/SVG cu PyMuPDF.
"""
import os, subprocess, pathlib, base64
import pymupdf

ROOT = pathlib.Path(__file__).resolve().parent.parent          # interventia5/comunicare
ASSETS = ROOT / 'assets'
SIGLE = ASSETS / 'sigle_oficiale'
FONTS = ASSETS / 'fonts'
BUILD = ROOT / 'src' / '_build'
CHROME = os.environ.get('CHROME', '/opt/pw-browsers/chromium-1194/chrome-linux/chrome')

# ---------------------------------------------------------------- paleta
VERDE = '#4FAB50'        # verde GAL (manual GAL)
VERDE_TEXT = '#3B8F3E'   # verde GAL ușor închis, pentru text mare pe alb
VERDE_INCHIS = '#2E6B31'
VERDE_CRUD = '#8DC63F'
MARO = '#3D2E31'         # maro GAL (manual GAL)
SOARE = '#F6B93B'
CREM = '#F7F3EA'
GRI = '#6E6266'

# ---------------------------------------------------------------- date proiect (din CF / contract)
TITLU = 'Educație pentru mediu în teritoriul GAL Napoca Porolissum – micro-granturi pentru mediu'
CONTRACT = 'C 36010804713061304413 / 08.09.2026'
BENEFICIAR = 'Asociația Grupul de Acțiune Locală Napoca Porolissum'
VALOARE = '138.643 euro'
PLAFON = '19.833,3 €'
SITE = 'www.napocaporolissum.ro'
EMAIL = 'contact@napocaporolissum.ro'
TELEFON = '0728 146 123'
ADRESA = 'str. Eroilor nr. 6, bl. I1, ap. 1, parter, Gilău, jud. Cluj'
LOCALITATI = ['Aghireșu', 'Beliș', 'Călățele', 'Căpușu Mare', 'Gilău', 'Huedin', 'Izvoru Crișului',
              'Măguri-Răcătău', 'Mănăstireni', 'Mărgău', 'Mărișel', 'Râșca', 'Săcuieu', 'Sâncraiu']

# Mențiunile obligatorii (Anexa II la contract, C1.1-6)
MENTIUNI = ('Proiect finanțat cu fonduri europene nerambursabile prin Planul Strategic PAC 2023 – 2027 (PS 2023 – 2027). '
            'PS 2023 – 2027 este implementat de Agenția pentru Finanțarea Investițiilor Rurale, din subordinea Ministerului '
            'Agriculturii și Dezvoltării Rurale. PS 2023 – 2027 este finanțat de Uniunea Europeană și Guvernul României prin '
            'Fondul european agricol pentru dezvoltare rurală.')
DATE_PROIECT = (f'Proiect: „{TITLU}” · Beneficiar: {BENEFICIAR} · Contract de finanțare {CONTRACT} · '
                f'Valoarea totală eligibilă: {VALOARE}, din care finanțare nerambursabilă PS 2023 – 2027: {VALOARE}.')


def uri(path):
    return pathlib.Path(path).resolve().as_uri()


def font_css():
    """Instanțe statice (generate din fonturile variabile) - Chromium le încorporează în PDF ca TrueType, nu Type 3."""
    st = FONTS / 'static'
    faces = [f"@font-face {{ font-family: 'Montserrat'; src: url('{uri(st / f'Montserrat-{w}.ttf')}') format('truetype'); font-weight: {w}; font-style: normal; }}"
             for w in (400, 500, 600, 700, 800)]
    faces.append(f"@font-face {{ font-family: 'Caveat'; src: url('{uri(st / 'Caveat-700.ttf')}') format('truetype'); font-weight: 400 700; }}")
    return '\n'.join(faces) + '\n'


def page_html(body, width, height, unit='mm', extra_css=''):
    """Document HTML de o pagină (sau mai multe .page) cu dimensiunea dată."""
    return f"""<!doctype html><html lang="ro"><head><meta charset="utf-8">
<style>
{font_css()}
@page {{ size: {width}{unit} {height}{unit}; margin: 0; }}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
html, body {{ -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
body {{ font-family: 'Montserrat', sans-serif; color: {MARO}; }}
.page {{ width: {width}{unit}; height: {height}{unit}; position: relative; overflow: hidden; page-break-after: always; }}
.page:last-child {{ page-break-after: auto; }}
{extra_css}
</style></head><body>{body}</body></html>"""


def render_pdf(html, out_pdf):
    BUILD.mkdir(parents=True, exist_ok=True)
    out_pdf = pathlib.Path(out_pdf); out_pdf.parent.mkdir(parents=True, exist_ok=True)
    src = BUILD / (out_pdf.stem + '.html')
    src.write_text(html, encoding='utf-8')
    cmd = [CHROME, '--headless=new', '--no-sandbox', '--disable-gpu', '--allow-file-access-from-files',
           '--run-all-compositor-stages-before-draw', '--virtual-time-budget=15000',
           '--no-pdf-header-footer', f'--print-to-pdf={out_pdf}', src.as_uri()]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=180)
    return out_pdf


def pdf_to_png(pdf, out_png, width_px=None, dpi=None, page=0, clip_mm=None, alpha=False):
    d = pymupdf.open(pdf); p = d[page]
    rect = p.rect
    if clip_mm:  # tăiere margine (de ex. bleed de 3 mm)
        m = clip_mm * 72 / 25.4
        rect = pymupdf.Rect(rect.x0 + m, rect.y0 + m, rect.x1 - m, rect.y1 - m)
    if width_px:
        z = width_px / rect.width
    else:
        z = (dpi or 150) / 72
    pix = p.get_pixmap(matrix=pymupdf.Matrix(z, z), clip=rect, alpha=alpha)
    pathlib.Path(out_png).parent.mkdir(parents=True, exist_ok=True)
    pix.save(out_png)
    return out_png


def pdf_to_svg(pdf, out_svg, page=0):
    d = pymupdf.open(pdf)
    svg = d[page].get_svg_image(text_as_path=True)
    pathlib.Path(out_svg).write_text(svg, encoding='utf-8')
    return out_svg


def img(path, css='', alt=''):
    return f'<img src="{uri(path)}" style="{css}" alt="{alt}">'


def svg_inline(path):
    """SVG oficial inclus ca imagine (păstrează vectorii la tipar)."""
    return uri(path)


# ---------------------------------------------------------------- bara de sigle (GIV AFIR V3, cap. 3)
def bara_sigle(h, gap=None, leader=True, leader_h=None, align='space-between', fundal='#fff', pad='0', split=None, row_gap=None):
    """Rândul principal: UE (Cofinanțat) · MADR · PS 2023-2027 · GAL · AFIR, toate la aceeași înălțime h.
    LEADER pe un rând separat (GIV V3, cap. 2.G). Pe formatele înguste, split=3 împarte rândul principal
    în 3 + 2 sigle, păstrând ordinea de citire. h, gap: șiruri CSS (ex. '11mm')."""
    gap = gap or f'calc({h} / 3)'
    row_gap = row_gap or f'calc({h} / 3)'
    leader_h = leader_h or h
    sig = [('eu_cofinantat.svg', 'Cofinanțat de Uniunea Europeană'), ('madr.svg', 'Guvernul României – MADR'),
           ('ps.svg', 'Planul Strategic PAC 2023-2027'), ('gal_color.png', 'GAL Napoca Porolissum'), ('afir.svg', 'AFIR')]
    imgs = [f'<img src="{uri(SIGLE / f)}" alt="{a}" style="height:{h};width:auto;display:block">' for f, a in sig]
    groups = [imgs] if not split else [imgs[:split], imgs[split:]]
    rows = ''.join(f'<div style="display:flex;align-items:center;justify-content:{align if len(g) > 2 else "flex-start"};gap:{gap};'
                   f'margin-top:{"0" if i == 0 else row_gap}">{"".join(g)}</div>' for i, g in enumerate(groups))
    row2 = (f'<div style="display:flex;margin-top:{row_gap}"><img src="{uri(SIGLE / "leader.svg")}" alt="LEADER" '
            f'style="height:{leader_h};width:auto;display:block"></div>') if leader else ''
    return f'<div class="bara-sigle" style="background:{fundal};padding:{pad}">{rows}{row2}</div>'
