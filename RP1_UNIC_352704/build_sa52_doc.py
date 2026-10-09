# -*- coding: utf-8 -*-
"""Generează documentul justificativ al SA5.2 (formarea cadrelor didactice) pentru RP1,
pe șablonul oficial „Antet_subsol_UNIC_Porolissum_PEO_A4_portret.docx” (antetul din 07.10.2026).
Sursele: folderul Drive „2. Achiziție servicii formare cadre didactice” (contract, ordin de începere,
dovada acreditării, calendar, suport de curs, capturile din „Începere curs” și „Desfățurare curs”)
și livrabilele Expertului GT 2 („Furnizor formare – corespondență”, „Recrutare cadre didactice”).
Textele între «…» sunt completări de făcut de echipa de proiect (evidențiate cu galben)."""
import os, re
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_COLOR_INDEX, WD_BREAK
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

HERE = os.path.dirname(os.path.abspath(__file__))
LIV = os.path.join(HERE, 'livrabile')
IMG = os.path.join(LIV, 'sa52_img')
SABLON = os.path.join(LIV, 'Antet_subsol_UNIC_Porolissum_PEO_A4_portret.docx')
OUT = os.path.join(LIV, 'SA 5.2_09.2026_Formarea cadrelor didactice.docx')
DRIVE_INREG = 'https://drive.google.com/file/d/1Ox9ReIS6BNGuRAicvYGff4537LcgQZFC/view'  # „Link curs.docx”

doc = Document(SABLON)
body = doc.element.body
for el in list(body):
    if not el.tag.endswith('}sectPr'):
        body.remove(el)
sec = doc.sections[0]
CONTENT_W = sec.page_width - sec.left_margin - sec.right_margin
st = next(x for x in doc.styles if x.type == 1 and x.name.lower() == 'normal')
st.font.name = 'Times New Roman'; st.font.size = Pt(12)
st.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')


def _runs(p, text, bold=False, size=None, color=None, italic=False):
    for part in re.split(r'(«[^»]*»)', text):
        if not part:
            continue
        r = p.add_run(part); r.bold = bold; r.italic = italic
        if size: r.font.size = Pt(size)
        if color: r.font.color.rgb = RGBColor(*color)
        if part.startswith('«'):
            r.font.highlight_color = WD_COLOR_INDEX.YELLOW
    return p


def P(text='', bold=False, size=None, align=None, space_after=6, italic=False, color=None, before=0):
    p = doc.add_paragraph()
    if align == 'center': p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    elif align == 'justify': p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_after = Pt(space_after); p.paragraph_format.space_before = Pt(before)
    _runs(p, text, bold=bold, size=size, italic=italic, color=color)
    return p


def B(text, size=11):
    """paragraf cu marcator manual (șablonul nu are stilul „List Bullet”)"""
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Cm(0.63); p.paragraph_format.first_line_indent = Cm(-0.63)
    p.paragraph_format.space_after = Pt(2); p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    r = p.add_run('•\t'); r.font.size = Pt(size)
    _runs(p, text, size=size)
    return p


def LINK(url, text=None, bold=False, size=11):
    p = doc.add_paragraph()
    r_id = p.part.relate_to(url, 'http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink', is_external=True)
    h = OxmlElement('w:hyperlink'); h.set(qn('r:id'), r_id)
    r = OxmlElement('w:r'); rPr = OxmlElement('w:rPr')
    c = OxmlElement('w:color'); c.set(qn('w:val'), '0563C1'); rPr.append(c)
    u = OxmlElement('w:u'); u.set(qn('w:val'), 'single'); rPr.append(u)
    sz = OxmlElement('w:sz'); sz.set(qn('w:val'), str(size * 2)); rPr.append(sz)
    if bold: rPr.append(OxmlElement('w:b'))
    r.append(rPr)
    t = OxmlElement('w:t'); t.text = text or url; t.set(qn('xml:space'), 'preserve'); r.append(t)
    h.append(r); p._p.append(h); p.paragraph_format.space_after = Pt(6)
    return p


