# -*- coding: utf-8 -*-
import docx, re
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

doc = docx.Document()

# ---------- page setup ----------
s = doc.sections[0]
s.page_width, s.page_height = Cm(21.0), Cm(29.7)
s.left_margin = s.right_margin = Cm(2.2)
s.top_margin = Cm(2.0); s.bottom_margin = Cm(2.0)

INK   = RGBColor(0x1A, 0x1A, 0x1A)
BLUE  = RGBColor(0x00, 0x3D, 0x82)
GREY  = RGBColor(0x5A, 0x5A, 0x5A)
RED   = RGBColor(0x9B, 0x1C, 0x1C)

st = doc.styles
n = st['Normal']
n.font.name = 'Calibri'; n.font.size = Pt(10.5); n.font.color.rgb = INK
n._element.rPr.rFonts.set(qn('w:eastAsia'), 'Calibri')
n.paragraph_format.space_after = Pt(6)
n.paragraph_format.line_spacing = 1.12

def cfg(name, size, bold, color, before, after, keep=False):
    x = st[name]
    x.font.name = 'Calibri'; x.font.size = Pt(size); x.font.bold = bold
    x.font.color.rgb = color
    x.paragraph_format.space_before = Pt(before)
    x.paragraph_format.space_after  = Pt(after)
    x.paragraph_format.keep_with_next = keep
    return x

cfg('Heading 1', 17, True, BLUE, 20, 8, True)
cfg('Heading 2', 14, True, BLUE, 16, 6, True)
cfg('Heading 3', 12, True, INK,  12, 4, True)
cfg('Heading 4', 10.5, True, GREY, 10, 3, True)

def shade(cell, hexcolor):
    tcPr = cell._tc.get_or_add_tcPr()
    sh = OxmlElement('w:shd'); sh.set(qn('w:val'), 'clear')
    sh.set(qn('w:color'), 'auto'); sh.set(qn('w:fill'), hexcolor)
    tcPr.append(sh)

def borders(tbl, color='BFBFBF', sz=4):
    tblPr = tbl._tbl.tblPr
    b = OxmlElement('w:tblBorders')
    for edge in ('top','left','bottom','right','insideH','insideV'):
        e = OxmlElement('w:'+edge)
        e.set(qn('w:val'),'single'); e.set(qn('w:sz'),str(sz))
        e.set(qn('w:space'),'0'); e.set(qn('w:color'),color)
        b.append(e)
    tblPr.append(b)

# ---------- inline markup: **bold**, //italic// ----------
TOK = re.compile(r'(\*\*.+?\*\*|//.+?//)', re.S)
def runs(p, text, size=None, color=None, italic=False, bold=False):
    for part in TOK.split(text):
        if not part: continue
        b, i = bold, italic
        if part.startswith('**') and part.endswith('**'): part, b = part[2:-2], True
        elif part.startswith('//') and part.endswith('//'): part, i = part[2:-2], True
        r = p.add_run(part); r.bold = b; r.italic = i
        if size: r.font.size = Pt(size)
        if color is not None: r.font.color.rgb = color
    return p

CHARS = {'n': 0}
def clean(t):
    return re.sub(r'\s+', ' ', re.sub(r'\*\*|//', '', t)).strip()

# ---------- block helpers ----------
def H1(t): doc.add_paragraph(t, style='Heading 1')
def H2(t): doc.add_paragraph(t, style='Heading 2')
def H3(t): doc.add_paragraph(t, style='Heading 3')
def H4(t): doc.add_paragraph(t, style='Heading 4')

def P(t, count=True):
    p = doc.add_paragraph(); runs(p, t)
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    if count: CHARS['n'] += len(clean(t)) + 1
    return p

def SMALL(t):
    p = doc.add_paragraph(); runs(p, t, size=8.5, color=GREY, italic=True)
    p.paragraph_format.space_after = Pt(8)
    return p

def FLAG(t):
    p = doc.add_paragraph(); p.paragraph_format.left_indent = Cm(0.4)
    p.paragraph_format.space_before = Pt(2); p.paragraph_format.space_after = Pt(6)
    runs(p, t, size=9, color=RED)
    return p

def BUL(items, count=True):
    for it in items:
        p = doc.add_paragraph(style='List Bullet'); runs(p, it)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.left_indent = Cm(0.6)
        if count: CHARS['n'] += len(clean(it)) + 1

def NUM(items):
    for it in items:
        p = doc.add_paragraph(style='List Number'); runs(p, it)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.left_indent = Cm(0.6)
        CHARS['n'] += len(clean(it)) + 1

def Q(t):
    """A question of the online form."""
    tbl = doc.add_table(rows=1, cols=1); tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    c = tbl.cell(0,0); shade(c, 'E8EEF7'); borders(tbl, 'C7D6EA', 4)
    p = c.paragraphs[0]; runs(p, t, size=10, color=BLUE, bold=True)
    p.paragraph_format.space_before = Pt(3); p.paragraph_format.space_after = Pt(3)
    doc.add_paragraph().paragraph_format.space_after = Pt(0)
    CHARS['n'] = 0          # start counting this answer

def COUNT(limit=5000, cut=None):
    n = CHARS['n']
    p = doc.add_paragraph()
    over = n > limit
    mark = 'within limit' if not over else 'OVER by %s — see below' % f'{n - limit:,}'
    runs(p, '≈ %s characters (assumed form limit %s — %s)' % (f'{n:,}', f'{limit:,}', mark),
         size=8, color=GREY if not over else RED, italic=True)
    p.paragraph_format.space_after = Pt(2 if over else 10)
    if over and cut:
        q = doc.add_paragraph(); q.paragraph_format.left_indent = Cm(0.4)
        q.paragraph_format.space_after = Pt(10)
        runs(q, 'HOW TO CUT IT: ' + cut, size=8.5, color=RED)
    CHARS['n'] = 0

def TBL(rows, widths=None, header=True, small=False, count=True):
    t = doc.add_table(rows=len(rows), cols=len(rows[0]))
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    borders(t)
    t.autofit = True
    for ri, row in enumerate(rows):
        for ci, val in enumerate(row):
            c = t.cell(ri, ci)
            c.text = ''
            p = c.paragraphs[0]
            p.paragraph_format.space_before = Pt(2); p.paragraph_format.space_after = Pt(2)
            first = True
            for line in str(val).split('\n'):
                tgt = p if first else c.add_paragraph()
                if not first:
                    tgt.paragraph_format.space_before = Pt(0); tgt.paragraph_format.space_after = Pt(2)
                runs(tgt, line, size=8.5 if small else 9.5,
                     bold=(header and ri == 0), color=BLUE if (header and ri == 0) else None)
                first = False
            if header and ri == 0: shade(c, 'E8EEF7')
            if count: CHARS['n'] += len(clean(str(val))) + 1
    if widths:
        for ri in range(len(rows)):
            for ci, w in enumerate(widths):
                t.cell(ri, ci).width = Cm(w)
    doc.add_paragraph().paragraph_format.space_after = Pt(0)
    return t

def CALLOUT(title, body, fill='FFF6E5', line='E8C97A'):
    tbl = doc.add_table(rows=1, cols=1); tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    c = tbl.cell(0,0); shade(c, fill); borders(tbl, line, 6)
    p = c.paragraphs[0]; runs(p, title, size=9.5, bold=True)
    p.paragraph_format.space_before = Pt(3)
    q = c.add_paragraph(); runs(q, body, size=9.5)
    q.paragraph_format.space_after = Pt(3)
    doc.add_paragraph().paragraph_format.space_after = Pt(0)

def PAGEBREAK():
    doc.add_page_break()

# =====================================================================
# COVER
# =====================================================================
p = doc.add_paragraph(); runs(p, 'ERASMUS+ KA152-YOU · MOBILITY OF YOUNG PEOPLE — YOUTH EXCHANGES', size=9, color=BLUE, bold=True)
p = doc.add_paragraph(); runs(p, 'VERIFAI', size=30, color=BLUE, bold=True)
p.paragraph_format.space_after = Pt(0)
p = doc.add_paragraph(); runs(p, 'Young Detectives Against Digital Disinformation', size=15, color=INK)
p.paragraph_format.space_after = Pt(12)
SMALL('Application content in English for the KA152-YOU online form · Call 2026, Round 2 · Deadline 1 October 2026, 12:00 Brussels time\n'
      'Applicant and coordinator: ASOCIAȚIA GRUPUL DE ACȚIUNE LOCALĂ NAPOCA POROLISSUM (E10181755 — RO) · National Agency: RO01 — ANPCDEFP\n'
      'Version 4 — revised against the review comments of 3 September 2026, **the live Call 2026 Round 2 application form**, the Erasmus+ 2026 Programme Guide, and the ANPCDEFP National Call 2026.')

CALLOUT('Aligned to the form you will actually fill in.',
        'Every question below is quoted **verbatim from the Call 2026 Round 2 form — Form ID KA152-YOU-691C4B41, deadline 01 Oct 2026 12:00 Brussels time** — and the sections follow that form’s own table of contents in its own order. '
        'This matters more than it sounds: the 2026 form differs from the 2024 one in several places, and two of them change what you have to do rather than just how a question is worded. '
        '**Each OID may appear in at most five Mobility of young people applications per round**, which is a real constraint for an active partner like YOBBA — check it before anything else. '
        'And the **Annexes** section carries a Timetable slot, so the full daily programme is annexed and the narrative field takes a summary; section 7.8 gives three, each with its measured length. Both are dealt with below.',
        'E8EEF7', 'C7D6EA')

CALLOUT('How to use this document.',
        'Each question of the online form appears in a blue box, exactly as it is worded in the form. The text underneath it is what goes into that field, '
        'and the grey line at the end of each answer gives you an approximate character count against the 5,000-character limit the form applies to most '
        'narrative fields. Red lines are actions that still have to be carried out before submission — they are not part of the answer and must be deleted '
        'before pasting. Everything marked [TO CONFIRM] depends on information that does not exist yet, mostly the two island partners.',
        'EAF3EA', '9FC49F')

H2('What changed in this version, and why')
SMALL('Internal note — not part of the form. Delete before pasting. This is the audit trail of the 27 review comments of 3 September 2026.')

TBL([
 ['#', 'Comment', 'What was changed'],
 ['C0', 'Give the exact source of the European percentages.',
  'The Flash Eurobarometer “Youth Survey 2024” (EP013EP), Ipsos for the European Parliament, 25,863 respondents aged 16–30, is now named in full at the point where the figures are first used, in the summary.'],
 ['C1, C23', 'Drop “pedagogical”; this is non-formal learning.',
  '“Pedagogical” is gone from the whole document. The method is now “the non-formal learning approach”, and the role is **Learning Programme Coordinator (non-formal learning)**, used consistently in the roles table, the daily programme, the evaluation section and the measurement-instruments pack.'],
 ['C2', 'The objectives are not SMART enough.',
  'The three objectives were rewritten with a named target group, a numeric threshold, the instrument that produces the number, and a calendar date rather than a month number. They are now worded identically in the summary, in the objectives table and in the evaluation table.'],
 ['C3, C18, C19', 'Stop calling them pupils; call them young people, and describe the profile properly.',
  '“Pupils” and “secondary-school pupils” are gone everywhere and replaced by “young people aged 14–17”. The profile now carries what actually matters: peripheral communities, daily AI and social-media use, thin access to non-formal and international opportunities, and the documented barriers. The age band is justified by shared needs, a similar stage of development and one coherent set of non-formal methods.'],
 ['C4, C26', 'Take schools out as venues and as main actors; use youth and community spaces.',
  'The four local initiatives are hosted in youth centres, libraries, community centres, the partner organisations’ own spaces and other accessible public spaces. The actors list now names youth organisations, libraries, community centres, local authorities and the Social Inclusion Centre. See the flagged decision at the end of this table.'],
 ['C5', '“Applicant” → “coordinator” for the Rural Youth Parliament project.', 'Changed.'],
 ['C6', 'Drop Growing Together; add EMPOWER.',
  'Growing Together is removed from the organisation’s description. EMPOWER takes its place, with the full title, action type, role and youth-work relevance to be completed — the sentence is built so those four facts drop straight in.'],
 ['C7, C10, C17, C27', 'Remove the survey of 94 adults from the needs analysis, the impact and the dissemination plan.',
  'The adult survey is out of the application entirely: needs, local impact, dissemination and the annex list. The evidence base is now the 153 young people, and the 96 of them aged 14–17. Parents stay in the document only in their real role — informing, supporting and protecting participants who are minors — not as a target group.'],
 ['C8', 'One of the two facilitators is designated by YOBBA.',
  'Written into the partner description, the roles table, the daily programme (the facilitators are now “Facilitator 1 — coordinator” and “Facilitator 2 — YOBBA”) and the observation arrangements. It was already implicit in the travel budget, which funds seven people from Türkiye.'],
 ['C9', 'After the partners are confirmed, show the need exists in each territory.',
  'A new subsection sets out the common consultation protocol all four partners run before submission — the same short instrument, at least 20–25 young people aged 14–17 per territory — and a table with one row per partner for the method, the number and profile consulted, and the main findings.'],
 ['C11', 'Say more naturally that the four contexts differ but the difficulties are similar.',
  'Rewritten. The paragraph now says plainly that the four communities do not look alike, and that what their young people share is narrower and more exact: unchecked information channels, almost no practical media-literacy offer, and a harder and more expensive route to any international activity.'],
 ['C12', 'Say the digital-transformation link in our own words, no quotations from the Guide.',
  'All quotation of the Guide is removed. The paragraph now describes what VERIFAI builds: responsible use of digital tools and AI, finding out where information came from, and telling manipulated or fabricated content from sound content. The 2026 national priority on tackling disinformation and promoting digital literacy is named.'],
 ['C13', 'Add the civic and electoral horizon.',
  'Added, in their own timescale: most of these participants vote for the first time within four to six years of this project, and the point is that by then they form opinions on information they have checked.'],
 ['C14', 'Rewrite inclusion around the participants’ concrete situation.',
  'Rewritten as four named barrier families — geographic, economic, linguistic, social — each with the measure that answers it, and cross-referenced to the detailed measures table.'],
 ['C15, C21, C22', 'No school portfolio, no recognition by schools.',
  'Every claim of school recognition is gone. Youthpass is presented as what it is: a process that helps a young person identify, document and present what they learned, and use it in further learning, volunteering, civic participation and the next mobility. The certificate of participation confirms participation and non-formal competences, and nothing else.'],
 ['C16', 'Take Ruraliada out of the local-impact description.',
  'Removed. The impact paragraph now refers to the community events the organisation runs annually, without naming that one.'],
 ['C20', 'Add a separate paragraph on how young people shaped the project.',
  'Added, as its own subsection: how they were consulted, what they asked for, and the three design decisions that exist because they asked — the venue inside the territory, no participation fee, and a programme with no lectures.'],
 ['C24', 'Preparatory visit: a staff member of the coordinator, not a facilitator.',
  'Changed, with the two tasks that person carries: verifying the logistical and safety arrangements on site, and finalising the mobility programme.'],
 ['C25', 'Check whether Turkish citizens really need a visa.',
  'Checked and kept, with the reason stated precisely: Romania has applied the Schengen acquis in full, land borders included, since 1 January 2025, and Turkish nationals holding ordinary passports are subject to the Schengen short-stay visa requirement. Re-verify with the Romanian Consulate General in İstanbul before submission — this is one of the things that changes.'],
], widths=[1.3, 5.4, 9.9], small=True, count=False)

H2('What changed after reading the live 2026 form')
SMALL('Internal note — not part of the form. Delete before pasting. Two of these reverse advice given in the previous version, which was aligned to the 2024 form; where that happened it is said plainly.')
TBL([
 ['What the 2026 form does', 'What it changes here'],
 ['**Annexes: the Declaration on Honour and the Timetable**, confirmed on the live form.',
  'The blank export rendered only the Declaration on Honour, and the caveat attached to that reading was the right one: a blank export does not show every upload slot. **The Timetable slot exists**, confirmed by opening the live form. '
  'So the full daily programme goes into the annexed timetable, where it has no character limit and where the expert expects to find it, and the narrative field carries a summary plus a pointer to it. Section 7.8 gives three '
  'ready-made versions of that summary with their measured lengths, so you can pick whichever the field actually takes. Check the Accession forms and Other Documents slots the same way while you are in there.'],
 ['**Each OID may be involved in at most five Mobility of young people applications per round** — coordinator or partner, it counts the same. Once the limit is reached the form will not let you submit.',
  'A genuine risk, and not for us. YOBBA has been a partner in six KA152 exchanges and is exactly the kind of organisation that gets asked again. **Ask YOBBA in writing, now, how many KA152 applications it is already in for this round**, and get the same confirmation from the two island partners when they are confirmed. Discovering this at 11:00 on 1 October is not a situation you can fix.'],
 ['**Participant contribution and fees is its own block inside Project details**, with the rules printed above the question.',
  'Moved out of the budget section and into section 7.4, where the form puts it, with our answer unchanged: no contribution of any kind.'],
 ['**Recognition of learning outcomes has two questions, not three.** The national-instrument question is gone.',
  '**This reverses part of the previous version.** The answer about the coordinator’s own certificate is kept, folded into the Youthpass answer where it still belongs, and marked so you can drop it if space is tight.'],
 ['**The quality standards are no longer printed in the form** — it links to an external PDF — and carry **three** confirmations, not one.',
  'Section 10 now lists all three. Note the middle one binds the co-beneficiaries as well, which is why adherence is written into the partnership agreement.'],
 ['**“Application conditions” is a new section** carrying EU values, **EU sanctions and restrictive measures**, original content and authorship, a data-protection acknowledgment, and the pre-submission checklist.',
  'The sanctions block is entirely new and was missing from the previous version. It needs a confirmation for the applicant **and every partner**. Section 12 covers all of it.'],
 ['**The authorship declaration now refers to the applicant organisation alone**, where the 2024 form said “the applicant and partner organisations”.',
  'Narrower, and stricter. Noted in section 12.'],
 ['**Two questions we “corrected” last time were right the first time.**',
  'The 2026 wording is “Are participants involved in activities facing challenges that hinder their participation?” and “Do you foresee Virtual/Blended activities and/or the use of any virtual component…?” — the original wording, not the 2024 variant. Reverted.'],
 ['**The activity list carries both “Number of participants” and “Number of persons”.**',
  'Added: 20 and 26. The distinction matters — participants are the 20 young people; persons includes the 4 group leaders and 2 facilitators.'],
 ['**The form’s own definition of a flow is printed in it**, and it confirms our split.',
  '“If some participants going to the same destination need to have different arrangements (for example, different travel distance or mode of travel, different duration etc.) then you should split that mobility flow into two or more separate ones.” Our four flows differ in exactly that way, so four is right.'],
], widths=[5.6, 11.0], small=True, count=False)

CALLOUT('Two decisions that are yours, not ours.',
        '**Schools.** Comments C4, C22 and C26 remove schools as venues, as recognition authorities and as main actors — all applied. But half the young people in our survey (50.0%) say school is where they hear about opportunities, and the previous expert assessment criticised the absence of a link to their educational path. The resolution written into this version: schools remain an **information channel** for the call, named as a channel and not as a project partner, while the link to the participants’ learning path is carried by Youthpass, by the local initiatives and by the peer-trainer role — not by any claim of school recognition. If you want schools out of the outreach section too, delete the two sentences marked in red there.\n'
        '**EMPOWER.** The organisation’s description needs the full title, the action, your role and one line on youth-work relevance. Until those arrive, that sentence is the only substantive gap in the applicant’s own profile.',
        'FDECEC', 'E3A9A9')

PAGEBREAK()

# =====================================================================
H1('0. Internal note — what this application does differently')
SMALL('Not part of the form. Delete before pasting. Keep it in the supporting file: it is the answer to the question the National Agency will ask if it compares the two applications.')

P('The previous application, //Inclusion2Income// (2026-1-RO01-KA152-YOU-000398541), scored 70/100 — Quality of project design 26/40, Quality of project management 21/30, '
  'Relevance, rationale and impact 23/30. It cleared every threshold and was still not competitive. The experts named five weaknesses. All five are structural, and all five '
  'are answered below, deliberately and visibly.', count=False)

TBL([
 ['What the experts wrote', 'What went wrong', 'What VERIFAI does differently'],
 ['“The two participant categories — 13–17 and 18–25 — have different needs and different approaches, and the mobility agenda does not take these differences into account.”',
  'One activity serving two populations that no youth worker would put in the same room for the same session.',
  'A single, tight age band: **14–17**. One group, one stage of development, one safeguarding regime, one set of non-formal methods. It also matches our evidence base exactly — the 96 young people aged 14–17 among our 153 respondents are the population the Romanian group is drawn from.'],
 ['“The mobility does not address young people’s need for education and does not encourage returning to school or continuing studies.”',
  'The link between the mobility and the participants’ own learning path was missing.',
  'The link is now built in, and it is built where this Action can actually deliver it: Youthpass is worked on from Day 1 as something a 16-year-old can use in the next learning activity, in volunteering, in a civic initiative and in the next mobility they apply for; each participant leaves with a role in a local initiative they design and lead; the toolkit stays with the youth workers, librarians and community educators who see them week to week; and the twenty continue as peer trainers in the partner organisations’ later activities. We do not claim recognition we cannot deliver.'],
 ['“The proposed activities are not clearly described, the link between them and the aim and objectives of the project is not visible, nor with the 8 targeted competences.” And: “the agenda does not name the persons responsible for coordinating the sessions.”',
  'This is where 14 of the 40 design points were lost.',
  'Every session in the agenda now carries five explicit attributes: the objective it serves, the method, the key competences it builds, the output it produces and the **named person responsible**. A separate competence matrix maps each of the eight European key competences to the sessions that build it and to the evidence that documents it. Nothing is claimed without a session and a piece of evidence behind it.'],
 ['“The application does not mention measures regarding the safety of the accommodation and of the spaces where activities take place.”',
  'An omission, cheap to fix, that cost management points.',
  'A dedicated venue-safety section: written risk assessment before contracting, verification in person during the preparatory visit, fire and evacuation, night supervision, room allocation, travel time to medical services and mobile signal coverage across the site.'],
 ['“None of the organisations has previous experience implementing projects under this Action.”',
  'A weakness the consortium could not argue away.',
  'YOBBA has taken part in **six KA152 youth exchanges** as a partner between 2022 and 2024, and the coordinator now has a KA154 project of its own under way. The consortium is no longer new to the Action, and this is stated where it counts.'],
], widths=[5.0, 4.0, 7.6], small=True, count=False)

CALLOUT('And one thing the previous application did not have at all.',
        'The three measurement instruments now exist as a written pack: the 15-item verification test with its marking scheme and a parallel Form B, the four-technique observation grid with its descriptors and observer-calibration protocol, and the ten-minute beneficiary exercise. '
        'Objectives O1, O2 and O3 are not assertions in this application — they are three instruments with thresholds fixed in advance, before any data exists, so that none of them can be adjusted later to rescue a result. '
        'What remains to be done is piloting them with 5–8 young people from the territory, and that is in the pre-submission list at the end.',
        'EAF3EA', '9FC49F')

PAGEBREAK()

# =====================================================================
H1('1. Context')

TBL([
 ['Field', 'Entry'],
 ['Project Title', 'VERIFAI: Young Detectives Against Digital Disinformation'],
 ['Project Acronym', 'VERIFAI'],
 ['Action', 'KA152-YOU — Mobility of young people / Youth Exchanges'],
 ['Project Start Date', '01/04/2027'],
 ['Project Duration', '18 months'],
 ['Project End Date', '30/09/2028'],
 ['National Agency of the applicant organisation', 'RO01 — Agenția Națională pentru Programe Comunitare în Domeniul Educației și Formării Profesionale (ANPCDEFP)'],
 ['Language used to fill in the form', 'English'],
], widths=[5.5, 11.1], count=False)

SMALL('Why these dates hold. The start date falls inside the eligible window for the 1 October 2026 deadline (projects starting between 1 January and 31 May 2027), and it leaves room for the '
      'National Agency’s selection results, announced roughly four months after the deadline. The 18-month duration sits inside the 3–24 month limit of the Action and leaves thirteen months '
      'after the mobility for application, multiplication and evaluation — which is the point: the exchange is the middle of this project, not the end of it.')

