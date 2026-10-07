# -*- coding: utf-8 -*-
"""Generează documentul de documentare a SA3.1 (informare și publicitate) pentru RP1,
după modelul „SA_6.1_06.2026_Informare și Publicitate” din proiectul PIDS, pe șablonul oficial
„Antet_subsol_UNIC_Porolissum_PEO_A4_portret.docx” (antet + subsol, de folosit la toate documentele proiectului).
Textele între «…» sunt completări de făcut de echipa de proiect (evidențiate cu galben)."""
import os, re
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_COLOR_INDEX, WD_BREAK
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

HERE = os.path.dirname(os.path.abspath(__file__))
LIV = os.path.join(HERE, 'livrabile')
IMG = os.path.join(LIV, 'sa31_img')
OUT = os.path.join(LIV, 'SA 3.1_07-09.2026_Informare și Publicitate.docx')
DATA_CAPTURI = '07.10.2026'

SABLON = os.path.join(LIV, 'Antet_subsol_UNIC_Porolissum_PEO_A4_portret.docx')  # antetul oficial (din 07.10.2026)
doc = Document(SABLON)
body = doc.element.body
for el in list(body):
    if not el.tag.endswith('}sectPr'):
        body.remove(el)
sec = doc.sections[0]  # marginile, antetul și subsolul rămân cele din șablon
CONTENT_W = sec.page_width - sec.left_margin - sec.right_margin

st = next(x for x in doc.styles if x.type == 1 and x.name.lower() == 'normal')
st.font.name = 'Times New Roman'; st.font.size = Pt(12)
st.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')

def _runs(p, text, bold=False, size=None, color=None, italic=False):
    """scrie textul, evidențiind cu galben fragmentele «…»"""
    for part in re.split(r'(«[^»]*»)', text):
        if not part:
            continue
        r = p.add_run(part)
        r.bold = bold; r.italic = italic
        if size: r.font.size = Pt(size)
        if color: r.font.color.rgb = RGBColor(*color)
        if part.startswith('«'):
            r.font.highlight_color = WD_COLOR_INDEX.YELLOW
    return p

def P(text='', bold=False, size=None, align=None, space_after=6, italic=False, color=None):
    p = doc.add_paragraph()
    if align == 'center': p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    elif align == 'justify': p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_after = Pt(space_after)
    _runs(p, text, bold=bold, size=size, italic=italic, color=color)
    return p

def LINK(url, text=None, bullet=False, bold=True):
    p = doc.add_paragraph()
    if bullet:  # șablonul nu are stilul „List Bullet”: marcator manual
        p.paragraph_format.left_indent = Cm(0.63); p.paragraph_format.first_line_indent = Cm(-0.63)
        p.add_run('•\t')
    part = p.part
    r_id = part.relate_to(url, 'http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink', is_external=True)
    h = OxmlElement('w:hyperlink'); h.set(qn('r:id'), r_id)
    r = OxmlElement('w:r'); rPr = OxmlElement('w:rPr')
    c = OxmlElement('w:color'); c.set(qn('w:val'), '0563C1'); rPr.append(c)
    u = OxmlElement('w:u'); u.set(qn('w:val'), 'single'); rPr.append(u)
    if bold:
        rPr.append(OxmlElement('w:b'))
    r.append(rPr)
    t = OxmlElement('w:t'); t.text = text or url; t.set(qn('xml:space'), 'preserve'); r.append(t)
    h.append(r); p._p.append(h)
    p.paragraph_format.space_after = Pt(6)
    return p

def TITLU(text, size=20, before=180):
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(before); p.paragraph_format.space_after = Pt(12)
    _runs(p, text, bold=True, size=size)
    return p

def PAGEBREAK():
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)

def IMAGINE(fname, width=None, legenda=None, max_h_cm=19.5):
    from PIL import Image
    path = os.path.join(IMG, fname)
    w, h = Image.open(path).size
    width = width or CONTENT_W
    if h / w * width > Cm(max_h_cm):
        width = int(Cm(max_h_cm) * w / h)
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.add_run().add_picture(path, width=width)
    p.paragraph_format.space_after = Pt(2)
    if legenda:
        P(legenda, size=10, italic=True, align='center', space_after=10, color=(0x40, 0x40, 0x40))