def TITLU(text, size=16, before=120):
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(before); p.paragraph_format.space_after = Pt(12)
    _runs(p, text, bold=True, size=size)
    return p


def H(text, size=13):
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(10); p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.keep_with_next = True
    _runs(p, text, bold=True, size=size)
    return p


def PAGEBREAK():
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)


def IMAGINE(fname, width=None, legenda=None, max_h_cm=20.5):
    from PIL import Image
    path = os.path.join(IMG, fname)
    w, h = Image.open(path).size
    width = width or CONTENT_W
    if h / w * width > Cm(max_h_cm):
        width = int(Cm(max_h_cm) * w / h)
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.keep_with_next = bool(legenda); p.paragraph_format.space_after = Pt(2)
    p.add_run().add_picture(path, width=width)
    if legenda:
        P(legenda, size=10, italic=True, align='center', space_after=10, color=(0x40, 0x40, 0x40))


def CHENAR(fname, legenda=None, max_h_cm=20.5):
    """captură de ecran cu chenar subțire (pentru lizibilitate pe fond alb)"""
    from PIL import Image
    path = os.path.join(IMG, fname)
    w, h = Image.open(path).size
    width = CONTENT_W - Cm(0.3)
    if h / w * width > Cm(max_h_cm):
        width = int(Cm(max_h_cm) * w / h)
    t = doc.add_table(rows=1, cols=1); t.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = t.rows[0].cells[0]; cell.width = width + Cm(0.3)
    _borders(cell, 'A6A6A6')
    p = cell.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.add_run().add_picture(path, width=width)
    if legenda:
        P(legenda, size=10, italic=True, align='center', space_after=8, color=(0x40, 0x40, 0x40))
    else:
        doc.add_paragraph().paragraph_format.space_after = Pt(2)


def _borders(cell, color='808080', sz='6'):
    tcPr = cell._tc.get_or_add_tcPr(); b = OxmlElement('w:tcBorders')
    for side in ('top', 'left', 'bottom', 'right'):
        e = OxmlElement('w:' + side); e.set(qn('w:val'), 'single'); e.set(qn('w:sz'), sz); e.set(qn('w:color'), color); b.append(e)
    tcPr.append(b)


def PLACEHOLDER(text, h_pt=50):
    t = doc.add_table(rows=1, cols=1)
    cell = t.rows[0].cells[0]; _borders(cell); cell.width = CONTENT_W
    p = cell.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(h_pt); p.paragraph_format.space_after = Pt(h_pt)
    _runs(p, '«' + text + '»', size=11, italic=True)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)


def TABEL(rows, widths, header=True, size=10.5):
    t = doc.add_table(rows=0, cols=len(widths)); t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, row in enumerate(rows):
        cells = t.add_row().cells
        for j, (txt, w) in enumerate(zip(row, widths)):
            c = cells[j]; c.width = Cm(w); _borders(c, '808080', '4')
            p = c.paragraphs[0]; p.paragraph_format.space_after = Pt(1)
            _runs(p, str(txt), bold=(header and i == 0), size=size)
            if header and i == 0:
                shd = OxmlElement('w:shd'); shd.set(qn('w:val'), 'clear'); shd.set(qn('w:color'), 'auto'); shd.set(qn('w:fill'), 'E7E6E6')
                c._tc.get_or_add_tcPr().append(shd)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)
    return t