# =====================================================================
H1('2. Topic — and where the priorities are visible')
CALLOUT('There is no priorities field in this Action.',
        'The KA152-YOU form asks only for **Topic** — up to three, selected from a list. The priorities are never selected anywhere, which means the only place they can be scored is the narrative. '
        'The National Call is explicit about the consequence: no application receives full marks on Relevance, however well argued, unless it addresses a priority and shows consistently how the project pursues it. '
        'The table below is therefore an internal check, not a form field — use it to confirm that each priority is actually visible in the text before you submit.',
        'FFF6E5', 'E8C97A')

H3('Priorities — internal check, not a form field')
TBL([
 ['Priority', 'Weight', 'Where it is visible in the design'],
 ['Digital transformation — digital skills and competences, and responsible use of digital technologies and AI', 'Main',
  'It is the subject of the project, not its packaging: it defines the need, the participant profile, every method, the four media products, the toolkit and the two instruments that measure the result.'],
 ['Participation in democratic life, common values and civic engagement', 'Main',
  'Verification is treated as a precondition of participation. Participants move from competence to practice through four local initiatives in which they work with youth organisations, libraries, community centres and local authorities in their own communities.'],
 ['Inclusion and diversity', 'Main',
  'At least 12 of 20 participants face documented barriers; at least 15 of 20 travel on a European mobility for the first time. No participation fee, transport paid from the door, and a selection process built so that language and confidence are not filters.'],
 ['Environment and fight against climate change', 'Secondary',
  'Green travel for all four groups where the route allows it, local and seasonal food through the short supply chains the organisation itself built, no printed materials — and one category of the disinformation analysed on Day 2 is environmental and climate content.'],
], widths=[5.0, 1.8, 9.8], count=False)

P('**The national priority for 2026, named.** The ANPCDEFP National Call for 2026 gives priority, under digital transformation, to projects that **tackle disinformation and promote digital literacy**, and, '
  'under participation in democratic life, to projects that build critical thinking and media education. VERIFAI is not adjacent to that priority — it is that priority, in a rural mountain territory and three other '
  'European peripheries, with a measured result attached to it.', count=False)

Q('Please select up to three topics addressed by your project')
BUL([
 'Digital skills and competences',
 'Critical thinking and media literacy',
 'Youth participation and civic engagement',
], count=False)
FLAG('[TO CHECK before submission] This is a closed dropdown and the wording of the list changes between calls. Open the live 2026 Round 2 form and pick the closest available equivalents — do not paste these labels blind. If a topic on the list mentions disinformation explicitly, take it: it is the exact national priority for 2026.')

PAGEBREAK()

# =====================================================================
H1('3. Project summary')
CALLOUT('Two things the form says about this section.',
        '**It will be published.** The form states that if the project is accepted, the summary is made public by the European Commission and the National Agencies. So these three answers have to work for someone who has never read the rest of the application — no internal shorthand, no forward references, full sentences. They are written that way.\n'
        '**A translation into English is required** under each of the three questions if the form is filled in another language. We are filling it in English, so this does not apply — but if you switch to Romanian at any point, remember that the English summary becomes a separate obligation.',
        'FFF6E5', 'E8C97A')

Q('What do you want to achieve by implementing the project? What are the objectives of your project? Please specify from the perspective of youth work practice.')

P('We want young people who use artificial intelligence every single day to stop taking at face value whatever it hands them. In our own survey of 153 young people in the Napoca Porolissum LAG territory, '
  '96.9% of those aged 14–17 already use AI tools, yet they rate their own digital competence at 3.25 out of 5, and half of them build their picture of the world from social media. Nobody has taught them how '
  'to check any of it. VERIFAI turns twenty of them, from four peripheral European communities, into detectives: young people who can identify a source, check a date and a context, compare two independent '
  'sources, recognise a reused image and spot the signature of AI-generated content — and who then pass that on to others at home.')

P('From a youth work perspective the practice problem is not ignorance. It is untrained confidence. The Flash Eurobarometer “Youth Survey 2024” (EP013EP), carried out by Ipsos for the European Parliament '
  'among 25,863 young people aged 16–30 across all 27 Member States, found that more than three quarters of them had met disinformation in the previous seven days, while 70% were confident they could '
  'recognise it. Confidence outruns competence — so the method cannot be a lecture. Participants meet the false material and commit to a judgement //before// the verdict is revealed, and discover for themselves '
  'that they were wrong. That controlled moment of being wrong is the core of the non-formal learning approach of this exchange, and it only works in a genuinely international group, where a stereotype is very '
  'hard to defend with someone from the targeted community sitting at the same table.')

P('The project has three objectives. Each one names its target group, its threshold, the instrument that produces the number and the date by which it has to be true.')

TBL([
 ['', 'Objective'],
 ['O1\nMeasured\ncompetence',
  'By **30 September 2028** (month 18), **at least 16 of the 20 participants aged 14–17** increase their score on the project’s 15-item, 30-point practical verification test by **at least 30%** against their own baseline, '
  'measured in **May 2027** (month 2) with the equivalent form of the same instrument and the same formula at both ends.'],
 ['O2\nDemonstrated\ncompetence',
  'By **15 August 2027**, the last day of the youth exchange, **at least 16 of the 20 participants** demonstrate **all four verification techniques** — identifying the source and the author; checking the date and the context; '
  'comparing at least two independent sources; verifying an image or a claim, including the indicators of AI-generated content — scoring the full 2 points on each, in the structured observation grid applied during '
  'session D4.1 by six observers trained and calibrated beforehand.'],
 ['O3\nTransfer to the\ncommunity',
  'Between **September 2027 and June 2028** (months 6–15), the 20 participants reach **at least 80 other young people** through **four local initiatives**, one in each partner community, and **at least 70%** of the young '
  'people reached pass the ten-minute closing exercise: naming two distinct checks, actually carrying one of them out, and drawing a conclusion that follows from what they found.'],
], widths=[2.6, 14.0])

P('**On the 30% threshold.** The figure is not decorative and it is not final. It is confirmed once the baseline exists, using relative growth — (final score − initial score) ÷ initial score × 100 — with the same '
  '30-point instrument at both ends. The recalibration rule is written down now, before any data exists: if the group mean comes in below 9/30 the threshold rises to +50%, because 30% off a very low base says '
  'nothing; if it comes in above 18/30 it falls to +20% and an absolute companion measure is added, because there is less room to grow. A participant who scores 24 or more at baseline meets O1 by holding 27 or more '
  'at the end. Fixing all of this in advance is what stops a threshold from quietly becoming a way of producing the answer we want.')
COUNT()

Q('What activities do you plan to implement? What is the number and profile of the participants involved?')

P('One youth exchange of seven activity days plus two travel days, hosted in the Napoca Porolissum LAG territory in the Apuseni Mountains, Romania, from 9 to 15 August 2027 — inside the school summer holiday '
  'of all four countries. The programme moves from self-diagnosis (“My Digital Map”) through the mechanics of manipulation (“Spot the Fake”), AI-generated content (“AI or human?”), a full fact-checking '
  'simulation (“Fact-checkers for a day”), a community and intercultural day in a village of the territory, media production (“Make It, Don’t Fake It”) and a public presentation with Youthpass reflection. Around it: '
  'four months of preparation with four joint online sessions and a preparatory visit, and ten months of local application in which the participants run four local initiatives in their own communities.')

P('**Twenty young people aged 14–17**, five from each of the four organisations, plus four group leaders and two facilitators — 26 people in total. They come from four peripheral communities: the rural mountain '
  'communes of the LAG territory in Cluj County (Romania), the İstanbul metropolitan periphery (Türkiye), inland Corsica (France) and inner Sardinia (Italy).')

P('They share the profile this project is built for. Almost all of them use AI tools and social media every day, and for a large part of them social media //is// the news; none of them has been taught how to check any of it. '
  'Their access to non-formal learning is thin and their access to international learning is close to nil: at least 15 of the 20 will be taking part in a European mobility for the first time, and in our territory 31.3% of '
  'young people aged 14–17 have never taken part in any non-formal education activity at all. At least 12 of the 20 face documented barriers — geographic (isolated mountain communes, two Mediterranean islands, '
  'a metropolitan periphery), economic, educational, linguistic or social. The group is built to be mixed in gender, in locality and, in the Romanian and island groups, in language.')
COUNT()

Q('What results and impact do you expect your project to have?')

P('**For the participants.** A measured increase in verification competence, documented by the same practical test at the start and at the end and by an observation grid applied during the mobility. Four short media '
  'products debunking real local myths, made by the participants themselves. Twenty Youthpass certificates built through daily reflection rather than handed out at the door. And, for most of them, a first '
  'international experience — which at fifteen, arriving from a mountain commune or an inland island village, is its own learning.')

P('**For the communities.** Four local initiatives reaching at least 80 more young people, hosted in youth centres, libraries, community centres, the partner organisations’ own spaces and other public places young '
  'people can actually get to. And a “Digital Detectives” toolkit — worksheets, exercises, games and verification grids, tested during the exchange and then rewritten on the basis of what happened in the field — '
  'published free of charge and handed to the youth workers, librarians and community educators who work with these young people week to week.')

P('**For the organisations.** A working method that survives the project. The coordinator integrates it into the youth animation work it already runs across its 14 partner municipalities; the partners translate the '
  'toolkit and keep using it. Beyond that, the four organisations end up with something none of them has now: a shared, evidenced answer to a problem all four of their communities have, in a form other peripheral '
  'territories can pick up. The results are published on the Erasmus+ Project Results Platform.')

P('**What we do not claim.** Twenty participants will not move a county-level statistic, still less a national one. The contribution is exactly what it is: measurable change in twenty young people, documented extension '
  'to at least eighty more, and three instruments and one toolkit that stay in use in four organisations after the money stops.')
COUNT()

H3('Summary of participating organisations')
TBL([
 ['#', 'Organisation', 'OID', 'Country', 'Role'],
 ['1', 'ASOCIAȚIA GRUPUL DE ACȚIUNE LOCALĂ NAPOCA POROLISSUM', 'E10181755', 'Romania', 'Applicant, coordinator, hosting organisation and sending organisation'],
 ['2', 'SINIRLARI AŞAN GENÇLIK DERNEĞI (YOBBA — Youth Beyond Borders Association)', 'E10094576', 'Türkiye', 'Sending organisation; thematic lead for media production and AI-generated content; designates one of the two facilitators'],
 ['3', '[TO CONFIRM — partner in Corsica]', '[TO CONFIRM]', 'France', 'Sending organisation; thematic lead for insularity and minority-language information'],
 ['1', '[TO CONFIRM — partner in Sardinia]', '[TO CONFIRM]', 'Italy', 'Sending organisation; thematic lead for community dialogue and local follow-up methodology'],
], widths=[0.8, 5.6, 2.2, 1.8, 6.2], count=False)

H3('Summary of activities')
TBL([
 ['Id.', 'Activity Type', 'Activity Title', 'Participants', 'Persons', 'Total grant (EUR)'],
 ['YEX01', 'Youth exchanges', 'VERIFAI: Young Detectives Against Digital Disinformation', '20', '26', '26,827.00'],
 ['', '', '**Total**', '**20**', '**26**', '**26,827.00**'],
], widths=[1.6, 2.8, 6.4, 2.0, 1.6, 2.2], count=False)

PAGEBREAK()

# =====================================================================
H1('4. Project budget')
SMALL('Indicative figures, built on the 2026 Programme Guide unit costs. The final amounts are produced by the form itself, flow by flow, once the distance calculator has been run for every place of origin. '
      '[TO CONFIRM: distances, once the partners’ departure cities are known.] The form also carries a checkbox stating whether the National Agency has requested a **financial guarantee** — check it when you open the live form, '
      'because if one is required it has to be arranged before the grant agreement, not discovered afterwards.')

CALLOUT('A 92 EUR correction, and how it was found.',
        'The travel line of 8,315.00 EUR only adds up if the Romanian flow carries **seven** people — five participants, one group leader and the facilitator designated by the coordinator — and the Turkish flow seven as well, '
        'once the facilitator designated by YOBBA is added under comment C8. That means **19** people travel in the 500–1,999 km band and qualify for the additional green-travel days, not the 18 the previous version assumed. '
        'Individual support therefore becomes **12,512.00**, the project total **31,587.00**, and the YEX01 activity grant **26,827.00**. Small, but it is exactly the kind of arithmetic an expert re-runs.',
        'FDECEC', 'E3A9A9')

TBL([
 ['Budget item', 'Grant (EUR)', 'Basis of calculation'],
 ['Organisational support', '2,500.00', '125 EUR × 20 participants'],
 ['Travel (green travel)', '8,315.00',
  'Türkiye 7 persons and Romania 7 persons (each group of 5 participants + 1 group leader, plus one facilitator in each); Corsica and Sardinia 6 persons each.\n'
  'Türkiye, Corsica, Sardinia: 19 persons × 417 EUR (band 500–1,999 km, green rate). Romania: 7 persons × 56 EUR (band 10–99 km, green rate)'],
 ['Individual support', '12,512.00', '26 persons × 9 days × 46 EUR = 10,764.00, plus **19** persons × 2 additional green-travel days × 46 EUR = 1,748.00 (the 19 are everyone in the Türkiye, Corsica and Sardinia flows)'],
 ['Inclusion support for organisations', '1,500.00', '125 EUR × 12 participants with fewer opportunities'],
 ['Inclusion support for participants', '2,000.00',
  'Real costs. Requested on separate, dedicated lines — one per type of cost, never as a global category — and justified individually in the preparation section, as the National Call requires'],
 ['Preparatory visit', '4,760.00', '680 EUR × 7 persons: 2 from each of the 3 sending organisations, one of them a young person, plus 1 staff member of the coordinating organisation'],
 ['**Total**', '**31,587.00**', 'Of which **26,827.00 EUR** is the YEX01 activity grant and 4,760.00 EUR the preparatory visit'],
], widths=[4.4, 2.2, 10.0], count=False)

P('**Three things the National Call requires us to get right, and how we do.** First, **group leaders**: the Call approves one group leader for every four young people. We request four group leaders for twenty '
  'participants — one per national group, below that ceiling — and we would in any case fall under the exception the Call makes for groups of minors and for national groups in which at least half of the young '
  'people face fewer opportunities. Both apply here: all twenty participants are minors, and at least 12 of the 20 face documented barriers. Second, **inclusion costs at real cost** are requested line by line, each '
  'with its own justification and its own added value, not bundled. Third, **no exaggerated requests**: the preparatory visit is the only non-standard item, and the three reasons for it are stated in the '
  'logistics section rather than assumed.', count=False)

SMALL('Note: the question on participant contributions is not in the budget section of the 2026 form — it sits inside Project details, and it is answered there, in section 7.4.')

PAGEBREAK()

# =====================================================================
H1('5. Participating organisations')
CALLOUT('Check this before anything else: the five-application limit.',
        'The 2026 form states that **each organisation (OID) can be involved in a total of five Mobility of young people applications per application round** — coordinator or partner, it makes no difference — and that once '
        'the limit is reached the system will not accept a further application carrying that OID. **YOBBA is the exposure here.** An organisation that has partnered in six KA152 exchanges is exactly the organisation that gets '
        'asked again, and it may already be in several applications for this round without anyone thinking to mention it. Ask YOBBA in writing now, and put the same question to the two island partners the day they are '
        'confirmed. This is not a quality problem you can argue your way out of on 1 October — it is a hard stop in the system.',
        'FDECEC', 'E3A9A9')

H2('5.1 Applicant and coordinator — ASOCIAȚIA GRUPUL DE ACȚIUNE LOCALĂ NAPOCA POROLISSUM')
TBL([
 ['Field', 'Entry'],
 ['Legal name', 'ASOCIAȚIA GRUPUL DE ACȚIUNE LOCALĂ NAPOCA POROLISSUM'],
 ['Acronym', 'LAG NAPOCA POROLISSUM'],
 ['OID / PIC', 'E10181755 / 935151490'],
 ['Address', 'Eroilor Street, Building I1, Gilău, 407310, Cluj County, Nord-Vest, Romania'],
 ['Is the organisation a public body?', 'No'],
 ['Is the organisation a non-profit?', 'Yes'],
 ['Legal representative', 'Marius Gheorghe Dumitrescu, President'],
 ['Contact person', 'Alina Ioana Baba, Manager — manager@napocaporolissum.ro'],
 ['Role in the project', 'Applicant, coordinator, hosting organisation, sending organisation'],
], widths=[5.0, 11.6], count=False)

Q('What are the activities and experience of the organisation in youth work?')

P('LAG Napoca Porolissum is a public-private partnership founded in 2011 under the LEADER programme, with 43 partners: 14 municipalities, one university and 28 private-sector members. It employs 13 people '
  'and works across a rural mountain territory of 14 localities in the Apuseni Mountains, Cluj County. Its mandate is local development through a bottom-up approach, and youth work has become a permanent '
  'strand of that mandate rather than an occasional add-on.')

P('In the youth field specifically, the organisation was the **coordinator** of the Erasmus+ project //Rural Youth Parliament — tool for youth involvement in local communities// (2021-1-RO01-KA220-YOU-000029265), '
  'which created and ran youth parliament simulations across rural communities, and it coordinates the Rural Youth Parliament that came out of it. It is currently implementing //CONNECT-R — Connecting rural youth '
  'with the EU// under KA154-YOU (2025 ID KA154-YOU-62F63343), and has been a partner in //YouProClima// (2023-1-IT03-KA220-YOU-000155348), //ALL4JOBS// (KA220-YOU-70101DB1) and //SMART+CULTURE// (KA210-YOU-C68333FA).')

P('It also brings the experience of **EMPOWER** — [TO COMPLETE: full project title], implemented under [TO COMPLETE: action, e.g. KA210-YOU / KA220-YOU / European Solidarity Corps] with the reference '
  '[TO COMPLETE: project number], in which LAG Napoca Porolissum acted as [TO COMPLETE: coordinator / partner]. Its relevance to VERIFAI is direct: [TO COMPLETE, in one sentence — what the project did with '
  'and for young people, and what the organisation took from it that this project uses, for example a working method for youth participation in rural communities].')
FLAG('[TO COMPLETE before submission — C6] Four facts are needed here: full title, action type, project number, role. Then one sentence on youth-work relevance. The sentence above is written so the facts drop straight in without rewriting anything around them.')

P('Beyond the Programme, the organisation runs the cultural and educational infrastructure that young people in this territory actually have. //Ruraliada — Culture in the Mountains//, funded through the National '
  'Recovery and Resilience Plan and implemented in 2024, was a three-day festival of visual, digital and performing arts in Beliș commune — painting, ceramics and multimedia workshops, improvisational theatre, '
  'encounters with artists — designed to motivate rural young people and to push local authorities to widen what they offer. //The School — children’s painting// brought professional artists into village schools '
  'across the county. The organisation runs Christmas markets in Mărișel and Beliș, an annual Diversity Day, and educational camps in Romania and abroad for children from socially disadvantaged communities. '
  'Through its Social Inclusion Centre and the //UNIC — Porolissum// project it works directly with vulnerable families in the territory, which is how it reaches young people that a call published online would never touch.')

P('And, crucially for this application, the organisation carried out the needs analysis on which VERIFAI is built: a bilingual Romanian/Hungarian survey of **153 young people** from 12 of the 14 localities of the '
  'territory, of whom **96 are aged 14–17** — the exact target group of this project.')
COUNT()

Q('Please describe the profile of each of the group members and what does each one bring to the project.')

TBL([
 ['Person and role in VERIFAI', 'Profile and contribution'],
 ['**Alina Ioana Baba**\nProject manager',
  'Two degrees (Legal Sciences; Public Administration), three master’s degrees (Public Management; Health Policy and Management; Rural Development) and a PhD in economics. More than twelve years in project '
  'management and rural development, with a strong record in animating local actors. Manager of the association for over ten years, responsible for a portfolio that includes Erasmus+ projects in youth, VET, school '
  'and adult education as well as transnational cooperation. Guest facilitator at workshops and conferences of the European Network for Rural Development. In VERIFAI she carries overall coordination, the relationship '
  'with the National Agency, the budget, reporting and risk decisions.'],
 ['**Claudiu Iancu**\nLearning Programme Coordinator (non-formal learning) and lead facilitator',
  'Youth worker and community facilitator, with a qualified Trainer certificate and five Europass mobility certificates. BSc in Economic Engineering in Agriculture, MSc in Rural Development. Around three years inside '
  'Local Action Groups, focused on rural development, social inclusion and non-formal education, after a background in adult education where he contributed as an expert to the training of over 1,000 adults. Directly '
  'involved in more than five Erasmus+ Youth projects; in the past three years he has organised and facilitated over 50 youth events — workshops, consultations, youth meetings and participation activities. Coordinator '
  'of the Rural Youth Parliament and youth leader in YouProClima. In VERIFAI he owns the learning programme, the three measurement instruments, the facilitation team and the Youthpass process.'],
 ['**Livia Golovatic**\nActivity coordinator and Romanian group leader',
  'BA in International Relations and European Studies, currently in the first year of a master’s in European Affairs and Programme Management. Assistant manager on the implementation of the Local Development '
  'Strategy, with experience in strategic planning support. Involved in Erasmus+ Youth and VET projects, contributing to implementation, activity coordination and cooperation with international partners, with practical '
  'experience in non-formal education and youth participation, including in EMPOWER [TO CONFIRM: her exact role there]. In VERIFAI she leads the Romanian group, runs the four joint online preparation sessions and '
  'coordinates the four local initiatives.'],
 ['**Marilena Georgescu**\nInclusion and safeguarding lead',
  'Higher education in Social Assistance and Law, master’s in Project Management, with vocational qualifications in human resources management, public procurement, entrepreneurship, train-the-trainer and '
  'socio-educational animation. Fourteen years managing projects for the social inclusion of vulnerable groups, vocational training and labour-market integration, and educational and cultural projects. Coordinator of '
  'social service centres including a day centre for children. In VERIFAI she is the designated safeguarding focal point — deliberately a person outside the facilitation team — and she leads the recruitment of '
  'participants with fewer opportunities through the Social Inclusion Centre.'],
 ['**Iulia Fătu**\nFinancial and logistics officer',
  'Two bachelor’s degrees (Accounting; Agri-food Economy) and two master’s degrees (Agribusiness; Audit and Financial Management of European Funds). Working in European projects since 2014, responsible for '
  'procurement documentation, project evaluation and monitoring, and the implementation of social infrastructure projects. In VERIFAI she handles the budget, procurement, venue and transport contracting, insurance, '
  'the written venue risk assessment and financial reporting.'],
], widths=[4.2, 12.4])

H4('How the team works together')
P('The five roles are separated on purpose. The project manager decides; the Learning Programme Coordinator owns the learning; the safeguarding lead sits outside the facilitation chain, so that a participant can '
  'raise a concern //about a facilitator//; and the financial officer is not the person negotiating with participants or families. The team meets weekly during the preparation and mobility months and monthly '
  'otherwise, with a written action log in which every decision has an owner and a date.')
COUNT()


PAGEBREAK()
H2('5.2 Partner organisation — SINIRLARI AŞAN GENÇLIK DERNEĞI / YOBBA (E10094576 — TR)')
TBL([
 ['Field', 'Entry'],
 ['Legal name', 'SINIRLARI AŞAN GENÇLIK DERNEĞI'],
 ['Acronym', 'YOBBA (Youth Beyond Borders Association)'],
 ['OID / PIC', 'E10094576 / 901841496'],
 ['Address', 'İnönü Mahallesi, Hakan Caddesi, Öz Feza Sitesi A Blok Kat 2/10, Küçükçekmece, 34295, İstanbul, Türkiye'],
 ['Is the organisation a public body?', 'No'],
 ['Is the organisation a non-profit?', 'Yes'],
 ['Legal representative', 'Doğan Can Karabudak, President'],
 ['Contact person', 'Aysu Zeybel, Project Coordinator'],
 ['Role in the project', 'Sending organisation; thematic lead for media production and AI-generated content; designates one of the two facilitators of the exchange'],
], widths=[5.0, 11.6], count=False)

Q('What are the activities and experience of the partner organisation in youth work?')

P('YOBBA is a youth association based in Küçükçekmece, in the metropolitan periphery of İstanbul, working with a volunteer community of more than 150 young people a year. Its declared core expertise is digital '
  'media: it trains young people in media work, gives them professional skills and puts them into projects with social impact, and it delivers digital literacy training to beneficiaries of companies and civil-society '
  'institutions. In 2020 its team founded the //ErasmusPlus Türkiye// platform, which produces content about opportunities at home and abroad and disseminates Erasmus+ projects nationally, with a following of around '
  '250,000; the president also runs a long-standing YouTube channel on travel and self-development.')