def PLACEHOLDER(text):
    """casetă pentru o captură/fotografie care trebuie adăugată"""
    t = doc.add_table(rows=1, cols=1)
    cell = t.rows[0].cells[0]
    tcPr = cell._tc.get_or_add_tcPr(); b = OxmlElement('w:tcBorders')
    for side in ('top', 'left', 'bottom', 'right'):
        e = OxmlElement('w:' + side); e.set(qn('w:val'), 'single'); e.set(qn('w:sz'), '6'); e.set(qn('w:color'), '808080'); b.append(e)
    tcPr.append(b)
    cell.width = CONTENT_W
    p = cell.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(60); p.paragraph_format.space_after = Pt(60)
    _runs(p, '«' + text + '»', size=11, italic=True)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

# ---------------------------------------------------------------- pagina de titlu
TITLU('S.A.3.1 – Derularea activităților de informare și publicitate a proiectului', size=20, before=150)
P('Perioada de raportare: iulie – septembrie 2026 (L1 – L3)', bold=True, size=14, align='center', space_after=4)
P('Raportul de progres nr. 1', size=13, align='center', space_after=40)
P('Proiect: UNIC – „Uniți pentru Nevoile Incluzive și Continuitatea Educației Elevilor”, cod SMIS 352704', size=11, align='center', space_after=2)
P('Beneficiar: Asociația Grupul de Acțiune Locală Napoca Porolissum', size=11, align='center', space_after=2)
P('Contract de finanțare nr. 11205/16.06.2026 – Programul Educație și Ocupare 2021-2027', size=11, align='center', space_after=60)
P('Conținut:', bold=True, size=11, space_after=2)
for item in ['1. Anunțul de începere a proiectului – publicare pe site-ul beneficiarului',
             '2. Subpagina dedicată proiectului pe site-ul beneficiarului',
             '3. Postări pe pagina de Facebook a proiectului',
             '4. Materiale de informare realizate (afiș A3, flyere)',
             '5. Expunerea afișului A3 și inscripționarea echipamentelor']:
    P(item, size=11, space_after=1)
P('', space_after=40)
P('Întocmit: Asistent manager, «nume prenume»', size=11, space_after=2)
P('Avizat: Manager de proiect, Baba Alina-Ioana', size=11, space_after=2)
P('Capturile de ecran au fost realizate la data de ' + DATA_CAPTURI + ', cu adresa URL activă.', size=10, italic=True, space_after=2)

# ---------------------------------------------------------------- 1. anunțul de începere
PAGEBREAK()
TITLU('ANUNȚUL DE ÎNCEPERE A PROIECTULUI', size=16, before=120)
P('publicat pe subpagina dedicată proiectului de pe site-ul beneficiarului', align='center', italic=True, space_after=4)
LINK('https://napocaporolissum.ro/unic-porolissum-2/')
P('Subpagina proiectului a fost creată la 02.07.2026, în secțiunea „Programe – PEO – Programul Educație și Ocupare”. '
  'Anunțul de începere a fost publicat la data de «__.07.2026» și cuprinde elementele prevăzute de Manualul de identitate vizuală 2021-2027: '
  'beneficiarul, titlul și codul MySMIS al proiectului, programul și prioritatea, fondul (FSE+), perioada și regiunea de implementare, valoarea totală, '
  'scopul, activitățile, grupul țintă, rezultatele urmărite și datele de contact.', align='justify', size=11)
PAGEBREAK()
LINK('https://napocaporolissum.ro/unic-porolissum-2/', bullet=True)
IMAGINE('site_acc_anunturi.png', legenda='Anunțul de începere a proiectului – secțiunea „Anunțuri” a subpaginii proiectului (captură ' + DATA_CAPTURI + ')')
P('«Se atașează și PDF-ul anunțului de începere, în forma avizată de Managerul de proiect, conform cererii de finanțare.»', size=10, italic=True)