# ---------------------------------------------------------------- pagina de titlu
TITLU('S.A.5.2 – Formarea personalului didactic din învățământul profesional și tehnic, inclusiv dual', size=18, before=120)
P('Documente justificative – luna septembrie 2026 (L3)', bold=True, size=14, align='center', space_after=4)
P('Raportul de progres nr. 1 (iulie – septembrie 2026)', size=13, align='center', space_after=30)
P('Proiect: UNIC – „Uniți pentru Nevoile Incluzive și Continuitatea Educației Elevilor”, cod SMIS 352704', size=11, align='center', space_after=2)
P('Beneficiar: Asociația Grupul de Acțiune Locală Napoca Porolissum', size=11, align='center', space_after=2)
P('Contract de finanțare nr. 11205/16.06.2026 – Programul Educație și Ocupare 2021-2027', size=11, align='center', space_after=2)
P('Acțiunea 8.f.1 – formarea personalului didactic din ÎPT (GSCS 8.F)', size=11, align='center', space_after=30)
P('Conținut:', bold=True, size=11, space_after=2)
CUPRINS = ['Fișa activității',
           'Recrutarea cadrelor didactice și identificarea furnizorului de formare (iulie – august 2026)',
           'Documentele contractuale: contractul de servicii, ordinul de începere, transmiterea către prestator',
           'Programul de formare acreditat și calendarul activităților de formare',
           'Debutul cursului (10.09.2026): informarea cursanților, suportul de curs, portofoliul cursantului',
           'Capturi de ecran din sesiunile online sincrone (10, 15 și 16.09.2026)',
           'Evidențele de participare',
           'Corespondența cu furnizorul în perioada derulării contractului',
           'Etape următoare (în afara perioadei de raportare)']
for i, item in enumerate(CUPRINS, 1):
    P(f'{i}. {item}', size=11, space_after=1)
P('', space_after=24)
P('Întocmit: «funcția, nume prenume»', size=11, space_after=2)
P('Avizat: Manager de proiect, Baba Alina-Ioana', size=11, space_after=2)
P('Capturile de ecran din sesiunile online au fost realizate de echipa de proiect în timpul sesiunilor (data și ora sunt vizibile în bara de activități a sistemului și în antetul Google Meet). '
  'Setul complet de capturi (48 de fișiere, 10 – 16.09.2026) și înregistrarea video a sesiunii din 10.09.2026 sunt arhivate electronic în dosarul activității; '
  'în acest document este inclusă o selecție reprezentativă, în ordine cronologică.', size=10, italic=True, space_after=2)

# ---------------------------------------------------------------- 1. fișa activității
PAGEBREAK()
TITLU('1. FIȘA ACTIVITĂȚII')
TABEL([
    ['Element', 'Date'],
    ['Subactivitate', 'SA5.2 – Formarea personalului didactic din ÎPT, inclusiv dual (acțiunea 8.f.1, GSCS 8.F); rezultat vizat: R17 – 4 cadre didactice formate'],
    ['Perioada de desfășurare', 'iulie – august 2026: recrutarea cadrelor didactice și identificarea furnizorului; 28.08.2026: contractarea; 10 – 18.09.2026: programul de formare (online); 09.10.2026: evaluarea finală (în afara perioadei de raportare)'],
    ['Furnizorul de formare', 'Asociația Proeuro-Cons, Slatina, jud. Olt (CIF 30793978) – furnizor de programe de formare continuă acreditate de Ministerul Educației și Cercetării'],
    ['Programul de formare', '„Abilitare informațională în combaterea abandonului școlar: un ghid pentru cadre didactice” – program complementar, categoria 2, domeniul tematic „Reziliență școlară”'],
    ['Acreditare', 'Aviz nr. 1555/DGMCDRSIP/30.06.2025, valabil 30.06.2025 – 01.07.2028; 12 credite profesionale transferabile (minimum 10 – maximum 12 CPT)'],
    ['Durata și forma', '30 de ore, integral online: 12 ore sincron (Google Meet) + 18 ore asincron (platforma Moodle a furnizorului); 12 ore componentă teoretică + 18 ore componentă practică'],
    ['Structura', 'Modulul 1 – Fundamentele abandonului școlar (10 h); Modulul 2 – Intervenții și strategii de prevenire a abandonului școlar (15 h); Modulul 3 – Monitorizarea eficienței intervențiilor de combatere a abandonului școlar (5 h)'],
    ['Seria / grupa', 'Seria 1, Grupa 1 – 4 cursanți înscriși (Calendarul activităților de formare nr. 445/28.08.2026)'],
    ['Formator', 'Nicoară Remus (Asociația Proeuro-Cons); responsabil program: Bold Nicolae'],
    ['Cursanți', '4 cadre didactice din unitățile de învățământ partenere, înregistrate în grupul țintă (categoria „personal didactic”): 3 de la Colegiul Tehnic Turda și 1 de la Liceul Teologic Reformat Cluj-Napoca'],
    ['Contract', 'Contract de servicii de formare cadre didactice nr. 2026082804/28.08.2026, semnat electronic de ambele părți la 28.08.2026; valoare 12.400,00 lei (3.100,00 lei/participant), prestatorul nefiind plătitor de TVA; valoare estimată: 24.000,00 lei'],
    ['Ordin de începere', 'nr. 2026082809/28.08.2026, semnat electronic de ambele părți; contractul și ordinul au fost transmise prestatorului prin e-mail la 01.09.2026, respectiv 04.09.2026'],
    ['Evaluarea finală', '09.10.2026, online sincron (Comisia de evaluare finală a furnizorului); documentele de absolvire se eliberează în maximum 30 de zile de la evaluare'],
    ['Facilități suplimentare contractate', 'două sesiuni fizice de orientare și sprijin aplicativ (maximum 3 ore fiecare), la Huedin și la Turda, fără cost suplimentar, programate de comun acord după finalizarea programului'],
], [4.2, 13.8])

