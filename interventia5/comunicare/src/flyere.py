# -*- coding: utf-8 -*-
"""Flyer 1: A5 față-verso „Ai o idee verde?”  ·  Flyer 2: A4 pliat în trei, „Ghid rapid pentru aplicanți”."""
from componente import *

BL = 3  # bleed mm


# ================================================================== FLYER 1 – A5 față-verso
def flyer_a5():
    W, H = 148 + 2 * BL, 210 + 2 * BL
    css = BASE_CSS + f"""
.a5 .pad {{ position:absolute; left:{BL+8}mm; right:{BL+8}mm; }}
.badge-row {{ display:flex; gap:3mm; align-items:center; }}
.pill {{ background:{VERDE}; color:#fff; border-radius:20mm; padding:2mm 4mm; font-weight:700; font-size:9.5pt; white-space:nowrap; }}
.sun {{ width:31mm; height:31mm; border-radius:50%; background:{SOARE}; color:{MARO}; display:flex; flex-direction:column;
        align-items:center; justify-content:center; text-align:center; line-height:1.05; box-shadow:0 0 0 2.4mm rgba(246,185,59,.25); }}
.sun .s1 {{ font-size:7pt; font-weight:600; }} .sun .s2 {{ font-size:15pt; font-weight:800; letter-spacing:-.3pt; }} .sun .s3 {{ font-size:6.5pt; font-weight:600; }}
.h-sec {{ font-size:10.2pt; font-weight:800; color:{MARO}; margin-bottom:1.8mm; display:flex; align-items:center; gap:2mm; }}
.h-sec:before {{ content:''; width:4mm; height:4mm; border-radius:50%; background:{VERDE}; display:inline-block; }}
.card {{ background:#fff; border-radius:3mm; padding:2.6mm 3mm; display:flex; gap:2.6mm; align-items:center; font-size:7.8pt; line-height:1.3; }}
.card .ico {{ width:10mm; height:10mm; flex:none; }}
.grid6 {{ display:grid; grid-template-columns:repeat(3,1fr); gap:2mm; }}
.tile {{ background:#fff; border-radius:3mm; padding:1.8mm 1.4mm 1.6mm; text-align:center; font-size:7pt; font-weight:600; line-height:1.2; }}
.tile .ico {{ width:8mm; height:8mm; margin:0 auto 1mm; }}
.crit {{ display:grid; grid-template-columns:46mm 1fr 9mm; align-items:center; gap:2mm; font-size:7.6pt; margin-bottom:1.1mm; }}
.bar {{ height:3.2mm; background:#E4DED2; border-radius:2mm; overflow:hidden; }}
.bar i {{ display:block; height:100%; background:{VERDE}; border-radius:2mm; }}
.steps {{ display:flex; justify-content:space-between; gap:1.5mm; }}
.step {{ flex:1; text-align:center; font-size:6.8pt; line-height:1.2; font-weight:600; }}
.step .n {{ width:7mm; height:7mm; border-radius:50%; background:{MARO}; color:#fff; font-weight:800; font-size:8.5pt;
            display:flex; align-items:center; justify-content:center; margin:0 auto 1.2mm; }}
"""
    # ------------------------------------------------ față
    fata = f"""
<div class="page a5" style="background:{CREM}">
  <div style="position:absolute;left:0;right:0;top:0;background:#fff;padding:{BL+6}mm {BL+8}mm 4mm">
    {bara_sigle('8.6mm', leader_h='6.6mm')}
  </div>
  <div class="pad" style="top:{BL+33}mm">
    <div class="logo-h" style="width:62mm">{lockup_orizontal('color')}</div>
    <div style="font-size:24.5pt;font-weight:800;line-height:1.04;letter-spacing:-.4pt;margin-top:6mm">
      Ai o idee <span class="verde">verde</span><br>pentru comunitatea ta?</div>
    <div style="font-size:9.6pt;line-height:1.38;margin-top:3.4mm;max-width:118mm">
      Școlile și ONG-urile din teritoriul <b>GAL Napoca Porolissum</b> pot primi <b>micro-granturi</b>
      pentru proiecte de educație și protecție a mediului: plantări, ecologizări, reciclare, ateliere, spectacole, sport.</div>
    <div class="badge-row" style="margin-top:5mm">
      <div class="sun"><span class="s1">până la</span><span class="s2">19.833,3 €</span><span class="s3">pe proiect</span></div>
      <div style="display:flex;flex-direction:column;gap:2.4mm">
        <span class="pill">6 micro-granturi</span>
        <span class="pill" style="background:{MARO}">100% nerambursabil</span>
        <span class="pill" style="background:{VERDE_CRUD};color:{MARO}">14 localități</span>
      </div>
    </div>
  </div>
  <div class="svgfill" style="position:absolute;left:0;right:0;bottom:{BL+17}mm;height:52mm">{peisaj('100%', '100%')}</div>
  <div style="position:absolute;left:0;right:0;bottom:0;height:{BL+19}mm;background:{VERDE_INCHIS};color:#fff;
              padding:3.2mm {BL+8}mm 0;display:flex;justify-content:space-between;align-items:flex-start">
    <div class="hand" style="font-size:17pt;line-height:1">{TAGLINE}</div>
    <div style="text-align:right;font-size:7.6pt;line-height:1.35"><b>{LANSARE}</b><br>Detalii: {SITE}</div>
  </div>
</div>"""
    # ------------------------------------------------ verso
    crit = [('Ore de voluntariat', 25), ('Proiecte comunitare', 25), ('Calitatea planului de intervenție', 30), ('Interviul cu juriul', 20)]
    crit_html = ''.join(f'<div class="crit"><span>{n}</span><div class="bar"><i style="width:{p/30*100:.0f}%"></i></div>'
                        f'<b style="text-align:right">{p} p</b></div>' for n, p in crit)
    tiles = [('plantare', 'Plantări și ecologizări'), ('reciclare', 'Reciclare, colectare selectivă'), ('teatru', 'Teatru, scenete, pictură'),
             ('sport', 'Sport pentru natură'), ('drona', 'Concursuri cu drone'), ('echipamente', 'Echipamente pentru mediu')]
    tiles_html = ''.join(f'<div class="tile"><div class="ico">{icon(k)}</div>{t}</div>' for k, t in tiles)
    steps = ['Citești ghidul apelului', 'Ceri consiliere gratuită', 'Scrii planul de intervenție', 'Depui online', 'Interviu și contract']
    steps_html = ''.join(f'<div class="step"><div class="n">{i}</div>{s}</div>' for i, s in enumerate(steps, 1))
    verso = f"""
<div class="page a5" style="background:{CREM}">
  <div class="pad" style="top:{BL+7}mm">
    <div class="h-sec">Cine poate aplica</div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:2.4mm">
      <div class="card"><div class="ico">{icon('scoala')}</div><div><b>Grădinițe, școli și licee</b> din teritoriul GAL</div></div>
      <div class="card"><div class="ico">{icon('ong')}</div><div><b>ONG-uri de mediu</b> cu sediu, filială sau activitate în teritoriu</div></div>
    </div>
    <div style="font-size:6.9pt;line-height:1.35;margin-top:1.6mm;color:{GRI}">{' · '.join(LOCALITATI)}</div>

    <div class="h-sec" style="margin-top:3.6mm">Ce poți face cu micro-grantul</div>
    <div class="grid6">{tiles_html}</div>
    <div style="font-size:7pt;margin-top:1.6mm;color:{GRI}">și acțiuni de conștientizare despre aer, apă, păduri, biodiversitate, energie regenerabilă, climă și transport curat.</div>

    <div class="h-sec" style="margin-top:3.6mm">Cum se aleg proiectele</div>
    {crit_html}
    <div style="font-size:7pt;color:{GRI};margin-top:.6mm">Prag minim: 50 din 100 de puncte · juriu mixt: echipa GAL și experți externi · un singur proiect pe solicitant.</div>

    <div class="h-sec" style="margin-top:3.6mm">Pașii până la grant</div>
    <div class="steps">{steps_html}</div>
  </div>
  <div style="position:absolute;left:{BL+8}mm;right:{BL+8}mm;bottom:{BL+29.5}mm;background:#fff;border-radius:3mm;padding:2.4mm 3mm;
              display:flex;gap:3mm;align-items:center">
    <div class="svgfill" style="width:16mm;height:16mm;flex:none">{qr()}</div>
    <div style="font-size:7.2pt;line-height:1.4;flex:1"><b style="font-size:8.2pt">Întrebări? Suntem aici.</b><br>
      {TELEFON} · {EMAIL}<br>{ADRESA}<br>{SITE} · Facebook: Asociația GAL Napoca Porolissum</div>
    <div class="logo-v" style="width:21mm;flex:none">{lockup_vertical('color')}</div>
  </div>
  <div style="position:absolute;left:0;right:0;bottom:0">{subsol_obligatoriu('5.9pt', pad=f'2.6mm {BL+8}mm {BL+2.4}mm')}</div>
</div>"""
    return page_html(fata + verso, W, H, extra_css=css)


