# -*- coding: utf-8 -*-
"""Fișa de identitate vizuală a proiectului (A4 orizontal, 2 pagini)."""
from componente import *

W, H = 297, 210


def cmyk(hexc):
    r, g, b = (int(hexc[i:i + 2], 16) / 255 for i in (1, 3, 5))
    k = 1 - max(r, g, b)
    if k >= 1: return (0, 0, 0, 100)
    c, m, y = ((1 - x - k) / (1 - k) for x in (r, g, b))
    return tuple(round(v * 100) for v in (c, m, y, k))


CULORI = [('Verde GAL', VERDE, 'culoarea principală (manualul GAL)', (54, 0, 53, 33)),
          ('Maro GAL', MARO, 'titluri și text (manualul GAL)', (0, 27, 20, 77)),
          ('Verde pădure', VERDE_INCHIS, 'fundaluri, benzi', None),
          ('Verde crud', VERDE_CRUD, 'accente, frunza din logo', None),
          ('Galben soare', SOARE, 'evidențieri: sume, date', None),
          ('Crem hârtie', CREM, 'fundal cald', None)]

CSS = BASE_CSS + f"""
.pg {{ padding:13mm 15mm; }}
h1 {{ font-size:22pt; font-weight:800; letter-spacing:-.4pt; }}
h2 {{ font-size:11.5pt; font-weight:800; margin-bottom:3mm; color:{VERDE_INCHIS}; text-transform:uppercase; letter-spacing:1pt; }}
.box {{ background:{CREM}; border-radius:4mm; padding:4mm; }}
.lbl {{ font-size:7.4pt; color:{GRI}; margin-top:2mm; text-align:center; }}
.txt {{ font-size:8.6pt; line-height:1.45; }}
.sw {{ border-radius:3mm; overflow:hidden; background:#fff; }}
.sw .c {{ height:18mm; }}
.sw .d {{ padding:2.2mm 2.6mm; font-size:7.2pt; line-height:1.4; }}
.rule {{ display:flex; gap:2.4mm; font-size:8.3pt; line-height:1.4; margin-bottom:2mm; }}
.ok:before {{ content:'✓'; color:{VERDE_TEXT}; font-weight:800; }}
.no:before {{ content:'✕'; color:#B3261E; font-weight:800; }}
"""


def pagina1():
    return f"""
<div class="page pg" style="background:#fff">
  <div style="display:flex;justify-content:space-between;align-items:flex-end">
    <div><h1>Identitatea vizuală a proiectului</h1>
      <div class="txt" style="color:{GRI}">„{TITLU}” · contract {CONTRACT}</div></div>
    <div class="hand" style="font-size:19pt;color:{VERDE_INCHIS};white-space:nowrap">{TAGLINE}</div>
  </div>
  <div style="display:grid;grid-template-columns:1.25fr 1fr;gap:8mm;margin-top:5mm">
    <div>
      <h2>Logo-ul</h2>
      <div class="box" style="display:flex;align-items:center;justify-content:center;height:42mm">
        <div class="logo-h" style="width:105mm">{lockup_orizontal('color')}</div></div>
      <div class="lbl">Varianta principală, orizontală</div>
      <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:4mm;margin-top:3mm">
        <div><div class="box" style="height:33mm;display:flex;align-items:center;justify-content:center"><div class="logo-v" style="width:34mm">{lockup_vertical('color')}</div></div><div class="lbl">Verticală</div></div>
        <div><div class="box" style="height:33mm;display:flex;align-items:center;justify-content:center;background:{VERDE_INCHIS}"><div class="logo-v" style="width:34mm">{lockup_vertical('alb')}</div></div><div class="lbl">Pe fundal închis</div></div>
        <div><div class="box" style="height:33mm;display:flex;align-items:center;justify-content:center"><div class="logo-v" style="width:34mm">{lockup_vertical('mono')}</div></div><div class="lbl">Monocromă (tipar alb-negru)</div></div>
      </div>
    </div>
    <div>
      <h2>Ideea</h2>
      <div style="display:flex;gap:5mm;align-items:center">
        <div class="svgfill" style="width:34mm;height:31mm;flex:none">{simbol_svg('color')}</div>
        <div class="txt"><b>Cartea deschisă</b> este educația. <b>Mugurele</b> care crește din ea este mediul și comunitatea care învață
          să-l protejeze. <b>Soarele</b> este energia ideilor locale. Micro-grantul e sămânța: mic, dar pune lucrurile în mișcare.</div>
      </div>
      <div class="txt" style="margin-top:4mm">Culorile vin din manualul GAL Napoca Porolissum (verde #4FAB50 și maro #3D2E31), ca proiectul
        să fie recunoscut imediat ca parte din familia GAL.</div>
      <h2 style="margin-top:6mm">Reguli de folosire</h2>
      <div class="rule"><span class="ok"></span><span>Spațiu liber în jurul logo-ului: cel puțin înălțimea literei „E” din „Educație”.</span></div>
      <div class="rule"><span class="ok"></span><span>Dimensiune minimă: 40 mm lățime la tipar (240 px pe ecran) pentru varianta orizontală; 12 mm pentru simbol.</span></div>
      <div class="rule"><span class="ok"></span><span>Se folosesc doar fișierele livrate (SVG, PDF, PNG), fără redesenare.</span></div>
      <div class="rule"><span class="no"></span><span>Nu se deformează, nu se recolorează, nu primește umbre sau contururi.</span></div>
      <div class="rule"><span class="no"></span><span>Nu înlocuiește sigla GAL în bara de sigle și nu intră pe placa, afișul sau autocolantul AFIR.</span></div>
    </div>
  </div>
  <h2 style="margin-top:4mm">Cum se așază pe un material</h2>
  <div style="display:grid;grid-template-columns:1.25fr 1fr;gap:8mm;align-items:center">
    <div style="border:.3mm solid #E2DCCF;border-radius:4mm;overflow:hidden">
      <div style="background:#fff;padding:4mm 5mm 3mm">{bara_sigle('6.4mm', leader_h='5mm')}</div>
      <div style="background:{CREM};padding:3mm 5mm;display:flex;align-items:center;gap:6mm">
        <div class="logo-h" style="width:48mm">{lockup_orizontal('color')}</div>
        <div style="font-size:11pt;font-weight:800;line-height:1.1">Titlul materialului<br><span class="verde">în culorile proiectului</span></div></div>
    </div>
    <div class="txt">Sus, pe fundal alb: <b>bara de sigle</b> a finanțatorilor. Dedesubt, în corpul materialului: <b>logo-ul proiectului</b>,
      titlul și mesajul. Jos: mențiunile obligatorii și datele de contact. Exemple complete: flyerele, afișele și postările livrate.</div>
  </div>
</div>"""