# ---------------------------------------------------------------- 2. recrutare + furnizor
PAGEBREAK()
TITLU('2. RECRUTAREA CADRELOR DIDACTICE ȘI IDENTIFICAREA FURNIZORULUI')
P('În lunile iulie – august 2026, Expertul grup țintă 2 a identificat, împreună cu conducerile unităților de învățământ partenere, cadrele didactice care lucrează direct cu elevii din grupul țintă și le-a informat cu privire la programul de formare; '
  'în paralel au fost identificați furnizorii de programe de formare continuă acreditate și au fost transmise solicitările de ofertă (procedura de achiziție este descrisă în SA2.1).', align='justify', size=11)
H('Cadrele didactice recrutate (grupa de formare)')
TABEL([
    ['Nr.', 'Cadrul didactic', 'Specializarea', 'Unitatea de învățământ'],
    ['1', 'Anderco Claudia-Maria', 'Limba și literatura română', 'Liceul Teologic Reformat Cluj-Napoca'],
    ['2', 'Tiron Maria-Emilia', 'Limba și literatura română – limba engleză', 'Colegiul Tehnic Turda'],
    ['3', 'Arkosi Corina-Lorena', 'Fizică (predă și matematică)', 'Colegiul Tehnic Turda'],
    ['4', 'Pleșoiu Viorica', 'Fizică – informatică', 'Colegiul Tehnic Turda'],
], [1.0, 5.0, 5.8, 6.2])
P('Sursa: „Lista profesori curs (4 cadre didactice recrutate)” – evidența Expertului GT 2. Dosarele de grup țintă ale cadrelor didactice (formular de înregistrare, declarații, adeverințe de la unitățile de învățământ) sunt atașate la SA4.1/SA4.2. '
  '«De verificat față de planificarea inițială (cadre didactice de la Turda și Huedin): grupa include un cadru didactic de la Liceul Teologic Reformat Cluj-Napoca, partener asociat din 09.09.2026 – de explicat în raport dacă reprezintă o modificare.»', size=10, italic=True, align='justify')
H('Corespondența pentru identificarea furnizorului')
CHENAR('coresp_02.jpg', 'Solicitare de colaborare – formatori pentru program de formare (e-mail transmis la 13.08.2026)')
PAGEBREAK()
CHENAR('coresp_01.jpg', 'Solicitările de ofertă pentru servicii de formare a cadrelor didactice, transmise furnizorilor acreditați la 19.08.2026 (căsuța de e-mail a proiectului)')

# ---------------------------------------------------------------- 3. documente contractuale
PAGEBREAK()
TITLU('3. DOCUMENTELE CONTRACTUALE')
P('Contractul de servicii de formare cadre didactice nr. 2026082804/28.08.2026 a fost încheiat în urma procedurii de achiziție directă (Referat de necesitate nr. 2026082407/24.08.2026, Nota justificativă din 26.08.2026) și semnat electronic de ambele părți la 28.08.2026. '
  'Ordinul de începere nr. 2026082809/28.08.2026 a fost emis în aceeași zi. Dosarul achiziției a fost încărcat în modulul Achiziții din MySMIS2021 la 07.09.2026.', align='justify', size=11)
