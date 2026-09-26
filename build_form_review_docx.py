# -*- coding: utf-8 -*-
import docx_engine as E
from docx_engine import H1, H2, H3, H4, P, SMALL, FLAG, BUL, NUM, TBL, CALLOUT, PAGEBREAK, doc

H1('VERIFAI — review of the filled application form')
SMALL('Form ID KA152-YOU-691C4B41 · Call 2026 Round 2 · export of 57 pages · checked against the application content document, the timetable annex and the arithmetic of the 2026 unit costs.')

CALLOUT('How to read this.',
        'Section 1 is what stops a submission or a payment. Section 2 is figures that contradict each other inside the form — the kind an assessor finds by reading two fields side by side. '
        'Section 3 is money the form is not currently asking for. Section 4 is content that went missing. Section 5 is the full typographic list. Section 6 says what is already right, so it is not disturbed.',
        'E8EEF7', 'C7D6EA')

# ---------------------------------------------------------------- 1
H2('1. Must be fixed before submission')
TBL([
 ['Where', 'What the form shows', 'Why it matters'],
 ['Annexes, p. 54', 'Declaration on Honour — **File size 0 kB, nothing uploaded.**',
  'The Declaration on Honour is mandatory. Without it the application is incomplete.'],
 ['Activity PREPV02, p. 36', '“Please describe who will take part in the Preparatory Visit.” — **the answer is empty.**',
  'A required narrative field left blank. The content exists already in the activity block of the content document; it needs pasting.'],
 ['PREPV02 flows 1–3, pp. 36–37', '**Start Date and End Date are blank on all three flows.** Flow 1 also has **no Sending Organisation and no Country of Origin.**',
  'Incomplete flow records. Flow 1 is the coordinator’s own two people, so the organisation has to be named there.'],
 ['Project budget, p. 9', '“**The National Agency has requested a financial guarantee.**”',
  'This is a condition on the grant, not a formality. Ask ANPCDEFP what form of guarantee and by when, because it can affect whether the project can be signed.'],
 ['Annexes, p. 54', 'The Annexes section contains **only a Declaration on Honour row. There is no timetable slot** in this export.',
  'The completed timetable annex cannot be attached here. Check the live form on screen; if there is genuinely no slot, the timetable is still worth keeping as a supporting document for the NA, and the session codes problem below has to be solved another way.'],
], widths=[3.4, 6.2, 7.0], small=True)