P('Its work spans youth policy volunteering, civil-society development, non-formal education and the recognition of youth work, international cooperation, environmental and animal welfare initiatives, work with '
  'refugees and migrants, women’s rights and gender equality, and the social inclusion of people with disabilities. It has run digital skills and technology training covering digital literacy and cyber-security, '
  'intercultural exchange programmes, entrepreneurship and innovation initiatives, and mental health and emotional resilience programmes delivered together with psychologists and counsellors. Activities with young '
  'people are designed and supervised with pedagogues and psychologists involved.')

P('**Experience in this Action specifically.** YOBBA has taken part in **six KA152 youth exchanges as a partner organisation between 2022 and 2024**, with coordinators in Hungary (2022-1-HU-01-KA152-45D10D09), '
  'Latvia (2023-LV02-KA152-YOU-000148179), Italy (2023-1-IT03-KA152-YOU-000147001; 2023-3-IT03-KA152-YOU-000183264; 2024-3-IT03-KA152-YOU-000282312) and Poland (2023-3-PL01-KA152-YOU-000183071).')

H4('What YOBBA brings to VERIFAI, and where it does not overlap with the coordinator')
P('YOBBA teaches young people to //produce// digital content. It does not teach them to //verify// it. That gap is exactly what this project fills, and it is why the division of labour between the two experienced '
  'partners is clean rather than duplicated. YOBBA leads Day 6, the media production day, and contributes substantially to Day 3 on AI-generated content, where knowing how such content is made is precisely what '
  'allows a fifteen-year-old to recognise it. The coordinator leads the verification days. A young person who can edit a convincing video but cannot check a source is a more efficient vector of disinformation, not an '
  'antidote — the partnership is designed around closing that circle.')

P('**One of the two facilitators of the exchange is designated by YOBBA.** This follows from the same logic: the sessions on AI-generated content, on the ethics of using AI in one’s own production and on media '
  'production need someone in the facilitation team who works with these tools professionally, not someone who read about them. That facilitator is part of the team from month 4, takes part in the observer '
  'calibration exercise, and applies the observation grid on Day 4 alongside the facilitator designated by the coordinator. YOBBA also brings dissemination reach that none of the other partners has.')
COUNT()

Q('Please describe the profile of each of the group members and what does each one bring to the project.')
TBL([
 ['Person and role', 'Profile and contribution'],
 ['**Doğan Can Karabudak**\nLegal representative; senior adviser on media production and AI content',
  'Computer engineer, founder of YOBBA, traveller and content creator. Alumnus of the Study of the United States Institutes programme (2014), where he worked on global environmental problems with participants from '
  'around the world; former vice-president of a student council. Has organised and contributed to numerous EU projects and training courses as leader and as participant, and has delivered over 100 seminars and '
  'training sessions. In VERIFAI he leads sessions D3.1 (AI-generated content) and D3.4 (the ethics of AI use), co-leads Day 6, and secures dissemination through the platforms YOBBA operates.'],
 ['**Aysu Zeybel**\nProject coordinator; Turkish group leader',
  'Graduate in Economics, University of Karabük. Learned sign language at university and has worked on projects with people with disabilities. Completed a ten-month European Solidarity Corps project in Tușnad, '
  'Romania, responsible for social media management, event announcements and creative development, running weekly activities with children with disabilities in kindergarten, after-school and middle-school settings, '
  'and supporting local events in the town — direct experience of intercultural life between Hungarian and Romanian communities, which is directly relevant to a project about how information travels inside language '
  'communities. Project coordinator at YOBBA, mentoring young people applying to volunteering projects. In VERIFAI she leads the Turkish group, prepares it before departure, supervises it throughout, and observes '
  'one mixed team on Day 4.'],
 ['**Facilitator designated by YOBBA**\n[TO CONFIRM: name]',
  'A facilitator with professional practice in digital content production and in generative AI tools, and with experience of working with young people in non-formal settings. Joins the team in month 4, takes part in the '
  'observer calibration exercise, co-facilitates sessions D2.3 and D4.2, supports D3.1, D3.4 and Day 6, and carries out the independent second scoring of five participants on Day 4.'],
], widths=[4.2, 12.4])
COUNT()

PAGEBREAK()
H2('5.3 Partner organisation — [TO CONFIRM — CORSICA, FRANCE]')
FLAG('Status at drafting. The Corsican partner is not yet identified. Internal deadline for a signed mandate and a completed Partner Identification Form: 20 September 2026. The text below is the profile we are searching against and the role the partner would hold; the organisation’s own description replaces the first paragraph once it is confirmed.')

P('**Profile sought.** A youth NGO, socio-cultural centre, youth service, cooperative or Local Action Group based in Corsica, with documented current work with young people aged 14–17, reaching those who live in '
  'inland or rural communes rather than only in Ajaccio or Bastia, and anchored in a community where the Corsican language is part of daily life. A valid OID, an adult group leader able to accompany minors for nine '
  'days, and the capacity to run one local initiative with at least 20 young people between months 6 and 15.')

P('**Why a Corsican partner is necessary and not decorative.** Around 11,000 young people aged 16–29 in Corsica are neither in employment nor in education or training — close to one in four of that age group — and '
  'the island records a higher share of inactive, unschooled and unemployed young people than the French national average. Access to mainland non-formal education is conditioned by the cost and the length of the '
  'journey: for a teenager from an inland commune, a learning activity in Marseille is effectively out of reach. And part of community communication happens in Corsican, on small local channels that no national '
  'fact-checker covers — which means false information circulating in that language almost never meets a correction.')

P('**Role in VERIFAI.** Sending organisation; thematic lead on Day 2 for the strand on how disinformation circulates in minority-language communities and small local media ecosystems; contributor to Day 5. '
  '**Deliverables:** a local needs note with its own consultation data (month 2, before submission where possible); five to eight documented cases of disinformation from its own community (month 4); recruitment and '
  'preparation of the French group; one local initiative in Corsica (by month 13); the French translation of the toolkit; and one group leader who observes a mixed team on Day 4.')
COUNT()

H2('5.4 Partner organisation — [TO CONFIRM — SARDINIA, ITALY]')
FLAG('Status at drafting: as above. Same internal deadline of 20 September 2026.')

P('**Profile sought.** A youth association, social cooperative or Local Action Group in inner Sardinia, working with young people aged 14–17 from small localities affected by depopulation, open to the Sardinian '
  'language and culture, with a valid OID, an adult group leader and the capacity to run one local initiative with at least 20 young people.')

P('**Why a Sardinian partner is necessary.** 17.8% of young people aged 15–29 in Sardinia are not in employment, education or training, against an Italian average of 15.2% and a European average of around 11%. '
  'The inner areas of the island are among the Italian territories with the sharpest demographic decline: young people emigrate, birth rates fall, and the educational and cultural offer contracts along with the '
  'population — so non-formal learning opportunities become rarest exactly where young people have fewest alternatives. As in Corsica and in our own territory, part of community life is carried in a language of its '
  'own, on small local channels.')

P('**Role in VERIFAI.** Sending organisation; thematic lead for the preparation and moderation of Day 5, the community dialogue day, and for the methodology of the local initiatives. **Deliverables:** a local needs '
  'note with its own consultation data; five to eight documented local cases (month 4); the local initiative model and its evaluation grid (month 5); recruitment and preparation of the Italian group; one local '
  'initiative in Sardinia (by month 13); the Italian translation of the toolkit; and one group leader who observes a mixed team on Day 4.')
COUNT()

PAGEBREAK()

# =====================================================================
H1('6. Project rationale')
H2('6.1 Needs and objectives')
Q('Why do you want to carry out this project? Please describe the issues and needs you want to address and your project’s objectives.')

H4('The need, in one sentence')
P('Young people aged 14–17 in the Napoca Porolissum LAG territory and in the peripheral partner communities of Corsica, Sardinia and the İstanbul periphery consume digital content and use AI tools every '
  'day, but have not acquired the habit of checking the source, the author, the date and the context of a piece of information before believing it and passing it on.')

H4('How we know: our own data')
P('This is not an assumption. Between spring and summer 2026 we ran a bilingual Romanian/Hungarian survey among young people in our territory and received **153 responses from 12 of our 14 localities** — '
  'Săcuieu (36), Gilău (30), Huedin (27), Mărișel (15), Căpușu Mare (10), Mărgău (9), Măguri-Răcătău (9), Călățele (6), Beliș (5), Mănăstireni (3), Aghireșu (2), Izvorul Crișului (1). **Ninety-six respondents are '
  'aged 14–17**, which is exactly the target group of this project. Here is what they told us.')

TBL([
 ['Finding', 'Aged 14–17 (n=96)', 'All (n=153)'],
 ['Already use artificial intelligence tools', '96.9%\n(45.8% often, 51.0% occasionally)', '90.8%'],
 ['Rate their own digital competence as low (1–2 out of 5)', '20.8%', '24.8%'],
 ['Mean self-assessed digital competence (1–5)', '3.25', '3.23'],
 ['Have never taken part in any non-formal education activity', '31.3%', '37.3%'],
 ['Name lack of information as a barrier to joining a mobility', '37.5% (first barrier named)', '36.6%'],
 ['Name cost / transport as a barrier', '34.4% / 31.2%', '37.9% / 34.0%'],
 ['Hear about opportunities from school / social media / the municipality', '50.0% / 49.0% / 6.2%', '41.8% / 51.6% / 10.5%'],
 ['Learn best through practical activities / through a course', '68.1% / 29.8%', '—'],
 ['Want activities organised in or near their own locality', '58.5%', '—'],
 ['Would take part in an Erasmus+ activity organised by the LAG', '60.4% yes + 25.0% maybe = **85.4%**', '88.9%'],
], widths=[8.6, 4.4, 3.6])

P('Two of those figures, read together, are the whole problem. Almost every young person in our territory already uses AI, and almost half of them build their picture of the world from social media — while rating '
  'their own digital competence at barely above the midpoint. Use is universal; competence has not followed it.')

H4('How we know: the same need in the other three communities')
P('A need demonstrated in one territory is not a need demonstrated across a partnership, and we do not want an expert to have to take the other three on trust. All four partners therefore run the **same short '
  'consultation** before submission: a ten-question instrument built from our own survey, translated locally, with **at least 20–25 young people aged 14–17** from the partner’s own community, plus one short '
  'focus group where numbers are small. Each partner delivers a one-page needs note with the method, the number and profile of the young people consulted, and the three main findings. Those notes go into the '
  'supporting file, and the figures come into the table below.')

TBL([
 ['Community', 'Consultation method and dates', 'Young people consulted — number and profile', 'Main findings'],
 ['Romania — LAG Napoca Porolissum\n//Done//',
  'Bilingual RO/HU online and paper questionnaire, spring–summer 2026, plus a validation meeting with 8–10 young people from the territory before submission.',
  '153 respondents from 12 of 14 localities, of whom 96 aged 14–17; 72.5% in education.',
  '96.9% use AI tools; 20.8% rate their own digital competence as low; 31.3% have never taken part in any non-formal activity; lack of information is the first barrier they name.'],
 ['Türkiye — YOBBA',
  '[TO CONFIRM: method and dates]',
  '[TO CONFIRM: number and profile of young people aged 14–17 consulted in Küçükçekmece and the surrounding periphery]',
  '[TO CONFIRM: three findings, ideally comparable to ours — daily AI and social-media use, self-assessed competence, previous participation in non-formal or international activities]'],
 ['France — [Corsica partner]', '[TO CONFIRM]', '[TO CONFIRM]', '[TO CONFIRM — with at least one finding on information circulating in Corsican on small local channels]'],
 ['Italy — [Sardinia partner]', '[TO CONFIRM]', '[TO CONFIRM]', '[TO CONFIRM — with at least one finding on the contraction of the local learning offer in depopulating inner areas]'],
], widths=[3.4, 3.6, 4.4, 5.2])
FLAG('[TO DO — C9] Send the ten-question instrument to the three partners as soon as each one is confirmed, with a two-week deadline. A partner that cannot produce 20 responses from its own community in two weeks is telling you something useful about its capacity.')

H4('How we know: European data')
P('The Flash Eurobarometer “Youth Survey 2024” (EP013EP), carried out by Ipsos for the European Parliament among 25,863 respondents aged 16–30 across all 27 Member States, with fieldwork between 25 September '
  'and 3 October 2024, found that more than three quarters of young Europeans believe they were exposed to disinformation in the previous seven days, while 70% feel confident they can recognise it — 18% very '
  'confident, 52% somewhat. Confidence outruns competence. Two further findings shape our design. Young people in rural areas are less confident (68%) than those in large cities (73%). And Romania records the '
  'highest share in the entire Union of young people saying they encountered no disinformation at all in the past week — 19%, against 1% in Cyprus and at most 11% anywhere else — while 31% of Romanian '
  'respondents declare themselves “very confident”. Romanian young people are simultaneously the least likely in Europe to notice disinformation and among the most certain they would recognise it.')

H4('What follows for the design')
P('If the problem were a lack of confidence, the answer would be encouragement. Because the problem is //untrained// confidence, the answer is a controlled experience of being wrong. Day 1 therefore starts with '
  'participants mapping their own media diet rather than with a presentation. On Day 2 the false material is judged before the verdict is revealed. And this is also why the project needs a genuinely international '
  'group and cannot be run at home: a stereotype is at its least defensible when a young person from the community it targets is sitting in the room.')

H4('Why these four communities')
P('The four communities do not look alike, and we are not going to pretend they do. A mountain commune in the Apuseni, a district on the edge of İstanbul, a village in inland Corsica and a small town in inner '
  'Sardinia have different histories, different languages, different economies and different problems. What their young people have in common is narrower, and more exact.')
BUL([
 '**Information reaches them through channels nobody corrects.** Each of the four communities has its own linguistic bubble — Hungarian in part of our territory, which is why our survey had to be bilingual; Corsican in Corsica; Sardinian in inner Sardinia; neighbourhood, family and community networks in the İstanbul periphery. National fact-checkers work in the majority language on subjects of national interest. Content circulating in those other channels is simply outside the safety net.',
 '**The practical media-literacy offer that exists elsewhere does not reach them.** Not a single one of the four communities has a standing activity where a fifteen-year-old can be taught, hands on, how to check an image or a source.',
 '**Getting to any international activity is harder and more expensive from where they live.** An isolated rural mountain area, two Mediterranean islands and a metropolitan periphery — four different geographies producing the same result at the door of a European programme.',
])
P('That overlap is what the project works on. It is also why a young person from each of the four recognises the other three within an hour of meeting them, which is the thing that makes an exchange work.')

H4('Objectives')
P('The three objectives are worded here exactly as they are worded in the project summary and in the evaluation table. Same numbers, same instruments, same dates, in all three places.')
TBL([
 ['', 'Objective', 'Instrument that produces the number'],
 ['O1', 'By **30 September 2028**, at least **16 of the 20** participants aged 14–17 improve their score on the practical verification test by at least **30%** against their own baseline of May 2027.',
  'The 15-item, 30-point verification test, Form A in month 2 and the equivalent Form B in month 18, same formula at both ends.'],
 ['O2', 'By **15 August 2027**, at least **16 of the 20** participants demonstrate all **four verification techniques** — source and author; date and context; two independent sources; image or claim including AI indicators — at full marks on each.',
  'The structured observation grid, four techniques scored 0–2, applied during session D4.1 by six calibrated observers, with 25% of participants double-scored independently.'],
 ['O3', 'Between **September 2027 and June 2028**, the 20 participants reach at least **80 other young people** through **four local initiatives**, and at least **70%** of those reached can apply two simple verification methods.',
  'The ten-minute beneficiary exercise at the end of each local initiative: name two distinct checks, carry one out, draw a conclusion that follows — all three conditions, or it does not count.'],
], widths=[1.0, 8.6, 7.0])
COUNT(6000, cut='This is the longest answer in the application and it is over on purpose, so that cutting is a choice rather than a scramble. Cut in this order. '
  '(1) The partner-consultation table: keep one summary sentence per partner in running text and move the full table to the supporting file — worth roughly 1,200 characters. '
  '(2) The survey table: keep the six findings the project actually uses (AI use, self-assessed competence, never took part in a non-formal activity, the three barriers, where they hear about opportunities, how they learn) '
  'and drop the rest — worth roughly 600. '
  '(3) The European-data paragraph: keep the Eurobarometer reference, the 76%/70% pair and the Romanian outlier; drop the rural/city comparison — worth roughly 400. '
  'Do NOT cut the three objectives, the four-community overlap, or the “what follows for the design” paragraph: those are what the previous assessment said was missing.')

PAGEBREAK()

Q('How does your project link to the objectives of the Erasmus programme and those of Youth Exchanges?')

P('**Digital transformation — the substance, not the label.** VERIFAI builds the part of digital competence that use alone never produces. Our participants can already operate the tools; what they cannot do is find '
  'out where something came from. So the project develops three things, in this order: using digital tools and AI tools responsibly and with their limits understood; checking sources — who published it, who wrote '
  'it, when, in what original context, and whether any independent source says the same; and recognising false, manipulated or artificially generated content, including content they could produce themselves. That '
  'is the priority, and it is also the whole project — it defines the need, the participant profile, every method in the agenda, the four media products, the toolkit and the two instruments that measure whether it '
  'worked. It also matches what the National Agency has said it is looking for in 2026: among the projects addressing digital transformation, priority goes to those that tackle disinformation and promote digital '
  'literacy.')

P('**Participation in democratic life, common values and civic engagement.** Checking a claim is a precondition of taking part: without it, a vote, a public argument or a civic initiative rests on false premises. Our '
  'participants are 14 to 17 now, which means most of them will cast their first ballot within four to six years of this project. The point is that by the time they get there, forming an opinion on information they '
  'have actually checked is a habit rather than an effort. In the meantime they practise the civic half of it for real: through the four local initiatives they step out of the learning room and into their own '
  'communities, working with youth organisations, libraries, community centres and local authorities, and taking responsibility for an activity that other young people attend.')

P('**Inclusion and diversity.** The barriers our participants face are concrete, and each is answered by a concrete measure. //Geographic// — isolated mountain communes, two Mediterranean islands, a metropolitan '
  'periphery: the exchange is hosted inside our own territory rather than in a host city, transport is organised and paid from each participant’s own front door, and the preparatory visit brings one young person '
  'from each sending organisation so that nobody arrives in August among strangers. //Economic// — 34.4% name cost and 31.2% transport as barriers: there is no participation fee of any kind, and the rule is written '
  'into the call from the day it is published. //Linguistic// — five languages in the room and, for some participants, a minority language at home: English is not a selection criterion, A2 is accepted, the methods are '
  'visual and practical, and a glossary in five languages is built with the participants rather than handed to them. //Social and educational// — 12.5% name lack of self-confidence, 10.4% say their family would not '
  'agree, 31.3% have never taken part in any non-formal activity: four months of preparation rather than four weeks, an online meeting with parents in each country in their own language before consents are '
  'signed, a named group leader with the group at every moment, and the stated right to leave a session without giving a reason. The full measures are set out in section 9.')

P('**Objectives of the Action.** Youth Exchanges exist to encourage intercultural dialogue and learning and a sense of being European, to develop young people’s competences and attitudes, to strengthen European '
  'values and break down prejudice and stereotypes, and to raise awareness of socially relevant subjects. VERIFAI addresses each of these directly, and the third one structurally: the working material of Day 2 '
  'includes real content that feeds ethnic, gender and migration stereotypes, and it is analysed in mixed teams in which young people from the targeted communities are present.')

P('**EU Youth Strategy and the European Youth Goals.** The project addresses Goal 4, //Information and Constructive Dialogue//, which is its very object; Goal 6, //Moving Rural Youth Forward//, since the activity '
  'takes place in a rural mountain territory and the multiplication happens in the participants’ own localities; and Goal 9, //Space and Participation for All//, since participants co-design the programme, choose the '
  'subjects to be verified and lead their own local initiatives. Within the “Connecting” field of action of the Strategy, the project creates exactly the link it looks for: young people from four European peripheries '
  'discovering that they have the same problem, and working on it together.')

P('**Common EU values.** Disinformation attacks human dignity through dehumanising content, equality through algorithmically amplified stereotypes, and the rule of law by eroding trust in institutions. Three '
  'concrete anchors, rather than a declaration. The ground rule of the exchange is that any claim made in debate must be verifiable, and it applies to facilitators exactly as it applies to participants. The group '
  'agreement negotiated by the participants on Day 1 includes non-discrimination and respect for every language and identity present in the room — Romanian, Hungarian, Turkish, Corsican, Sardinian, Italian, '
  'French. And the analysis of stereotype-bearing content is deliberately done in the presence of the people it targets.')
COUNT(5000, cut='Only just over. Cut the inclusion paragraph down to its four barrier names plus a cross-reference to section 8.3, where the same measures are set out in full — worth roughly 500 characters '
  'and it removes a genuine repetition. If more is needed, shorten the EU Youth Strategy paragraph to the three Goal numbers and one line each. Keep the first two paragraphs intact: digital transformation and '
  'democratic participation are the two priorities this application is scored on.')

H2('6.2 Impact')
Q('How will your project benefit the young participants involved in the project, during and after the project lifetime?')

P('**A competence they did not have, measured rather than asserted.** Every participant takes the same 15-item practical verification test in month 2 and its equivalent in month 18, and the target is a 30% '
  'improvement for at least 16 of the 20. During the mobility an observation grid records whether each participant //actually performs// four named techniques in the Day 4 simulation — not whether they can describe '
  'them. That distinction matters here more than it would elsewhere, because our starting point is a group that already believes it can spot a fake.')

P('**A first European experience, for most of them.** At least 15 of the 20 will be taking part in a European mobility for the first time, and in our territory 31.3% of young people aged 14–17 have never taken part in '
  'any non-formal education activity at all. For those participants the gain is not only thematic: working in a mixed international team, in English, with people they have never met, is itself the learning. It is also '
  'what they asked for — 60.4% of the 14–17 group named foreign languages and intercultural communication as what they most want out of a European mobility.')

P('**Something to do afterwards.** The project does not end when they get off the bus. Each participant leaves the mobility with a written commitment and a role in one of the four local initiatives, which they design '
  'and lead themselves, with the group leader supporting rather than directing. This is where a fifteen-year-old moves from “I learned something” to “I taught twenty people”, and in our experience it is the part '
  'that changes how they see themselves.')

P('**Learning they can name, document and use.** Youthpass is worked on from Day 1 through a learning diary and daily reflection groups — in the national group and in the participant’s own language first, then in '
  'plenary — and closed on Day 7 in a dedicated session. The value is in the process, not the paper: it teaches a sixteen-year-old to identify what they actually learned, to document it with evidence they can point '
  'to, and to present it in a form someone else understands. That is a transferable skill in itself, and it is what makes the certificate usable afterwards — in the next learning activity they join, in volunteering, in a '
  'civic initiative in their own community, and in the next international mobility they apply for.')

P('**Six months later.** A follow-up questionnaire in month 12 asks what they still use. The honest expectation is not that all twenty become fact-checkers. It is that they have acquired a reflex — the pause before '
  'sharing — and that the four local initiatives have given at least some of them a taste for organising something in their own community.')
COUNT()

Q('How will your project benefit the organisations or the groups of young people implementing the project, during and after the project lifetime?')

P('**For the coordinator.** LAG Napoca Porolissum has run youth projects as partner and as coordinator, but this is its first project as **hosting organisation** for a youth exchange. That is a deliberate step in the '
  'organisation’s development. Hosting means owning the learning programme, the venue, the safety of twenty minors and the relationship with the host community, and it converts a network of 43 partners and 14 '
  'municipalities from a rural-development asset into a youth-work asset. The organisation ends the project with a tested non-formal learning programme, three measurement instruments it did not have, and a child '
  'protection policy that will apply to everything it does afterwards.')

P('**For YOBBA.** The partner brings production expertise and gains the verification methodology it currently lacks. For an organisation whose core business is training young people to make digital content, and '
  'whose platform reaches around 250,000 followers, acquiring a structured approach to source verification changes what it can responsibly teach. YOBBA takes the toolkit into its own volunteer programme of more '
  'than 150 young people a year.')

P('**For the two island partners.** Both are expected to be newcomers to this Action or less experienced in it. They gain a first structured experience of KA152 alongside a coordinator that carries the administrative '
  'and financial load, a method adapted to communities that have a language of their own, and a documented local initiative they can show to their own municipalities and funders. [TO CONFIRM once the partners '
  'are known.]')