# ---------------------------------------------------------------- 2. subpagina
PAGEBREAK()
TITLU('SUBPAGINA PROIECTULUI PE SITE-UL BENEFICIARULUI', size=16, before=120)
LINK('https://napocaporolissum.ro/unic-porolissum-2/')
P('Subpagina prezintă elementele de identitate vizuală ale proiectului și ale finanțării, descrierea și obiectivul proiectului, justificarea, '
  'rezultatele așteptate, activitățile, anunțurile și metodologiile publicate.', align='justify', size=11)
PAGEBREAK()
LINK('https://napocaporolissum.ro/unic-porolissum-2/', bullet=True)
IMAGINE('site_header.png', legenda='Partea superioară a subpaginii – coperta și antetul proiectului (captură ' + DATA_CAPTURI + ')')
IMAGINE('site_acc_despre.png', legenda='Secțiunea „Despre proiectul UNIC”')
PAGEBREAK()
LINK('https://napocaporolissum.ro/unic-porolissum-2/', bullet=True)
IMAGINE('site_acc_rezultate.png', legenda='Secțiunea „Rezultatele proiectului UNIC”')
IMAGINE('site_acc_metodologii.png', legenda='Secțiunea „Metodologii” – documentele publicate la 16.07.2026')
P('Documente publicate pe subpagină:', bold=True, size=11, space_after=2)
LINK('https://napocaporolissum.ro/wp-content/uploads/METODOLOGIE_GT_CU_ANEXE_UNIC_352704_16.07.2026.pdf',
     'Metodologia privind identificarea, recrutarea, înscrierea, verificarea, selectarea, validarea și menținerea grupului țintă (16.07.2026)', bullet=True, bold=False)
LINK('https://napocaporolissum.ro/wp-content/uploads/METODOLOGIE_SPRIJIN_FINANCIAR_CU_ANEXE_UNIC_352704_16.07.2026.pdf',
     'Metodologia privind acordarea sprijinului financiar pentru transport, cazare și masă (16.07.2026)', bullet=True, bold=False)

# ---------------------------------------------------------------- 3. facebook
PAGEBREAK()
TITLU('POSTĂRI PE PAGINA DE FACEBOOK A PROIECTULUI', size=16, before=120)
P('„UNIC: Viitor prin Educație”', bold=True, size=14, align='center', space_after=4)
LINK('https://www.facebook.com/unic.viitorprineducatie?locale=ro_RO')
P('Pagina proiectului a fost creată la «__.__.2026» și avea, la data capturii (' + DATA_CAPTURI + '), 588 de urmăritori. '
  'Secțiunea „Prezentare” conține titlul proiectului, mențiunea cofinanțării de către Uniunea Europeană prin Programul Educație și Ocupare (PEO 2021-2027), '
  'codul MySMIS 352704, adresa de e-mail și trimiterea către subpagina proiectului de pe site-ul beneficiarului. '
  'În perioada iulie – septembrie 2026 au fost publicate «__» postări.', align='justify', size=11)
PAGEBREAK()
LINK('https://www.facebook.com/unic.viitorprineducatie?locale=ro_RO', bullet=True)
IMAGINE('fb_pagina.png', legenda='Pagina de Facebook a proiectului – antet, secțiunea „Prezentare” și ultima postare din perioada de raportare (captură ' + DATA_CAPTURI + ')')
PAGEBREAK()
P('Postări publicate în perioada de raportare (una pe pagină, cu link și captură de ecran, în ordine cronologică):', bold=True, size=11)
P('«Se completează din pagina proiectului, după autentificare: pentru fiecare postare se copiază link-ul (Distribuie → Copiază link) și se inserează captura de ecran a postării, cu data vizibilă.»', size=10, italic=True)
for i in range(1, 7):
    PAGEBREAK()
    LINK('https://www.facebook.com/unic.viitorprineducatie', f'«Postarea {i} – link: https://www.facebook.com/share/p/…»', bullet=True)
    if i == 6:
        P('29.09.2026 – „Au început activitățile proiectului UNIC la Colegiul Tehnic Turda!” (postare cu fotografii și video din cadrul activităților SA5.3 / SA5.4)', size=11)
    else:
        P(f'«data postării» – «tema postării {i}»', size=11)
    PLACEHOLDER(f'captură de ecran postarea {i}')