IMAGINE('contract-01.jpg', legenda='Contractul de servicii de formare cadre didactice nr. 2026082804/28.08.2026 – pagina 1 (extras; contractul integral, 11 pagini, este atașat la dosarul achiziției)', max_h_cm=18.5)
PAGEBREAK()
IMAGINE('contract-11.jpg', legenda='Contractul nr. 2026082804/28.08.2026 – pagina de semnături (semnături electronice: achizitor 28.08.2026, ora 10:30; prestator 28.08.2026, ora 10:33)', max_h_cm=20.5)
PAGEBREAK()
IMAGINE('ordin-1.jpg', legenda='Ordinul de începere a contractului de prestări servicii formare cadre didactice nr. 2026082809/28.08.2026, semnat electronic de ambele părți', max_h_cm=20.5)
PAGEBREAK()
CHENAR('coresp_04.jpg', 'Transmiterea contractului semnat către Asociația Proeuro-Cons – e-mail din 01.09.2026')
CHENAR('coresp_05.jpg', 'Transmiterea ordinului de începere către Asociația Proeuro-Cons – e-mail din 04.09.2026')

# ---------------------------------------------------------------- 4. program acreditat + calendar
PAGEBREAK()
TITLU('4. PROGRAMUL DE FORMARE ACREDITAT ȘI CALENDARUL ACTIVITĂȚILOR')
P('Programul „Abilitare informațională în combaterea abandonului școlar: un ghid pentru cadre didactice” figurează în Lista cursurilor de pregătire profesională acreditate de Ministerul Educației și Cercetării (actualizată la 15.05.2026), '
  'cu Avizul nr. 1555/DGMCDRSIP/30.06.2025, valabil până la 30.06.2028, 30 de ore, 12 CPT, domeniul tematic „Reziliență școlară”. Extrasul din listă (paginile 1 și 100) a fost certificat de reprezentantul legal al beneficiarului și face parte din dosarul achiziției.', align='justify', size=11)
IMAGINE('acreditare-2.jpg', legenda='Lista programelor acreditate – pagina 100 din 116: programele Asociației Proeuro-Cons, inclusiv „Abilitare informațională în combaterea abandonului școlar” (Aviz 1555/DGMCDRSIP/30.06.2025, 30 ore, 12 CPT)', max_h_cm=12)
PAGEBREAK()
P('Calendarul activităților de formare nr. 445/28.08.2026 (Anexa nr. 2 la Procedura specifică nr. 29.611/24.07.2025 a Ministerului Educației și Cercetării), avizat de reprezentantul legal al furnizorului și de responsabilul de program, '
  'stabilește perioada formării 10 – 18.09.2026, locația (platforma online a furnizorului – Google Workspace și Moodle), distribuția celor 30 de ore pe module și pe tipuri de activitate și data evaluării finale (09.10.2026, ora 16:00, online sincron).', align='justify', size=11)
P('Sesiunile online sincrone (12 ore) conform calendarului: 10.09.2026 (4 h), 15.09.2026 (2 h), 16.09.2026 (3 h) și 17.09.2026 (3 h); activitățile asincrone (18 ore) s-au desfășurat pe platforma Moodle în zilele de 11, 12, 14, 15, 16, 17 și 18.09.2026.', align='justify', size=11)
IMAGINE('calendar-1.jpg', legenda='Calendarul activităților de formare nr. 445/28.08.2026 – pagina 1', max_h_cm=12.5)
PAGEBREAK()
IMAGINE('calendar-2.jpg', legenda='Calendarul activităților de formare nr. 445/28.08.2026 – pagina 2 (sesiunile din 14 – 18.09.2026, evaluarea finală din 09.10.2026, avizare)', max_h_cm=13)