P('**For all four.** The partnership produces something none of them has separately: an evidenced answer to a problem all four communities share, in a form other peripheral territories can pick up. In month 17 the '
  'four organisations formally assess whether to continue — either with a second exchange hosted by another partner, or with a youth participation project focused on dialogue with local decision-makers. The '
  'decision is minuted either way, including if it is not to continue.')
COUNT()

Q('What would be the impact of your project beyond the participants and participating organisations, at local, regional, national, if any European level?')

P('**Local.** At least 80 young people reached directly through the four local initiatives, hosted in youth centres, libraries, community centres, the partner organisations’ own spaces and other accessible public '
  'places. In Romania, the results are also presented across the 14 localities of the LAG territory through the community events the organisation already runs every year, so that young people who did not take part '
  'still meet the material, and so that the four media products circulate where the myths they debunk actually circulate.')

P('**Regional.** The “Digital Detectives” toolkit is offered free of charge to the youth organisations, libraries and community centres of the territory, with a presentation session for the youth workers and '
  'librarians who will use it. The 14 partner municipalities receive the evaluation report and a short set of recommendations. Romania has no coordinated national media-literacy strategy and its policies in this area '
  'are fragmented across separate legal frameworks; in that context, a tested, free, ready-to-use set of materials in the hands of people who already work with rural young people has a value out of proportion to '
  'the size of this project.')

P('**National and European.** Results are published on the Erasmus+ Project Results Platform. YOBBA disseminates through the ErasmusPlus Türkiye platform. The coordinator shares the method through the LEADER '
  'and ELARD networks, where it already has transnational cooperation experience — a channel that reaches Local Action Groups across rural Europe, an audience that rarely encounters media-literacy tools at all. '
  'The target is at least four organisations outside the partnership confirming in writing that they use the toolkit.')

P('**What we do not claim.** Twenty participants will not move a county-level statistic. The contribution is stated as it is: measurable change in twenty young people, documented extension to at least eighty more, '
  'and instruments that stay in use in four organisations after the project ends.')
COUNT()

PAGEBREAK()

# =====================================================================
H1('7. Project details — Activity 01')
P('The form asks you to list the activities, then to describe each one, then to break each one into **flows**. A flow is a group of people travelling from one place of origin to the venue over the same dates, in the same '
  'distance band — and it is the level at which the form computes travel and individual support. Getting the flows right is what makes the budget reconcile, so they are set out in full below.', count=False)

H3('7.1 Activity list')
TBL([
 ['Id.', 'Activity Type', 'Activity Title', 'Number of participants', 'Number of persons', 'Total grant (EUR)'],
 ['01', 'Youth exchanges', 'VERIFAI: Young Detectives Against Digital Disinformation', '20', '26', '26,827.00'],
 ['', '', '**Total**', '**20**', '**26**', '**26,827.00**'],
], widths=[1.2, 2.6, 6.0, 2.4, 2.0, 2.4], count=False)
SMALL('Participants are the 20 young people. Persons adds the 4 group leaders and the 2 facilitators. The form asks for both and they are not interchangeable.')

H3('7.2 Description of the activity (Activity 01)')
TBL([
 ['Field', 'Entry', 'Field', 'Entry'],
 ['Id.', '01', 'Total no. of participants', '20'],
 ['Activity Type', 'Youth exchanges', 'Of which, with fewer opportunities', '12'],
 ['Activity Title', 'VERIFAI: Young Detectives Against Digital Disinformation', 'No. of group leaders', '4'],
 ['Start date', '09/08/2027 (Monday)', 'No. of facilitators', '2 (one designated by the coordinator, one by YOBBA)'],
 ['End date', '15/08/2027 (Sunday)', 'No. of accompanying persons', '0'],
 ['Duration excluding travel', '7 days', 'Total no. of persons', '26'],
 ['Travel days', '08/08/2027 (arrival)\n16/08/2027 (departure)', 'Total Activity grant', '**26,827.00 EUR**'],
], widths=[3.6, 4.7, 3.6, 4.7], count=False)
FLAG('[TO CHECK on the live form] The blank form shows only Id, Activity Type, Activity Title, start and end dates, number of facilitators and total grant at this level — the rest of these fields appear as you fill it in, and some (such as a question on whether the activity is itinerant) exist in some calls and not others. Fill what the live form actually asks and keep the figures above as your reference sheet.')

H3('7.3 Flows summary (Activity 01)')
CALLOUT('The form’s own definition, and why we have four flows.',
        'The form defines a mobility flow as “a participant or a group of participants going to the same destination for the same duration of time and with same arrangements”, and adds: “If some participants going to the '
        'same destination need to have different arrangements (for example, different travel distance or mode of travel, different duration etc.) then you should split that mobility flow into two or more separate ones.” '
        'Our four groups go to the same destination but sit in two different distance bands and, because of the additional green-travel days, two different durations. So four flows is not a presentational choice — it is what the form requires.',
        'E8EEF7', 'C7D6EA')
P('Four flows, one per sending country. The two facilitators travel inside the flows of their own organisations rather than as a separate flow — the form does allow a **flow with facilitators only**, but splitting them out '
  'here would create two flows of one person each and would not change a single euro. **[DECISION: confirm this when filling the form.]**', count=False)

TBL([
 ['Flow', 'Place of origin', 'Participants', 'Group leaders', 'Facilitators', 'Persons', 'Fewer opport.', 'Distance band', 'Travel type', 'Days'],
 ['1', 'Cluj County, Romania\n[TO CONFIRM: departure city]', '5', '1', '1 (coordinator)', '**7**', '3', '10–99 km', 'Green', '9'],
 ['2', 'İstanbul, Türkiye', '5', '1', '1 (YOBBA)', '**7**', '3', '500–1,999 km', 'Green', '11'],
 ['3', 'Corsica, France\n[TO CONFIRM: departure city]', '5', '1', '—', '**6**', '3', '500–1,999 km', 'Green', '11'],
 ['4', 'Sardinia, Italy\n[TO CONFIRM: departure city]', '5', '1', '—', '**6**', '3', '500–1,999 km', 'Green', '11'],
 ['', '**Total**', '**20**', '**4**', '**2**', '**26**', '**12**', '', '', ''],
], widths=[0.9, 3.1, 1.6, 1.5, 1.9, 1.3, 1.5, 1.9, 1.3, 0.9], small=True, count=False)
SMALL('City of venue for all four flows: the accommodation unit in the Napoca Porolissum LAG territory, Apuseni Mountains, Cluj County, Romania [TO CONFIRM]. Start date 09/08/2027, end date 15/08/2027 for all four. '
      '“Days” counts the 7 activity days plus 2 travel days, and for flows 2, 3 and 4 the 2 additional days that green travel over that distance makes eligible.')

H3('7.4 Participant contribution and fees')
SMALL('The form prints the rules above this question: any contribution must be low, proportional to the grant, clearly justified, explained to participants, collected on a non-profit basis, and must not create unfair barriers. '
      'Fees cannot be collected from participants with fewer opportunities, and no other service provider may collect fees either.')
Q('Are you planning to ask for any contributions from participants?')
P('**No** — and this is a decision, not an omission. In our survey, cost is the second barrier young people aged 14–17 name to taking part in a mobility (34.4%) and transport is the third (31.2%). A fee of any size '
  'would filter out precisely the young people this project exists for, and a family deciding whether to let a fourteen-year-old leave the country for nine days should not also be deciding whether they can afford it. '
  'Since at least 12 of our 20 participants are participants with fewer opportunities, from whom the Programme does not permit fees in any case, a fee would also have to be charged to some participants and not others — '
  'inside a group of twenty who spend nine days together. The rule is therefore written into the local call in all four countries from the day it is published: travel, accommodation, meals, insurance, materials and '
  'transport from the participant’s own front door are covered in full, and nothing is asked of the participant or the family at any point.')
COUNT(2000)

H3('7.5 Budget per flow')
TBL([
 ['Flow', 'Travel', 'Individual support', 'Flow total'],
 ['1 — Romania (7 persons)', '7 × 56 = **392.00**', '7 × 9 × 46 = **2,898.00**', '3,290.00'],
 ['2 — Türkiye (7 persons)', '7 × 417 = **2,919.00**', '7 × 11 × 46 = **3,542.00**', '6,461.00'],
 ['3 — France / Corsica (6 persons)', '6 × 417 = **2,502.00**', '6 × 11 × 46 = **3,036.00**', '5,538.00'],
 ['4 — Italy / Sardinia (6 persons)', '6 × 417 = **2,502.00**', '6 × 11 × 46 = **3,036.00**', '5,538.00'],
 ['**Subtotal, flows**', '**8,315.00**', '**12,512.00**', '**20,827.00**'],
 ['Organisational support (activity level)', '', '125 × 20', '2,500.00'],
 ['Inclusion support for organisations (activity level)', '', '125 × 12', '1,500.00'],
 ['Inclusion support for participants (activity level, real costs)', '', 'separate dedicated lines', '2,000.00'],
 ['**Total Activity grant**', '', '', '**26,827.00**'],
], widths=[5.6, 3.6, 3.8, 3.6], count=False)
SMALL('Preparatory visit (4,760.00 EUR) sits at project level, not inside the activity, which is why the project total is 31,587.00 and the activity grant 26,827.00.')

H3('7.6 Activity compliance check')

SMALL('Minimum 16 and maximum 60 participants per activity (we have 20); minimum 4 participants per group (5); at least two groups from two different countries (four); one group '
      'leader per national group (four, which is below the national ceiling of one per four young people); at most two facilitators (two); duration between 5 and 21 days excluding travel (seven); participants aged '
      'between 13 and 30 at the start date (14–17); and the activity takes place in the country of one of the participating organisations, which is also the country of the National Agency receiving this application.')

Q('Please describe the background of the participants in each participating group and how each group was formed. Please also provide information on the group leaders, the age of the participants and how country balance is ensured. If necessary, explain how the gender balance is respected.')

H4('The four groups')
TBL([
 ['Group', 'Participants', 'Background, and why these young people are affected by the problem'],
 ['**Romania**\nLAG Napoca Porolissum', '5 young people aged 14–17\n+ 1 group leader',
  'Young people from the rural mountain communes of the LAG territory: Săcuieu, Gilău, Huedin, Mărișel, Căpușu Mare, Mărgău, Măguri-Răcătău, Călățele, Beliș, Mănăstireni, Aghireșu, Izvorul Crișului. Communities '
  'with a thin offer of youth activities and with information circulating in two languages, Romanian and Hungarian. From our survey of this exact population: 96.9% already use AI tools, 20.8% rate their digital '
  'competence as low, 31.3% have never taken part in a non-formal education activity, and lack of information is the first barrier they name. The group is deliberately built to be linguistically mixed, with at least '
  'one Hungarian-speaking participant, because the language question is part of the subject matter.'],
 ['**Türkiye**\nYOBBA', '5 young people aged 14–17\n+ 1 group leader',
  'Young people from Küçükçekmece and the surrounding İstanbul periphery — a dense and diverse district that includes families with migrant and refugee backgrounds. Information travels there through neighbourhood, '
  'family and community networks that national fact-checking never reaches. YOBBA recruits from a volunteer community of over 150 young people a year, prioritising those who have not previously taken part in an '
  'international activity. [TO CONFIRM: YOBBA’s own consultation data on this age group.]'],
 ['**France**\n[Corsica partner]', '5 young people aged 14–17\n+ 1 group leader',
  'Young people from inland and rural communes of Corsica, with limited access to the mainland non-formal education offer because of the cost and the length of the journey, and living in communities where part '
  'of daily communication happens in Corsican, on small local channels with no fact-checking coverage. Around one in four young people aged 16–29 on the island is neither in employment nor in education or '
  'training. [TO CONFIRM: the partner’s own consultation data and localities.]'],
 ['**Italy**\n[Sardinia partner]', '5 young people aged 14–17\n+ 1 group leader',
  'Young people from small localities of inner Sardinia affected by depopulation, where the educational and cultural offer contracts as the population falls. 17.8% of young people aged 15–29 in Sardinia are not in '
  'employment, education or training, against 15.2% nationally and around 11% across Europe. [TO CONFIRM: the partner’s own consultation data and localities.]'],
], widths=[3.0, 3.0, 10.6])

H4('Age, and why the band is this narrow')
P('All twenty participants are young people aged **14 to 17** at the start date of the activity. The band is deliberately tight, for three reasons that all point the same way. They **share the same need** — the survey '
  'evidence behind this project describes exactly this age group, not a wider one. They are at a **similar stage of development**, which means one register of language, one level of abstraction and one set of '
  'expectations about autonomy works for the whole room, instead of two. And it lets us use **one coherent set of non-formal methods** — visual, practical, game-based, built on small mixed teams and peer '
  'teaching — that genuinely fits all of them, rather than a programme that half the group finds childish and the other half finds over their head. A band crossing into legal adulthood would also put minors and '
  'adults in the same accommodation and the same group dynamic, which is a safeguarding problem before it is a learning one.')

H4('Country and gender balance')
P('**Country balance is exact:** five participants and one group leader from each of the four countries, so no national group can dominate the dynamic, and every mixed team of five has one member from each '
  'country. **Gender balance is a binding rule at group level, not an aspiration at project level:** each national group must include at least 40% of each gender — in a group of five, at least two — and the team of '
  'four group leaders is itself gender-balanced. Participants who do not identify within that binary are counted according to their own declaration and are not required to declare anything. The rule is checked '
  'twice, at selection and at final confirmation, by the activity coordinator, and a group that does not meet it is re-opened rather than waved through.')

H4('Group leaders')
P('Each national group has one group leader aged 18 or over, experienced in youth work and in accompanying minors, who travels with the group and stays with it throughout, including at night. Group leaders are '
  'responsible for safeguarding and wellbeing, for the daily reflection in the national group in its own language, for attendance and the code of conduct, for observing one mixed team on Day 4, and afterwards for '
  'supporting their group’s local initiative. Confirmed: **Livia Golovatic** (Romania) and **Aysu Zeybel** (Türkiye), who has herself completed a ten-month European Solidarity Corps placement working weekly with '
  'children in Romania. [TO CONFIRM: group leaders for Corsica and Sardinia.] All four take part in a **two-day online leaders’ briefing in month 4** covering safeguarding, the code of conduct, the escalation chain, '
  'facilitating reflection, and the calibrated use of the observation grid — including the exercise in which all six observers score the same recorded sequence and compare, until they agree on at least 80% of '
  'judgements.')
COUNT(6000)

Q('Please describe the role and involvement of the participants from each participating group in all phases (planning before, during and follow-up).')

H4('Before the application was written — where this project came from')
P('The subject of this project was not chosen by the coordinator’s staff. It came from **153 young people** in the territory who answered our survey, and it was then put back to them for checking. The consultation '
  'was not a formality and it changed the design in ways an expert can verify against the data.')
BUL([
 '**They told us what the problem was.** We went in expecting to hear about a lack of digital skills in general. What came back was narrower: near-universal use of AI tools (96.9% of the 14–17 group), a self-assessed competence barely above the midpoint (3.25 out of 5), and social media as the main window on the world for half of them. That is the need this project addresses, and it is their formulation, not ours.',
 '**They told us where to hold it.** 58.5% asked for learning activities organised in or near their own locality. So the exchange is hosted inside the LAG territory, in the Apuseni, rather than in a comfortable host city — and the host community became part of the programme on Day 5 instead of being scenery.',
 '**They told us what stops them.** Cost (34.4%) and transport (31.2%) are the second and third barriers they name. So there is no participation fee of any kind, transport is paid from each participant’s own front door, and the rule is published with the call rather than explained later.',
 '**They told us how they learn.** 68.1% learn through practical activities; 29.8% through a course. So there are no lectures in this programme, and every session produces an output or a decision taken by the participants themselves.',
 '**They told us what they want out of a mobility.** 60.4% of the 14–17 group named foreign languages and intercultural communication — which is why the mixed teams are recomposed daily and why the working language rule is deliberately generous rather than selective.',
])
P('A **validation meeting with 8–10 young people** from the territory is held before submission. They confirm the wording of the need, review the draft objectives in plain language, and produce the first list of the '
  'claims and rumours they want to see checked — a list that becomes the working material of Day 2 rather than a consultation record filed away.')
FLAG('[TO DO before submission — C20] Hold the validation meeting and minute it: date, number and age of participants, the three things they confirmed and the two things they changed. That minute belongs in the supporting file. An expert who sees a co-design claim without a date and a number discounts it.')

H4('Planning, months 1–4')
P('Once selected, participants do not simply wait for August. Four online sessions of 90 minutes each bring the four groups together in **mixed national composition**, not country by country. **Session 1:** meeting '
  'each other and negotiating the first draft of the group agreement. **Session 2:** participants choose the local disinformation cases that will be analysed during the mobility — each group brings five to eight '
  'documented real cases from its own community, and the participants themselves decide which ones make the working set. **Session 3:** distribution of roles for the mobility — photo and video documentation, '
  'activity diary, energisers, mediation, contact with the host community, timekeeping — and preparation of the intercultural evening. **Session 4:** safety, digital rules, practical arrangements, and questions '
  'answered live by the group leaders. Between sessions a moderated communication group keeps the cohort in contact. A separate online meeting is held with the parents, in each country and in its own language.')

H4('During the mobility')
P('Every day has a **host team of the day**: a mixed team of four participants, one from each country, who open the day, keep the timing, run the energisers and close the day. Teams are recomposed daily so that '
  'every participant works with every nationality at least once. The daily reflection groups — first in the national group and in the participant’s own language, then in plenary — feed directly into adjusting the next '
  'day’s programme, and the adjustments are made **visibly**, so participants see their feedback change something rather than disappear into a form. On Day 6 the participants plan their own local initiatives: date, '
  'venue, audience, partners, who does what.')

H4('Follow-up, months 6–18')
P('The four local initiatives are designed and led by the participants, with the group leader in a support role rather than a coordinating one. Each initiative reaches at least 20 young people and is hosted in a youth '
  'centre, a library, a community centre, the partner organisation’s own space or another accessible public place in the participants’ own community. In month 17 the participants take part in a participatory '
  'evaluation session that feeds the final report — so they close the project as evaluators rather than as beneficiaries. The cohort communication group stays open throughout, and all four organisations involve the '
  'twenty as peer trainers in their later activities.')
COUNT(6000)

PAGEBREAK()

Q('What will the participants learn about the chosen topic of the activity? Which learning outcomes or competences will be developed?')

P('The learning outcomes are expressed against the **eight European key competences for lifelong learning**, the framework Youthpass uses, and each one is tied to the specific sessions that build it and to the '
  'evidence that documents it. This is the competence matrix that governs the agenda in the next section, and the rule is strict in both directions: no session exists in the programme without an entry here, and '
  'no competence is claimed without a session and a piece of evidence behind it. This answers, directly, the point on which the previous application lost 14 of its 40 design points.')

TBL([
 ['Key competence', 'What the participant will be able to do', 'Built in sessions', 'Evidence'],
 ['**KC4 Digital**\n//primary//',
  'Identify the source and the author of an online item; check its date and its original context; run a reverse image search; compare a claim against at least two independent sources; recognise the indicators of '
  'AI-generated text, image, audio and video; use AI tools in their own production ethically and with attribution.',
  'D1.3, D2.1, D2.2, D3.1, D3.2, D3.3, D4.1, D4.2, D6.1',
  'Baseline and final practical test; Day 4 observation grid (four named techniques); the “How I recognise AI-generated content” sheet; the four media products.'],
 ['**KC1 Literacy**\n//primary//',
  'Distinguish fact from opinion and from inference in a text; identify emotional framing, cropped context and false authority; construct a documented verdict in writing that another person can follow and check.',
  'D2.1, D2.2, D2.3, D4.1, D4.2, D4.3',
  'The manipulation-techniques grid produced by the participants; four written verdicts with their sources.'],
 ['**KC6 Citizenship**\n//primary//',
  'Explain why verification is a precondition of democratic participation; argue a position with evidence and accept being refuted by evidence; take part in a dialogue with community members and local '
  'institutions; design and run an activity that serves their own community.',
  'D1.2, D2.3, D5.1, D5.2, D6.3, D7.1',
  'The group agreement; the Day 5 record of local rumours; the four local initiative plans and the initiatives themselves.'],
 ['**KC5 Personal, social and learning to learn**\n//primary//',
  'Assess their own media habits and name their own weak points; recognise that they were wrong about a claim and say so; work in a mixed international team; set a learning target and evaluate their own progress '
  'against it.',
  'D1.3, D2.2, every daily reflection group, D7.2',
  '“My Digital Map” from Day 1 compared with the Day 7 reflection; the individual learning diary; Youthpass.'],
 ['**KC2 Multilingual**',
  'Work and produce a shared result in English at a functional level; support and be supported across languages; understand that information circulates differently inside a minority language.',
  'All mixed-team sessions; D2.3, D5.3',
  'The manipulation grid produced in five languages; the media products in English plus a local language.'],
 ['**KC8 Cultural awareness and expression**',
  'Recognise how stereotypes about their own and other communities are built and amplified; present a message visually and narratively; understand the host community from inside it.',
  'D2.2, D5.2, D5.3, D6.1, D6.2',
  'The stereotype analysis in mixed teams; the intercultural evening; the four media products.'],
 ['**KC7 Entrepreneurship**',
  'Turn an idea into a plan with a date, a venue, an audience, partners and named responsibilities; carry it out and report on it.',
  'D6.3, and the four local initiatives in months 6–15',
  'The four local initiative plans with owners and deadlines; the reports on the initiatives held.'],
 ['**KC3 Mathematical, science and technology**\n//secondary//',
  'Read a statistic critically: check the population measured, the year, the sample and what the figure does not say; recognise a graph designed to mislead.',
  'D2.1, D4.1',
  'The statistics exercise inside D2.1; the verdicts, where numerical claims appear.'],
], widths=[3.0, 6.6, 3.0, 4.0], small=True)

P('**What we do not claim.** Seven days do not produce expert fact-checkers. What they produce is a reflex — the pause before sharing — and four techniques the participant can actually perform, which is what '
  'objective O2 measures and what the observation grid records.')
COUNT(6000)

Q('What are the basic elements of the activity? Please describe at the very least the venue(s), non-formal learning methods and the daily programme.')

H4('Venue')
P('The activity takes place in an accommodation unit **inside the Napoca Porolissum LAG territory**, in the Apuseni Mountains, Cluj County — not in a neutral host city. That is a direct consequence of our data: '
  '58.5% of respondents in the territory asked for learning activities to be organised in or near their own locality, and the host community is itself part of the programme on Day 5. Requirements: capacity for at '
  'least 30 people, one plenary room, at least four separate spaces for small-team work, stable internet, and accessibility. [TO CONFIRM: the unit, with a written offer, before submission.]')

H4('Non-formal learning methods')
BUL([
 '**Learning through controlled error** — the central method. Participants receive the false material, commit to a judgement, and only then learn the verdict. The surprise is the instrument that works on overconfidence, and it is used deliberately on Day 2 before any teaching happens.',
 '**Mixed international teams, recomposed daily**, so that every participant works with every nationality.',
 '**Simulation and role play:** the verification newsroom (D4.1), the information tribunal (D2.3), an escape room built around the verification route (D3.3).',
 '**Structured debate with an explicit rule:** every claim must be supportable with evidence, facilitators included.',
 '**Peer-to-peer teaching:** each team teaches the others the tool it tested (D3.2).',
 '**Media production as applied learning** (Day 6), led by the partner with demonstrated expertise in it.',
 '**Daily reflection** in the national group and in the participant’s own language, then in plenary; plus an individual learning diary.',
 '**Outdoor activities and energisers** in the natural setting of the territory.',
])
P('There are **no lectures** in this programme. Every session produces an output or a decision taken by the participants. That is not a stylistic preference: in our territory only 29.8% of respondents said a course '
  'is the format that helps them learn, against 68.1% who chose practical activities.')

H3('7.7 Daily programme — the full table, which goes into the Timetable annex')
P('Each session carries the objective it serves, the method, the key competences it builds, the output it produces and the **named person responsible** for running it. Session codes correspond to the competence '
  'matrix above. “Facilitator 1” is designated by the coordinator; “Facilitator 2” is designated by YOBBA.')
COUNT(6000)

AG = [['Code', 'Session', 'Serves', 'Method', 'Compet.', 'Output', 'Responsible']]
def DAY(t): AG.append([t, '', '', '', '', '', ''])
def S(*r): AG.append(list(r))

