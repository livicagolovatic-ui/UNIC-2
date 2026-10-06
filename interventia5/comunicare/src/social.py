# -*- coding: utf-8 -*-
"""Postări social media 1080 × 1350 px (4:5, Facebook și Instagram).
Model A – „Anunț” (fundal verde, mesaj mare).  Model B – „Card informativ” (fundal crem, iconițe / carduri / bare).
Fiecare imagine are în header emblema UE cu „Cofinanțat de Uniunea Europeană” și restul barei de sigle (GIV AFIR V3, B-(2))."""
from componente import *

W, H = 1080, 1350
PAD = 60

CSS = BASE_CSS + f"""
.hdr {{ position:absolute; left:0; right:0; top:0; height:212px; background:#fff; padding:40px {PAD}px 0; }}
.ftr {{ position:absolute; left:0; right:0; bottom:0; height:120px; background:#fff; padding:0 {PAD}px;
        display:flex; align-items:center; justify-content:space-between; border-top:6px solid {SOARE}; }}
.kick {{ display:inline-block; background:{SOARE}; color:{MARO}; font-weight:800; font-size:24px; letter-spacing:2px;
         padding:10px 22px; border-radius:40px; text-transform:uppercase; }}
.ttl {{ font-weight:800; letter-spacing:-1.5px; line-height:1.02; }}
.tile {{ background:#fff; border-radius:24px; padding:32px 14px 28px; text-align:center; font-size:25px; font-weight:700; line-height:1.18; }}
.tile .ico {{ width:96px; height:96px; margin:0 auto 16px; }}
.card {{ background:#fff; border-radius:26px; padding:30px 32px; display:flex; gap:28px; align-items:center; }}
.card .ico {{ width:108px; height:108px; flex:none; }}
.chip {{ background:#fff; border-radius:30px; padding:10px 20px; font-size:25px; font-weight:600; }}
.crit {{ display:grid; grid-template-columns:1fr 92px; gap:8px 18px; align-items:end; margin-bottom:26px; }}
.crit .n {{ font-size:30px; font-weight:700; }} .crit .p {{ font-size:38px; font-weight:800; color:{VERDE_TEXT}; text-align:right; }}
.crit .bar {{ grid-column:1 / span 2; height:22px; background:#E4DED2; border-radius:12px; overflow:hidden; }}
.crit .bar i {{ display:block; height:100%; background:{VERDE}; border-radius:12px; }}
.li {{ display:grid; grid-template-columns:72px 1fr; gap:24px; align-items:center; margin-bottom:24px; font-size:33px; line-height:1.22; }}
.li .n {{ width:72px; height:72px; border-radius:50%; background:{SOARE}; color:{MARO}; font-weight:800; font-size:36px;
          display:flex; align-items:center; justify-content:center; }}
.ph {{ background:rgba(246,185,59,.28); border-radius:8px; padding:0 8px; }}
"""


def header():
    return f'<div class="hdr">{bara_sigle("60px", leader_h="44px", gap="14px", row_gap="16px")}</div>'


def footer(site=True):
    return (f'<div class="ftr"><div class="logo-h" style="width:330px">{lockup_orizontal("color")}</div>'
            f'<div style="text-align:right;font-size:24px;font-weight:700;line-height:1.3">{SITE}<br>'
            f'<span style="font-weight:500;color:{GRI};font-size:20px">#EducatiePentruMediu</span></div></div>')


def model_a(kicker, titlu, corp, jos=''):
    """Anunț: fundal verde închis, titlu mare alb, text sau listă, peisaj jos."""
    body = f"""
<div class="page" style="background:{VERDE_INCHIS}">
  {header()}
  <div style="position:absolute;left:{PAD}px;right:{PAD}px;top:262px;color:#fff;z-index:2">
    <span class="kick">{kicker}</span>
    <div class="ttl" style="font-size:78px;margin-top:30px">{titlu}</div>
    <div style="margin-top:34px">{corp}</div>
    {jos}
  </div>
  <div class="svgfill" style="position:absolute;left:0;right:0;bottom:120px;height:250px;opacity:.95">{peisaj('100%', '100%')}</div>
  {footer()}
</div>"""
    return page_html(body, W, H, unit='px', extra_css=CSS)


def model_b(titlu, continut, sub=''):
    """Card informativ: fundal crem, titlu maro cu accent verde, conținut liber (grilă, carduri, bare)."""
    body = f"""
<div class="page" style="background:{CREM}">
  {header()}
  <div style="position:absolute;left:{PAD}px;right:{PAD}px;top:258px">
    <div class="ttl" style="font-size:70px">{titlu}</div>
    {f'<div style="font-size:30px;line-height:1.3;margin-top:16px;color:{GRI}">{sub}</div>' if sub else ''}
    <div style="margin-top:38px">{continut}</div>
  </div>
  {footer()}
</div>"""
    return page_html(body, W, H, unit='px', extra_css=CSS)


def corp_text(t):
    return f'<div style="font-size:36px;line-height:1.36;max-width:900px">{t}</div>'


def corp_lista(items):
    return ''.join(f'<div class="li"><div class="n">{i}</div><div>{t}</div></div>' for i, t in enumerate(items, 1))


def grila(tiles, cols=3):
    return (f'<div style="display:grid;grid-template-columns:repeat({cols},1fr);gap:22px">'
            + ''.join(f'<div class="tile"><div class="ico">{icon(k)}</div>{t}</div>' for k, t in tiles) + '</div>')


def bare(crit):
    mx = max(p for _, p in crit)
    return ''.join(f'<div class="crit"><div class="n">{n}</div><div class="p">{p} p</div>'
                   f'<div class="bar"><i style="width:{p/mx*100:.0f}%"></i></div></div>' for n, p in crit)