# ---------------------------------------------------------------- 5. debutul cursului
PAGEBREAK()
TITLU('5. DEBUTUL CURSULUI – 10.09.2026')
P('La 09.09.2026 furnizorul a transmis cursanților și beneficiarului e-mailul „Informații debut curs”, cu confirmarea înscrierii, calendarul activităților, linkul sesiunilor Google Meet (sesiunea din 10.09.2026, 16:00 – 20:00), '
  'regulile de participare (prezență minimă, utilizarea numelui complet pentru evidențele de participare), structura portofoliului cursantului și informații privind evaluarea finală și eliberarea documentelor de absolvire. '
  'E-mailul a fost retransmis membrilor echipei de proiect la 10.09.2026, ora 08:37.', align='justify', size=11)
CHENAR('email_debut_1.jpg', 'E-mailul „Informații debut curs” – partea 1: confirmarea înscrierii, data începerii (10.09.2026), formatorul, linkul Google Meet')
PAGEBREAK()
CHENAR('email_debut_2.jpg', 'E-mailul „Informații debut curs” – partea 2: calendarul, platforma Moodle, condițiile de participare')
CHENAR('email_debut_3.jpg', 'E-mailul „Informații debut curs” – partea 3: evaluarea finală, documentele de absolvire, atașamentele (OMEC 3986/2025, procedura specifică, calendarul, portofoliul cursantului, suportul de curs)')
PAGEBREAK()
H('Suportul de curs și portofoliul cursantului')
P('Cursanții au primit suportul de curs în format electronic („Abilitare informațională în combaterea abandonului școlar: un ghid pentru cadre didactice” – program de dezvoltare profesională continuă complementar, Asociația Proeuro-Cons, 29 de pagini), '
  'pagina de gardă a portofoliului cursantului cu structura acestuia, precum și OMEC nr. 3986/2025 și Procedura specifică nr. 29.611/24.07.2025 cu Anexa 2. Materialele sunt arhivate în dosarul activității.', align='justify', size=11)
t = doc.add_table(rows=1, cols=2); t.alignment = WD_TABLE_ALIGNMENT.CENTER
for cell, f in zip(t.rows[0].cells, ['suport-01.jpg', 'suport-02.jpg']):
    cp = cell.paragraphs[0]; cp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cp.add_run().add_picture(os.path.join(IMG, f), width=Cm(8.4))
P('Suportul de curs – coperta și prima pagină a Modulului 1 („Fundamentele abandonului școlar”)', size=10, italic=True, align='center', space_after=10, color=(0x40, 0x40, 0x40))
H('Înregistrarea sesiunii din 10.09.2026')
P('Sesiunea de debut (Google Meet „AIC S1G1-2026”, 10.09.2026, 15:49 – 19:54) a fost înregistrată; fișierul video (3,2 GB) este arhivat în dosarul electronic al activității și poate fi pus la dispoziția ofițerului de monitorizare la cerere.', align='justify', size=11)
LINK(DRIVE_INREG, 'Înregistrarea sesiunii din 10.09.2026 – link de acces (Google Drive, dosarul proiectului)')