DAY('**Day 0 — Sunday 8 August 2027: arrival** (travel day, not counted among the seven activity days)')
S('D0.1','Arrival, accommodation, guided safety tour of the venue','—','Guided walk-through: exits, assembly point, first-aid kit, staff rooms, evacuation drill','—','Signed arrival and room list','Iulia Fătu (logistics) with the four group leaders')
S('D0.2','Informal dinner and first contact','—','Informal','KC2','—','Group leaders')

DAY('**Day 1 — Monday 9 August: who we are and what we consume**')
S('D1.1','Getting to know each other across languages','O2','Name games, non-verbal and visual ice-breakers, mixed-team formation','KC2, KC5','The four mixed teams for the week','Facilitator 1 (coordinator)')
S('D1.2','Our group agreement','O2','Negotiation in small groups then plenary consensus; non-discrimination and respect for all languages present are non-negotiable clauses','KC6, KC5','Group agreement, signed by all 26 people present','Claudiu Iancu (LAG)')
S('D1.3','“My Digital Map” — each participant maps their own media diet over one ordinary day: what they open, in what order, for how long, and where each piece of information came from','O1','Individual mapping on paper, then comparison in mixed teams; no judgement, no correction','KC4, KC5','20 individual digital maps, kept and re-read on Day 7','Claudiu Iancu (LAG)')
S('D1.4','Safety, protection and digital rules; introduction to Youthpass and the learning diary; what else Erasmus+ offers them after this project','O1, O2','Interactive briefing; the safeguarding focal point introduces herself in person and gives her direct contact details','KC5','Each participant holds the contact chain and 2 personal learning targets','Marilena Georgescu (safeguarding) and Claudiu Iancu')
S('D1.5','Reflection: national groups, then plenary','—','Guided reflection in the participant’s own language','KC5','Diary entries; feedback that shapes Day 2','The four group leaders')

DAY('**Day 2 — Tuesday 10 August: Spot the Fake**')
S('D2.1','**The judgement, before the verdict.** Teams receive a mixed set of real and false items — including two misleading statistics and one manipulated graph — and must sort them. Only afterwards is the answer key revealed','O1, O2','Learning through controlled error; the team decision is recorded before disclosure','KC1, KC4, KC3','Each team’s score, kept as the informal starting point of the week','Facilitator 1 (coordinator)')
S('D2.2','The mechanics of manipulation: emotional headlines, cropped context, false authority, numbers out of context. Worked on the real cases the four groups brought from their own communities, including content carrying ethnic, gender and migration stereotypes, analysed in mixed teams','O1, O2','Case gallery; pair analysis; naming the technique used','KC1, KC4, KC8, KC5','The shared grid of manipulation techniques, produced by participants in five languages','Claudiu Iancu (LAG), with the Corsican partner leading the strand on minority-language circulation [TO CONFIRM]')
S('D2.3','“The information tribunal”: structured debate on where opinion ends and falsehood begins','O2','Role-played debate under the rule that every claim must be evidenced','KC1, KC6, KC2','An agreed working distinction between opinion, error and deliberate falsehood','Facilitator 2 (YOBBA)')
S('D2.4','Reflection and decompression','—','National groups then plenary; short decompression sequence after work on distressing content','KC5','Diary; adjustment of Day 3','Group leaders; Marilena Georgescu available for individual conversations')

DAY('**Day 3 — Wednesday 11 August: AI or human?**')
S('D3.1','AI-generated content: text, image, voice, video. What the tools can and cannot do, and what traces they leave','O1, O2','Hands-on comparison of real and generated pairs; participants generate examples themselves and try to fool each other','KC4, KC3','The “How I recognise AI-generated content” sheet, written by the participants','Doğan Can Karabudak (YOBBA), with Claudiu Iancu')
S('D3.2','**Tool laboratory.** Each of the four teams tests one free verification tool — reverse image search, web archive, context and metadata checking, a fact-checking resource from one of the four countries — and then teaches it to the others','O1, O2','Peer-to-peer teaching; each team must produce a two-minute demonstration','KC4, KC2, KC5','Annotated tool list, with one national verification resource per partner country, usable at home','Facilitator 1, with the four group leaders supporting their teams')
S('D3.3','“The verification route” escape room: teams race through source → author → date → context → two independent sources → image','O2','Game; the route is repeated until it becomes automatic','KC4, KC5','Every participant has performed the full route at least twice','Livia Golovatic (LAG)')
S('D3.4','Ethics of AI use: when is it legitimate, and what must be declared','O2','Case discussion; participants write the rule they will apply on Day 6','KC6, KC5','The group’s own AI-use rule for its own productions','Doğan Can Karabudak (YOBBA)')
S('D3.5','Reflection; observer refresher (30 min, team only, after participants)','—','National groups then plenary','KC5','Diary; the six observers re-read the descriptors and settle what counts as a prompt','Group leaders; Claudiu Iancu for the observer refresher')

DAY('**Day 4 — Thursday 12 August: fact-checkers for a day — the assessed day**')
S('D4.1','**The verification newsroom.** Mixed teams receive real viral claims and take each one through the whole route to a documented verdict: source, author, date, context, two independent sources, image check','O2','Full simulation, three hours, facilitators intervening only when asked. The observation grid for objective O2 is applied here','KC4, KC1, KC3, KC5','Four documented verdicts with sources; observation data recording, for each of the 20 participants, whether they performed each of the four techniques','Claudiu Iancu (LAG) moderating, not scoring; the four group leaders each observing one mixed team; Facilitators 1 and 2 double-scoring 5 participants each, independently')
S('D4.2','Cross-examination: each team presents its verdict and the others try to break it','O2','Adversarial peer review under evidence rules','KC1, KC4, KC2','Verdicts revised where the challenge succeeded','Facilitator 2 (YOBBA)')
S('D4.3','What we got wrong, and why','O1, O2','Collective analysis of the errors made during the day, facilitators’ errors included','KC5, KC1','List of the traps the group actually fell into','Claudiu Iancu')
S('D4.4','Reflection and mid-week check; observer moderation meeting immediately after D4.1','—','National groups then plenary; mid-point review of individual learning targets','KC5','Diary; adjustment of Days 5–7; moderated observation scores','Group leaders; Claudiu Iancu chairing the moderation')

DAY('**Day 5 — Friday 13 August: the community and intercultural day**')
S('D5.1','Visit to a village of the LAG territory, through the organisation’s partnership network','O3','Field visit; guided observation','KC6, KC8','—','Livia Golovatic (LAG), with the host municipality')
S('D5.2','Conversation with residents and municipal representatives: what rumours and false information actually circulate here, through which channels, and who gets hurt','O3','Facilitated dialogue in small mixed groups, with interpreting; participants prepare the questions the evening before','KC6, KC8, KC2','The record of real local rumours, which becomes the working material for Day 6','[Sardinia partner] leading the method, with Livia Golovatic on the local relationship')
S('D5.3','Preparation and running of the intercultural evening, with produce from local producers of the territory','O2','Participant-led preparation; each national group presents its community, including its language','KC8, KC2, KC5','—','The four group leaders; participants in the roles assigned in month 3')

DAY('**Day 6 — Saturday 14 August: Make It, Don’t Fake It**')
S('D6.1','Media production technique: how a short video or an infographic is built to be clear and honest','O3','Practical session led by the partner whose declared core expertise is digital media','KC4, KC8','—','Doğan Can Karabudak and Aysu Zeybel (YOBBA)')
S('D6.2','**Production.** Each team produces a short video or infographic debunking one of the local myths collected on Day 5, using AI ethically and with declared attribution, under the rule the group wrote on Day 3','O3','Team production with technical support on request','KC4, KC8, KC1, KC2','Four media products, in English plus a local language','YOBBA leading; all facilitators supporting')
S('D6.3','Planning the four local initiatives: date, venue, audience, partner institution, responsibilities, indicator','O3','Work in national groups on a common template; participants decide, group leaders advise','KC7, KC6, KC5','Four local initiative plans, each with named owners and deadlines','[Sardinia partner] providing the template and method; group leaders supporting')
S('D6.4','Reflection; media safeguarding check of everything produced','—','National groups; two-step content review before anything is published','KC5','Diary; approved content','Group leaders; Marilena Georgescu approving publication')

DAY('**Day 7 — Sunday 15 August: public presentation, evaluation, Youthpass**')
S('D7.1','Public presentation of the results, with guests from the host community, the partner municipalities and the local press','O3','Participant-led presentation; the four media products are shown and explained','KC6, KC8, KC2','Public visibility; first contacts for the local initiatives','Participants; Livia Golovatic coordinating; Alina Ioana Baba receiving guests')
S('D7.2','Youthpass reflection session: the eight key competences, worked through against the individual learning diaries and the Day 1 digital maps','O1, O2','Structured individual and peer reflection; each participant names and evidences what changed','KC5, all','20 Youthpass certificates, plus 4 for the group leaders','Claudiu Iancu (LAG)')
S('D7.3','Participatory evaluation of the activity','—','Non-formal evaluation methods; anonymous written questionnaire in parallel','KC5','Evaluation data for the project report','Facilitators 1 and 2')
S('D7.4','Written commitments for the four local initiatives; closing','O3','Public commitment in front of the whole group','KC7, KC6','Four signed commitments, with dates','Group leaders')

DAY('**Day 8 — Monday 16 August 2027: departure** (travel day)')

t = TBL(AG, widths=[1.1, 5.0, 1.0, 3.4, 1.3, 2.6, 2.2], small=True)
# merge the day-divider rows into one full-width shaded band
for r in t.rows:
    if r.cells[0].text.strip().startswith('Day') and r.cells[1].text.strip() == '':
        merged = r.cells[0].merge(r.cells[len(r.cells) - 1])
        shade(merged, 'F0F4FA')
COUNT(8000, cut='**Do not cut this — annex it.** The Timetable slot exists on the live form, so this table goes there in full, where it has no character limit and where the expert expects to find it. The narrative field '
  'then takes the day-level summary in 7.8, which measures about 4,600 characters against roughly 10,000 for this table, plus the venue paragraph and the methods list — about 1,900 characters together — and the pointer '
  'sentence that sends the reader to the annex. If even that is too long for the live field, the summary is the part to shorten, because the annex already carries the detail.')
SMALL('Note on merged rows: in the online form the day headers are typed as their own lines. Here they are left as full-width rows so the structure stays readable when the table is pasted or exported.')

PAGEBREAK()
H3('7.8 What goes into the field, now that the Timetable annex exists')
CALLOUT('The full programme is annexed. The field gets a summary.',
        'The Timetable slot exists on the live form, so the table in 7.7 goes there in full — all 24 sessions with all five attributes, no character limit, and in the place an expert looks for it. That leaves the narrative '
        'field needing a **summary** plus a sentence pointing at the annex, rather than the whole programme squeezed in. Three versions are given below, shortest first, each labelled with its own measured character count. '
        '**Take the shortest one that leaves room for the venue paragraph and the methods list** (about 1,900 characters together) inside whatever limit the live field turns out to have. '
        'Whichever you choose, end it with the pointer sentence — that is what sends the expert to the annex instead of leaving them to assume the detail does not exist.',
        'EAF3EA', '9FC49F')

H4('The pointer sentence — use it with any of the three')
P('The full seven-day programme is annexed as the project timetable. Every session in it carries five attributes: the objective it serves, the non-formal method used, the key competences it builds, the output it '
  'produces, and the person responsible for running it — and the session codes below match the competence matrix and the timetable exactly.')

SUMMARY = [
 '**Day 0, Sun 8 Aug — arrival.** Travel day. Accommodation, guided safety tour of the venue with an evacuation drill (D0.1), informal first contact (D0.2).',
 '**Day 1, Mon 9 Aug — who we are and what we consume.** Serves O1 and O2. The group forms itself and looks at its own habits before anyone teaches anything: mixed-team formation (D1.1), the group agreement the participants '
 'negotiate themselves (D1.2), “My Digital Map”, in which each participant maps one ordinary day of their own media diet (D1.3), and the safety, safeguarding and Youthpass briefing (D1.4). Outputs: the four mixed teams, a '
 'signed group agreement, 20 digital maps kept for Day 7, and two personal learning targets each. Led by Claudiu Iancu and Marilena Georgescu, with Facilitator 1.',
 '**Day 2, Tue 10 Aug — Spot the Fake.** Serves O1 and O2. The controlled-error day: teams commit to a verdict on a mixed set of real and false items before the answer key is revealed (D2.1), then take apart the mechanics of '
 'manipulation on the real cases their own four communities brought, including content carrying ethnic, gender and migration stereotypes (D2.2), and close with a structured debate on where opinion ends and falsehood begins '
 '(D2.3). Outputs: the manipulation-techniques grid produced by participants in five languages. Led by Claudiu Iancu and Facilitators 1 and 2, with the Corsican partner leading the minority-language strand.',
 '**Day 3, Wed 11 Aug — AI or human?** Serves O1 and O2. Participants generate AI content themselves and try to fool each other, then write their own recognition sheet (D3.1); four teams each test one free verification tool '
 'and teach it to the others (D3.2); the verification route is drilled as an escape room until it is automatic (D3.3); and the group writes the AI-use rule it will apply to its own productions on Day 6 (D3.4). Led by Doğan '
 'Can Karabudak of YOBBA with Claudiu Iancu, Facilitator 1 and Livia Golovatic.',
 '**Day 4, Thu 12 Aug — fact-checkers for a day. The assessed day.** Serves O2. A three-hour verification newsroom in which mixed teams take real viral claims through the whole route to a documented verdict, with facilitators '
 'intervening only when asked (D4.1) — this is where the observation grid for objective O2 is applied, by four group leaders each observing one mixed team, with Facilitators 1 and 2 independently double-scoring five '
 'participants each. Then cross-examination of each verdict by the other teams (D4.2) and a collective analysis of the day’s errors, the facilitators’ included (D4.3). Outputs: four documented verdicts with sources, and '
 'per-participant data on all four techniques.',
 '**Day 5, Fri 13 Aug — the community and intercultural day.** Serves O3. A visit to a village of the territory (D5.1) and a facilitated dialogue with residents and municipal representatives about the rumours that actually '
 'circulate there, through which channels, and who gets hurt (D5.2) — the record of those rumours becomes the working material for Day 6. The day closes with the intercultural evening, prepared by the participants, with '
 'produce from local producers (D5.3). Method led by the Sardinian partner, local relationship by Livia Golovatic.',
 '**Day 6, Sat 14 Aug — Make It, Don’t Fake It.** Serves O3. Led by YOBBA, the partner whose core expertise is digital media: how a short video or infographic is built to be clear and honest (D6.1), then production, each team '
 'debunking one of the myths collected on Day 5, using AI under the rule the group wrote on Day 3 (D6.2). In parallel, the four national groups plan their own local initiatives on a common template — date, venue, audience, '
 'partner institution, responsibilities, indicator (D6.3). Outputs: four media products in English plus a local language, and four initiative plans with named owners and deadlines.',
 '**Day 7, Sun 15 Aug — presentation, evaluation, Youthpass.** Serves O1, O2 and O3. A public presentation by the participants to guests from the host community, the municipalities and the local press (D7.1); the Youthpass '
 'session, in which each participant re-reads their own Day 1 digital map against their learning diary and names, with evidence, what changed (D7.2); a participatory evaluation (D7.3); and the written, publicly made '
 'commitments to the four local initiatives (D7.4). Outputs: 20 Youthpass certificates plus 4 for the group leaders, and four signed commitments with dates.',
 '**Day 8, Mon 16 Aug — departure.** Travel day.',
 '**Every evening**, reflection runs first in the national group and in the participant’s own language, then in plenary, and what comes out of it visibly changes the next day’s programme (D1.5, D2.4, D3.5, D4.4, D6.4).',
]
for s in SUMMARY: P(s)
LEN_S = sum(len(clean(s)) + 1 for s in SUMMARY)
COUNT(5000)
SMALL('Version 1 — day-level summary, %s characters. Recommended: it keeps the objectives, the methods, the outputs and the named leads visible in the field, and sends the expert to the annex for the session-by-session detail.' % f'{LEN_S:,}')

PAGEBREAK()
H3('7.9 Two longer versions, if the field has room')
CALLOUT('Only if you want the session-by-session detail in the field as well.',
        'Neither of these is necessary now that the timetable is annexed — the annex carries the full detail. They exist because a field with a generous limit is a free opportunity to put the five attributes in front of the '
        'expert twice, and because you may prefer not to rely on the annex being read. **Version A** is the 7.7 table rewritten as running text, one line per session. **Version B** is the same content in compressed notation, '
        'with every descriptive clause cut. Each heading carries its own measured length.',
        'FFF6E5', 'E8C97A')
SMALL('Legend: O1–O3 are the project objectives; KC1–KC8 the European key competences; F1 the facilitator designated by the coordinator, F2 the facilitator designated by YOBBA; GL the group leaders.')
CMP = [
 ('**Day 0 — Sun 8 Aug, arrival (travel day).**',
  'D0.1 Arrival, accommodation and guided safety tour — exits, assembly point, first-aid kit, evacuation drill; output: signed arrival and room list; Iulia Fătu with the four GL. '
  'D0.2 Informal dinner and first contact — KC2; GL.'),
 ('**Day 1 — Mon 9 Aug, who we are and what we consume.**',
  'D1.1 Getting to know each other across languages — O2; non-verbal and visual ice-breakers, mixed-team formation; KC2, KC5; output: the four mixed teams for the week; F1. '
  'D1.2 Our group agreement — O2; negotiation in small groups then plenary consensus, with non-discrimination and respect for all languages as non-negotiable clauses; KC6, KC5; output: agreement signed by all 26; Claudiu Iancu. '
  'D1.3 “My Digital Map”, each participant maps their own media diet over one ordinary day — O1; individual mapping then comparison in mixed teams, no judgement; KC4, KC5; output: 20 digital maps, re-read on Day 7; Claudiu Iancu. '
  'D1.4 Safety, protection and digital rules; Youthpass and the learning diary introduced — O1, O2; interactive briefing, the safeguarding focal point introduces herself in person; KC5; output: contact chain and 2 personal learning targets per participant; Marilena Georgescu and Claudiu Iancu. '
  'D1.5 Reflection, national groups then plenary — guided reflection in the participant’s own language; KC5; output: diary entries and feedback shaping Day 2; the four GL.'),
 ('**Day 2 — Tue 10 Aug, Spot the Fake.**',
  'D2.1 The judgement before the verdict: teams sort a mixed set of real and false items, including two misleading statistics and a manipulated graph, and only then see the key — O1, O2; learning through controlled error, decisions recorded before disclosure; KC1, KC4, KC3; output: each team’s score, the informal starting point of the week; F1. '
  'D2.2 The mechanics of manipulation — emotional headlines, cropped context, false authority, numbers out of context — worked on the real cases the four groups brought, including content carrying ethnic, gender and migration stereotypes, analysed in mixed teams — O1, O2; case gallery, pair analysis, naming the technique; KC1, KC4, KC8, KC5; output: the shared manipulation-techniques grid in five languages; Claudiu Iancu with the Corsican partner on minority-language circulation. '
  'D2.3 “The information tribunal”, structured debate on where opinion ends and falsehood begins — O2; role-played debate under the rule that every claim must be evidenced; KC1, KC6, KC2; output: an agreed working distinction between opinion, error and deliberate falsehood; F2. '
  'D2.4 Reflection and decompression — national groups then plenary, with a short decompression sequence after distressing content; KC5; output: diary, adjustment of Day 3; GL, with Marilena Georgescu available individually.'),
 ('**Day 3 — Wed 11 Aug, AI or human?**',
  'D3.1 AI-generated text, image, voice and video: what the tools can and cannot do, and what traces they leave — O1, O2; hands-on comparison of real and generated pairs, participants generate examples and try to fool each other; KC4, KC3; output: the “How I recognise AI-generated content” sheet, written by participants; Doğan Can Karabudak with Claudiu Iancu. '
  'D3.2 Tool laboratory: each team tests one free verification tool — reverse image search, web archive, context and metadata checking, a national fact-checking resource — then teaches it to the others — O1, O2; peer-to-peer teaching, two-minute demonstration per team; KC4, KC2, KC5; output: annotated tool list with one national resource per partner country; F1 with the four GL. '
  'D3.3 “The verification route” escape room: source → author → date → context → two independent sources → image — O2; game, repeated until automatic; KC4, KC5; output: every participant has run the full route twice; Livia Golovatic. '
  'D3.4 Ethics of AI use: when is it legitimate and what must be declared — O2; case discussion, participants write the rule they will apply on Day 6; KC6, KC5; output: the group’s own AI-use rule; Doğan Can Karabudak. '
  'D3.5 Reflection; plus a 30-minute observer refresher for the team after participants leave — KC5; output: diary, and the six observers agree what counts as a prompt; GL, Claudiu Iancu for the refresher.'),
 ('**Day 4 — Thu 12 Aug, fact-checkers for a day (the assessed day).**',
  'D4.1 The verification newsroom: mixed teams take real viral claims through the whole route to a documented verdict — O2; three-hour full simulation, facilitators intervening only when asked, the O2 observation grid applied here; KC4, KC1, KC3, KC5; output: four documented verdicts with sources, plus observation data recording for each of the 20 participants whether they performed each of the four techniques; Claudiu Iancu moderating and not scoring, the four GL each observing one mixed team, F1 and F2 independently double-scoring five participants each. '
  'D4.2 Cross-examination: each team presents its verdict and the others try to break it — O2; adversarial peer review under evidence rules; KC1, KC4, KC2; output: verdicts revised where the challenge succeeded; F2. '
  'D4.3 What we got wrong, and why — O1, O2; collective analysis of the day’s errors, facilitators’ included; KC5, KC1; output: the list of traps the group actually fell into; Claudiu Iancu. '
  'D4.4 Reflection and mid-week check, with the observer moderation meeting immediately after D4.1 — national groups then plenary, mid-point review of individual learning targets; KC5; output: diary, adjustment of Days 5–7, moderated observation scores; GL, Claudiu Iancu chairing.'),
 ('**Day 5 — Fri 13 Aug, the community and intercultural day.**',
  'D5.1 Visit to a village of the LAG territory — O3; field visit with guided observation; KC6, KC8; Livia Golovatic with the host municipality. '
  'D5.2 Conversation with residents and municipal representatives: what rumours actually circulate here, through which channels, and who gets hurt — O3; facilitated dialogue in small mixed groups with interpreting, questions prepared the evening before; KC6, KC8, KC2; output: the record of real local rumours, which becomes the working material for Day 6; the Sardinian partner leading the method, Livia Golovatic on the local relationship. '
  'D5.3 Preparation and running of the intercultural evening, with produce from local producers — O2; participant-led, each national group presents its community including its language; KC8, KC2, KC5; the four GL, participants in the roles assigned in month 3.'),
 ('**Day 6 — Sat 14 Aug, Make It, Don’t Fake It.**',
  'D6.1 Media production technique: how a short video or infographic is built to be clear and honest — O3; practical session led by the partner whose core expertise is digital media; KC4, KC8; Doğan Can Karabudak and Aysu Zeybel. '
  'D6.2 Production: each team makes a short video or infographic debunking one of the local myths collected on Day 5, using AI ethically and with declared attribution under the rule the group wrote on Day 3 — O3; team production with technical support on request; KC4, KC8, KC1, KC2; output: four media products in English plus a local language; YOBBA leading, all facilitators supporting. '
  'D6.3 Planning the four local initiatives — date, venue, audience, partner institution, responsibilities, indicator — O3; work in national groups on a common template, participants decide and GL advise; KC7, KC6, KC5; output: four initiative plans with named owners and deadlines; the Sardinian partner providing template and method. '
  'D6.4 Reflection and media safeguarding check of everything produced — national groups, two-step content review before publication; KC5; output: diary, approved content; GL, Marilena Georgescu approving.'),
 ('**Day 7 — Sun 15 Aug, public presentation, evaluation, Youthpass.**',
  'D7.1 Public presentation with guests from the host community, the partner municipalities and the local press — O3; participant-led, the four media products shown and explained; KC6, KC8, KC2; output: public visibility and first contacts for the local initiatives; participants, Livia Golovatic coordinating, Alina Ioana Baba receiving guests. '
  'D7.2 Youthpass reflection session: the eight key competences worked through against the learning diaries and the Day 1 digital maps — O1, O2; structured individual and peer reflection, each participant names and evidences what changed; KC5 and all; output: 20 Youthpass certificates plus 4 for the GL; Claudiu Iancu. '
  'D7.3 Participatory evaluation of the activity — non-formal evaluation methods with an anonymous written questionnaire in parallel; KC5; output: evaluation data for the project report; F1 and F2. '
  'D7.4 Written commitments for the four local initiatives, and closing — O3; public commitment in front of the whole group; KC7, KC6; output: four signed commitments with dates; GL.'),
 ('**Day 8 — Mon 16 Aug, departure (travel day).**', ''),
]
LEN_A = sum(len(clean(h + (' ' + b if b else ''))) + 1 for h, b in CMP)
H4('Version A — full sentences, %s characters' % f'{LEN_A:,}')
for head, body in CMP:
    P(head + (' ' + body if body else ''))
