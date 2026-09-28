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
H2('1. Preparatory visit — make it one number')
P('The form declares **4 persons and 2,720.00** in two flows. That is the correct reading: the unit cost covers travel and subsistence, and Alina Baba and Livia Golovatic are '
  'local, so they incur neither. Do not change the budget. Change the narrative so it says the same thing — and say plainly that six people take part while four are funded, '
  'because a reviewer reads that as cost discipline rather than as a discrepancy.')
H4('Replace the whole of “Please describe who will take part in the Preparatory Visit.”')
P('**Six people take part in the visit and four of them are funded.** The two from the coordinating organisation live and work in the territory, so they travel nowhere and '
  'cost the project nothing; the preparatory visit grant is requested only for the four who fly in. We chose all six by one rule: whoever has to sign something, facilitate '
  'something or reassure somebody in August should have stood in the building first.')
P('**Funded, from Genç Gönüllüler Derneği (Türkiye), two people:** the facilitator GGD designates for the exchange, and one young person already selected to take part. The '
  'facilitator is the one person whose work depends on conditions that cannot be described in writing — the AI and media production days need a room where twenty-one young '
  'people can edit video on a connection that holds — so the facilitator measures it, plans those two days against the actual spaces and agrees with our lead facilitator who '
  'runs what. This is the facilitator counted on this activity. The Turkish group leader who will accompany the group in August joins the working sessions online and receives '
  'the room allocation, the emergency arrangements and photographs of the floors his group will sleep on before he agrees to the travel plan.')
P('**Funded, from KEA IM Syrou (Greece), two people:** Evgenia Kalogeropoulou, social worker and proposed Greek group leader, and one young person already selected. Evgenia '
  'co-designs the Day 5 community dialogue, which is a facilitated social-work exercise before it is a media-literacy one, so she walks the village, meets the residents who '
  'have agreed to take part and the staff of the mayor’s office, and agrees the route and the timing on the spot. She is also the safeguarding counterpart for the Greek group, '
  'which makes the on-site check her own responsibility rather than someone else’s report to her.')
P('**Taking part on site at no cost to the project, from the coordinating organisation:** Alina Ioana Baba, project manager, and Livia Golovatic, activity coordinator and '
  'group leader of the Romanian group. Alina carries the budget, the contracts and the risk decisions, so she is the person who walks the corridors, tests the doors and '
  'windows and drives the route to the nearest hospital before she signs anything — the venue is contracted by her, on the spot if it passes and not at all if it does not. '
  'Livia will accompany the Romanian group in August and runs the four joint online preparation sessions, so she checks the rooms and the common spaces against the written '
  'risk assessment prepared by our financial and logistics officer and carries the answers back into the preparation.')
P('The two young people are not observers. Each is chosen from among those who declared, voluntarily and confidentially, a situation limiting their access to opportunities, '
  'because the barrier this measure answers is the social one: 12.5% of the young people in our survey said what stops them is lack of self-confidence. They have a defined job '
  '— they check the rooms and the common spaces from a participant’s point of view rather than an organiser’s, they take part in the village walk, and what they say is written '
  'into the final programme. Afterwards each describes the place to their own group in their own language, in the third online preparation session, which is worth more than any '
  'photograph we could send. Because they are minors, the visit carries the same protections as the exchange: written parental consent before booking, travel and medical '
  'insurance, and each young person accompanied throughout by the adult from their own organisation.')
P('All four funded travellers are already part of Activity YEXMS01 — one facilitator, one group leader and two of the twenty-one participants — so the preparatory visit adds '
  'no new people to the project, only an earlier date. [TO CONFIRM with the partners: which staff member GGD designates, and the identity of the two young people, which '
  'follows selection in month 2.]')
H4('Then two one-line repairs in the same activity')
TBL([
 ['Where', 'Now', 'Replace with'],
 ['“Why you want to carry out a Preparatory Visit”, last sentence of the grounds paragraph',
  '…and it is why two of the **six** places go to young people rather than staff, as described above.',
  '…and it is why two of the **four funded places** go to young people rather than staff, as described above.'],
 ['Timetable annex, Preparatory Visits sheet, “Participating organisations” cell',
  '**6 persons in total**, two from each of the three organisations…',
  '**Six people take part, four of them funded**: two from Genç Gönüllüler Derneği and two from KEA IM Syrou travel and are covered by the preparatory visit grant; Alina Ioana '
  'Baba and Livia Golovatic, of the coordinating and hosting organisation, take part on site at no cost to the project.'],
], widths=[3.6, 5.6, 7.4], small=True)

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

H2('4. Inclusion support for participants — request it, do not delete the promise')
P('The text promises door-to-door transport “through the inclusion support category on a dedicated budget line” and real-cost support on separate lines. All three flows '
  'currently declare 0.00 with an empty justification. Deleting the promise would cost design points; requesting the money keeps the promise and adds the funds. Enter a figure '
  'per flow and paste this into the **“Description and justification of expenses”** box on each flow, adjusting the amounts to your own estimates.')
P('Inclusion support is requested at real cost for the domestic legs that stand between a participant and the point of departure, because those legs are exactly what the '
  'economic and geographical barriers consist of in these three territories. For the Greek flow it covers the inter-island ferry legs and transfers that bring seven young '
  'people from small islands of the Cyclades and the Dodecanese to a single departure point before the group is even assembled — the longest and most expensive part of their '
  'journey, and the one a family would otherwise have to fund itself. For the Romanian flow it covers transport from communes such as Măguri-Răcătău and Beliș, where there is '
  'no scheduled service that matches a departure time. For the Turkish flow it covers transport from the rural localities behind the İstanbul periphery. A reserve within the '
  'same line is kept for any accessibility, dietary or health need declared after selection on the confidential specific-needs sheet, supported at real cost and justified '
  'individually. Every amount will be evidenced by invoice or ticket; nothing is paid by a family and reimbursed afterwards, because a reimbursement model excludes precisely '
  'the participants this support exists for.')
FLAG('Suggested build-up to price yourselves: Greek flow, 7 participants × ferry and transfer costs — the largest item; Romanian flow, 7 × local transport; Turkish flow, '
     '7 × local transport; plus a reserve for a declared specific need. The content document assumed 2,000.00 in total. Enter what you can evidence, not a round number.')

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

H2('9. Accompanying persons — restore the passage the question asks for')
P('“What specific measures (e.g. **accompanying persons**, reinforced mentorship, accessibility measures)…” currently answers the second and third examples and not the first. '
  'Paste this into the geographical-obstacles paragraph, after “…does not have to solve the first leg alone.”')
P('**Accompanying persons** are set by the journey rather than by the minimum: four group leaders and two facilitators, six adults for twenty-one minors, one adult per 3.5 '
  'participants, below the National Call’s ceiling of one leader per four young people. The Greek flow carries two group leaders because its route — ferry to Piraeus, flight, '
  'then overland to the Apuseni — is the longest in the project and has at least one transfer where a group of fourteen-year-olds could be split. Every group is accompanied '
  'from its own departure point to Beliș and back and is never handed over mid-route.')

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
P('And in money, if items 5 and 6 are taken: **+972.00** on the Turkish travel line, **+2,484.00** across the three individual-support lines, plus whatever inclusion support '
  'for participants you can evidence — taking the activity grant from 21,638.00 towards the 27,094.00 the content document computes.')

E.doc.save('/home/user/UNIC-2/VERIFAI_Corrections_To_Apply.docx')
print('saved')