# ---------------------------------------------------------------- 6. capturi sesiuni
SESIUNI = [
    ('10.09.2026', '16:00 – 20:00 (4 ore sincron) – Modulul 1 – Fundamentele abandonului școlar',
     [('meet_2361.jpg', 'Sesiunea din 10.09.2026, ora 16:04 – deschiderea sesiunii: formatorul și cele 4 cadre didactice conectate (Google Meet „AIC S1G1-2026”)'),
      ('meet_2364.jpg', 'Sesiunea din 10.09.2026, ora 16:22 – material video prezentat de formator (ecran partajat)'),
      ('meet_2365.jpg', 'Sesiunea din 10.09.2026, ora 16:22 – participanții în timpul prezentării'),
      ('meet_2367.jpg', 'Sesiunea din 10.09.2026, ora 17:01 – participanții în timpul sesiunii'),
      ('meet_2374.jpg', 'Sesiunea din 10.09.2026, ora 18:04 – participanții în timpul sesiunii'),
      ('meet_2378.jpg', 'Material de curs prezentat în sesiunea din 10.09.2026 – „Corpul astral (emoții) – energetic” (suportul de curs deschis pe ecranul partajat)'),
      ('meet_2380.jpg', 'Sesiunea din 10.09.2026, ora 19:41 – prezentarea „Personalitatea omului” (ecran partajat de formator)'),
      ('meet_2381.jpg', 'Sesiunea din 10.09.2026, ora 19:53 – încheierea sesiunii')]),
    ('15.09.2026', '16:00 – 20:00, din care 2 ore sincron – Modulul 2 – Intervenții și strategii de prevenire a abandonului școlar',
     [('meet_2382.jpg', 'Sesiunea din 15.09.2026, ora 18:04 – deschiderea părții sincrone: formatorul și cele 4 cadre didactice'),
      ('meet_2385.jpg', 'Sesiunea din 15.09.2026, ora 18:50 – „Personalitatea omului” (ecran partajat de formator)'),
      ('meet_2386.jpg', 'Material de curs prezentat în sesiunea din 15.09.2026 – etapele dezvoltării sistemului intelectual (14 – 21 de ani)'),
      ('meet_2388.jpg', 'Sesiunea din 15.09.2026, ora 19:16 – etapele dezvoltării copilului și tânărului (ecran partajat)'),
      ('meet_2390.jpg', 'Sesiunea din 15.09.2026, ora 19:23 – „Temperamentele umane – cele patru temperamente”'),
      ('meet_2391.jpg', 'Sesiunea din 15.09.2026, ora 19:25 – temperamentul coleric (ecran partajat)'),
      ('meet_2395.jpg', 'Sesiunea din 15.09.2026, ora 19:49 – temperamentul flegmatic (ecran partajat)'),
      ('meet_2398.jpg', 'Sesiunea din 15.09.2026, ora 19:59 – sinteza celor patru temperamente, încheierea sesiunii')]),
    ('16.09.2026', '16:00 – 20:00, din care 3 ore sincron – Modulul 2 – Intervenții și strategii de prevenire a abandonului școlar',
     [('meet_2399.jpg', 'Sesiunea din 16.09.2026, ora 17:11 – „Libera inițiativă” (ecran partajat de formator)'),
      ('meet_2400.jpg', 'Material de curs prezentat în sesiunea din 16.09.2026 – „Libera inițiativă”'),
      ('meet_2401.jpg', 'Sesiunea din 16.09.2026, ora 17:22 – „Critică / Feedback corectiv” (ecran partajat)'),
      ('meet_2403.jpg', 'Sesiunea din 16.09.2026, ora 17:44 – „Harta conștiinței” (ecran partajat)'),
      ('meet_2404.jpg', 'Material de curs prezentat în sesiunea din 16.09.2026 – „Imitarea”'),
      ('meet_2406.jpg', 'Sesiunea din 16.09.2026, ora 18:11 – „Omul educat” (ecran partajat)'),
      ('meet_2407.jpg', 'Sesiunea din 16.09.2026, ora 18:20 – tipurile de inteligență (ecran partajat)'),
      ('meet_2408.jpg', 'Sesiunea din 16.09.2026, ora 18:24 – tipurile de inteligență (continuare)')]),
]
PAGEBREAK()
TITLU('6. CAPTURI DE ECRAN DIN SESIUNILE ONLINE SINCRONE')
P('Sesiunile sincrone s-au desfășurat pe Google Meet (întâlnirea „AIC S1G1-2026”, cod MNVTJBUYNH), cu formatorul Nicoară Remus și cele 4 cadre didactice. Capturile de mai jos au fost realizate în timpul sesiunilor; '
  'data și ora sunt vizibile în bara de activități (colțul din dreapta jos) și în antetul Google Meet. Capturile care redau ecranul partajat de formator documentează conținutul parcurs (suportul de curs și materialele de prezentare).', align='justify', size=11)
for zi, interval, capturi in SESIUNI:
    PAGEBREAK()
    H(f'Sesiunea din {zi} – {interval}', size=12)
    for i, (f, leg) in enumerate(capturi):
        if i and i % 2 == 0:
            PAGEBREAK()
        CHENAR(f, leg, max_h_cm=9.6)