COUNT(5000, cut='Do not trim this one by hand. Use the day-level summary in 7.8, or Version B below — both keep every attribute. Trimming A ad hoc is how the five attributes per session quietly disappear again, and their '
  'absence is precisely what cost 14 of the 40 design points last time.')

SMALL('Notation: **O1–O3** project objectives · **KC1–KC8** key competences · **F1** facilitator designated by the coordinator · **F2** facilitator designated by YOBBA · **GL** group leaders · **CI** Claudiu Iancu · '
      '**LG** Livia Golovatic · **MG** Marilena Georgescu · **IF** Iulia Fătu · **AB** Alina Ioana Baba · **DK** Doğan Can Karabudak · **AZ** Aysu Zeybel · **[CO]** Corsican partner · **[SA]** Sardinian partner. '
      'Each entry reads: code · session · objectives served · method · competences · output · responsible.')
TIGHT = [
 '**D0 Sun 8 Aug, arrival (travel day).** D0.1 venue safety tour · — · guided walk-through, exits, assembly point, evacuation drill · — · signed arrival and room list · IF + GL. D0.2 informal dinner · — · informal · KC2 · — · GL.',
 '**D1 Mon 9 Aug, who we are and what we consume.** D1.1 getting to know each other across languages · O2 · non-verbal ice-breakers, mixed-team formation · KC2 KC5 · the four mixed teams · F1. '
 'D1.2 group agreement · O2 · small-group negotiation then plenary consensus, non-discrimination and respect for all languages non-negotiable · KC6 KC5 · agreement signed by all 26 · CI. '
 'D1.3 “My Digital Map” · O1 · individual mapping then mixed-team comparison, no judgement · KC4 KC5 · 20 digital maps, re-read Day 7 · CI. '
 'D1.4 safety, protection, digital rules, Youthpass and diary · O1 O2 · interactive briefing, safeguarding focal point introduced in person · KC5 · contact chain + 2 learning targets each · MG + CI. '
 'D1.5 reflection · — · national groups in own language, then plenary · KC5 · diary, feedback shaping Day 2 · GL.',
 '**D2 Tue 10 Aug, Spot the Fake.** D2.1 judgement before the verdict · O1 O2 · controlled error, decisions recorded before the key is revealed · KC1 KC4 KC3 · team scores as the week’s starting point · F1. '
 'D2.2 mechanics of manipulation, on the groups’ own local cases incl. stereotype content · O1 O2 · case gallery, pair analysis, naming the technique · KC1 KC4 KC8 KC5 · manipulation grid in five languages · CI + [CO] on minority-language circulation. '
 'D2.3 information tribunal · O2 · role-played debate, every claim evidenced · KC1 KC6 KC2 · working distinction opinion / error / falsehood · F2. '
 'D2.4 reflection and decompression · — · national then plenary, decompression after distressing content · KC5 · diary, Day 3 adjusted · GL + MG available.',
 '**D3 Wed 11 Aug, AI or human?** D3.1 AI-generated text, image, voice, video · O1 O2 · hands-on real/generated pairs, participants generate and try to fool each other · KC4 KC3 · the AI-recognition sheet · DK + CI. '
 'D3.2 tool laboratory, four free tools incl. one national resource per country · O1 O2 · peer teaching, two-minute demo per team · KC4 KC2 KC5 · annotated tool list usable at home · F1 + GL. '
 'D3.3 verification-route escape room · O2 · game, repeated until automatic · KC4 KC5 · full route run twice per participant · LG. '
 'D3.4 ethics of AI use · O2 · case discussion, participants write their own rule · KC6 KC5 · the group’s AI-use rule for Day 6 · DK. '
 'D3.5 reflection + 30-min observer refresher · — · national then plenary · KC5 · diary; observers agree what counts as a prompt · GL, CI.',
 '**D4 Thu 12 Aug, fact-checkers for a day — assessed.** D4.1 verification newsroom · O2 · three-hour simulation, facilitators intervene only on request, O2 observation grid applied · KC4 KC1 KC3 KC5 · four documented verdicts + per-participant data on all four techniques · CI moderating without scoring, 4 GL each observing one mixed team, F1 and F2 double-scoring 5 each. '
 'D4.2 cross-examination · O2 · adversarial peer review under evidence rules · KC1 KC4 KC2 · verdicts revised where challenged · F2. '
 'D4.3 what we got wrong · O1 O2 · collective error analysis, facilitators included · KC5 KC1 · list of traps the group fell into · CI. '
 'D4.4 reflection, mid-week check, observer moderation · — · national then plenary, learning targets reviewed · KC5 · diary, Days 5–7 adjusted, moderated scores · GL, CI chairing.',
 '**D5 Fri 13 Aug, community and intercultural day.** D5.1 village visit · O3 · field visit, guided observation · KC6 KC8 · — · LG + host municipality. '
 'D5.2 dialogue with residents and municipal representatives on real local rumours · O3 · facilitated small mixed groups with interpreting, questions prepared the night before · KC6 KC8 KC2 · record of local rumours, the raw material for Day 6 · [SA] on method, LG on the local relationship. '
 'D5.3 intercultural evening with local producers · O2 · participant-led, each group presents its community and language · KC8 KC2 KC5 · — · GL + participants in month-3 roles.',
 '**D6 Sat 14 Aug, Make It, Don’t Fake It.** D6.1 media production technique · O3 · practical session by the digital-media partner · KC4 KC8 · — · DK + AZ. '
 'D6.2 production, debunking a Day 5 myth, AI used ethically under the group’s own rule · O3 · team production, technical support on request · KC4 KC8 KC1 KC2 · four media products, English + a local language · YOBBA leading. '
 'D6.3 planning the four local initiatives · O3 · national groups on a common template, participants decide · KC7 KC6 KC5 · four plans with named owners and deadlines · [SA] template and method. '
 'D6.4 reflection + media safeguarding check · — · two-step content review before publication · KC5 · diary, approved content · GL, MG approving.',
 '**D7 Sun 15 Aug, presentation, evaluation, Youthpass.** D7.1 public presentation with community, municipalities and press · O3 · participant-led, media products shown and explained · KC6 KC8 KC2 · visibility, first contacts for the local initiatives · participants, LG coordinating, AB receiving guests. '
 'D7.2 Youthpass session against the diaries and the Day 1 maps · O1 O2 · structured individual and peer reflection, each names and evidences what changed · KC5 + all · 20 Youthpass + 4 for GL · CI. '
 'D7.3 participatory evaluation · — · non-formal methods + anonymous written questionnaire · KC5 · evaluation data for the report · F1 F2. '
 'D7.4 written commitments for the local initiatives, closing · O3 · public commitment before the group · KC7 KC6 · four signed commitments with dates · GL.',
 '**D8 Mon 16 Aug, departure (travel day).**',
]
LEN_B = sum(len(clean(t)) + 1 for t in TIGHT)
H4('Version B — same content in compressed notation, %s characters' % f'{LEN_B:,}')
for t in TIGHT: P(t)
COUNT(5000, cut='Version B is already cut to the bone. If it still does not fit and you do not want the day-level summary of 7.8 instead, take these in order and stop as soon as it fits. '
  '(1) Delete the D0 and D8 lines — they are travel days and are stated in the activity dates anyway: about 300 characters. '
  '(2) Delete the method clause from the five reflection sessions (D1.5, D2.4, D3.5, D4.4, D6.4) — the method is identical every evening and is described in full in the preparation and recognition answers: about 350. '
  '(3) Replace each responsible person’s initials with their role code where the person is already named in the roles table: about 200. '
  'Never cut an objective, a competence code or an output — those three are what the assessment is looking for.')

PAGEBREAK()

Q('How will the groups of participants cooperate and communicate between them to prepare and follow-up on the Youth Exchange?')

P('**Before.** Four joint online sessions of 90 minutes in months 3 and 4, in **mixed national composition** rather than country by country, so the teams that will work together in August have already met. A shared '
  'workspace holds the documents, the case files and the templates; a moderated messaging group, with clear rules and no sharing of personal data, keeps day-to-day contact going. Between sessions each group has '
  'a concrete deliverable **for the others**: five to eight documented cases of disinformation from its own community, uploaded to the shared space, which the whole cohort then reviews. The group leaders hold their '
  'own separate channel and a two-day online briefing.')
P('**During.** Mixed teams recomposed daily; the host team of the day; the daily reflection cycle running from the national group into the plenary; and a visible feedback loop, where changes requested one evening '
  'appear in the next day’s programme.')
P('**After.** The cohort communication group stays open for the whole 18 months and becomes the working space for the four local initiatives: each group posts its plan and the others comment before it happens. A '
  'joint online meeting is held after the first two initiatives, in month 10, so that the two groups that have not yet run theirs learn from what went wrong rather than repeating it. A follow-up questionnaire in month '
  '12 and a participatory evaluation session in month 17 close the cycle. The four media products and the toolkit circulate through all four organisations’ channels, and each group is expected to disseminate the '
  'other three groups’ products, not only its own.')
COUNT()

PAGEBREAK()
# =====================================================================
H1('8. Project design')
H2('8.1 Preparation, support and follow-up')
Q('How will you prepare the participants before the start of the activity (e.g. intercultural, linguistic, risk-prevention etc.) and how will you support them during and after the activity?')

H4('Before')
P('Preparation runs over **four months, not four weeks**, because 31.3% of the young people in our target population have never taken part in any non-formal education activity and 12.5% name lack of '
  'self-confidence as a barrier. For a fourteen-year-old leaving the country for the first time, the preparation //is// the inclusion measure.')
BUL([
 '**Baseline (month 2).** The 15-item practical verification test is taken by all 20 participants before any learning activity, together with a short questionnaire on media habits. It establishes the starting value for objective O1 and it tells the facilitators what the group actually cannot do — which is not always what they say they cannot do.',
 '**Four joint online sessions (months 3–4)**, 90 minutes each, in mixed national teams: meeting each other and drafting the group agreement; choosing the local cases to be analysed; distributing roles and preparing the intercultural evening; safety, digital rules and practical arrangements.',
 '**Linguistic preparation.** A “detective’s glossary” of about 60 working terms in five languages, produced //with// the participants rather than handed to them, plus two light conversation sessions inside the online meetings. The aim is functional confidence, not language teaching: A2 is enough, and the programme is built so that it is.',
 '**Intercultural preparation.** Each group prepares a short presentation of its own community for the intercultural evening, including its language. Group leaders run a session on expectations and stereotypes before departure — deliberately, since the project itself works on stereotypes.',
 '**Risk prevention and safeguarding.** Each participant and each parent receives a participant pack: programme, house rules, code of conduct, contact chain, emergency numbers, the safeguarding focal point’s name and direct contact, and the media and consent rules. An online meeting is held with the parents, in each country in its own language, where questions are answered live.',
 '**Practical.** Parental consents, travel and medical insurance, medical information sheets, dietary and accessibility requirements, travel bookings. For the Turkish group, the visa procedure starts in month 3 — see the risk register.',
 '**Group leaders’ briefing (month 4):** two online half-days on safeguarding, the escalation chain, facilitating reflection, and the calibrated use of the observation grid across six different observers.',
 '**Inclusion support, prepared individually.** Where a participant needs support beyond the standard arrangements, it is identified here, in the preparation phase, costed on a separate line, and justified by what it makes possible — not requested as a lump sum and explained afterwards.',
])

H4('During')
P('Each national group stays with its own group leader throughout, including at night. The daily reflection happens first in the national group and in the participant’s own language, which is where a participant '
  'who is struggling is most likely to say so, and only then in plenary. The **safeguarding focal point** is present, is introduced in person on Day 1 and is available for individual conversations every day; she is '
  'deliberately not part of the facilitation team, so that a concern about a facilitator can be raised at all. A buddy system pairs participants across countries for language and social support. And any participant '
  'may leave a session without giving a reason — a rule stated on Day 1 and repeated before the sessions that work with distressing content.')

H4('After')
P('Support does not stop at the bus. The cohort communication group stays open for 18 months. Each participant leaves with a written commitment and a role in a local initiative, and the group leader supports '
  'them through it: the initiative is theirs to run, but they are not left alone to run it. A joint online meeting in month 10 lets the two groups that have already delivered pass on what they learned. A follow-up '
  'questionnaire in month 12 and the final test in month 18 close the loop, and the participatory evaluation session in month 17 brings the twenty back into the project as evaluators rather than beneficiaries.')
COUNT(6000)

Q('What measures will you put in place to ensure the safety and protection of participants?')
P('All twenty participants are minors. The measures below are specific, several of them exist because the assessment of our previous application found them missing, and all of them meet the requirements the '
  'National Call sets for the mobility of minors — adequate preparation before departure with the parents involved, and group leaders selected for their competence in working with minors and in preventing and '
  'handling conflict, bullying and abuse, who prepare alongside the young people and commit in writing to the rules.')

H4('Safety of the accommodation and of the activity spaces')
BUL([
 '**Written risk assessment of the venue before contracting**, covering: fire safety certification and evacuation routes; the state of the electrical installations and heating; the security of doors, windows and balconies; lighting of outdoor areas; separation of participant accommodation from any unrelated guests; distance and travel time to the nearest medical facility and to the nearest hospital; mobile signal coverage across the whole site; and the suitability of the outdoor spaces used for activities.',
 '**Verification on site during the preparatory visit in month 3**, by the logistics officer together with representatives of the sending organisations. The venue is not confirmed until it has been seen.',
 '**Evacuation drill on Day 0**, immediately after arrival, with the assembly point shown to every participant. The guided safety tour is a scheduled session (D0.1), not an informality.',
 '**Room allocation by gender and by age**, minors accommodated only with minors; the four group leaders sleep on the same floors as their groups; a night-duty rota so that at least one adult is awake and reachable at all times.',
 '**Activity spaces checked daily** by the logistics officer; a first-aid kit in the plenary room and one carried on every off-site activity; at least one member of the team holding a valid first-aid qualification. [TO CONFIRM: who, and the certificate’s validity date.]',
 '**Off-site activity (Day 5):** transport by a licensed carrier, written route and timing, headcount at every boarding, one adult per group at all times.',
])

H4('Protection of participants')
BUL([
 '**Child protection policy** of the coordinating organisation, signed by every adult involved — staff, facilitators, group leaders — and presented to the participants on Day 1. [TO CONFIRM: the policy must be adopted before submission.]',
 '**A designated safeguarding focal point**, Marilena Georgescu, outside the facilitation team, introduced in person on Day 1, whose contact details go to participants and parents before departure. A named counterpart is designated in each partner organisation.',
 '**Written parental consents** for participation, travel, emergency medical care and use of images, obtained before departure; notarised where national law requires it, as is expected for the Turkish group.',
 '**Code of conduct negotiated with the participants themselves** on Day 1 (session D1.2) rather than imposed, including non-discrimination, respect for all languages present, and explicit rules on harassment and bullying.',
 '**Insurance** — health, accident and civil liability — for all 26 people for the whole travel period, arranged and verified centrally by the coordinator rather than left to each sending organisation.',
 '**Emergency protocol:** a 24/7 contact chain, the full list of parents’ contacts held by the coordinator and by each group leader, a designated reference medical facility identified during the preparatory visit, and an interpreter reachable for the Turkish and French groups.',
 '**Group leaders committed in writing.** Every group leader signs the child protection policy and the set of house rules before departure, and takes part in the preparation alongside the young people of their own group, as the National Call requires.',
 '**Digital protection and data:** explicit consent for photographs and video; no publication of identifiable images of minors without consent; no personal data of third parties in the material produced; a two-step review before anything is published, with the safeguarding focal point approving; all data processed under the GDPR, stored in restricted folders and anonymised in the supporting file.',
])

H4('Protocol for sensitive content')
P('Working with real disinformation exposes participants to violent, discriminatory or distressing material — about war, health, migration. The measures are specific rather than reassuring. All working material is '
  'pre-screened by the facilitators and explicit content is excluded. Every analysis session ends with a short decompression sequence (D2.4). Participants have a stated right to leave a session without justifying '
  'it. And an adult outside the facilitation team is available for an individual conversation every day. These rules are announced on Day 1, together with the group agreement, and repeated before Day 2.')
COUNT(6000)

Q('What activities are foreseen after the end of the Youth Exchange? How will the participants follow-up on the activity?')
BUL([
 '**Months 6–15 — four local initiatives.** Each national group runs one activity in its own community, reaching at least 20 young people, hosted in a youth centre, a library, a community centre, the partner organisation’s own space or another accessible public place. The participants design and lead them; the group leader supports. Each initiative uses the “Digital Detectives” toolkit, screens the four media products made during the mobility, and ends with the ten-minute exercise measuring whether the young people reached can apply two simple verification methods — the evidence for objective O3. Two initiatives are due by month 10 and two by month 15, so the later ones benefit from the earlier ones.',
 '**Month 10 — joint online review** between the four groups, where the two that have delivered pass on what worked and what did not, and the toolkit is revised on the basis of real use rather than intentions.',
 '**Month 12 — follow-up questionnaire** at six months after the mobility: what they still use, and what they have done with it.',
 '**Months 16–17 — the toolkit and dissemination.** The final version of “Digital Detectives” is published, translated by the partners, and presented to the youth workers, librarians and community educators of the territory. Results are presented across the 14 localities of the LAG territory and at the community events the organisation already runs. Participants co-present.',
 '**Month 17 — participatory evaluation session** with the participants, feeding the final report.',
 '**Month 18 — final test**, comparison with the baseline, evaluation report, and reporting back to participants, parents, community partners and the National Agency.',
])
P('**Where this leads for them.** The follow-up is deliberately built so that the learning has somewhere to go. The local initiatives put the participants in front of other young people in their own community, which '
  'is the point at which the competence becomes theirs. The toolkit is left with the youth workers, librarians and community educators who see them week to week, so the method does not leave with us. Youthpass '
  'gives them a way to name and evidence what they gained, so they can use it in whatever they apply for next — another learning activity, a volunteering placement, a civic initiative, another mobility. And the '
  'twenty continue as peer trainers in the four organisations’ later activities. The project does not run alongside their learning and then stop; it leaves a competence, a document that describes it, and a place '
  'to keep using it.')
COUNT(6000)

PAGEBREAK()

H2('8.2 Recognition of learning outcomes')
Q('How will you support participants to be aware of what they have learned and which competences they have developed or improved? Please remember to include the methods that support reflection and documentation of the learning outcomes in the daily timetable of each activity.')

CALLOUT('The form asks for something specific here, and we can point at it.',
        'It asks that the methods supporting reflection and documentation appear **in the daily timetable itself**. In our agenda they are scheduled sessions with codes, not good intentions: **D1.4** introduces Youthpass, '
        'the eight key competences and the learning diary; **D1.5, D2.4, D3.5, D4.4, D6.4** are the daily reflection cycle, national group first and then plenary; **D4.4** is the mid-point review of each participant’s own '
        'learning targets; and **D7.2** is the closing Youthpass session. When you answer this question, name those codes — the expert can then find them in the annexed timetable.',
        'EAF3EA', '9FC49F')

P('**Youthpass is used, and used as a process rather than as a certificate issued at the door.** It begins on Day 1 (session D1.4), when the eight key competences are introduced and each participant sets two '
  'personal learning targets and receives a learning diary. It continues every evening through the reflection cycle — national group in the participant’s own language first, then plenary — and is reviewed at the '
  'mid-point on Day 4. It closes on Day 7 in a dedicated session (D7.2) in which participants re-read their own “Digital Map” from Day 1 alongside their diary and name, with evidence, what changed. Certificates '
  'are issued to all 20 participants and to the 4 group leaders.')

P('**Awareness of learning is built into the structure rather than added at the end,** in three concrete ways. First, the Day 1 digital map is kept and returned on Day 7: participants compare their own description '
  'of their media habits before and after, which turns an abstract competence gain into something they can see. Second, the observation grid applied on Day 4 records whether each participant actually performed '
  'each of four named techniques, so the conversation is about evidence rather than impression — and participants are told on Day 1 that this observation happens, what is observed and why, because it is their '
  'learning data and concealed assessment of minors is neither necessary nor acceptable. Third, the baseline and final test gives each participant a personal figure, communicated to them individually in month 18, '
  'not only aggregated for the report.')

P('**What the process is actually for.** Youthpass here teaches a transferable skill in its own right: identifying what you learned, documenting it with evidence you can point to, and presenting it in a form '
  'someone else understands. That is what makes the certificate useful to a sixteen-year-old afterwards — in the next learning activity they join, in volunteering, in a civic initiative in their own community, and in '
  'the next international mobility they apply for. The competence matrix in the activity section is the reference document for the whole process: every competence claimed is tied to the sessions that build it and '
  'to the evidence that documents it, and facilitators work from that same matrix when supporting participants to write their Youthpass.')
COUNT()

Q('The Erasmus Programme promotes the use of instruments/certificates like Youthpass or Europass, to validate the competences acquired by the participants during their experiences abroad. Will your project make use of such European instruments/certificates?')
P('Yes — **Youthpass**, for all 20 participants and all 4 group leaders. It is used as a process running from Day 1 to Day 7, as described above, and not as a certificate handed out at the door. Europass is not used in '
  'this project: our participants are 14 to 17 and are not in a mobility that produces a Europass Mobility document, so claiming it would be decoration. We would rather name one instrument we genuinely use well '
  'than two we use loosely.')
COUNT(2000)

FLAG('[NOT A QUESTION IN THE 2026 FORM] The 2024 form asked separately about national instruments; the 2026 form does not. The paragraph below is kept because it is still true and still worth saying — append it to the Youthpass answer above if you have room, and drop it if you do not.')
P('Alongside Youthpass, The coordinating organisation issues its own **certificate of participation** in Romanian and English. It states that the young person took part in the activity and names the '
  'competences they developed through non-formal learning, with the evidence behind each one — and that is all it claims. We make no claim of formal recognition for it, and participants and parents are told '
  'plainly what it is and what it is not, so that nobody is given an expectation the document cannot carry. Partners are asked, during the preparation phase, to identify any equivalent instrument used for '
  'recognising non-formal learning in France, Italy and Türkiye, and to explain it to their own participants on the same terms.', count=False)

PAGEBREAK()
H2('8.3 Participants with fewer opportunities')
FLAG('[NOTE on the form] This section opens with a Yes/No. The questions that follow — the type of challenges, how you will reach these participants, and the support measures — only appear once you answer Yes, and a blank export does not render them. Check the exact labels on the live form; the answers below cover the substance whatever the labels turn out to be.')
Q('Are participants involved in activities facing challenges that hinder their participation?')
P('Yes. **At least 12 of the 20 participants — 60%.**')
COUNT(500)

Q('What type of challenges are these participants facing?')
BUL([
 '**Geographical barriers** — the principal one, affecting essentially the whole group: isolated rural mountain communes, two Mediterranean islands, and a metropolitan periphery. Living in a remote or rural region, on a small island or in a peripheral, less-served area is recognised as an obstacle to participation, and all four groups qualify on that ground alone.',
 '**Economic barriers** — 34.4% of the young people aged 14–17 in our survey name cost as a barrier to taking part in a mobility, and 31.2% name transport. In these households the first 80 kilometres are a real obstacle, not a detail.',
 '**Educational barriers** — 31.3% have never taken part in any non-formal education activity, and some come from households with no experience of European programmes at all. For them the difficulty is not only getting there; it is knowing that such a thing exists and is meant for them.',
 '**Linguistic barriers** — part of our own territory communicates in Hungarian, inland Corsica in Corsican, inner Sardinia in Sardinian. A young person whose community life happens in a minority language has less access to information in the majority language, and none at all to correction of what circulates in their own.',
 '**Social barriers** — 12.5% name lack of self-confidence and 10.4% say their family would not agree. Among the respondents there are young people reached through the social worker (six), young people with childcare responsibilities (five mention small children as a barrier) and young people from Roma communities. Two respondents wrote about exclusion directly: “There shouldn’t be differences of class or gender — if you’re in the 12th grade you should be able to go on Erasmus too” and “The right to study; Roma don’t put an emphasis on school.”',
 '**Health or disability** — not known before selection. The specific-needs sheet allows it to be declared confidentially, and the support that follows is costed individually rather than assumed.',
])
COUNT(4000)

