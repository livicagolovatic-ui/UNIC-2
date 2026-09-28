# -*- coding: utf-8 -*-
import docx_engine as E
from docx_engine import H1, H2, H3, H4, P, SMALL, FLAG, BUL, NUM, TBL, CALLOUT, PAGEBREAK

H1('VERIFAI — corrections to apply before submission')
SMALL('Keyed to the text as it stands in the final export (Form ID KA152-YOU-691C4B41). Each entry gives the form section, what is there now, and what to put in its place. '
      'Nothing here rewrites a field you have already reworded unless the fix requires it.')

CALLOUT('Do these four first if you do nothing else.',
        '1 — the preparatory visit, which is currently three different sizes in three places.  2 — the stale figures from the 20-participant and four-country versions.  '
        '3 — the learning-outcomes field that promises eight competences and delivers six.  4 — inclusion support for participants, promised in the text and zero in the budget. '
        'Together they are worth most of the gap between 74–82 and 84–88.',
        'FBEAEA', 'E0A0A0')

# ================================================================= 1
H2('1. Preparatory visit — the form fields are right; one sentence is not')
CALLOUT('Confirmed: the preparatory visit is correctly set up.',
        '**4 persons, 2,720.00, two flows of two, one facilitator on the GGD flow** — that is right and should not be touched. The unit cost covers travel and subsistence, and '
        'Alina Baba and Livia Golovatic are local, so no unit cost is claimed for them. Six people in the room, four funded, is a perfectly ordinary and well-run arrangement.',
        'EAF3EA', '9FC49F')
P('One sentence in the narrative does not match it, and it is a slip rather than a judgement. The paragraph currently reads:')
P('//“For Genç Gönüllüler Derneği, the facilitator it designates for the exchange, **M. Talha Serenli, the group leader proposed to accompany the Turkish group in August**, and '
  'one young person already selected for the exchange.”//')
P('That lists **three** people for GGD, which with KEA’s two and the coordinator’s two makes seven named against four declared — and the same paragraph then says the Turkish '
  'group leader takes part in the working sessions **online**. Two versions of the sentence appear to have been merged. Delete the middle clause:')
P('For Genç Gönüllüler Derneği, the facilitator it designates for the exchange and one young person already selected for the exchange.')
P('The opening sentence is then worth one clause, so that “six” and “four” are never read as a contradiction: //“Six people take part in the visit and four of them are funded — '
  'the coordinator’s two work in the territory, travel nowhere and are not claimed.”// Everything else in the field can stay as written.')

# ================================================================= 2
H2('2. Stale figures — a straight find and replace')
TBL([
 ['Form section', 'Find', 'Replace with'],
 ['Background of participants', '(25%, target 15 of 20)', '(25%, target 16 of 21)'],
 ['Background of participants', '(25%, target 12 of 20)', '(25%, target 13 of 21)'],
 ['Background of participants', 'Target: at least 60 applications for the 21 places.', 'Target: at least 63 applications for the 21 places.'],
 ['Background of participants', 'the cohort is divided into mixed teams , each containing', 'the cohort is divided into four mixed teams of five or six, each containing'],
 ['Background of participants', 'All twenty one participants are aged 14 to 17', 'All twenty-one participants are aged 14 to 17'],
 ['Background of participants', 'at final confirmation.Four, all 18 or over, experienced in youth work',
  'at final confirmation. Four group leaders accompany the groups, all aged 18 or over, experienced in youth work'],
 ['Background of participants', 'The group travels with two accompanying adults because of the length of the journey.',
  'The group travels with two group leaders rather than one because of the length of the journey.'],
 ['Background of participants', 'with Ioulia Dialeisma as second accompanying adult', 'with Ioulia Dialeisma as second group leader'],
 ['Role of participants', 'all four organisations involve the twenty as peer trainers', 'all three organisations involve the twenty-one as peer trainers'],
 ['Impact, beyond participants', 'the LEADERnetwork', 'the LEADER and ELARD networks'],
 ['Impact, benefit to participants', '…a taste for organising something in their own community', '…a taste for organising something in their own community.'],
 ['Project summary', 'O1 : By the end of the project', 'O1: By the end of the project'],
 ['Virtual components', 'Estimated share: **85**', 'Estimated share: **100** — every participant takes the baseline test online and attends all four online sessions'],
], widths=[3.4, 6.2, 7.0], small=True)
SMALL('The two “accompanying adults” changes matter more than they look: the activity declares No. of Accompanying Persons = 0, and “accompanying adult” is a funded category in '
      'Programme language. Calling the Greek pair group leaders removes a question the assessor would otherwise have to ask.')