PAGEBREAK()
H('Sesiunea din 17.09.2026 – 16:00 – 20:00, din care 3 ore sincron – Modulele 2 și 3', size=12)
PLACEHOLDER('capturi de ecran din sesiunea sincronă din 17.09.2026 – nu au fost identificate în dosarul electronic; se adaugă dacă au fost realizate (sau se menționează că sesiunea este documentată prin raportul de prezență al furnizorului)', h_pt=80)

# ---------------------------------------------------------------- 7. prezența
PAGEBREAK()
TITLU('7. EVIDENȚELE DE PARTICIPARE')
P('Participarea la sesiunile sincrone este evidențiată prin rapoartele de participare generate automat de Google Meet (fișierul „AIC S1G1-10.09.2026-PREZENTA.xlsx” pentru sesiunea de debut) și prin evidențele nominale ale furnizorului, '
  'care, conform art. 3.3 din contract, pune la dispoziția beneficiarului documentele de prezență, centralizatoarele și raportul de activitate. Sinteza raportului Google Meet pentru 10.09.2026:', align='justify', size=11)
TABEL([
    ['Participant', 'Calitatea', 'Prima conectare', 'Ultima deconectare'],
    ['Nicoară Remus', 'formator', '15:40', '19:54'],
    ['Anderco Claudia-Maria', 'cursant', '16:00', '19:54'],
    ['Arkosi Corina-Lorena', 'cursant', '16:00', '19:54'],
    ['Pleșoiu Viorica', 'cursant', '16:00', '19:54'],
    ['Tiron Maria-Emilia', 'cursant', '16:02', '19:54'],
], [5.5, 3.0, 4.5, 5.0])
P('Toate cele 4 cadre didactice au participat la sesiunea de debut pe întreaga durată (reconectările din timpul sesiunii sunt consemnate în raport). '
  '«Rapoartele de participare pentru sesiunile din 15, 16 și 17.09.2026 și evidența activităților asincrone de pe platforma Moodle se solicită furnizorului odată cu raportul de activitate, înainte de recepția serviciilor.»', align='justify', size=11)

# ---------------------------------------------------------------- 8. corespondența
PAGEBREAK()
TITLU('8. CORESPONDENȚA CU FURNIZORUL')
P('Comunicarea cu furnizorul s-a realizat prin e-mail, de pe adresa proiectului, și a vizat transmiterea documentelor contractuale, constituirea grupei, informațiile de debut și derularea sesiunilor.', align='justify', size=11)
CHENAR('coresp_03.jpg', 'Corespondența cu Asociația Proeuro-Cons în luna septembrie 2026 (căsuța de e-mail a proiectului – firul „Informații debut curs” și mesajele conexe)')

# ---------------------------------------------------------------- 9. etape următoare
PAGEBREAK()
TITLU('9. ETAPE URMĂTOARE (ÎN AFARA PERIOADEI DE RAPORTARE)')
B('09.10.2026 – evaluarea finală a cursanților, online sincron, pe baza portofoliilor realizate pe parcursul programului;')
B('în maximum 30 de zile de la evaluare – eliberarea documentelor de absolvire (certificate/atestate cu 12 CPT) de către furnizor și transmiterea lor cursanților;')
B('recepția serviciilor de formare (proces-verbal de recepție, raportul de activitate și evidențele nominale ale furnizorului), factura și plata (12.400,00 lei);')
B('organizarea celor două sesiuni fizice de orientare și sprijin aplicativ (Huedin și Turda), conform art. 5.4 din contract, la date stabilite de comun acord;')
B('raportarea rezultatului R17 (4 cadre didactice formate și certificate) și a indicatorilor aferenți în Raportul de progres nr. 2, cu atașarea copiilor documentelor de absolvire.')
P('', space_after=20)
P('Întocmit: «funcția, nume prenume» ______________________', size=11, space_after=14)
P('Avizat: Manager de proiect, Baba Alina-Ioana ______________________', size=11)

doc.save(OUT)
print('OK ->', OUT, os.path.getsize(OUT) // 1024, 'KB')