# ---------------------------------------------------------------- 2
H2('2. Figures that contradict each other inside the form')
SMALL('Each row is two statements in the same application that cannot both be true.')
TBL([
 ['One field says', 'Another field says', 'Fix'],
 ['Selection criteria, p. 24: “first participation in a European mobility … **target 15 of 20**”; “a situation limiting access to opportunities … **target 12 of 20**”',
  'Activity table and fewer-opportunities field: **16 of 21** first-timers, **13 of 21** with fewer opportunities',
  'Left over from the 20-participant version. Change to 16 of 21 and 13 of 21.'],
 ['Selection, p. 24: “Target: **at least 60 applications** for the 21 places”',
  'Reach-out field, p. 42: “**at least 63 applications** for 21 places”, twice',
  'Use 63 in both.'],
 ['Logistics, p. 45: “…plus one staff member from the coordinating organisation, **five people in total**”. Prep-visit justification, p. 35: “two of the **five travellers**”',
  'PREPV02 declares **6 persons** (2 + 2 + 2) and a grant of 4,080.00',
  'Change both to six, and say the coordinator sends two.'],
 ['Prep-visit justification, p. 35, and the timetable annex: a **two-day** visit on **16–17/06/2027**',
  'PREPV02 header: **09/06/2027 – 11/06/2027**, a **three-day** visit',
  'Decide the dates, then update the annex, which currently has only two days.'],
 ['Logistics, p. 45: the Greek flow has “**four eligible travel days**”. Prep-visit text, p. 36: same phrase',
  'Flow 1 (Greece) declares **Travel Days: 2**',
  'Either claim the extra days in the flow, or remove the phrase. See section 3.'],
 ['Environmental practices, p. 44: “the budget is built on the **green rates for all three flows**”',
  'Flow 2 (Türkiye) is costed at **309 EUR**, the non-green rate. Only Greece (417) and Romania (56) use green rates',
  'Either set the Turkish flow to green travel, or correct the sentence.'],
 ['Measures for fewer opportunities, p. 42: transport paid from the front door “**through the inclusion support category on a dedicated budget line**”, and inclusion support for participants “requested at real cost on separate dedicated lines”',
  'All three flows declare **Inclusion support for participants: 0.00**, with the justification box empty',
  'Either request it with a justification, or stop promising it. As written, the promise has no budget behind it.'],
 ['Role of participants, p. 25: “**all four organisations** involve **the twenty** as peer trainers”',
  'The consortium is **three** organisations and **twenty-one** participants',
  'Left over from the four-country version. Correct both words.'],
 ['Erasmus objectives, p. 21: measures answer “the **linguistic** one” and “the social and **educational** ones”',
  'The declared challenge types, p. 42, are **geographical, economic and social** only',
  'Reword so language support is a measure open to everyone rather than the answer to a barrier you have not declared.'],
 ['Recognition of learning, p. 41: “**The competence matrix above** is the reference document for the whole process”',
  'There is no competence matrix anywhere in the form',
  'Dangling cross-reference. Either reinstate the matrix or drop the sentence.'],
 ['Partnerships, p. 47 and Recognition, p. 41 cite **session codes** (D1.2, D2.1, D4.1, D6.1, D1.5 …)',
  'The codes were removed from the basic-elements field and the timetable is not annexed, so **they are defined nowhere**',
  'Either restore the codes in the daily programme, or remove them from the two fields that cite them.'],
 ['Basic elements, p. 25: “with **8 and 16 August as travel days**”, and Day 0 is arrival',
  'Flow 3 (Romania) declares **Travel Days: 0** and only 7 days of individual support',
  'If the Romanian group also arrives on 8 August, the flow should say 2 travel days. See section 3.'],
 ['Background of participants, p. 24: the Greek group “travels with **two accompanying adults**”, and Ioulia Dialeisma is the “second **accompanying adult**”',
  'The activity declares **No. of Accompanying Persons: 0** and 4 group leaders',
  'In Programme terms these two are **group leaders**. Using “accompanying adults” invites a question about an undeclared category. Change the words, not the people.'],
], widths=[5.6, 5.2, 5.8], small=True)

# ---------------------------------------------------------------- 3
H2('3. Money the form is not currently asking for')
P('The budget arithmetic is internally correct — I recomputed every line and each one matches to the cent, including the 21,638.00 activity grant and the 25,718.00 total. '
  'The question is not whether the sums are right but whether four choices behind them are the ones you meant to make.')
TBL([
 ['Line', 'Now', 'If changed', 'Difference'],
 ['Turkish flow travel', '9 × 309 = 2,781.00 (non-green rate)', '9 × 417 = 3,753.00 (green rate)', '**+972.00**'],
 ['Greek flow travel days', '2 days → 9 days of individual support, 3,726.00', '4 days → 11 days, 4,554.00', '**+828.00**'],
 ['Turkish flow travel days', '2 days → 9 days, 3,726.00', '4 days → 11 days, 4,554.00', '**+828.00**'],
 ['Romanian flow travel days', '0 days → 7 days, 2,898.00', '2 days → 9 days, 3,726.00', '**+828.00**'],
 ['Inclusion support for participants', '0.00, justification empty', 'real costs on dedicated lines', '**+ what you justify**'],
 ['**Activity grant**', '**21,638.00**', 'with all four plus 2,000.00 inclusion', '**27,094.00**'],
], widths=[4.0, 4.6, 4.6, 3.4], small=True)
P('That last figure is worth noticing: **27,094.00 is exactly the activity grant in the content document**. The two budgets differ by precisely these four decisions and nothing else, '
  'which means the difference is a set of choices rather than an arithmetic disagreement.')