def pagina2():
    sw = ''
    for nume, hx, rol, cm in CULORI:
        c = cm or cmyk(hx)
        r, g, b = (int(hx[i:i + 2], 16) for i in (1, 3, 5))
        bord = ';border:.3mm solid #E2DCCF' if hx == CREM else ''
        sw += (f'<div class="sw"><div class="c" style="background:{hx}{bord}"></div><div class="d"><b>{nume}</b><br>{hx} · RGB {r}/{g}/{b}<br>'
               f'CMYK {c[0]}/{c[1]}/{c[2]}/{c[3]}<br><span style="color:{GRI}">{rol}</span></div></div>')
    return f"""
<div class="page pg" style="background:#fff">
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:9mm">
    <div>
      <h2>Culori</h2>
      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:3mm">{sw}</div>
      <div class="txt" style="font-size:7.4pt;color:{GRI};margin-top:2mm">Valorile CMYK ale culorilor noi sunt orientative; se confirmă cu tipografia la prima comandă.</div>
      <h2 style="margin-top:6mm">Fonturi</h2>
      <div style="font-size:19pt;font-weight:800;line-height:1.1">Montserrat ExtraBold</div>
      <div class="txt">titluri · Montserrat Regular și SemiBold pentru text (fontul din manualul GAL; gratuit, licență OFL)</div>
      <div class="hand" style="font-size:22pt;color:{VERDE_INCHIS};margin-top:3mm;line-height:1">Caveat – accente scurte, sloganul</div>
      <div class="txt" style="margin-top:2mm"><b>Calibri</b> rămâne obligatoriu pe placa, afișul și autocolantul AFIR, care se completează pe modelele oficiale.</div>
    </div>
    <div>
      <h2>Bara de sigle (obligatorie pe orice material al proiectului)</h2>
      <div class="box" style="background:#fff;border:.3mm solid #E2DCCF">{bara_sigle('9mm', leader_h='7mm')}</div>
      <div class="txt" style="margin-top:3mm">
        <div class="rule"><span class="ok"></span><span><b>Ordinea, de la stânga la dreapta:</b> emblema UE cu „Cofinanțat de Uniunea Europeană” · MADR · PS 2023-2027 · GAL Napoca Porolissum · AFIR (Ghidul AFIR de identitate vizuală V3, cap. 3).</span></div>
        <div class="rule"><span class="ok"></span><span><b>LEADER pe un rând separat</b> de emblema UE (cap. 2.G). Pe paginile web, emblema UE cu „Uniunea Europeană” poate sta pe același rând cu LEADER.</span></div>
        <div class="rule"><span class="ok"></span><span><b>Toate siglele au aceeași înălțime</b>, iar spațiul dintre ele este de cel puțin 1/5 din înălțime. Pe formate înguste (A5, panoul de 99 mm), bara se poate așeza pe două rânduri, 3 + 2, în aceeași ordine.</span></div>
        <div class="rule"><span class="ok"></span><span><b>Sigla AFIR:</b> minimum 13 mm înălțime acolo unde formatul permite (afișe A3 și mai mari). Pe A5 nu încape; de confirmat cu OJFIR odată cu lista materialelor.</span></div>
        <div class="rule"><span class="ok"></span><span><b>Pe fiecare material:</b> cele trei mențiuni obligatorii (Anexa II, C1.1-6), datele proiectului și „Material distribuit gratuit”.</span></div>
        <div class="rule"><span class="no"></span><span>Emblema UE nu se modifică, nu se decupează și nu se pune pe fotografii fără fundal alb.</span></div>
      </div>
    </div>
  </div>
  <div style="position:absolute;left:15mm;right:15mm;bottom:9mm;font-size:6.6pt;color:{GRI};line-height:1.4">{MENTIUNI} {DATE_PROIECT}</div>
</div>"""


def build(out_dir):
    pdf = render_pdf(page_html(pagina1() + pagina2(), W, H, extra_css=CSS), out_dir / 'Fisa_identitate_vizuala_proiect.pdf')
    pngs = [pdf_to_png(pdf, out_dir / f'Fisa_identitate_vizuala_pagina{i+1}.png', dpi=110, page=i) for i in range(2)]
    return pdf, pngs


if __name__ == '__main__':
    print(build(ROOT / 'logo'))