PAGEBREAK()
# ================================================================= 3
H2('3. Learning outcomes — restore the two missing competences')
P('The field opens by naming //the eight European key competences// and covers six. Paste this paragraph back in, immediately before “Attitudes are the part we can shape but '
  'not certify.”')
P('The follow-up carries **entrepreneurship competence (KC7)**: turning an idea into a plan with a date, a venue, an audience, partners and named responsibilities, then running '
  'it and reporting on what happened, which is a different skill from having the idea. **Mathematical and technological competence (KC3)** is developed in one narrow but useful '
  'direction — reading a statistic critically, asking who was measured, when and how many, what the figure does not say, and recognising a graph built to mislead.')
P('And restore the closing sentence, which an assessor reads as a mark of honesty rather than of modesty — put it at the very end of the field:')
P('We are careful about what we claim. Seven days do not produce expert fact-checkers, and we will not write that they do. What seven days produce is that pause before sharing, '
  'four techniques a participant can actually perform under observation, and one local initiative each has led — which is exactly what objective O2 measures and what the '
  'observation grid records.')

H2('4. Inclusion support — correct what the text says it pays for')
CALLOUT('This corrects advice given in the first version of this pack.',
        'The earlier version told you to fund door-to-door domestic transport from inclusion support and to request a figure for it. That was wrong on both counts, and the '
        'National Call settles it: the additional real-cost funding attaches to //“un participant cu nevoi speciale a cărui condiție fizică, mentală sau de sănătate este de așa '
        'natură încât participarea la mobilitate nu este posibilă fără sprijin suplimentar”// — a participant whose physical, mental or health condition makes participation '
        'impossible without extra support, including where they need an accompanying person. It is not a transport subsidy and not a general entitlement for everyone with fewer '
        'opportunities.',
        'FBEAEA', 'E0A0A0')
P('Two things follow, and neither of them requires you to ask for money you cannot evidence.')
P('**Domestic travel is already paid — by the travel grant, not by inclusion support.** The travel unit cost is calculated by distance band from the participant’s place of '
  'origin, so the leg from a commune of the Apuseni or from a small island to the point of departure sits inside the 56.00, 309.00 or 417.00 already requested. Saying it comes '
  'from inclusion support is both wrong and unnecessary, because the stronger claim is the true one: the journey is paid from the participant’s own front door because that is '
  'what the travel grant is for and because we book it centrally rather than reimbursing a family afterwards.')
P('**Inclusion support for participants is correctly 0.00 now**, and the text should say why rather than promise a line that is empty. Replace the sentence in the '
  '“specific measures” field:')
TBL([
 ['Now', 'Replace with'],
 ['Transport is organised and paid from each participant’s own front door to the point of departure, **through the inclusion support category on a dedicated budget line**, so '
  'that a young person from Măguri-Răcătău, or one who must take an inter-island ferry before reaching an airport, does not have to solve the first leg alone.',
  'Transport is organised and paid from each participant’s own front door to the point of departure, booked and paid centrally by the coordinator out of the travel grant, which '
  'is calculated from each participant’s own place of origin, so that a young person from Măguri-Răcătău, or one who must take an inter-island ferry before reaching an airport, '
  'never has to fund or solve the first leg themselves and never waits to be reimbursed.'],
 ['**Inclusion support for participants is requested at real cost on separate dedicated lines**, each justified individually, for a documented need such as an extra ferry leg, '
  'additional domestic transport or an accessibility cost.',
  'No inclusion support for participants is requested at this stage, and that is a statement of fact rather than an omission: it covers the additional real costs of a '
  'participant whose health, disability or specific condition would otherwise make participation impossible, and we cannot know of such a case before selection in month 2. The '
  'confidential specific-needs sheet exists precisely to surface one, and if it does we will request the support at real cost, with its own justification, including an '
  'accompanying person where that is what the participant needs.'],
], widths=[7.4, 9.0], small=True)
P('**Inclusion support for organisations stays exactly as it is.** The 1,625.00 at 125.00 for each of the 13 participants with fewer opportunities is the category that does '
  'attach to that group, and it is correctly claimed.')