FLAG('Before changing anything, verify in the 2026 Programme Guide how many travel days green travel makes eligible for the 500–1,999 km band. Each additional day is worth 9 × 46 = 414.00 per flow. '
     'And confirm that a coach or train route from İstanbul genuinely qualifies as green travel before switching the Turkish flow to 417 — if the group flies, the 309 rate is correct and it is the sentence on p. 44 that has to change.')
P('One question is now settled by the form itself: **organisational support is 125 × 21 = 2,625.00**, counting participants only, not group leaders or facilitators. '
  'The caveat in the content document about this can be deleted. The preparatory visit at 6 × 680 also shows that two people per organisation are fundable, including the host’s own.')

PAGEBREAK()
# ---------------------------------------------------------------- 4
H2('4. Content that went missing in the transfer')
TBL([
 ['Where', 'What is missing', 'Why it matters'],
 ['Learning outcomes, p. 25', 'The paragraph covering **entrepreneurship competence (KC7)** and **mathematical and technological competence (KC3)**, and the closing paragraph “We are careful about what we claim…”',
  'The field opens by saying the framework is “the **eight** European key competences” and then covers six. An assessor who counts will notice.'],
 ['Measures for fewer opportunities, p. 42', 'The passage on **accompanying persons** — six adults for twenty-one minors, one per 3.5, the Greek flow’s second adult and why, the additional travel days',
  '“Accompanying persons” is the **first example the question itself gives**. The answer now does not address it.'],
 ['Impact, p. 21', 'The final sentence ends without a full stop: “…a taste for organising something in their own community”',
  'Looks like the text was cut mid-paste.'],
 ['Virtual components, p. 43', 'Estimated share of participants using virtual components: **85**',
  'All 21 take the baseline test online and attend the four online sessions, so this looks like it should be **100**. If 85 is deliberate, nothing in the text explains it.'],
 ['Evaluation, p. 49', 'The section uses **ALL-CAPS headings** (MEASURING THE LEARNING OBJECTIVES, CHECKING THE QUALITY…)',
  'Not an error, but it is the one section written in a different register from the rest, and it is the opposite of the narrative style you asked for elsewhere.'],
 ['Topic selection, p. 22', '**Digital literacy · Digital safety and data protection · Media literacy and tackling disinformation**',
  'Coherent, but the application argues at length for democratic participation and for inclusion of rural and island young people, and neither is among the three topics. Worth a second look.'],
], widths=[3.4, 6.6, 6.6], small=True)

H3('Two claims about your own record that need care')
P('**“The expert assessment of our previous KA152 application said in so many words that it did not describe measures for the safety of the accommodation…”** (p. 35). '
  'The past-participation table on p. 14 records **0 KA152 applications as applicant** and 5 as partner. As written, the sentence and the table contradict each other. '
  'Either the assessment relates to an application where the association was a partner — in which case say so — or the table needs updating. It is a strong argument; it just has to match the record.')
P('**CONNECT-R** appears under “Our relevant Erasmus+ experience” (p. 12) with no role stated. The past-participation table shows KA154 as **partner** (1 application, 1 granted), which fits: '
  'the project is coordinated by Union Nationale des Maisons Familiales Rurales in France. Adding “as partner” costs three words and removes any suggestion of overclaiming. '
  'The opposite applies to **EMPOWER+**, where the association **is the coordinator of nine organisations across seven countries** — the form does not say so, and that is a real strength going unclaimed.')

