# -*- coding: utf-8 -*-
"""Afiș 1: A3 campanie „Natura are nevoie de ideile tale.”  ·  Afiș 2: A3 sesiune de informare (șablon cu câmpuri de completat).
Notă: afișele promoționale NU înlocuiesc afișul informativ publicitar obligatoriu (model AFIR A.3, A2), care se folosește neschimbat."""
from componente import *

BL = 3
W, H = 297 + 2 * BL, 420 + 2 * BL
M = BL + 15  # margine laterală

CSS = BASE_CSS + f"""
.hdr {{ position:absolute; left:0; right:0; top:0; background:#fff; padding:{BL+11}mm {M}mm 7mm; }}
.pill {{ display:inline-block; background:{VERDE}; color:#fff; border-radius:30mm; padding:3.2mm 7mm; font-weight:700; font-size:17pt; white-space:nowrap; }}
.sun {{ width:62mm; height:62mm; border-radius:50%; background:{SOARE}; color:{MARO}; display:flex; flex-direction:column; align-items:center;
        justify-content:center; text-align:center; line-height:1.05; box-shadow:0 0 0 5mm rgba(246,185,59,.25); }}
.band {{ position:absolute; left:0; right:0; bottom:0; background:{VERDE_INCHIS}; color:#fff; }}
.qrbox {{ background:#fff; border-radius:3mm; padding:2.4mm; }}
.ph {{ background:#FFF1C9; border-bottom:.8mm solid {SOARE}; padding:0 2mm; }}
.det {{ display:grid; grid-template-columns:18mm 1fr; gap:5mm; align-items:center; background:#fff; border-radius:5mm; padding:4.4mm 6mm; }}
.det .ico {{ width:18mm; height:18mm; }}
.det .l {{ font-size:13pt; font-weight:600; color:{GRI}; }}
.det .v {{ font-size:22pt; font-weight:800; line-height:1.1; }}
.ag {{ display:grid; grid-template-columns:14mm 1fr; gap:5mm; align-items:center; margin-bottom:3.6mm; font-size:15pt; line-height:1.25; }}
.ag .ico {{ width:15mm; height:15mm; }}
"""


def banda_jos(titlu, sub, h_band=80):
    return f"""
<div class="band" style="height:{BL+h_band}mm">
  <div style="position:absolute;left:{M}mm;right:{M}mm;top:7mm;display:flex;align-items:center;gap:9mm">
    <div class="logo-v" style="width:44mm;flex:none">{lockup_vertical('alb')}</div>
    <div style="flex:1">
      <div style="font-size:19pt;font-weight:800;line-height:1.15">{titlu}</div>
      <div style="font-size:12.5pt;line-height:1.4;margin-top:2mm;opacity:.95">{sub}</div>
    </div>
    <div class="qrbox" style="width:34mm;height:34mm;flex:none"><div class="svgfill" style="width:100%;height:100%">{qr()}</div></div>
  </div>
  <div style="position:absolute;left:{M}mm;right:{M}mm;bottom:{BL+5}mm;font-size:8.2pt;line-height:1.4;opacity:.92">
    {MENTIUNI}<br>{DATE_PROIECT} Material distribuit gratuit.</div>
</div>"""


def afis_campanie():
    body = f"""
<div class="page" style="background:{CREM}">
  <div class="hdr">{bara_sigle('14mm', leader_h='11mm')}</div>
  <div style="position:absolute;left:{M}mm;right:{M}mm;top:{BL+62}mm">
    <div class="logo-h" style="width:118mm">{lockup_orizontal('color')}</div>
    <div style="font-size:62pt;font-weight:800;line-height:.98;letter-spacing:-1.5pt;margin-top:11mm">
      Natura are nevoie<br>de <span class="verde">ideile tale.</span></div>
    <div style="font-size:19pt;line-height:1.36;margin-top:8mm;max-width:225mm">
      <b>Micro-granturi</b> pentru grădinițe, școli, licee și ONG-uri de mediu din teritoriul <b>GAL Napoca Porolissum</b>,
      pentru proiecte de educație și protecție a mediului.</div>
    <div style="display:flex;gap:9mm;align-items:center;margin-top:11mm">
      <div class="sun"><span style="font-size:14pt;font-weight:600">până la</span><span style="font-size:31pt;font-weight:800;letter-spacing:-.6pt">19.833,3 €</span>
        <span style="font-size:13pt;font-weight:600">pe proiect</span></div>
      <div style="display:flex;flex-direction:column;gap:4.4mm;align-items:flex-start">
        <span class="pill">6 micro-granturi</span>
        <span class="pill" style="background:{MARO}">100% nerambursabil</span>
        <span class="pill" style="background:{VERDE_CRUD};color:{MARO}">14 localități din teritoriu</span>
      </div>
    </div>
  </div>
  <div class="svgfill" style="position:absolute;left:0;right:0;bottom:{BL+79}mm;height:112mm">{peisaj('100%', '100%')}</div>
  <div class="hand" style="position:absolute;right:{M}mm;bottom:{BL+88}mm;font-size:40pt;color:#fff;text-shadow:0 .6mm 2mm rgba(0,0,0,.25)">{TAGLINE}</div>
  {banda_jos(LANSARE + '.', f'Află cine poate aplica și ce se finanțează: {SITE} · {TELEFON} · {EMAIL}')}
</div>"""
    return page_html(body, W, H, extra_css=CSS)