H2('5. Green travel on the Turkish flow')
P('The environmental field says //“the budget is built on the green rates for all three flows”// while flow 2 is costed at 309.00, the non-green rate for 500–1,999 km. '
  'Two ways to close it, and the first is worth **+972.00**:')
NUM([
 '**Preferred** — set flow 2 to green travel at 417.00 per person (9 × 417 = 3,753.00), if the group travels overland by coach or train. İstanbul to Cluj is about 1,300 km '
 'and takes roughly a day by road, which is why the additional travel days below matter. Confirm the route is real before you claim it.',
 '**If the group flies** — change the sentence to: “For each group the low-emission option is analysed — train, coach, ferry — and the option chosen and the reason are '
 'documented; the Romanian and Greek flows travel green, and for the Turkish flow the distance and the timing of an overland route with minors made it unworkable, so the '
 'standard rate is requested and the emissions are reduced everywhere else in the project.” Stating that openly costs nothing; claiming green rates you have not budgeted does.',
])

H2('6. Travel days — make the flows match the programme')
P('The basic-elements field and the annex both say 8 and 16 August are travel days, and the Greek flow is described twice as having four eligible travel days. The flows '
  'declare 2 for Greece, 2 for Türkiye and **0 for Romania**. Bring them into line with the programme, and check the 2026 Programme Guide for how many travel days green '
  'travel makes eligible on this band before claiming the extra two.')
TBL([
 ['Flow', 'Declared now', 'Should be', 'Individual support effect'],
 ['1 — Greece', '2 travel days, 9 days paid', '4 travel days, 11 days paid', '3,726.00 → 4,554.00 (**+828.00**)'],
 ['2 — Türkiye', '2 travel days, 9 days paid', '4 travel days, 11 days paid', '3,726.00 → 4,554.00 (**+828.00**)'],
 ['3 — Romania', '0 travel days, 7 days paid', '2 travel days, 9 days paid', '2,898.00 → 3,726.00 (**+828.00**)'],
], widths=[2.6, 3.8, 3.8, 4.6], small=True)
P('If you would rather not claim the extra days, the alternative is to delete “and four eligible travel days” from the logistics answer and remove the arrival and departure day '
  'blocks from the annex — but that weakens the description of how twenty-one minors actually get there, so claiming is the better route.')

PAGEBREAK()
# ================================================================= 7
H2('7. The barrier language')
TBL([
 ['Where', 'Now', 'Replace with'],
 ['Link to Erasmus objectives',
  '…which answers the economic one; English is not a selection criterion and A2 is accepted, with a glossary built in four languages, which answers **the linguistic one**; and '
  'preparation runs over four months… which answers **the social and educational ones**.',
  '…which answers the economic one; and preparation runs over four months rather than four weeks, with a parents’ meeting in each country before consents are signed and a '
  'stated right to leave a session without giving a reason, which answers **the social one**. English is not a selection criterion and A2 is accepted, with a glossary built in '
  'four languages, so that language is never a filter for anyone.'],
], widths=[3.2, 6.4, 7.0], small=True)
SMALL('You declared three challenge types — geographical, economic, social. This sentence answered five. Keeping the language support but presenting it as a measure open to '
      'everyone removes the mismatch without losing anything.')

H2('8. The competence matrix reference')
TBL([
 ['Where', 'Now', 'Replace with'],
 ['Recognition of learning outcomes',
  'The **competence matrix above** is the reference document for the whole process, since every competence claimed is tied to the sessions that build it…',
  'The **annexed project timetable** is the reference document for the whole process: every session in it carries its objective, its non-formal method, the key competences it '
  'builds, its output and the person responsible, so every competence claimed is tied to the sessions that build it…'],
], widths=[3.2, 6.4, 7.0], small=True)

H2('9. Accompanying persons — withdrawn')
CALLOUT('This withdraws an item from the first version of this pack.',
        'The earlier version asked you to paste a passage beginning “**Accompanying persons** are set by the journey rather than by the minimum: four group leaders and two '
        'facilitators…”. Do not use it. A group leader and an accompanying person are different categories, and conflating them would have introduced an error rather than '
        'removed one.',
        'FBEAEA', 'E0A0A0')