# ---------------------------------------------------------------- 5
H2('5. Typography and language')
H4('Missing space after a full stop — 17 places, all from pasting text that lost its paragraph breaks')
BUL([
 'p. 11 “…European learning opportunities.**A** central part…”',
 'p. 12 “…geographical or social barriers.**O**ur European experience…”',
 'p. 14 “…education and digital technologies.**T**he island context…”',
 'p. 15 “…and other local organisations.**I**ts ongoing provision…”',
 'p. 18 “…volunteer and cooperation networks.**G**GD brings…”',
 'p. 20 “…before believing it and passing it on.**B**etween spring and summer 2026…”',
 'p. 24 “…at selection and at final confirmation.**F**our, all 18 or over…”',
 'p. 25 — six occurrences inside the learning-outcomes field alone: “…that records it.**T**he rule runs…”, “…a session and evidence.**T**he centre of it…”, “…the four media products.**T**he same days build…”, “…are what show it.**T**he competence we care about…”, “…Youthpass are the record.**C**itizenship competence…”, “…the initiatives themselves are the proof.**T**wo competences grow…”',
 'p. 25 “…the Greek group recognises at once.**C**ultural awareness…”',
 'p. 42 “…not by good intentions.**A**gainst geographical obstacles…”',
 'p. 42 “…never handed over mid-route.**T**he activity itself is held in Beliș…”',
 'p. 46 “…from two months before departure until the end.**T**he main risks are managed…”',
])
H4('Other')
BUL([
 'p. 24 “**All twenty one participants**” — should be twenty-one, hyphenated. The same field later writes “twenty-one” correctly.',
 'p. 24 “…the cohort is divided into **mixed teams ,** each containing…” — the number of teams has dropped out and there is a space before the comma. Two sentences later it says “The **four** working teams”. Should read “four mixed teams of five or six”.',
 'p. 24 “…checks both at selection and at final confirmation.**Four, all 18 or over**, experienced in youth work…” — the group-leaders answer begins mid-air, with no subject. Needs an opener such as “Four group leaders accompany the groups, all aged 18 or over…”.',
 'p. 25 “simulation and role play**;s**tructured debate” — no space after the semicolon.',
 'p. 25 “peer teaching **;** media production” and “before the answer key is revealed **;** then the mechanics” — space before the semicolon.',
 'p. 5 “**O1 :** By the end of the project” — space before the colon; O2 and O3 are correct.',
 'p. 22 “the **LEADERnetwork**” — missing space. Elsewhere the form correctly writes “the LEADER and ELARD rural networks”.',
 'p. 41 “the baseline and final test **gives** each participant a personal figure” — should be “give”.',
 'p. 4 Project title “**VERIFAI-Young Detectives** Against Digital Disinformation” uses a hyphen with no spaces, while the activity title uses a colon: “VERIFAI: Young Detectives…”. Make them the same.',
 'pp. 7, 11 Legal name “ASOCIATIA GRUPUL DE ACTIUNE **LOCALANAPOCA** POROLISSUM” — a missing space in the name held in the Organisation Registration System. It carries into every table in the form. It can only be corrected in ORS, not in the form.',
])

# ---------------------------------------------------------------- 6
H2('6. What is already right')
P('So it is not disturbed while fixing the rest:')
BUL([
 'Every budget figure adds up. Travel, individual support, organisational support and inclusion support for organisations each reconcile exactly, per flow and in total.',
 'Flow composition is correct: 7 + 7 + 7 participants, two group leaders on the Greek flow, one leader and one facilitator on each of the other two, 9 persons per flow, 27 in all.',
 'Participants with fewer opportunities split 4 + 4 + 5 across the flows and total 13, matching the activity header and the narrative.',
 'Dates, duration and venue are consistent: 09–15/08/2027, seven days excluding travel, three groups, Beliș, Cluj County.',
 'The three challenge types selected — geographical, economic, social — match the fewer-opportunities answers.',
 'All three Erasmus+ Youth Quality Standards boxes are ticked.',
 'The three organisation profiles are well written, and the KEA and GGD sections are honest about what each has not done before.',
 'Sustainability, dissemination and the participants’ role read cleanly and carry the latest versions of the text.',
])

FLAG('One thing to be comfortable with before signing: the Application conditions include “I confirm that no other organisations or individuals external to the applicant organisation have been paid or otherwise compensated for drafting the application.”')

E.doc.save('/home/user/UNIC-2/VERIFAI_Form_Review.docx')
print('saved')