Q('How will you reach out to these participants?')
P('The first barrier these young people name is not money. It is information: **37.5%** of 14–17-year-olds in our survey say the reason opportunities pass them by is that they never hear about them. So outreach is '
  'treated as a project activity with its own indicator, not as an administrative formality. **Target: at least 60 applications for the 20 places.**')
BUL([
 '**Through the youth networks the four organisations already run** — the volunteer communities, the Rural Youth Parliament, the participants of previous activities. These are the people who can say what an exchange is actually like.',
 '**Peer-to-peer**, because friends are the channel for 38.5% of them: young people who have taken part in the organisations’ previous activities carry the call into their own circles, in their own words.',
 '**Through social media (49.0%)**, in a format adapted to the age group and produced //with// young people already active in the organisations, not written by staff and posted at them.',
 '**Through libraries, community centres and local youth spaces**, where the call is presented in person rather than pinned up.',
 '**Through the LAG’s Social Inclusion Centre and the UNIC — Porolissum project**, which work directly with vulnerable households. This is how the project reaches young people who would never see an online call — and six of our survey respondents did in fact hear about opportunities through a social worker.',
 '**Not through municipal noticeboards**, which reach 6.2% of this age group. The 14 partner municipalities are used for validating the need and hosting activities, not for recruitment. Saying that plainly is what our own data requires.',
])
FLAG('[DECISION — C4 / C26] Schools were removed as venues, as recognition authorities and from the actors list. They remain the single largest information channel in our own data (50.0%), so the call is also carried into the schools of the territory — as a channel, not as a project partner. If you want them out of outreach as well, delete the next sentence.')
P('The call is also carried into the schools of the territory, because that is where half of these young people say they hear about opportunities — as an information channel only, with the activity, the selection and '
  'the follow-up run entirely through the youth and community structures listed above.')
COUNT(4000)

Q('What specific measures will you implement to support their participation?')
TBL([
 ['Barrier', 'Measure'],
 ['Informational', 'The outreach plan above, with a target of at least 60 applications for 20 places; the call translated into four languages; a plain-language version written for parents rather than for funders.'],
 ['Economic', '**No contribution of any kind is asked of participants.** Travel, accommodation, meals, insurance and materials are covered in full, and the rule is stated in writing from the day the call is published — because that is what allows a family to let a child apply at all.'],
 ['Transport', 'Transport organised and paid from the participant’s home to the point of departure, through the inclusion support category, on a dedicated budget line. A young person from Măguri-Răcătău or from an inland Corsican commune does not have to solve the first 80 kilometres alone.'],
 ['Educational and linguistic', 'English is not a selection criterion; A2 is accepted; the “detective’s glossary” in five languages; visual and practical methods; pair work; group leaders interpreting on request; and deliberate cross-language support built into the mixed teams.'],
 ['Social and confidence', 'The preparatory visit includes **one young person from each sending organisation**, so a participant arrives in August already knowing someone who has been there. The cohort communication group is active two months before departure. The online meeting with parents. Accompaniment by the group leader throughout the journey. And the stated right to leave a session.'],
 ['Health or disability', 'The specific-needs sheet allows confidential declaration; the venue is chosen to be accessible; additional inclusion support at real cost is requested where needed, on its own line, with its own justification. [TO CONFIRM at selection.]'],
 ['Family reluctance', 'Named as a barrier by 10.4%. The parents’ online meeting is held in each country in the local language, with the safeguarding focal point present and the full programme, supervision arrangements and contact chain explained. **Parental consent is obtained after that meeting, not before it.**'],
], widths=[3.4, 13.2])
COUNT(5000)

PAGEBREAK()
H2('8.4 Virtual learning / Blended activities and use of virtual components')
Q('Do you foresee Virtual/Blended activities and/or the use of any virtual component, before, during or after the activity?')
P('Yes — before and after the physical activity. Approximately **26 persons** take part in the virtual components: 20 participants, 4 group leaders and 2 facilitators.')
COUNT(500)

Q('If yes, please describe them.')
P('**Before (months 3–4).** Four joint online sessions of 90 minutes each, in mixed national teams, described in the preparation section. A shared online workspace holds the documents, the case files uploaded by '
  'each group, and the templates. A moderated messaging group with explicit rules keeps day-to-day contact. A separate online meeting with parents in each country, and a two-day online briefing for the group '
  'leaders, including the observer calibration exercise. The baseline test is administered online.')
P('**After (months 6–18).** The cohort communication group remains the working space for preparing the four local initiatives: each group posts its plan and the others comment before it happens. A joint online '
  'review meeting in month 10; the follow-up questionnaire in month 12; the participatory evaluation session in month 17, held online across the four countries; and the final test in month 18.')
P('**Why this is not decoration.** Two reasons, both from the data. First, for a group in which 31.3% have never taken part in a non-formal activity and 12.5% name lack of confidence as a barrier, the virtual phase '
  'lowers the threshold: they arrive in August having already met the people they will be working with, which is a different thing from arriving among strangers. Second, the subject of this project //is// the digital '
  'environment — so the way the project itself uses digital tools is part of the message. The rules the cohort applies in its own communication group (consent, no personal data of third parties, no sharing of '
  'unverified content) are the rules the project teaches.')
COUNT()

H2('8.5 Environmentally friendly practices')
Q('Will you include sustainable and environmental-friendly practices in your activities?')
P('Yes.')
BUL([
 '**Green travel.** For each group the low-emission option is analysed — train, coach, ferry, to the extent each qualifies as green travel under the rules of the applicable call — including the additional eligible travel days, and the option chosen and the reason are documented. The budget is built on the green rates for all four groups. [TO CONFIRM: the eligibility of each transport combination at the time of submission.]',
 '**Food from the territory.** Meals are mostly local and seasonal, sourced from producers in the LAG territory through the short supply chains the organisation itself developed in its rural-development work. That is not a gesture: it is the organisation’s own infrastructure, and it lets participants see a short supply chain instead of hearing about one. No individually packaged portions.',
 '**Materials.** No folders, no printed handouts; worksheets are digital; workshop materials are reusable; waste is separated at the venue; and participants are asked to bring reusable bottles.',
 '**Local movement** on foot or by a single group transport.',
 '**Awareness through the content itself.** One of the categories of disinformation analysed on Day 2 is environmental and climate content. Participants work on real examples of misleading environmental claims — which for this particular group is a far more durable environmental lesson than a briefing on recycling, and it is consistent with the method of the whole project: they learn to distrust the slogan, including the green one.',
])
COUNT(4000)

PAGEBREAK()

# =====================================================================
H1('9. Project management')
Q('How will you manage the project (agreements with partners etc.) and make sure that it is done in line with the Erasmus Youth Quality Standards? You will find the quality standards further down in the application form.')

H4('Roles, separated on purpose')
TBL([
 ['Role', 'Who', 'Responsibility'],
 ['Project manager', 'Alina Ioana Baba (LAG)', 'Overall coordination, relationship with the National Agency, budget, reporting, risk decisions, partnership agreements'],
 ['**Learning Programme Coordinator**\n(non-formal learning)', 'Claudiu Iancu (LAG)', 'The learning programme, the three measurement instruments, observer calibration and moderation, the facilitation team, the Youthpass process'],
 ['Activity coordinator and RO group leader', 'Livia Golovatic (LAG)', 'The four joint online preparation sessions, coordination of the four local initiatives, the Romanian group, gender and locality balance checks'],
 ['Safeguarding focal point', 'Marilena Georgescu (LAG)', 'Receives and handles concerns; approves publication of content; outside the facilitation chain by design'],
 ['Finance and logistics', 'Iulia Fătu (LAG)', 'Budget execution, procurement, venue, transport, insurance, financial reporting, the written venue risk assessment'],
 ['Media production and AI lead', 'YOBBA', 'Day 6 and the technical module; sessions D3.1 and D3.4; dissemination through its platforms; designates one of the two facilitators'],
 ['Group leaders (4)', 'One per organisation, aged 18+', 'Recruitment, preparation, accompaniment, supervision, national-group reflection, observation of one mixed team on Day 4, and the local initiative afterwards'],
 ['Facilitators (2)', 'One designated by the coordinator, one by YOBBA\n[TO CONFIRM: names]', 'Session facilitation, independent double-scoring on the observation grid, daily programme adjustment'],
], widths=[3.6, 4.4, 8.6])

H4('Agreements and governance')
P('A **written partnership agreement** is signed with each partner in month 1, before any expenditure, setting out: tasks and deliverables with dates, the exact budget share and the conditions and timing of '
  'transfers, recruitment and selection obligations, safeguarding obligations, data protection, reporting duties, visibility rules, and what happens if a partner does not deliver. The agreement is not a formality — '
  'it is the document that makes the deliverables in the timeline enforceable.')
P('**Coordination meetings** are held online monthly in months 1–5 and every two months thereafter, with a standard agenda, a written minute circulated within 48 hours, and a rotating chair. A shared action log '
  'records every decision with an owner and a deadline. The risk register is reviewed at every meeting.')

H4('Alignment with the Erasmus+ Youth Quality Standards')
TBL([
 ['Standard', 'How it is met'],
 ['Basic principles: inclusion and diversity, environmental sustainability, digital transformation, participation', 'All four appear as design decisions traceable to evidence, and the correlation between each survey finding and the design decision it produced is documented in the supporting file.'],
 ['Fair and transparent participant selection', 'Published criteria, identical across four countries, a commission of at least two people per organisation, and the outcome communicated with reasons to every candidate — including those who are not selected.'],
 ['Preparation of participants', 'Four months, four joint online sessions, a preparatory visit, linguistic and intercultural components, a parents’ meeting in each country, and a baseline that tells the facilitators what the group actually cannot do.'],
 ['Definition, assessment and recognition of learning outcomes', 'The competence matrix tied to sessions and to evidence; the baseline and final test; the observation grid with calibrated observers; Youthpass as a process from Day 1.'],
 ['Protection and safety of participants', 'Child protection policy, safeguarding focal point outside the facilitation team, written venue risk assessment verified on site, parental consents, central insurance, emergency protocol, sensitive-content protocol.'],
 ['Sharing results and knowledge of the Programme', 'The toolkit published free of charge, results on the Erasmus+ Project Results Platform, dissemination through the LEADER and ELARD networks, and a Day 1 session telling participants what else the Programme offers them after this project.'],
], widths=[5.0, 11.6])
COUNT(6000)

Q('How will you organise the practical and logistical part of the project (e.g. travel, accommodation, insurance, visa, social security, mentoring and support, preparatory meetings with partners etc.)?')

P('**Preparatory visit, month 3.** Held in the LAG territory, with two people from each of the three sending organisations — one of them a young person — plus **one staff member from the coordinating '
  'organisation**, seven people in total. That staff member has two concrete tasks: contributing to the on-site verification of the logistical and safety arrangements, and finalising the mobility programme with the '
  'partners while everyone is in the same room. The visit as a whole verifies the venue and its safety in person, settles the division of the thematic days, meets the host community, and lets a young person from '
  'each group see where they will be coming. It is requested and justified on three grounds: all twenty participants are minors, two of the four partners are new to us, and a venue’s suitability cannot be assessed '
  'from photographs.')
P('**Travel.** Booked centrally by the coordinator for all four groups, so that no sending organisation carries a cash-flow burden and so that green options are compared on the same basis. Distances are confirmed '
  'with the European Commission distance calculator once departure cities are known. Domestic transport from participants’ homes to the point of departure is organised and paid by the project.')
P('**Accommodation and meals.** One venue inside the LAG territory, contracted after a written risk assessment and an on-site check during the preparatory visit. Rooms allocated by gender and age, minors with '
  'minors, group leaders on the same floors. Meals mostly local and seasonal from producers in the territory; dietary requirements collected in month 4 and confirmed with the venue in writing.')
P('**Insurance.** Health, accident and civil liability for all 26 people for the whole travel period, contracted centrally by the coordinator and verified before departure, rather than left to each partner to arrange '
  'and hope.')
P('**Visas — the principal logistical risk.** Romania has applied the Schengen acquis in full, land borders included, since 1 January 2025, and Turkish nationals holding ordinary passports are subject to the '
  'Schengen short-stay visa requirement. For minors that means notarised parental authorisations, invitation letters, proof of accommodation and insurance, and consulate appointments that have to be booked '
  'well ahead. The procedure therefore begins in month 3, five months before the activity: invitation letters issued by the coordinator, a complete file checked by the coordinator before submission to the '
  'consulate, and reserve participants prepared in parallel with their own files ready. This is not a theoretical risk, and we treat it as the item most likely to cost the project a participant.')
FLAG('[VERIFY before submission — C25] The above is correct as at drafting, but visa arrangements between the EU and Türkiye do change. Confirm the current requirement and the appointment lead time directly with the Romanian Consulate General in İstanbul, and note the date of the check in the supporting file.')
P('**Mentoring and support.** Each participant has a group leader throughout, a cross-country buddy, and access to the safeguarding focal point. The cohort communication group is active from two months before '
  'departure until the end of the project.')
COUNT(6000)

H4('Risk register')
TBL([
 ['Risk', 'Likelihood', 'Impact', 'Prevention and contingency'],
 ['Visas not obtained for the Turkish group', 'High', 'High', 'Procedure starts month 3; invitation letters, accommodation and insurance proofs prepared in advance; consulate appointments booked early; reserve participants with complete files prepared in parallel'],
 ['The two island partners are not confirmed in time', 'Medium', 'High', 'Internal deadline 20 September 2026; a parallel search list; fallback to a three-organisation consortium (20 participants split 7–7–6, fully eligible); second fallback to the 12 February 2027 deadline'],
 ['Withdrawal of participants', 'Medium', 'Medium', 'A reserve list of at least 2 young people per national group, prepared alongside the main group and kept informed'],
 ['A partner fails to deliver on time', 'Medium', 'Medium', 'Deliverables with dates in the partnership agreement; monthly action log; a reminder, then a joint problem-solving call, then documented reallocation of the task'],
 ['Low English level blocking participation', 'Medium', 'Medium', 'Glossary in five languages, visual methods, interpreting by group leaders, deliberately balanced mixed teams'],
 ['Medical or safety incident', 'Low', 'High', 'Insurance, emergency protocol, reference medical facility identified during the preparatory visit, first-aid trained staff member, night duty rota'],
 ['A participant distressed by the working content', 'Medium', 'Medium', 'Sensitive-content protocol; pre-screened material; the right to leave a session; daily individual availability of the safeguarding focal point'],
 ['Observers cannot apply the grid consistently', 'Medium', 'Medium', 'The month 4 calibration exercise with an 80% agreement target; if it is not reached, the grid is simplified before the mobility and the decision is minuted — never after seeing the results'],
 ['Bad weather for outdoor sessions', 'Medium', 'Low', 'An indoor alternative planned for every outdoor session'],
 ['One of the four local initiatives not delivered', 'Low', 'Medium', 'Written commitments made publicly on Day 7; interim reporting deadline in month 10; methodological support from the partner leading that component'],
], widths=[4.4, 1.8, 1.4, 9.0], count=False)

PAGEBREAK()

H2('9.1 Partnerships')
Q('How and why did you choose your project partners? What experiences and competences will they bring to the project?')

P('The partnership is built around one shared structural condition, not around geographical variety. All four territories are peripheral, and each has its own linguistic bubble — Hungarian in part of our territory, '
  'Corsican in Corsica, Sardinian in inner Sardinia, neighbourhood and community networks in the İstanbul periphery — and content circulating in those languages and networks is not covered by national '
  'fact-checkers, who work in the majority language on subjects of national interest. Each partner has the same problem in a different form, and each brings a distinct competence to it. That is why the project '
  'cannot be delivered by one organisation, and why swapping a partner for a more convenient one elsewhere would weaken it rather than simplify it.')

TBL([
 ['Partner', 'Why chosen', 'What it leads and delivers'],
 ['**LAG Napoca Porolissum**\nRomania — applicant, coordinator, host, sending',
  'Owns the evidence base (153 young people surveyed), the territory, the venue, the relationship with 14 municipalities and a network of 43 partners, and an in-house youth worker and trainer. Its own survey '
  'identified the problem in the first place.',
  '**Leads:** overall coordination, budget, reporting, risk, the learning programme, local logistics, safety, the relationship with the host community, evaluation.\n'
  '**Delivers:** partnership agreements (M1), the verification test and observation grid piloted and locked (M1–M2), the baseline and final test (M2, M18), the programme and worksheets (M4), venue and services '
  '(M4), the evaluation report (M18), the final toolkit (M17).\n**Leads sessions:** D1.2, D1.3, D1.4, D2.1, D2.2, D3.2, D3.3, D4.1, D4.3, D5.1, D7.2.'],
 ['**YOBBA**\nTürkiye — sending',
  'The only partner with declared and demonstrated core expertise in digital media, a volunteer community of 150+ young people a year, and **six KA152 youth exchanges as a partner between 2022 and 2024**. It '
  'teaches production; it does not teach verification — which is exactly the complementarity this project needs.',
  '**Leads:** the media production module (D6.1, D6.2), the AI-content session (D3.1) and the ethics-of-AI session (D3.4); pre-departure digital preparation; **and designates one of the two facilitators.**\n'
  '**Delivers:** the production module and technical guide (M4), recruitment and preparation of the Turkish group (M2–M4), the local initiative in Küçükçekmece (by M12), dissemination through its platforms (M5–M17).'],
 ['**[Corsica partner]**\nFrance — sending',
  'Sought for direct current work with young people aged 14–17 in inland or rural communes of the island, in a community where the Corsican language is in daily use and the local media ecosystem is small. '
  '[TO CONFIRM]',
  '**Proposed:** leads the Day 2 strand on how disinformation circulates in minority-language communities; contributes to Day 5; observes one mixed team on Day 4.\n'
  '**Delivers:** its own local needs note with consultation data (M2), 5–8 documented local cases (M4), recruitment and preparation of the French group, the local initiative in Corsica (by M13), the French '
  'translation of the toolkit. [TO NEGOTIATE]'],
 ['**[Sardinia partner]**\nItaly — sending',
  'Sought for work with young people aged 14–17 in small depopulating localities of inner Sardinia, and for experience of dialogue with local institutions. [TO CONFIRM]',
  '**Proposed:** leads the preparation and method of Day 5 (community dialogue) and the methodology of the local initiatives (D6.3); observes one mixed team on Day 4.\n'
  '**Delivers:** its own local needs note with consultation data (M2), 5–8 documented local cases (M4), the local initiative model and its evaluation grid (M5), recruitment and preparation of the Italian group, '
  'the local initiative in Sardinia (by M13), the Italian translation of the toolkit. [TO NEGOTIATE]'],
], widths=[3.4, 5.6, 7.6], small=True)
SMALL('We deliberately avoid the formulation that all partners contribute to all activities. Each partner leads named sessions and delivers named products by named dates, and the partnership agreement is what makes that enforceable.')
COUNT(6000)

Q('How will you communicate with them?')
TBL([
 ['Purpose', 'Channel', 'Frequency, owner, rules'],
 ['Formal coordination and accountability', 'Email and a shared document workspace', 'All decisions, deliverables and versions live here. Response time: 3 working days. Nothing that binds a partner exists only in a chat.'],
 ['Coordination meetings', 'Video call', 'Monthly in months 1–5, every two months thereafter; standard agenda; written minute within 48 hours; rotating chair.'],
 ['Fast operational contact', 'Closed messaging group, core team only', 'During the preparation and mobility weeks; no personal data of participants, ever.'],
 ['Group leaders', 'Separate channel + two-day online briefing in month 4', 'Safeguarding, escalation, reflection facilitation, and calibrated use of the observation grid across six observers.'],
 ['Participants', 'Moderated cohort group + four joint online sessions', 'Active from month 3 to month 18; explicit rules; facilitators moderate.'],
 ['Parents', 'Online meeting per country, in the local language, plus the written participant pack', 'Months 3–4, before parental consents are signed.'],
], widths=[3.6, 4.6, 8.4])
COUNT(3000)

Q('How will you monitor and coordinate their contribution?')
P('Each partner has deliverables with dates written into the partnership agreement, and those same deliverables appear in the shared action log with an owner. At every coordination meeting the log is reviewed '
  'line by line: delivered, in progress, or late. Escalation is defined in advance and is proportionate — a reminder from the project manager; then a joint problem-solving call with the relevant leads; then, only if '
  'necessary, a documented reallocation of the task, recorded in the action log. Payments to partners are staged against deliverables rather than against the calendar.')
P('Because the four organisations are of genuinely different kinds — a rural Local Action Group, a media-focused youth association in a metropolitan periphery, and two island organisations — monitoring uses '
  'one common backbone with partner-specific expectations: the same reporting template and the same dates for everyone, but the content of what each is asked for follows the role they actually hold. **Quality is '
  'monitored as well as delivery.** The Learning Programme Coordinator reviews the local cases each partner submits in month 4 against a common standard, because those cases are the working material of the whole '
  'mobility, and a weak set from one country would quietly degrade Day 2 for everyone.')
COUNT(3000)

Q('Which other actors (organisations or individuals) will be involved and how?')
BUL([
 '**Youth organisations and youth structures in the four territories** — carrying the call to young people in their own networks, hosting local initiatives, and taking the toolkit into their own standing activity afterwards.',
 '**Libraries and community centres** — hosts for the local initiatives and for the presentation of the toolkit, and the places where it stays available afterwards.',
 '**Local authorities — the 14 partner municipalities of the LAG territory and their counterparts in the other three countries** — validating the need, hosting the Day 5 community dialogue, providing spaces for the local initiatives, and receiving the evaluation report and its recommendations. Not used for recruitment, because our data shows they reach only 6.2% of this age group.',
 '**The LAG’s Social Inclusion Centre and the UNIC — Porolissum project** — outreach to young people from vulnerable households, and the channel through which the inclusion targets are actually met rather than hoped for.',
 '**Local producers of the territory** — supplying meals through short supply chains, and taking part in the intercultural evening.',
 '**Residents of the host village** — interlocutors in the Day 5 dialogue. They are participants in the learning, not scenery: the record of local rumours they help produce becomes the working material of Day 6.',
 '**Local press** — invited to the Day 7 public presentation, and a channel to the adults of the territory.',
 '**National fact-checking and verification resources in the four countries** — used as reference material in the Day 3 tool laboratory, one per partner country, so that participants leave with a resource usable at home in their own language. [TO CONFIRM: the final list, checked for being free of charge and appropriate for minors.]',
 '**The LEADER and ELARD networks** — dissemination of the method to Local Action Groups across rural Europe, an audience that rarely encounters media-literacy tools at all.',
])
COUNT(4000)

PAGEBREAK()

H2('9.2 Evaluation')
Q('How will you evaluate your project’s success? Which activities will you carry out in order to assess whether, and to what extent, your project has reached its objectives and results?')
P('Every indicator has a baseline, a target, an instrument, an owner and a moment of measurement. Nothing is claimed here that is not measured, and the three main instruments exist in writing.')