def afis_sesiune():
    agenda = [('scoala', 'Cine poate aplica și ce inițiative se finanțează'),
              ('carte', 'Cum arată un plan de intervenție bun'),
              ('calendar', 'Criteriile de selecție și calendarul apelului'),
              ('interviu', 'Întrebările voastre, cu răspunsuri pe loc')]
    ag = ''.join(f'<div class="ag"><div class="ico">{icon(k)}</div><div>{t}</div></div>' for k, t in agenda)
    body = f"""
<div class="page" style="background:{CREM}">
  <div class="hdr">{bara_sigle('14mm', leader_h='11mm')}</div>
  <div style="position:absolute;left:{M}mm;right:{M}mm;top:{BL+56}mm;z-index:2">
    <span class="pill" style="font-size:15pt;letter-spacing:1.5pt">SESIUNE DE INFORMARE</span>
    <div style="font-size:44pt;font-weight:800;line-height:1.02;letter-spacing:-1pt;margin-top:7mm">
      Micro-granturi pentru mediu:<br><span class="verde">află cum poți aplica</span></div>
    <div style="display:grid;grid-template-columns:1.45fr 1fr;gap:6mm;margin-top:8mm">
      <div class="det"><div class="ico">{icon('calendar')}</div><div><div class="l">Data</div><div class="v"><span class="ph">[ziua, ZZ luna 2027]</span></div></div></div>
      <div class="det"><div class="ico">{icon('ora')}</div><div><div class="l">Ora</div><div class="v"><span class="ph">[10:00 – 12:00]</span></div></div></div>
      <div class="det" style="grid-column:1 / span 2"><div class="ico">{icon('loc')}</div><div><div class="l">Locul</div>
        <div class="v"><span class="ph">[sala, adresa, localitatea]</span></div></div></div>
    </div>
    <div style="display:grid;grid-template-columns:1.25fr 1fr;gap:10mm;margin-top:9mm">
      <div><div style="font-size:19pt;font-weight:800;margin-bottom:5mm">Ce discutăm</div>{ag}</div>
      <div style="background:#fff;border-radius:5mm;padding:7mm">
        <div style="font-size:16pt;font-weight:800">Pentru cine</div>
        <div style="font-size:13.5pt;line-height:1.4;margin-top:3mm">Directori și profesori din grădinițe, școli și licee,
          reprezentanți ai ONG-urilor de mediu din cele 14 localități ale teritoriului GAL Napoca Porolissum.</div>
        <div style="font-size:16pt;font-weight:800;margin-top:6mm">Intrarea este liberă</div>
        <div style="font-size:13.5pt;line-height:1.4;margin-top:3mm">Confirmă participarea la<br><b>{TELEFON}</b> sau <b>{EMAIL}</b></div>
        <div style="font-size:10.5pt;line-height:1.4;margin-top:5mm;color:{GRI}">La sesiune semnezi lista de prezență și completezi un scurt chestionar de evaluare.</div>
      </div>
    </div>
  </div>
  <div class="svgfill" style="position:absolute;left:0;right:0;bottom:{BL+79}mm;height:44mm">{peisaj('100%', '100%', soare=False)}</div>
  {banda_jos('Proiectul „Educație pentru mediu” – micro-granturi pentru școli și ONG-uri', f'Detalii despre apel: {SITE}')}
</div>"""
    return page_html(body, W, H, extra_css=CSS)


def build(out_dir):
    res = {}
    for name, fn in [('Afis1_A3_campanie', afis_campanie), ('Afis2_A3_sesiune_informare_SABLON', afis_sesiune)]:
        pdf = render_pdf(fn(), out_dir / f'{name}_tipar_bleed3mm.pdf')
        png = out_dir / f'{name}.png'
        pdf_to_png(pdf, png, dpi=150, clip_mm=BL)
        res[name] = (pdf, png)
    return res


if __name__ == '__main__':
    for k, v in build(ROOT / 'afise').items():
        print(k, v[0].name, v[1].name)