# ---------------------------------------------------------------- 4. materiale
PAGEBREAK()
TITLU('MATERIALE DE INFORMARE REALIZATE', size=16, before=120)
P('Materialele au fost realizate în luna iulie 2026 (versiuni finale din 31.07.2026), cu elementele obligatorii de identitate vizuală '
  '(emblema Uniunii Europene cu mențiunea „Cofinanțat de Uniunea Europeană”, sigla Guvernului României, sigla beneficiarului și sigla proiectului), '
  'și au fost utilizate în întâlnirile de informare cu unitățile de învățământ partenere și cu elevii.', align='justify', size=11)
P('• Afiș A3 al proiectului (fișier: „Afiș A3_proiect UNIC2.pdf”);', size=11, space_after=1)
P('• Flyer de prezentare a proiectului pentru unitățile de învățământ, față-verso (fișier: „flyer_UNIC_352704_scoli_fata_verso.pdf”);', size=11, space_after=1)
P('• Flyer de prezentare a proiectului, format 12 × 17 cm, față-verso (fișier: „Flyer-UNIC2 (12 x 17 cm).pdf”).', size=11, space_after=8)
PAGEBREAK()
P('Afiș A3 al proiectului', bold=True, size=12, align='center')
PLACEHOLDER('imagine afiș A3 – se inserează din fișierul „Afiș A3_proiect UNIC2.pdf”')
PAGEBREAK()
P('Flyer de prezentare pentru unitățile de învățământ (față)', bold=True, size=12, align='center')
IMAGINE('flyer_scoli-1.png', max_h_cm=22)
PAGEBREAK()
P('Flyer de prezentare pentru unitățile de învățământ (verso)', bold=True, size=12, align='center')
IMAGINE('flyer_scoli-2.png', max_h_cm=22)
PAGEBREAK()
P('Flyer 12 × 17 cm (față și verso)', bold=True, size=12, align='center')
t = doc.add_table(rows=1, cols=2)
for cell, f in zip(t.rows[0].cells, ['flyer_12x17-1.png', 'flyer_12x17-2.png']):
    cp = cell.paragraphs[0]; cp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cp.add_run().add_picture(os.path.join(IMG, f), width=Cm(7.6))

# ---------------------------------------------------------------- 5. afiș expus + autocolante
PAGEBREAK()
TITLU('EXPUNEREA AFIȘULUI A3 ȘI INSCRIPȚIONAREA ECHIPAMENTELOR', size=16, before=120)
P('Conform cererii de finanțare și Ghidului de identitate vizuală (Anexa 18 la Manualul beneficiarului), afișul A3 al proiectului este expus '
  'într-un loc vizibil publicului la sediul de implementare al beneficiarului din comuna Gilău «și la unitățile de învățământ partenere în care se desfășoară activitățile». '
  'Echipamentele IT recepționate la 18.09.2026 «au fost inscripționate cu autocolante conținând elementele de identitate vizuală la data de __.__.2026».', align='justify', size=11)
PLACEHOLDER('fotografie – afișul A3 expus la sediul beneficiarului (Gilău), cu data')
PLACEHOLDER('fotografii – afișul A3 expus la Colegiul Tehnic Turda / Liceul Tehnologic „Vlădeasa” Huedin / Liceul Teologic Reformat Cluj-Napoca')
PLACEHOLDER('fotografii – autocolantele aplicate pe echipamentele IT (laptopuri, desktopuri, multifuncționale)')

doc.save(OUT)
print('OK ->', OUT)