# ================================================================== FLYER 2 – A4 pliat în trei (6 panouri de 99 mm)
def flyer_trifold():
    W, H = 297 + 2 * BL, 210 + 2 * BL
    css = BASE_CSS + f"""
.panel {{ position:absolute; top:0; bottom:0; width:{99}mm; }}
.pin {{ position:absolute; left:8mm; right:8mm; }}
.kicker {{ display:inline-block; background:{VERDE}; color:#fff; font-weight:700; font-size:7.6pt; letter-spacing:.8pt;
           text-transform:uppercase; padding:1.3mm 3mm; border-radius:10mm; }}
.ph {{ font-size:15pt; font-weight:800; line-height:1.08; letter-spacing:-.2pt; margin:3mm 0 3mm; }}
.txt {{ font-size:8.3pt; line-height:1.42; }}
.li {{ display:flex; gap:2.6mm; align-items:flex-start; margin-bottom:2.6mm; font-size:8.1pt; line-height:1.36; }}
.li .ico {{ width:9mm; height:9mm; flex:none; }}
.g12 {{ display:grid; grid-template-columns:repeat(3,1fr); gap:2mm; }}
.t {{ background:#fff; border-radius:2.6mm; padding:2.2mm 1mm 1.8mm; text-align:center; font-size:6.6pt; font-weight:600; line-height:1.18; }}
.t .ico {{ width:8.4mm; height:8.4mm; margin:0 auto 1.2mm; }}
.stp {{ display:grid; grid-template-columns:7mm 1fr; gap:2.4mm; align-items:start; margin-bottom:2.2mm; font-size:7.9pt; line-height:1.33; }}
.stp .n {{ width:7mm; height:7mm; border-radius:50%; background:{MARO}; color:#fff; font-weight:800; font-size:8.4pt;
           display:flex; align-items:center; justify-content:center; }}
.pt {{ display:flex; justify-content:space-between; font-size:7.7pt; padding:1.2mm 0; border-bottom:.3mm dashed #CFC6B8; }}
"""
    X = lambda i: f'left:{BL + 99 * i}mm'
    # ------------------------------------------------ exterior: [clapetă interioară | spate | copertă]
    clapeta = f"""
<div class="panel" style="{X(0)};background:{CREM}">
  <div class="pin" style="top:{BL+12}mm">
    <span class="kicker">De ce acum</span>
    <div class="ph">Ideile bune există.<br><span class="verde">Le lipsește doar un început.</span></div>
    <div class="txt">În satele și orașul din teritoriul GAL Napoca Porolissum, colectarea selectivă e încă la început,
      iar copiii și tinerii au prea puține ocazii să învețe despre mediu prin activități practice.</div>
    <div class="txt" style="margin-top:2.6mm">Școlile și ONG-urile au idei, dar de multe ori nu au resurse ca să le ducă mai departe.
      <b>Micro-grantul vine exact aici:</b> finanțează integral o inițiativă locală, cu rezultate pe care comunitatea le vede.</div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:2mm;margin-top:5mm">
      {''.join(f'<div style="background:#fff;border-radius:2.6mm;padding:2.4mm 3mm"><div style="font-size:14pt;font-weight:800;color:{VERDE_TEXT};line-height:1">{n}</div><div style="font-size:7pt;font-weight:600;margin-top:.8mm">{t}</div></div>' for n, t in [('6', 'micro-granturi'), ('19.833,3 €', 'maximum pe proiect'), ('100%', 'finanțare nerambursabilă'), ('14', 'localități din teritoriu')])}
    </div>
    <div class="hand" style="font-size:20pt;color:{VERDE_INCHIS};margin-top:5mm;line-height:1">{TAGLINE}</div>
  </div>
  <div class="svgfill" style="position:absolute;left:0;right:0;bottom:0;height:38mm">{peisaj('100%', '100%')}</div>
</div>"""
    spate = f"""
<div class="panel" style="{X(1)};background:#fff">
  <div class="pin" style="top:{BL+16}mm;text-align:center">
    <div class="logo-v" style="width:44mm;margin:0 auto">{lockup_vertical('color')}</div>
    <div style="font-size:9.6pt;font-weight:800;margin-top:7mm">Întrebări? Suntem aici.</div>
    <div class="txt" style="margin-top:2mm">{TELEFON}<br>{EMAIL}<br>{SITE}<br>Facebook: Asociația GAL Napoca Porolissum<br>{ADRESA}</div>
    <div class="svgfill" style="width:24mm;height:24mm;margin:4mm auto 1.6mm">{qr()}</div>
    <div style="font-size:7pt;color:{GRI}">Scanează pentru apel și ghid</div>
    <img src="{uri(SIGLE / 'gal_color.png')}" style="width:34mm;display:block;margin:7mm auto 0" alt="GAL Napoca Porolissum">
  </div>
  <div style="position:absolute;left:0;right:0;bottom:0">{subsol_obligatoriu('5.6pt', pad=f'3mm 6mm {BL+3}mm')}</div>
</div>"""
    coperta = f"""
<div class="panel" style="{X(2)};background:{CREM}">
  <div style="position:absolute;left:0;right:0;top:0;background:#fff;padding:{BL+6}mm 6mm 3.4mm">
    {bara_sigle('7.8mm', leader_h='6mm', gap='2.4mm', split=3, row_gap='2.4mm')}
  </div>
  <div class="pin" style="top:{BL+43}mm">
    <div class="logo-h" style="width:70mm">{lockup_orizontal('color')}</div>
    <div style="font-size:21pt;font-weight:800;line-height:1.04;letter-spacing:-.3pt;margin-top:6mm">
      Micro-granturi<br><span class="verde">pentru mediu</span></div>
    <div style="font-size:9.6pt;font-weight:600;margin-top:2.6mm">Ghid rapid pentru școli și ONG-uri</div>
    <div style="display:flex;gap:2mm;margin-top:5mm;flex-wrap:wrap">
      <span class="kicker" style="background:{SOARE};color:{MARO}">până la 19.833,3 €</span>
      <span class="kicker">6 granturi</span><span class="kicker" style="background:{MARO}">100% nerambursabil</span>
    </div>
  </div>
  <div class="svgfill" style="position:absolute;left:0;right:0;bottom:{BL+12}mm;height:44mm">{peisaj('100%', '100%')}</div>
  <div style="position:absolute;left:0;right:0;bottom:0;height:{BL+12}mm;background:{VERDE_INCHIS};color:#fff;font-size:7.4pt;
              padding:3mm 8mm;font-weight:600">{LANSARE} · {SITE}</div>
</div>"""
    exterior = f'<div class="page" style="background:{CREM}">{clapeta}{spate}{coperta}</div>'

    # ------------------------------------------------ interior: [cine | ce | cum]
    cine = f"""
<div class="panel" style="{X(0)};background:#fff">
  <div class="pin" style="top:{BL+12}mm">
    <span class="kicker">Cine poate aplica</span>
    <div class="ph">Școli și ONG-uri<br><span class="verde">din teritoriul nostru</span></div>
    <div class="li"><div class="ico">{icon('scoala')}</div><div><b>Unități de învățământ</b> – grădinițe, școli, licee – din teritoriul GAL Napoca Porolissum.</div></div>
    <div class="li"><div class="ico">{icon('ong')}</div><div><b>Organizații neguvernamentale</b> active în educația pentru mediu, cu sediu, filială sau activitate dovedită în teritoriu.</div></div>
    <div class="txt" style="font-size:7.6pt;color:{GRI}">Solicitantul are personalitate juridică și poate depune un singur proiect în sesiune.
      Activitățile se desfășoară exclusiv în teritoriul GAL.</div>
    <div style="font-size:8.6pt;font-weight:800;margin:5mm 0 2mm">Cele 14 localități</div>
    <div style="display:flex;flex-wrap:wrap;gap:1.4mm">{''.join(f'<span style="background:{CREM};border-radius:6mm;padding:1mm 2.4mm;font-size:7.2pt;font-weight:600">{l}</span>' for l in LOCALITATI)}</div>
    <div style="background:{CREM};border-radius:3mm;padding:3mm 3.4mm;margin-top:5mm">
      <div style="display:flex;gap:2mm;align-items:center;font-size:8.6pt;font-weight:800;margin-bottom:1.6mm"><span class="ico" style="width:6.5mm;height:6.5mm">{icon('calendar')}</span>Calendar estimativ</div>
      {''.join(f'<div class="pt" style="border-color:#D9CFBF"><span>{a}</span><b>{b}</b></div>' for a, b in [('Lansarea apelului', 'începutul lui 2027'), ('Depunerea proiectelor', '30 de zile'), ('Evaluare și interviuri', 'max. 30 de zile'), ('Contestații', '5 + 5 zile lucrătoare'), ('Contractele de grant', 'după selecție')])}
      <div style="font-size:6.8pt;color:{GRI};margin-top:1.6mm">Datele exacte se publică pe {SITE}.</div>
    </div>
  </div>
</div>"""
    keys = ['plantare', 'reciclare', 'ecologizare', 'apa', 'aer', 'biodiversitate', 'clima', 'transport', 'energie', 'teatru', 'pictura', 'afterschool',
            'sport', 'drona', 'echipamente']
    tiles = ''.join(f'<div class="t"><div class="ico">{icon(k)}</div>{ICON_LABEL[k]}</div>' for k in keys)
    ce = f"""
<div class="panel" style="{X(1)};background:{CREM}">
  <div class="pin" style="top:{BL+12}mm">
    <span class="kicker">Ce se finanțează</span>
    <div class="ph">Idei care se văd<br><span class="verde">în comunitate</span></div>
    <div class="g12">{tiles}</div>
    <div class="txt" style="font-size:7.4pt;margin-top:3mm;color:{GRI}">Acțiuni de conștientizare, mai ales pentru copii și tineri, activități practice,
      culturale și sportive cu temă de mediu, precum și echipamente care sprijină protecția mediului.</div>
    <div style="background:{VERDE_INCHIS};color:#fff;border-radius:3mm;padding:3mm 3.4mm;margin-top:3.4mm;font-size:7.9pt;line-height:1.38">
      <b style="color:{SOARE}">100% nerambursabil.</b> Grantul acoperă integral cheltuielile eligibile ale sub-proiectului,
      până la 19.833,3 €. Plata se face în două tranșe: avans la semnarea contractului și restul după realizarea acțiunilor.</div>
  </div>
</div>"""
    crit = [('Ore de voluntariat', 25), ('Proiecte comunitare (min. 2, cu ≥ 20 participanți)', 25),
            ('Calitatea planului de intervenție', 30), ('Interviul cu juriul (min. 12 p)', 20)]
    cum = f"""
<div class="panel" style="{X(2)};background:#fff">
  <div class="pin" style="top:{BL+12}mm">
    <span class="kicker">Cum aplici</span>
    <div class="ph">Cinci pași<br><span class="verde">până la grant</span></div>
    <div class="stp"><div class="n">1</div><div><b>Citește ghidul apelului</b>, publicat pe {SITE} la lansare.</div></div>
    <div class="stp"><div class="n">2</div><div><b>Vino la o sesiune de informare</b> sau cere consiliere gratuită, la sediu ori online.</div></div>
    <div class="stp"><div class="n">3</div><div><b>Scrie planul de intervenție:</b> obiective, activități, analiză SWOT, echipă, promovare, buget.</div></div>
    <div class="stp"><div class="n">4</div><div><b>Depune dosarul online</b> în cele 30 de zile ale apelului.</div></div>
    <div class="stp"><div class="n">5</div><div><b>Prezintă proiectul la interviu.</b> Urmează rezultatele, contestațiile și contractul de grant.</div></div>
    <div style="font-size:8.6pt;font-weight:800;margin:3.4mm 0 1mm">Punctajul (max. 100, prag 50)</div>
    {''.join(f'<div class="pt"><span>{n}</span><b>{p} p</b></div>' for n, p in crit)}
    <div class="txt" style="font-size:7pt;color:{GRI};margin-top:2mm">GAL oferă informații și consiliere, nu redactează proiecte.
      Granturile se acordă în ordinea punctajului, până la epuizarea bugetului.</div>
    <div style="border:.4mm solid {VERDE};border-radius:3mm;padding:2.6mm 3.2mm;margin-top:3.4mm;font-size:7.5pt;line-height:1.36">
      <b>Dacă proiectul tău câștigă:</b> organizezi cel puțin 2 proiecte comunitare cu minimum 20 de participanți,
      afișezi la locul activităților afișul informativ PS 2023 – 2027, raportezi către GAL și primești 2 vizite de monitorizare.</div>
  </div>
</div>"""
    interior = f'<div class="page" style="background:#fff">{cine}{ce}{cum}</div>'
    return page_html(exterior + interior, W, H, extra_css=css)


def build(out_dir):
    res = {}
    for name, fn, pages in [('Flyer1_A5_fata-verso', flyer_a5, 2), ('Flyer2_A4_pliat_in_trei', flyer_trifold, 2)]:
        pdf = render_pdf(fn(), out_dir / f'{name}_tipar_bleed3mm.pdf')
        pngs = []
        for i in range(pages):
            png = out_dir / f'{name}_pagina{i+1}.png'
            pdf_to_png(pdf, png, dpi=200, page=i, clip_mm=BL); pngs.append(png)
        res[name] = (pdf, pngs)
    return res


if __name__ == '__main__':
    for k, v in build(ROOT / 'flyere').items():
        print(k, v[0].name, [p.name for p in v[1]])