P('In this Action a **group leader** is an adult who accompanies a national group to ensure the young people’s learning, protection and safety — which is what your four are. An '
  '**accompanying person** is someone who escorts a participant whose condition makes participation impossible without that support; the National Call ties it to the same '
  'real-cost provision as inclusion support for participants. The form keeps three separate counters — group leaders, facilitators, accompanying persons — precisely because '
  'they are not interchangeable.')
P('So **No. of Accompanying Persons = 0 alongside 4 group leaders is correct**, needs no justification and should not be changed. The only thing worth doing is making sure the '
  'narrative never calls a group leader an accompanying person, which the find-and-replace pairs in section 2 already handle.')
P('If you still want the supervision ratio in the “specific measures” field — it is a fair inclusion measure and the field has room — use wording that keeps the categories '
  'straight:')
P('Supervision is set by the journey rather than by the minimum: four group leaders and two facilitators, six adults for twenty-one minors, one adult per 3.5 participants, '
  'below the National Call’s ceiling of one group leader for every four young people. The Greek group travels with two group leaders rather than one because its route — ferry '
  'to Piraeus, flight, then overland to the Apuseni — is the longest in the project and has at least one transfer where a group of fourteen-year-olds could be split. Every '
  'group is accompanied from its own departure point to Beliș and back and is never handed over mid-route.')

H2('10. Missing spaces after a full stop — 17 places')
SMALL('All are the result of pasted text losing its paragraph breaks. Search for each string and insert the space.')
BUL([
 'learning opportunities.**A** central part · social barriers.**O**ur European experience · digital technologies.**T**he island context · local organisations.**I**ts ongoing '
 'provision · cooperation networks.**G**GD brings · passing it on.**B**etween spring and summer',
 'final confirmation.**F**our (fixed by item 2 above) · that records it.**T**he rule runs · a session and evidence.**T**he centre of it · four media products.**T**he same days '
 'build · what show it.**T**he competence we care about · the record.**C**itizenship competence · themselves are the proof.**T**wo competences grow · recognises at once.'
 '**C**ultural awareness',
 'good intentions.**A**gainst geographical obstacles · handed over mid-route.**T**he activity itself · until the end.**T**he main risks are managed',
])
P('Also: “simulation and role play**;s**tructured debate” needs a space after the semicolon, and “peer teaching **;** media production”, “before the answer key is revealed **;** '
  'then the mechanics” have a space before it that should be removed.')

H2('11. The third topic')
P('You currently select Digital literacy skills and competences · Digital safety and data protection · Media literacy and tackling disinformation. The middle one is the '
  'weakest fit: nothing in the application is about data protection as a subject. The text argues at length for democratic participation and for the inclusion of rural and '
  'island young people, and neither appears. Replace it with whichever of those two the form’s list offers — a participation or active-citizenship topic if there is one, '
  'otherwise an inclusion topic. Topics are what the National Agency uses to route and classify the application, so they should mirror the priorities the text actually argues.')

H2('12. Outside the form')
BUL([
 '**The financial guarantee.** The budget page states that the National Agency has requested one. Ask ANPCDEFP what form it takes and by when, because it is a condition on '
 'signature rather than on scoring.',
 '**GGD’s accession form.** The uploaded file is “ACF -accession forms_E10309307 (1).pdf” where KEA’s reads “_signed”. Open it and check there is a signature.',
 '**The five-applications-per-OID limit.** The form states it explicitly. Confirm with GGD and KEA that neither is already named in five KA152 applications this round.',
 '**The 14–17 age band** remains as decided, against the 14–18 in the guide’s worked example. Nothing needs changing; it is recorded here so the decision is not lost.',
])

H2('What this is worth')
TBL([
 ['Criterion', 'As submitted', 'With items 1–11 applied'],
 ['Relevance, rationale and impact', '23–25 / 30', '**26–27 / 30**'],
 ['Quality of the project design', '29–32 / 40', '**33–35 / 40**'],
 ['Quality of the project management', '22–25 / 30', '**25–26 / 30**'],
 ['**Total**', '**74–82**', '**84–88**'],
], widths=[6.0, 4.8, 5.8], small=True)
P('And in money, if items 5 and 6 are taken: **+972.00** on the Turkish travel line, **+2,484.00** across the three individual-support lines, with inclusion support for participants correctly left at zero. That takes the activity grant from 21,638.00 to 25,094.00.')

E.doc.save('/home/user/UNIC-2/VERIFAI_Corrections_To_Apply.docx')
print('saved')