# ---------------------------------------------------------------- modele (șabloane)
def sablon_a():
    return model_a('[Etichetă]', '[Titlul postării,<br>pe cel mult 3 rânduri]',
                   corp_text('<span class="ph">[Un text scurt, de cel mult 25 de cuvinte: ce, cine, până când.]</span>'),
                   f'<div style="margin-top:40px;font-size:30px;font-weight:700;color:{SOARE}">[Detaliu sau dată importantă]</div>')


def sablon_b():
    tiles = [('plantare', '[Element 1]'), ('reciclare', '[Element 2]'), ('teatru', '[Element 3]'),
             ('sport', '[Element 4]'), ('drona', '[Element 5]'), ('echipamente', '[Element 6]')]
    return model_b('[Întrebarea sau titlul<br><span class="verde">cardului informativ]</span>', grila(tiles),
                   sub='[Subtitlu opțional, un rând]')


# ---------------------------------------------------------------- cele 5 postări
def p1():
    return model_a('Proiect nou', 'Pornim<br>micro-granturile<br>pentru mediu!',
                   corp_text('<b>6 micro-granturi</b> de până la <b>19.833,3 €</b>, 100% nerambursabile, pentru grădinițe, școli, licee '
                             'și ONG-uri de mediu din teritoriul GAL Napoca Porolissum.'),
                   f'<div style="margin-top:40px;font-size:32px;font-weight:700;color:{SOARE}">Apelul se lansează la începutul anului 2027.</div>')


def p2():
    cards = (f'<div class="card"><div class="ico">{icon("scoala")}</div><div><div style="font-size:38px;font-weight:800">Grădinițe, școli și licee</div>'
             f'<div style="font-size:28px;margin-top:6px">din teritoriul GAL Napoca Porolissum</div></div></div>'
             f'<div class="card" style="margin-top:22px"><div class="ico">{icon("ong")}</div><div><div style="font-size:38px;font-weight:800">ONG-uri de mediu</div>'
             f'<div style="font-size:28px;margin-top:6px">cu sediu, filială sau activitate dovedită în teritoriu</div></div></div>'
             f'<div style="font-size:28px;font-weight:800;margin:36px 0 14px">Din cele 14 localități:</div>'
             f'<div style="display:flex;flex-wrap:wrap;gap:12px">{"".join(f"<span class=chip>{l}</span>" for l in LOCALITATI)}</div>'
             f'<div style="font-size:27px;line-height:1.35;margin-top:30px;color:{GRI}">Un singur proiect pe solicitant. Activitățile se desfășoară '
             f'exclusiv în teritoriul GAL.</div>')
    return model_b('Cine poate<br><span class="verde">aplica?</span>', cards)


def p3():
    tiles = [('plantare', 'Plantări și ecologizări'), ('reciclare', 'Reciclare și colectare selectivă'), ('teatru', 'Teatru, scenete, pictură'),
             ('sport', 'Sport pentru natură'), ('drona', 'Concursuri cu drone'), ('echipamente', 'Echipamente pentru mediu')]
    extra = (f'<div style="font-size:27px;line-height:1.35;margin-top:30px;color:{GRI}">Și acțiuni de conștientizare despre aer, apă, păduri, '
             f'biodiversitate, energie regenerabilă, schimbări climatice și transport curat.</div>')
    return model_b('Ce idei pot primi<br><span class="verde">finanțare?</span>', grila(tiles) + extra)


def p4():
    crit = [('Ore de voluntariat', 25), ('Proiecte comunitare', 25), ('Calitatea planului de intervenție', 30), ('Interviul cu juriul', 20)]
    extra = (f'<div style="display:flex;gap:16px;flex-wrap:wrap;margin-top:14px">'
             f'<span class="chip" style="background:{MARO};color:#fff">Prag minim: 50 din 100</span>'
             f'<span class="chip">Juriu: echipa GAL + experți externi</span><span class="chip">Un proiect pe solicitant</span></div>'
             f'<div style="font-size:27px;line-height:1.35;margin-top:28px;color:{GRI}">Granturile se acordă în ordinea punctajului, '
             f'până la epuizarea bugetului. Criteriile complete sunt în metodologia de selecție.</div>')
    return model_b('Cum se aleg<br><span class="verde">proiectele?</span>', bare(crit) + extra,
                   sub='Transparent, după criterii publice, cu punctaj de la 0 la 100.')


def p5():
    items = ['Formați echipa care va duce proiectul.', 'Țineți evidența orelor de voluntariat: contează la punctaj.',
             'Gândiți cel puțin 2 acțiuni comunitare, fiecare cu minimum 20 de participanți.',
             f'Scrieți-ne la {EMAIL} și vă anunțăm primii când se deschide apelul.']
    return model_a('Pregătește-te din timp', '4 lucruri de făcut<br>chiar de acum', corp_lista(items))


POSTARI = [('Postarea1_anunt_proiect', p1), ('Postarea2_cine_poate_aplica', p2), ('Postarea3_ce_se_finanteaza', p3),
           ('Postarea4_cum_se_aleg_proiectele', p4), ('Postarea5_pregateste-te_din_timp', p5)]


def build(out_dir):
    res = []
    for name, fn in [('ModelA_anunt_SABLON', sablon_a), ('ModelB_card_informativ_SABLON', sablon_b)] + POSTARI:
        pdf = render_pdf(fn(), BUILD / f'{name}.pdf')
        png = out_dir / f'{name}.png'
        pdf_to_png(pdf, png, width_px=W)
        from PIL import Image
        im = Image.open(png)
        if im.size != (W, H): im.crop((0, 0, W, H)).save(png)
        res.append(png)
    return res


if __name__ == '__main__':
    for p in build(ROOT / 'social'):
        print(p.name)