TBL([
 ['Indicator', 'Baseline', 'Target', 'Instrument', 'When and who'],
 ['Mean score on the practical verification test (O1)', 'Established in month 2', '+30% or more, for at least 16 of 20', 'Identical 15-item, 30-point practical test (Form A / Form B), administered online, closed-device', 'Months 2 and 18; Learning Programme Coordinator'],
 ['Participants correctly applying 4 verification techniques (O2)', '0 at selection', 'At least 16 of 20', 'Structured observation grid, 4 techniques scored 0–2, six calibrated observers, 25% double-scored', 'Day 4, and again in short form at the local initiatives; the 2 facilitators and the 4 group leaders'],
 ['Young people reached through local initiatives (O3)', '0', 'At least 80 (at least 20 per community)', 'Attendance lists, short activity reports, photographs with consent', 'After each initiative, months 6–15; the four group leaders'],
 ['Beneficiaries able to apply 2 simple methods (O3)', 'Established by 3 questions at the start of each workshop', 'At least 70%', 'The 10-minute exercise at the end of each local initiative', 'At each initiative; group leader'],
 ['Overconfidence sub-score (items 9 and 14)', 'Established in month 2', 'Moves proportionally more than the total score', 'Same test, reported as a separate 4-point sub-score', 'Months 2 and 18; Learning Programme Coordinator'],
 ['Confidence gap (believed minus actual ability)', 'Established in month 2', 'Narrower at month 18', 'Unscored confidence question, converted to the test scale and subtracted from the actual score', 'Months 2 and 18; Learning Programme Coordinator'],
 ['First-time participants in a European mobility', '—', 'At least 15 of 20', 'Selection form', 'Month 2; selection commission'],
 ['Participants with fewer opportunities', '—', 'At least 12 of 20', 'Selection form and specific-needs sheet', 'Month 2; selection commission'],
 ['Gender balance', '—', 'At least 40% of each gender in every national group', 'Participant list', 'Month 2 and final confirmation; activity coordinator'],
 ['Applications received', '0', 'At least 60 for 20 places', 'Application register', 'Month 2; each partner for its own group'],
 ['Satisfaction and perceived learning', '—', 'At least 80% positive', 'End-of-mobility questionnaire and daily reflection records', 'Daily and on Day 7; facilitators'],
 ['Retention at 6 months', '—', 'At least 15 of 20 still applying something', 'Follow-up questionnaire', 'Month 12; activity coordinator'],
 ['External uptake of the toolkit', '0', 'At least 4 organisations outside the partnership confirm use', 'Written confirmations', 'Months 16–18; communication officer'],
], widths=[3.6, 2.8, 3.0, 4.0, 3.2], small=True)

H4('Evaluation activities, in order')
BUL([
 '**Before month 2 — piloting.** Both instruments are piloted with 5–8 young people aged 14–17 from the territory who are not project participants. Any item that more than 80% or fewer than 10% of the pilot group answers correctly is rewritten. Neither instrument is used on the cohort untested.',
 '**Month 2 — baseline.** The practical test plus a media-habits questionnaire, for all 20. The threshold recalibration rule is applied once, on the group mean, and the decision is recorded in writing.',
 '**Month 4 — observer calibration.** All six observers score the same recorded sequence independently and compare, with a target of exact agreement on at least 80% of judgements. If it is not reached, the grid is simplified before the mobility, and that decision is minuted — never after seeing the results.',
 '**Continuous during the mobility.** Daily reflection groups whose output visibly adjusts the next day’s programme; facilitator observation; the Day 4 observation grid with moderation immediately afterwards; a mid-week check of individual learning targets.',
 '**End of mobility (Day 7).** Participatory evaluation, anonymous written questionnaire, Youthpass reflection, and the comparison of each participant’s Day 1 digital map with their Day 7 reflection.',
 '**After each local initiative.** Attendance, a short report, and the ten-minute exercise with the young people reached.',
 '**Month 10.** Joint online review between the four groups, feeding a revision of the toolkit based on real use.',
 '**Month 12.** Follow-up questionnaire at six months.',
 '**Month 17.** Participatory evaluation session with the participants, plus a consortium evaluation meeting with all four partners.',
 '**Month 18.** Final test, comparison with the baseline, evaluation report, and results communicated individually to each participant and collectively to parents, community partners, the 14 municipalities and the National Agency.',
])

P('**On honesty in evaluation.** The instruments are designed so that failure is visible. A practical test can show no improvement; an observation grid can record that a participant did not perform a technique; a '
  'participant who does not take both forms is excluded from the calculation and reported as excluded, rather than quietly dropped from the denominator. We prefer that to a satisfaction questionnaire that always '
  'comes back positive. Fifteen items and twenty participants is not a validated psychometric instrument and we will not describe it as one: it is fit for tracking change inside this cohort and for telling the team '
  'where the learning worked, and the final report will say what was achieved and what was not.')
COUNT(6000)

H2('9.3 Sustainability of the results')
Q('What will you do to make sure that your project continues to have effects also after it ends?')
P('**Something concrete stays behind, and someone owns it.** The “Digital Detectives” toolkit — worksheets, exercises, games, verification grids, the manipulation-techniques grid produced by the participants and '
  'the AI-recognition sheet they wrote themselves — is tested during the mobility, revised in month 10 on the basis of what actually worked in the four local initiatives, and published free of charge in month 17 in '
  'English and Romanian, with French, Italian and Turkish translations delivered by the partners. It is not a report about the project. It is a set of materials a youth worker can pick up and use on a Tuesday afternoon.')
P('**It enters standing activity, not an archive.** The coordinator integrates the toolkit into the youth animation work it already runs across its 14 partner municipalities and into the community events it holds '
  'every year. YOBBA takes it into a volunteer programme of more than 150 young people annually. The two island partners integrate it into their own youth work. Each organisation names, in the partnership '
  'agreement, the person who owns it afterwards — a named person, not a department.')
P('**The twenty stay.** Participants are not released at the end. They have each already run a local initiative; the organisations then involve them as peer trainers, which is both cheaper and more effective than '
  'recruiting a new cohort from scratch. The cohort communication group remains open.')
P('**The instruments stay too.** The verification test, the observation grid and the beneficiary exercise are reusable, and the coordinator ends the project owning three measurement instruments it did not have '
  'before — which changes what it can honestly claim in every youth project it writes afterwards.')
P('**The partnership decides its own future.** In month 17 the four organisations formally assess whether to continue, and with what: a second exchange hosted by another partner, or a youth participation project '
  'on dialogue with local decision-makers. The decision is minuted either way, including if it is not to continue.')
COUNT(5000)

Q('Are you planning measures to make sure that the results produced are used and beneficial to others beyond the project’s lifetime? If yes, which ones?')
P('Yes. Four measures, each with an addressee rather than a general intention.')
BUL([
 '**To youth organisations, libraries and community centres in the territory:** the toolkit offered free, with a presentation session in month 17 for the youth workers, librarians and community educators who will actually use it. Romania has no coordinated national media-literacy strategy and its policies in this area are fragmented across separate legal frameworks; in that context a free, tested set of materials in the hands of people who already work with rural young people has value out of proportion to the size of this project.',
 '**To youth organisations across Europe:** publication on the Erasmus+ Project Results Platform; dissemination through YOBBA’s platforms; and dissemination through the LEADER and ELARD networks, where the coordinator already has transnational cooperation experience. Target: **at least four organisations outside the partnership confirm in writing that they use the toolkit.**',
 '**To local institutions:** the evaluation report and a short set of recommendations delivered to the 14 partner municipalities and to the partner institutions in the other three countries.',
 '**To the communities themselves:** the four media products remain in circulation on the organisations’ channels. Unlike a report, they are the kind of thing people actually watch.',
])
COUNT(4000)

H2('9.4 Dissemination of project results')
Q('How will you make your project visible outside your organisation and partner organisations? How will you share its results and success? With whom will you share the results?')
TBL([
 ['Audience', 'Channel', 'Product', 'Indicator and owner'],
 ['Young people in the four communities', 'The four local initiatives; the organisations’ social media; youth centres, libraries and community centres', 'Workshops, the four media products, the toolkit', 'At least 80 young people reached directly; group leaders'],
 ['Communities of the LAG territory', 'The 14 partner municipalities; the community events the organisation runs annually; local press', 'The Day 7 public presentation; a “Digital Detectives” stand at two community events', 'At least 2 community events and 3 items in local press; communication officer'],
 ['Parents and legal guardians of the participants', 'The parents’ meetings in each country; the participant pack; the local initiatives and the Day 7 presentation', 'Information on the programme, the supervision arrangements and the contact chain; presentations by the participants themselves', 'One meeting per country before consents are signed; 100% of families reached with the pack; group leaders. **Parents are involved in informing, supporting and protecting participants who are minors — they are not a target group of the project.**'],
 ['Youth organisations and youth workers in Europe', 'Erasmus+ Project Results Platform; the partners’ networks; YOBBA’s platforms; LEADER and ELARD', 'The “Digital Detectives” toolkit', 'Toolkit published and freely downloadable; at least 4 external organisations confirm use'],
 ['Local institutions and decision-makers', 'Direct meetings; presentations in local councils', 'Evaluation report; short recommendations', 'At least 4 institutions informed; project manager'],
], widths=[3.2, 4.2, 4.2, 5.0], small=True)

P('**Visibility of the Programme.** All materials produced — toolkit, media products, presentations, press releases — carry the European Union emblem and the funding statement, in line with the Programme’s rules. '
  'On Day 1 participants have a short session on what Erasmus+ is and what stays open to them afterwards — the European Solidarity Corps, DiscoverEU, other exchanges — so that this project is not the end of their '
  'contact with the Programme.')
P('**Safeguarding in dissemination.** Because all participants are minors, every piece of content goes through a two-step review: the participant responsible for documentation prepares it, and the safeguarding '
  'focal point approves it before publication. No identifiable images of minors without written consent; no personal data of third parties; no location details for minors. This rule is written into the group '
  'agreement on Day 1, and it is itself part of the learning.')
COUNT(5000)

Q('How will you involve participants in such activities?')
P('Participants are the producers of the disseminated results, not their subject. They make the four media products; they design and lead the four local initiatives; they present publicly on Day 7 to guests from '
  'the community, the municipalities and the press; they co-present the results across the localities of the territory in months 16–17; and defined documentation roles — photo and video, activity diary, contact with '
  'the host community — are assigned in month 3 and held throughout. A fifteen-year-old explaining to a room of other young people how to check whether a photograph is what it claims to be is a more effective '
  'dissemination instrument than any press release the organisation could write — and it is also the moment the learning stops being ours and becomes theirs.')
COUNT(3000)

PAGEBREAK()

# =====================================================================
H1('10. Erasmus Youth Quality Standards')
SMALL('The 2026 form no longer prints the standards. It links to erasmus-youth-quality-standards_en.pdf and asks you to open it, read it and confirm three statements. Open the linked PDF — the confirmation says you have.')
TBL([
 ['To confirm in the form', 'Our position'],
 ['I have read the above Erasmus Youth quality standards', 'Read, and worked through: the alignment table in section 9 maps each standard to the concrete measure that meets it.'],
 ['I confirm that I, my organisation and the co-beneficiaries (where applicable) adhere to the Erasmus Youth quality standards',
  'Note that this binds the **co-beneficiaries** too, not only the coordinator. That is why adherence to the standards is written into the partnership agreement signed with each partner in month 1 — so the confirmation is backed by something each partner has signed, rather than being a promise made on their behalf.'],
 ['I understand and agree that Erasmus Youth quality standards will be used as part of the criteria for evaluation of the activities implemented under this project',
  'Understood and accepted. The standards are also how the project is monitored internally: the alignment table is reviewed at the month 17 consortium evaluation meeting, not only written for the application.'],
], widths=[6.0, 10.6], count=False)

H1('11. Annexes')
TBL([
 ['Form slot', 'What goes in it', 'Status'],
 ['**Declaration on Honour**\n//confirmed//', 'Downloaded from the form, printed, signed by the legal representative, attached.', 'To prepare'],
 ['**Timetable**\n//confirmed//',
  'The timetable of the youth exchange, and of the preparatory visit. **This is where the full daily programme goes** — the table in section 7.7, with all five attributes for each of the 24 sessions: the objective it serves, '
  'the method, the key competences, the output, and the named person responsible. No character limit here, and it is where an expert looks for exactly the thing the previous assessment found missing. If the form provides a '
  'template, use it rather than pasting our table into a document of our own.',
  'Ready — to be transferred into the form’s template'],
 ['**Accession forms**\n[TO CHECK]', 'One per partner, signed by each legal representative. Whether or not the slot exists, the pre-submission checklist states that accession forms are due **at the latest before the signature '
  'of the grant agreement**, and that a signed accession form is a condition for signing it. So they do not block submission — they block contracting.', 'Check while you are in the form'],
 ['**Other Documents**\n[TO CHECK]', 'If this slot exists, it is worth using, and in this order: the **measurement-instruments pack** first — it is the single document that turns O1, O2 and O3 from claims into instruments — '
  'then the youth survey instrument and analysis, then the partners’ one-page needs notes. Attach only what is short and relevant: the National Call warns explicitly against uploading unrequested annexes for volume.',
  'Check while you are in the form'],
], widths=[3.0, 10.6, 3.0], small=True, count=False)

FLAG('[TO CHECK while you are in the live form — two minutes, and it matters] The blank export showed only the Declaration on Honour; the Timetable slot turned out to exist anyway. So check the other two the same way. If an “Other Documents” slot exists, attaching the measurement-instruments pack is the cheapest quality gain available to this application.')

P('**What the accession-form timing means for your internal deadline.** Accession forms are due before the grant agreement is signed, not at submission. What you need **at submission** is each partner’s valid OID entered in '
  'the form. That changes the 20 September internal deadline from “signed mandate or no partner” to “confirmed partner with a valid OID and its needs note”, which is a materially easier target. The National Call adds that the '
  'accession forms must be the 2026 versions and that you should secure the originals in good time.', count=False)

P('**Legal status documents** are not uploaded here either: they go into the Organisation Registration System against the applicant’s OID.', count=False)

H1('12. Application conditions')
SMALL('A new section in the 2026 form, and the one most likely to be met for the first time at 11:00 on 1 October. It carries four blocks of confirmations plus the pre-submission checklist.')

H3('12.1 EU values')
TBL([
 ['To confirm in the form', 'Where the project actually delivers it'],
 ['I confirm that I, my organisation and the co-beneficiaries (where applicable) adhere to the EU values mentioned in Article 2 of the TEU and Article 21 of the EU Charter of Fundamental Rights',
  'Adherence is written into the partnership agreement signed with every partner in month 1, so it binds all four organisations and not only the coordinator.'],
 ['I understand and agree that EU values will be used as part of the criteria for evaluation of the activities implemented under this project',
  'The project is built on these values rather than merely compatible with them. Non-discrimination and respect for every language and identity present are non-negotiable clauses of the group agreement the participants '
  'themselves negotiate on Day 1 (D1.2). The working material of Day 2 is real content carrying ethnic, gender and migration stereotypes, analysed in mixed teams in which young people from the targeted communities '
  'are present. The ground rule of the whole exchange — every claim must be evidenced, facilitators included — is a rule-of-law habit practised in miniature. And the minority-language strand exists precisely because '
  'the rights of people belonging to minorities include the right not to have falsehood circulate unchecked in their own language.'],
], widths=[5.6, 11.0], small=True, count=False)

H3('12.2 EU sanctions and restrictive measures')
FLAG('[NEW IN 2026 — ACTION REQUIRED] This block did not exist in the earlier form and it concerns **every partner**, not only the applicant. Check each organisation against the EU Sanctions Map before submitting, and record the date you checked in the supporting file.')
TBL([
 ['To confirm in the form', 'What to do about it'],
 ['I confirm that I / my organisation / project partner are NOT included on the list of persons or entities subject to EU sanctions. If included, the application will be rejected.',
  'Check the applicant and all three partners at sanctionsmap.eu. Note that the EU Official Journal carries the official list and prevails over the Sanctions Map if the two differ. No reason to expect a problem with any of our four organisations — but the declaration is absolute, so check rather than assume.'],
 ['I / my organisation / project partners are not established in Russia, nor are any of our proprietary rights directly or indirectly owned for more than 50% by a legal person, entity or body established in Russia, and are therefore NOT subject to EU restrictive measures under Regulation (EU) 833/2014.',
  'This is the option that applies to us: the four organisations are established in Romania, Türkiye, France and Italy. Confirm ownership as well as establishment — the test is about who owns more than 50%, not only where the organisation is registered. Ask each partner to confirm in writing, and keep those confirmations.'],
 ['(Alternative) …ARE established in Russia or more than 50% Russian-owned, and therefore subject to restrictive measures, requiring an exemption under Article 5(1–2) of Regulation (EU) 833/2014, failing which the application will be rejected.',
  'Not applicable. Do not tick it.'],
], widths=[7.0, 9.6], small=True, count=False)

H3('12.3 Original content and authorship')
TBL([
 ['To confirm in the form', 'Our position'],
 ['I confirm that this application contains original content authored by **the applicant organisation**.',
  'Note the wording narrowed: the 2024 form said “the applicant and partner organisations”. It is now the applicant alone. True here, and worth protecting — the National Call states that ANPCDEFP runs the European '
  'Commission’s anti-plagiarism software, and that passages identical or similar to another application, **including your own from a previous deadline**, are treated as double funding and can cause rejection. '
  'Practical consequence: do not reuse paragraphs from the Inclusion2Income application of the previous round. This document is a fresh draft, which is the safe position; keep it that way through the final edit.'],
 ['I confirm that no other organisations or individuals external to **the applicant organisation** have been paid or otherwise compensated for drafting the application.',
  'Confirm only if it is true of your situation. The declaration is about who was **paid or compensated to draft** the application — not about the internal drafts, working documents or tools used along the way by the applicant’s own team.'],
], widths=[6.0, 10.6], small=True, count=False)

H3('12.4 Protection of personal data and other acknowledgments')
P('One acknowledgment to tick: that information concerning the organisation, the application, the operational and financial capacity assessments, compliance with eligibility and exclusion criteria, previously funded '
  'projects and — if the grant is awarded — the implementation and monitoring of this project may be made accessible to authorised persons of the European Commission, EACEA and the National Agencies, for programme '
  'implementation and the protection of EU financial interests. Nothing here needs preparing; read the privacy statement the form links to before ticking it.', count=False)

H3('12.5 Pre-submission checklist')
TBL([
 ['Form checklist item', 'Our position'],
 ['It fulfils the eligibility criteria listed in the Programme Guide.', 'Verified in section 7.6: participant numbers, group sizes, number of countries, group leaders, facilitators, duration, ages, and the country of the venue.'],
 ['All relevant fields in the application form have been completed.', 'Every field marked [TO CONFIRM] in this document is a field that is not yet complete. The short list in section 14 is the order to close them in.'],
 ['You have chosen the correct National Agency of the country in which your organisation is established.', 'RO01 — ANPCDEFP. The applicant is established in Gilău, Cluj County, Romania, and the activity takes place in Romania.'],
], widths=[6.0, 10.6], small=True, count=False)

H1('13. Supporting file')
SMALL('Kept, not uploaded unless requested. This is what you need to be able to produce if the National Agency asks — including for the operational-capacity check, which it may run on any application.')
TBL([
 ['#', 'Document', 'Status', 'Note'],
 ['4', 'The youth questionnaire: instrument, 153 anonymised responses, and the analysis', 'Ready', 'The evidence base of the whole application'],
 ['2', 'Minute of the validation meeting with 8–10 young people', 'To do before submission', 'Evidence that young people took part in designing the project — with a date, a number and what changed'],
 ['3', 'The three measurement instruments: the verification test (Forms A and B), the marking scheme, the observation grid with its descriptors, the observer calibration protocol and the beneficiary exercise', '**Drafted**', 'Objectives O1, O2 and O3 are not measurable without them. Form A must be built as an online form and both instruments piloted before month 2'],
 ['4', 'Child protection policy and parental consent templates in four languages', 'To adopt', 'All participants are minors; the National Call makes this a condition it will verify'],
 ['5', 'Venue: written offer and risk assessment', 'To obtain', 'Determines budget, risk and the credibility of the whole practical section'],
 ['6', 'Partners’ needs notes, one page each with their own consultation data', 'To obtain', 'Each partner must show the problem exists in its own community — see the consultation protocol in section 6.1'],
 ['7', 'Full references for the European sources cited', 'Partly ready', 'Eurobarometer, INSEE, ISTAT — links and access dates to be recorded'],
 ['8', 'Distance calculations from the Commission’s distance calculator', 'To do', 'Once departure cities are known'],
 ['9', 'CVs of the implementation team and the list of ongoing projects', 'Ready', 'Not requested at application, but the National Agency may request them for the operational-capacity check'],
], widths=[0.9, 6.6, 2.6, 6.5], small=True, count=False)

H1('14. Before you submit — the short list')
P('Seven things decide whether this application beats 70 points. Five of them are not writing.', count=False)
TBL([
 ['#', 'What', 'Why it decides the score', 'By when'],
 ['0', '**Every OID is clear of the five-application limit.** Ask YOBBA in writing how many KA152 applications it is already in for this round, and ask each island partner the day it is confirmed.',
  'The 2026 form refuses a submission once an OID is in five Mobility of young people applications for the round. YOBBA has partnered in six KA152 exchanges and is the likeliest to be at or near the limit. This is a hard stop in the system, not something an expert can be persuaded about.',
  'Now, and again in the final week'],
 ['1', '**The two island partners exist**, each with a valid OID entered in the form and a one-page needs note with its own consultation data.',
  'Everything else in this document is written; this is not. A consortium with two unnamed partners is not a consortium, and the needs notes are what turn “four communities with the same problem” from a claim into evidence. '
  'Note the relief the form gives you: the **accession forms are due at the latest before the grant agreement is signed**, not at submission — so what you need by 20 September is a confirmed partner with an OID, not a signed mandate in hand.',
  '20 September 2026 (internal). Fallbacks: a three-organisation consortium of 20 participants split 7–7–6, which is fully eligible; or the 12 February 2027 deadline, which moves the exchange to summer 2028 and produces a stronger application than a rushed one.'],
 ['2', '**Form A is built as an online form, and both instruments are piloted** with 5–8 young people aged 14–17 from the territory. Form B is drafted in month 2 and locked before the baseline results are seen.',
  'Objectives O1 and O2 are the backbone of this application. The instruments now exist on paper — but an instrument nobody has tested is still a promise, and the previous assessment penalised exactly the gap between what was claimed and what could be shown.',
  'Form A before submission; piloting before month 2'],
 ['3', '**The venue is identified, with a written offer and a written risk assessment.**',
  'The previous assessment noted the absence of any measures on the safety of accommodation and activity spaces. That section is now written — it also has to be true, and the budget depends on it.',
  'Before submission'],
 ['4', '**The validation meeting with young people is held and minuted**, and the EMPOWER details are filled in.',
  'A co-design claim without a date and a number is discounted. The EMPOWER sentence is the only substantive gap left in the coordinator’s own profile.',
  'Before submission'],
 ['5', '**The figures are identical everywhere.**',
  'The concept note still cites 121 respondents, 17.3% and 99.2%. The current dataset gives 153, 20.8% and 96.9%. An expert who compares the documents will see it, and a single mismatched number costs more credibility than it should.',
  'Final read-through, both documents side by side'],
 ['6', '**The full daily programme is uploaded to the Timetable annex**, and the narrative field carries the day-level summary from 7.8 plus the pointer sentence.',
  'The annex is where the five attributes per session become visible with no character limit — and their absence is what cost 14 of the 40 design points last time. The pointer sentence is what stops an expert assuming the '
  'detail was never written. While you are in the Annexes section, check whether the Accession forms and Other Documents slots exist too: if Other Documents does, attaching the measurement-instruments pack is the cheapest '
  'quality gain available to this application.',
  'When filling the form'],
 ['7', '**The four flows and the per-flow budget are entered exactly as in sections 7.3 and 7.5**, and the form’s own totals are compared against 26,827.00 and 31,587.00.',
  'The form computes travel and individual support per flow. If the flows are entered with the wrong number of people, the totals move and nothing else in the application explains why. This is also where the 92 EUR error was hiding.',
  'When filling the form'],
], widths=[0.8, 4.4, 5.8, 5.6], small=True, count=False)

CALLOUT('One last check before you paste.',
        'Read the three objectives in section 3, in section 6.1 and in the evaluation table of section 9.2. They must be word-for-word identical — same thresholds, same instruments, same dates. '
        'Then read the measurement-instruments pack against them and confirm the same. That consistency is the single cheapest quality signal in the whole application, and it is the first thing an expert '
        'who is reading forty applications will notice.',
        'EAF3EA', '9FC49F')

SMALL('Version 3, revised 15 September 2026. Built on the draft of 3 September 2026, the 27 review comments of the same date, the official KA152-YOU application form (Form ID KA152-YOU-4E0F2C76), the Erasmus+ 2026 '
      'Programme Guide, and the ANPCDEFP National Call 2026 (KA152-YOU, deadline 1 October 2026, 12:00 Brussels time). Section order and question wording follow the official form; the reference export is Call 2024 '
      'Round 1, so check every field label against the live 2026 Round 2 form before pasting.')

import os
out = '/home/user/UNIC-2/VERIFAI_KA152_Application_EN_v4.docx'
doc.save(out)
print('saved', out, os.path.getsize(out), 'bytes')
