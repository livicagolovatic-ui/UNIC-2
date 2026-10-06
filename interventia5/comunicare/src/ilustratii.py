# -*- coding: utf-8 -*-
"""Ilustrații vectoriale proprii: peisajul Apusenilor și iconițele pentru tipurile de inițiative eligibile."""
from common import *


def peisaj(w=1200, h=520, soare=True, cer=None, id_='p'):
    """Dealuri în straturi, brazi, soare. Se scalează pe lățime (preserveAspectRatio slice)."""
    cer_rect = f'<rect width="1200" height="520" fill="{cer}"/>' if cer else ''
    sun = f'<circle cx="930" cy="250" r="100" fill="{SOARE}" opacity=".2"/><circle cx="930" cy="250" r="74" fill="{SOARE}"/>' if soare else ''
    def brad(x, y, s, col):
        return (f'<g transform="translate({x} {y}) scale({s})" fill="{col}">'
                f'<polygon points="0,-60 18,-30 10,-30 26,-6 12,-6 30,18 -30,18 -12,-6 -26,-6 -10,-30 -18,-30"/>'
                f'<rect x="-4" y="18" width="8" height="12"/></g>')
    brazi_dep = ''.join(brad(x, y, s, '#7FB46A') for x, y, s in
                        [(120, 300, .55), (160, 292, .7), (205, 304, .5), (690, 270, .6), (730, 262, .75), (1040, 290, .55), (1080, 282, .7)])
    brazi_ap = ''.join(brad(x, y, s, VERDE_INCHIS) for x, y, s in
                       [(70, 400, 1.0), (125, 410, .8), (330, 392, .9), (980, 380, 1.05), (1040, 392, .85), (1125, 384, 1.0)])
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 520" width="{w}" height="{h}" preserveAspectRatio="xMidYMax slice">
{cer_rect}{sun}
<path d="M0 300 C 150 230, 260 250, 380 210 C 500 170, 600 230, 720 200 C 850 165, 980 220, 1200 190 L1200 520 L0 520Z" fill="#D7EBCB"/>
<path d="M0 330 C 120 290, 240 300, 360 270 C 480 240, 560 300, 700 280 C 860 255, 960 300, 1200 260 L1200 520 L0 520Z" fill="#B7DA98"/>
{brazi_dep}
<path d="M0 380 C 160 340, 300 370, 450 345 C 610 318, 720 375, 880 350 C 1010 330, 1100 360, 1200 340 L1200 520 L0 520Z" fill="{VERDE_CRUD}"/>
<path d="M0 430 C 180 395, 330 430, 520 410 C 700 390, 820 440, 1000 420 C 1100 410, 1160 420, 1200 415 L1200 520 L0 520Z" fill="{VERDE}"/>
{brazi_ap}
<path d="M0 480 C 200 455, 420 490, 640 470 C 860 450, 1020 485, 1200 468 L1200 520 L0 520Z" fill="{VERDE_INCHIS}"/>
</svg>"""


# ---------------------------------------------------------------- iconițe 64x64, desenate într-o singură culoare (c) + fundal (b)
def _ico(body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">{body}</svg>'

ICON_LABEL = {
    'plantare': 'Plantări de arbori',
    'reciclare': 'Reciclare și colectare selectivă',
    'ecologizare': 'Ecologizare',
    'apa': 'Protecția apei',
    'aer': 'Aer curat',
    'padure': 'Păduri',
    'biodiversitate': 'Biodiversitate',
    'clima': 'Schimbări climatice',
    'transport': 'Transport cu emisii scăzute',
    'energie': 'Resurse regenerabile',
    'teatru': 'Teatru și scenete',
    'pictura': 'Pictură în școli',
    'afterschool': 'Cluburi after-school',
    'sport': 'Sport pentru natură',
    'drona': 'Concursuri cu drone',
    'echipamente': 'Echipamente pentru mediu',
    'scoala': 'Grădinițe, școli, licee',
    'ong': 'ONG-uri de mediu',
    'comunitate': 'Proiecte comunitare',
    'voluntariat': 'Voluntariat',
    'carte': 'Plan de intervenție',
    'interviu': 'Interviu',
    'consiliere': 'Consiliere',
    'online': 'Depunere online',
    'calendar': 'Calendar',
    'contract': 'Contract de grant',
    'ora': 'Ora',
    'loc': 'Locul',
}


def icon(name, c=VERDE_INCHIS, b='#FFFFFF'):
    sw = 'stroke-width="5" stroke-linecap="round" stroke-linejoin="round"'
    I = {
    'plantare': f'<path d="M10 54 Q32 42 54 54Z" fill="{c}"/><path d="M32 50 V28" stroke="{c}" {sw} fill="none"/>'
                f'<path d="M31 34 C22 32 15 25 14 15 C24 16 31 23 31 34Z" fill="{c}"/><path d="M33 30 C36 21 44 15 52 16 C51 25 43 31 33 30Z" fill="{c}"/>',
    'reciclare': f'<path d="M20 20 A17 17 0 0 1 47 22" stroke="{c}" {sw} fill="none"/><path d="M50 13 L50 26 L38 24Z" fill="{c}"/>'
                 f'<path d="M48 40 A17 17 0 0 1 22 47" stroke="{c}" {sw} fill="none"/><path d="M15 52 L14 39 L27 41Z" fill="{c}"/>'
                 '',
    'ecologizare': f'<path d="M18 22 H46 L42 56 H22Z" fill="{c}"/><rect x="14" y="15" width="36" height="6" rx="3" fill="{c}"/><rect x="27" y="9" width="10" height="6" rx="2" fill="{c}"/>'
                   f'<path d="M28 28 V48 M36 28 V48" stroke="{b}" stroke-width="3" stroke-linecap="round"/>',
    'apa': f'<path d="M32 6 C25 18 14 29 14 40 A18 18 0 0 0 50 40 C50 29 39 18 32 6Z" fill="{c}"/>'
           f'<path d="M23 42 A9 9 0 0 0 31 50" stroke="{b}" stroke-width="3.5" fill="none" stroke-linecap="round"/>',
    'aer': f'<path d="M8 24 H40 A7 7 0 1 0 33 17" stroke="{c}" {sw} fill="none"/><path d="M8 35 H48 A7 7 0 1 1 41 42" stroke="{c}" {sw} fill="none"/><path d="M8 46 H28" stroke="{c}" {sw}/>',
    'padure': f'<polygon points="32,5 46,25 39,25 52,42 36,42 36,58 28,58 28,42 12,42 25,25 18,25" fill="{c}"/>',
    'biodiversitate': f'<ellipse cx="22" cy="24" rx="12" ry="14" transform="rotate(-25 22 24)" fill="{c}"/><ellipse cx="42" cy="24" rx="12" ry="14" transform="rotate(25 42 24)" fill="{c}"/>'
                      f'<ellipse cx="24" cy="44" rx="8" ry="10" transform="rotate(25 24 44)" fill="{c}"/><ellipse cx="40" cy="44" rx="8" ry="10" transform="rotate(-25 40 44)" fill="{c}"/>'
                      f'<rect x="29.5" y="18" width="5" height="36" rx="2.5" fill="{b}"/><rect x="30.5" y="19" width="3" height="34" rx="1.5" fill="{c}"/>'
                      f'<path d="M31 18 C29 12 26 9 22 8 M33 18 C35 12 38 9 42 8" stroke="{c}" stroke-width="2.5" fill="none" stroke-linecap="round"/>',
    'clima': f'<path d="M26 12 A6 6 0 0 1 38 12 V36 A12 12 0 1 1 26 36Z" fill="{c}"/><circle cx="32" cy="46" r="6" fill="{b}"/>'
             f'<path d="M32 18 V40" stroke="{b}" stroke-width="4" stroke-linecap="round"/><path d="M44 16 H52 M44 24 H50 M44 32 H52" stroke="{c}" stroke-width="3.5" stroke-linecap="round"/>',
    'transport': f'<circle cx="16" cy="42" r="10" stroke="{c}" {sw} fill="none"/><circle cx="48" cy="42" r="10" stroke="{c}" {sw} fill="none"/>'
                 f'<path d="M16 42 L25 24 H41 L48 42 M25 24 L32 42 L41 24 M22 18 H30 M41 24 L39 16 H46" stroke="{c}" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>',
    'energie': f'<circle cx="22" cy="20" r="8" fill="{c}"/><path d="M22 4 V8 M22 32 V36 M6 20 H10 M34 20 H38 M11 9 L13.5 11.5 M30.5 28.5 L33 31 M11 31 L13.5 28.5 M30.5 11.5 L33 9" stroke="{c}" stroke-width="3" stroke-linecap="round"/>'
               f'<path d="M30 58 L36 38 H58 L52 58Z" fill="{c}"/><path d="M41 39 L37 57 M48 39 L44 57 M34 48 H55" stroke="{b}" stroke-width="2"/>',
    'teatru': f'<path d="M12 12 H44 V28 A16 16 0 0 1 12 28Z" fill="{c}"/><circle cx="21" cy="22" r="3.2" fill="{b}"/><circle cx="35" cy="22" r="3.2" fill="{b}"/>'
              f'<path d="M20 32 Q28 39 36 32" stroke="{b}" stroke-width="3" fill="none" stroke-linecap="round"/>'
              f'<path d="M30 32 H54 V44 A12 12 0 0 1 30 44Z" fill="{c}" stroke="{b}" stroke-width="2.5"/><path d="M36 50 Q42 45 48 50" stroke="{b}" stroke-width="2.5" fill="none" stroke-linecap="round"/>'
              f'<circle cx="37" cy="39" r="2.3" fill="{b}"/><circle cx="47" cy="39" r="2.3" fill="{b}"/>',
    'pictura': f'<path d="M32 8 C16 8 6 20 6 32 C6 46 18 56 30 56 C36 56 37 50 34 47 C31 44 33 39 38 39 H45 C53 39 58 34 58 27 C58 16 46 8 32 8Z" fill="{c}"/>'
               f'<circle cx="19" cy="27" r="4.5" fill="{b}"/><circle cx="28" cy="17" r="4.5" fill="{b}"/><circle cx="41" cy="17" r="4.5" fill="{b}"/><circle cx="19" cy="41" r="4.5" fill="{b}"/>',
    'afterschool': f'<rect x="8" y="14" width="48" height="32" rx="3" fill="{c}"/><path d="M18 26 C22 22 26 30 30 26 S38 22 42 26" stroke="{b}" stroke-width="3" fill="none" stroke-linecap="round"/>'
                   f'<path d="M18 36 H34" stroke="{b}" stroke-width="3" stroke-linecap="round"/><path d="M22 46 L18 58 M42 46 L46 58" stroke="{c}" {sw}/>',
    'sport': f'<circle cx="32" cy="32" r="24" fill="{c}"/><path d="M32 18 L42 25 L38 37 H26 L22 25Z" fill="{b}"/>'
             f'<path d="M32 18 V9 M42 25 L52 21 M38 37 L44 47 M26 37 L20 47 M22 25 L12 21" stroke="{b}" stroke-width="3" stroke-linecap="round"/>',
    'drona': f'<rect x="24" y="26" width="16" height="12" rx="4" fill="{c}"/><path d="M24 28 L14 18 M40 28 L50 18 M24 36 L14 46 M40 36 L50 46" stroke="{c}" stroke-width="4" stroke-linecap="round"/>'
             f'<ellipse cx="14" cy="16" rx="10" ry="3" fill="{c}"/><ellipse cx="50" cy="16" rx="10" ry="3" fill="{c}"/><ellipse cx="14" cy="48" rx="10" ry="3" fill="{c}"/><ellipse cx="50" cy="48" rx="10" ry="3" fill="{c}"/>'
             f'<circle cx="32" cy="32" r="3" fill="{b}"/>',
    'echipamente': f'<rect x="8" y="24" width="48" height="30" rx="4" fill="{c}"/><path d="M24 24 V17 A3 3 0 0 1 27 14 H37 A3 3 0 0 1 40 17 V24" stroke="{c}" {sw} fill="none"/>'
                   f'<path d="M8 36 H56" stroke="{b}" stroke-width="3"/><rect x="28" y="32" width="8" height="8" rx="1.5" fill="{b}"/>',
    'scoala': f'<path d="M6 26 L32 10 L58 26Z" fill="{c}"/><rect x="11" y="28" width="42" height="26" fill="{c}"/><rect x="27" y="38" width="10" height="16" fill="{b}"/>'
              f'<rect x="16" y="34" width="7" height="7" fill="{b}"/><rect x="41" y="34" width="7" height="7" fill="{b}"/><circle cx="32" cy="20" r="3" fill="{b}"/>',
    'ong': f'<path d="M32 54 C12 41 8 29 14 20 C20 12 29 14 32 21 C35 14 44 12 50 20 C56 29 52 41 32 54Z" fill="{c}"/>'
           f'<path d="M32 26 V44 M32 36 C27 34 24 30 24 25 M32 32 C37 30 40 26 40 22" stroke="{b}" stroke-width="3" fill="none" stroke-linecap="round"/>',
    'comunitate': f'<circle cx="32" cy="18" r="8" fill="{c}"/><path d="M18 46 A14 14 0 0 1 46 46Z" fill="{c}"/>'
                  f'<circle cx="13" cy="26" r="6" fill="{c}"/><path d="M2 50 A11 11 0 0 1 22 44 L20 50Z" fill="{c}"/>'
                  f'<circle cx="51" cy="26" r="6" fill="{c}"/><path d="M62 50 A11 11 0 0 0 42 44 L44 50Z" fill="{c}"/>',
    'voluntariat': f'<path d="M6 40 H16 L28 46 H42 C46 46 46 52 42 52 H28 M16 40 V58 M6 58 H16 M42 52 L54 46 C58 44 60 50 56 52 L40 60 H16" stroke="{c}" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
                   f'<path d="M36 36 C24 28 22 21 26 16 C29 12 34 13 36 17 C38 13 43 12 46 16 C50 21 48 28 36 36Z" fill="{c}"/>',
    'carte': f'<path d="M32 16 C24 10 14 9 6 11 V50 C14 48 24 49 32 55 Z" fill="{c}"/><path d="M32 16 C40 10 50 9 58 11 V50 C50 48 40 49 32 55 Z" fill="{c}"/>'
             f'<path d="M32 18 V54" stroke="{b}" stroke-width="2.5"/><path d="M12 22 C18 21 23 22 27 24 M12 31 C18 30 23 31 27 33 M37 24 C41 22 46 21 52 22 M37 33 C41 31 46 30 52 31" stroke="{b}" stroke-width="2.2" stroke-linecap="round"/>',
    'interviu': f'<path d="M6 12 H40 V36 H20 L10 44 V36 H6Z" fill="{c}"/><path d="M26 40 H58 V58 H52 V64 L44 58 H26Z" fill="{c}" stroke="{b}" stroke-width="2.5"/>'
                f'<path d="M13 20 H33 M13 28 H27" stroke="{b}" stroke-width="3" stroke-linecap="round"/>',
    'consiliere': f'<circle cx="22" cy="20" r="9" fill="{c}"/><path d="M6 54 A16 16 0 0 1 38 54Z" fill="{c}"/>'
                  f'<path d="M38 8 H60 V26 H48 L42 32 V26 H38Z" fill="{c}"/><path d="M45 15 H54 M45 20 H51" stroke="{b}" stroke-width="2.5" stroke-linecap="round"/>',
    'online': f'<rect x="6" y="10" width="52" height="34" rx="3" fill="{c}"/><rect x="10" y="14" width="44" height="26" fill="{b}"/>'
              f'<path d="M32 36 V20 M25 26 L32 19 L39 26" stroke="{c}" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/><path d="M20 54 H44 M28 44 L26 54 M36 44 L38 54" stroke="{c}" stroke-width="4" stroke-linecap="round"/>',
    'calendar': f'<rect x="8" y="12" width="48" height="44" rx="5" fill="{c}"/><rect x="12" y="24" width="40" height="28" rx="2" fill="{b}"/>'
                f'<path d="M20 8 V18 M44 8 V18" stroke="{c}" {sw}/><path d="M18 32 H24 M30 32 H36 M42 32 H46 M18 42 H24 M30 42 H36" stroke="{c}" stroke-width="4" stroke-linecap="round"/>',
    'ora': f'<circle cx="32" cy="32" r="25" fill="{c}"/><circle cx="32" cy="32" r="19" fill="{b}"/><path d="M32 19 V32 L41 38" stroke="{c}" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>',
    'loc': f'<path d="M32 60 C32 60 12 38 12 25 A20 20 0 0 1 52 25 C52 38 32 60 32 60Z" fill="{c}"/><circle cx="32" cy="25" r="8" fill="{b}"/>',
    'contract': f'<path d="M14 6 H40 L52 18 V58 H14Z" fill="{c}"/><path d="M40 6 V18 H52" fill="{b}" opacity=".6"/>'
                f'<path d="M21 26 H44 M21 34 H44 M21 42 H34" stroke="{b}" stroke-width="3" stroke-linecap="round"/><path d="M34 50 C38 46 40 52 44 48 S48 50 50 49" stroke="{b}" stroke-width="2.5" fill="none" stroke-linecap="round"/>',
    }
    return _ico(I[name])


if __name__ == '__main__':
    cells = ''.join(f'<div style="width:46mm;text-align:center;margin:3mm 0"><div style="width:20mm;height:20mm;margin:0 auto">{icon(n)}</div>'
                    f'<div style="font-size:8pt;font-weight:600;margin-top:2mm">{n}</div></div>' for n in ICON_LABEL)
    body = (f'<div class="page" style="padding:8mm"><div style="height:60mm;margin-bottom:6mm;border-radius:4mm;overflow:hidden;background:{CREM}">'
            f'{peisaj("100%", "100%")}</div><div style="display:flex;flex-wrap:wrap">{cells}</div></div>')
    pdf = render_pdf(page_html(body, 210, 297, extra_css='svg{display:block;width:100%;height:100%}'), BUILD / 'test_ilustratii.pdf')
    pdf_to_png(pdf, BUILD / 'test_ilustratii.png', dpi=90)
    print('ok')
