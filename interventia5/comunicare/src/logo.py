# -*- coding: utf-8 -*-
"""Logo-ul proiectului: o carte deschisă din care crește un mugur, cu soarele în fundal.
Cartea = educația; mugurele = mediul; micro-grantul = sămânța care pornește creșterea.
"""
from common import *

SCHEME = {
    # pagini carte, linie pagini, tulpină, frunză stânga, frunză dreapta, mugur, soare, text 1, text 2, subtitlu
    'color': dict(pag=MARO, linie=CREM, tulp='#2E7D32', f1=VERDE, f2=VERDE_CRUD, mug=VERDE, soare=SOARE,
                  t1=MARO, t2=VERDE_TEXT, t3=GRI, nerv='#FFFFFF'),
    'alb':   dict(pag='#FFFFFF', linie=VERDE_INCHIS, tulp='#FFFFFF', f1='#FFFFFF', f2='#FFFFFF', mug='#FFFFFF',
                  soare=SOARE, t1='#FFFFFF', t2='#FFFFFF', t3='#FFFFFF', nerv=VERDE_INCHIS),
    'mono':  dict(pag=MARO, linie='#FFFFFF', tulp=MARO, f1=MARO, f2=MARO, mug=MARO, soare='#B9AFB1',
                  t1=MARO, t2=MARO, t3=MARO, nerv='#FFFFFF'),
}


def simbol(v='color'):
    c = SCHEME[v]
    return f"""
  <circle cx="141" cy="50" r="21" fill="{c['soare']}"/>
  <path d="M100 146 C 100 122, 95 104, 100 80" fill="none" stroke="{c['tulp']}" stroke-width="6.5" stroke-linecap="round"/>
  <path d="M99 116 C 86 95, 62 87, 43 93 C 51 115, 76 124, 99 116 Z" fill="{c['f1']}"/>
  <path d="M97 114 C 82 103, 66 98, 52 97" fill="none" stroke="{c['nerv']}" stroke-width="2" stroke-linecap="round" opacity=".75"/>
  <path d="M100 92 C 110 67, 135 56, 159 60 C 152 85, 127 98, 100 92 Z" fill="{c['f2']}"/>
  <path d="M103 89 C 117 79, 133 71, 150 66" fill="none" stroke="{c['nerv']}" stroke-width="2" stroke-linecap="round" opacity=".75"/>
  <path d="M100 82 C 94 71, 96 59, 104 51 C 109 62, 107 74, 100 82 Z" fill="{c['mug']}"/>
  <path d="M100 145 C 78 129, 48 125, 20 131 L 20 157 C 48 151, 78 156, 100 172 Z" fill="{c['pag']}"/>
  <path d="M100 145 C 122 129, 152 125, 180 131 L 180 157 C 152 151, 122 156, 100 172 Z" fill="{c['pag']}"/>
  <path d="M93 151 C 76 141, 52 138, 30 141" fill="none" stroke="{c['linie']}" stroke-width="2.4" stroke-linecap="round" opacity=".9"/>
  <path d="M107 151 C 124 141, 148 138, 170 141" fill="none" stroke="{c['linie']}" stroke-width="2.4" stroke-linecap="round" opacity=".9"/>
  <path d="M100 145 L 100 172" stroke="{c['linie']}" stroke-width="2.4" opacity=".9"/>
"""


def lockup_orizontal(v='color'):
    c = SCHEME[v]
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 200" width="760" height="200">
<g>{simbol(v)}</g>
<text x="212" y="92" font-family="Montserrat" font-weight="800" font-size="66" fill="{c['t1']}" letter-spacing="-1">Educație</text>
<text x="214" y="157" font-family="Montserrat" font-weight="700" font-size="50" fill="{c['t2']}" letter-spacing="-0.5">pentru mediu</text>
<text x="216" y="189" font-family="Montserrat" font-weight="600" font-size="15.5" fill="{c['t3']}" letter-spacing="2.6">MICRO-GRANTURI · GAL NAPOCA POROLISSUM</text>
</svg>"""


def lockup_vertical(v='color'):
    c = SCHEME[v]
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 400" width="460" height="400">
<g transform="translate(130 0) scale(1)">{simbol(v)}</g>
<text x="230" y="262" text-anchor="middle" font-family="Montserrat" font-weight="800" font-size="62" fill="{c['t1']}" letter-spacing="-1">Educație</text>
<text x="230" y="326" text-anchor="middle" font-family="Montserrat" font-weight="700" font-size="48" fill="{c['t2']}" letter-spacing="-0.5">pentru mediu</text>
<text x="230" y="364" text-anchor="middle" font-family="Montserrat" font-weight="600" font-size="14.5" fill="{c['t3']}" letter-spacing="2.4">MICRO-GRANTURI · GAL NAPOCA POROLISSUM</text>
</svg>"""


def simbol_svg(v='color'):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="10 20 180 162" width="180" height="162">{simbol(v)}</svg>'


def build(out_dir):
    out_dir.mkdir(parents=True, exist_ok=True)
    made = []
    for name, fn, w, h in [('orizontal', lockup_orizontal, 760, 200), ('vertical', lockup_vertical, 460, 400),
                           ('simbol', simbol_svg, 180, 162)]:
        for v in ('color', 'alb', 'mono'):
            svg = fn(v)
            bg = VERDE_INCHIS if v == 'alb' else 'transparent'
            html = page_html(f'<div class="page" style="background:transparent">{svg}</div>', w, h, unit='px',
                             extra_css='svg{display:block;width:100%;height:100%}')
            pdf = BUILD / f'logo_{name}_{v}.pdf'
            render_pdf(html, pdf)
            base = out_dir / f'logo_proiect_{name}_{v}'
            pdf_to_svg(pdf, str(base) + '.svg')
            pdf_to_png(pdf, str(base) + '.png', width_px=w * 4, alpha=True)
            import shutil; shutil.copy(pdf, str(base) + '.pdf')
            made.append(base)
    return made


if __name__ == '__main__':
    for b in build(ROOT / 'logo'):
        print(b.name)
