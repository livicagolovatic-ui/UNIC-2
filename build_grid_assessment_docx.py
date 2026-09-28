# -*- coding: utf-8 -*-
import docx_engine as E
from docx_engine import H1, H2, H3, H4, P, SMALL, FLAG, BUL, NUM, TBL, CALLOUT, PAGEBREAK

H1('VERIFAI — assessment against the KA152 evaluation grid')
SMALL('Final application, Form ID KA152-YOU-691C4B41, 58-page export, read in full with the submitted timetable annex. '
      'Scored against the three award criteria published in the Erasmus+ Programme Guide for Mobility of young people.')

CALLOUT('The headline.',
        'This is a strong application. The needs case rests on your own primary evidence, the design has a measurement architecture almost no KA152 application has, and the '
        'management section is unusually concrete. My estimate as submitted is **74–82 of 100**, comfortably over the 60 threshold and over the 70.0 the previous attempt scored. '
        'The gap between that and the **84–88** the same text would score is made up almost entirely of internal contradictions that cost nothing to fix — figures in one field '
        'that disagree with figures in another. That is the whole of my advice.',
        'E8EEF7', 'C7D6EA')

H2('The grid')
TBL([
 ['Criterion', 'Maximum', 'Minimum to pass', 'Previous application (2026 R1)', 'Estimate as submitted', 'If the contradictions are fixed'],
 ['Relevance, rationale and impact', '30', '15', '23', '**23–25**', '**26–27**'],
 ['Quality of the project design', '40', '20', '26', '**29–32**', '**33–35**'],
 ['Quality of the project management', '30', '15', '21', '**22–25**', '**25–26**'],
 ['**Total**', '**100**', '**60 overall**', '**70.0**', '**74–82**', '**84–88**'],
], widths=[4.4, 1.6, 2.2, 3.0, 2.6, 2.8], small=True)
SMALL('These are my estimates against the published criteria, not a prediction of what an assessor will do. Ranges rather than single figures, because the same text can move '
      'several points depending on how closely one reader cross-checks fields against each other.')

# ---------------------------------------------------------------- 1
H2('1. Relevance, rationale and impact — 23–25 of 30')
H4('What earns the points')
P('The needs case is built on primary evidence you collected yourselves: 153 responses from 12 of your 14 localities, 96 of them from the exact age group, reported with real '
  'figures rather than impressions. Most KA152 applications assert a need; this one measures it. It is then triangulated against the Flash Eurobarometer EP013EP and Greek DESI '
  'and national data, and the two datasets are read together to produce a diagnosis — **untrained confidence rather than ignorance** — which then drives the method. That '
  'need→analysis→method chain is precisely what this criterion rewards, and it is the strongest thing in the application.')
P('The participant profile is specific and defensible: 13 of 21 with declared barriers, 16 of 21 on a first European mobility, three peripheral territories whose shared '
  'structural condition is argued rather than assumed. The impact section names what happens beyond the room — four local initiatives, at least 80 young people, a tested '
  'toolkit, three reusable instruments — and then states its own limits: //“Twenty-one participants will not move a county-level statistic.”// Assessors read a great many '
  'applications that promise to transform a region; a stated limit next to evidenced claims reads as competence, not modesty.')
H4('What costs points')
BUL([
 '**The declared barrier types contradict the rationale.** The form declares geographical, economic and social. The Erasmus-objectives field still says measures answer '
 '“the linguistic one” and “the social and **educational** ones”. A reader who has both pages open sees two different lists.',
 '**The three topics do not match the argument.** You argue at length for democratic participation and for inclusion of rural and island young people, then select Digital '
 'literacy, Digital safety and data protection, and Media literacy. The second of those is the weakest fit; nothing in the application is about data protection as a subject.',
 '**Stale figures from the 20-participant and four-country versions survive.** “target 15 of 20”, “target 12 of 20”, “at least 60 applications”, “all **four** organisations”, '
 '“involve **the twenty** as peer trainers”. Individually small; together they tell an assessor the consortium and the numbers changed late and the text was not swept. That '
 'costs more than the arithmetic does, because it invites the question of what else was not updated.',
])

# ---------------------------------------------------------------- 2
H2('2. Quality of the project design — 29–32 of 40')
H4('What earns the points')
P('This is where the application is furthest above the field. Preparation runs four months, not four weeks, and it is sequenced: baseline test in month 2 //before// any '
  'learning activity, four joint online sessions in mixed national composition so the August teams have already met, a four-language glossary built with the participants, a '
  'parents’ meeting in each country in the local language before consents are signed, a two-day group leaders’ briefing. The preparatory visit is justified on four grounds and '
  'now has its own activity, its own programme and its own annex sheet.')
P('Participants are involved at every stage in ways that can be checked rather than claimed: the subject came from the survey and was validated back to young people before '
  'submission; they choose the cases analysed on Day 2; documentation roles are assigned in month 3; the content desk rotates by national group during the week; the host team '
  'of the day means all twenty-one lead once; they design and lead the four local initiatives; they close the project as evaluators in month 17.')
P('The learning-outcomes architecture is the single strongest design element. Three instruments exist **in writing before submission** — a fifteen-item practical test in two '
  'equivalent forms, an observation grid scoring four named techniques 0–2 with six calibrated observers and ten of twenty-one double-scored, and a ten-minute beneficiary '
  'exercise — with a piloting rule, a recalibration rule fixed in advance, and an observer calibration whose outcome is decided before any participant result is seen. Youthpass '
  'runs as a process from Day 1 with a learning diary and a sealed Day 1 artefact returned on Day 7. Very few KA152 applications can show any of this.')
P('Safety and protection is comprehensive and specific: written venue risk assessment verified on site before contracting, evacuation drill on arrival, room allocation with '
  'minors only with minors and leaders on the same floors, night-duty rota, safeguarding focal point deliberately outside the facilitation chain, sensitive-content protocol '
  'with a stated right to leave a session, central insurance, emergency protocol, GDPR handling and two-person review before anything involving a minor is published.')
P('The annexed timetable does its job: every session carries its objective, its non-formal method, the competences it builds, its output and the person responsible, across nine '
  'day blocks plus the three-day preparatory visit. It also resolves the session codes cited elsewhere in the form.')
H4('What costs points')
BUL([
 '**The learning-outcomes field opens by naming “the eight European key competences” and then covers six.** Entrepreneurship (KC7) and mathematical/technological (KC3) are '
 'missing. This is the field that carries the most design points, and the inconsistency is inside a single paragraph of itself.',
 '**“The competence matrix above is the reference document for the whole process” points at nothing** — the matrix was removed when the field became prose. An assessor '
 'looking for the document that ties competences to sessions and evidence finds a dangling reference. It exists in the annex; the form does not say so.',
 '**The measures field no longer answers “accompanying persons”**, which is the first example the question itself offers. The six-adults-for-twenty-one-minors reasoning and '
 'the Greek flow’s second adult were dropped from it.',
 '**Inclusion support for participants is promised in the text and is zero in the budget.** The measures field says door-to-door transport is paid “through the inclusion '
 'support category on a dedicated budget line”; all three flows declare 0.00 with an empty justification. A measure with no money behind it is the kind of thing this '
 'criterion is designed to catch.',
 '**The group-leaders answer begins “Four, all 18 or over, experienced in youth work…” with no subject**, straight after a full stop with no space. It is the answer about '
 'who supervises twenty-one minors, and it is the least legible sentence in the application.',
 '**Travel days contradict the programme.** The basic-elements field and the annex both say 8 and 16 August are travel days for everyone; the Romanian flow declares 0.',
])

PAGEBREAK()
# ---------------------------------------------------------------- 3
H2('3. Quality of the project management — 22–25 of 30')
H4('What earns the points')
P('Roles are separated by name and with a reason, not by title: the safeguarding lead sits outside the facilitation chain //so that a participant can raise a concern about a '
  'facilitator//. The partnership agreement is signed in month 1 before any expenditure and carries deliverables with dates, budget shares, transfer conditions, safeguarding '
  'obligations and what happens if a partner does not deliver. Escalation is defined in advance and proportionate, payments are staged against deliverables rather than the '
  'calendar, and the action log is reviewed line by line at every meeting.')
P('Evaluation is the strongest management element, and it is honest in a way assessors notice: instruments built so that failure is visible, a participant who misses one form '
  'of the test reported as excluded rather than dropped from the denominator, and an explicit refusal to call fifteen items over twenty-one participants a validated '
  'psychometric instrument. Dissemination names five audiences with a channel, an owner and a countable target each, adds the partners’ own channels with a posting rhythm and '
  'a fifteen-post commitment, and local media with a six-item target. Sustainability names four things that stay and, in the partnership agreement, //a person// responsible '
  'for each — “a name, not a department”.')
P('The risk treatment is concrete where it matters: visas are identified as the principal risk, with the Schengen position stated correctly, the procedure starting in month 3, '
  'and reserve participants prepared with complete files.')
H4('What costs points')
BUL([
 '**The preparatory visit is three different sizes in three places.** The activity header and the flows declare **4 persons / 2,720.00** in two flows. The narrative says '
 '“**Six** people travel or take part on site, two from each of the three organisations” and “two of the **six** places”. The annex says **6 persons**. On top of that the '
 'narrative now lists **three** people for GGD — the facilitator, M. Talha Serenli, and a young person — and then says in the same paragraph that the Turkish group leader '
 'takes part **online**. This is the most visible inconsistency in the application and it sits in a field an assessor reads closely, because it is a funded activity.',
 '**“The budget is built on the green rates for all three flows”** — the Turkish flow is costed at 309 EUR, the non-green rate. Green is 417.',
 '**“Four eligible travel days” for the Greek flow** appears twice in the narrative; the flow declares 2.',
 '**The financial guarantee the National Agency has requested is nowhere addressed** in the application.',
 '**Typographic accumulation.** 17 missing spaces after full stops, “All twenty one participants”, “mixed teams ,” with the number dropped, “LEADERnetwork”, “O1 :”, and an '
 'Impact field whose last sentence has no full stop. No single one matters. Together they read as a document assembled at speed, and this is the criterion where that '
 'impression is charged.',
 '**GGD’s accession form may be unsigned** — the filename is “ACF -accession forms_E10309307 (1).pdf” where KEA’s reads “_signed”. Worth opening before submission.',
])

# ---------------------------------------------------------------- fixes
H2('The fix list, in order of points per minute spent')
TBL([
 ['#', 'Fix', 'Where', 'Criterion'],
 ['1', 'Make the preparatory visit one number everywhere. The form says 4 persons and 2,720.00, which is the defensible reading — the host’s own staff travel nowhere. '
       'Rewrite the narrative for two partners × two people, remove the third GGD name, and correct the annex.', 'PREPV02 narrative + annex', 'Management'],
 ['2', 'Sweep the stale figures: 15 of 20 → 16 of 21; 12 of 20 → 13 of 21; 60 applications → 63; “all four organisations” → three; “the twenty” → twenty-one.',
       'Background of participants; role of participants', 'Relevance + design'],
 ['3', 'Restore the KC7 and KC3 sentence, or change “the eight key competences” to name the six actually covered.', 'Learning outcomes', 'Design'],
 ['4', 'Decide the inclusion support for participants: either request it with a justification, or delete the two sentences that promise it.', 'Measures field + flows', 'Design + management'],
 ['5', 'Align the barrier language: remove “the linguistic one” and “educational”, keeping language support as a measure open to everyone.', 'Erasmus objectives field', 'Relevance'],
 ['6', 'Either set the Turkish flow to green travel (+972.00) or change the sentence claiming green rates for all three flows.', 'Environmental practices + flow 2', 'Management'],
 ['7', 'Fix “The competence matrix above” — point it at the annexed timetable, which does carry the matrix.', 'Recognition of learning', 'Design'],
 ['8', 'Give the group-leaders answer a subject: “Four group leaders accompany the groups, all aged 18 or over…”.', 'Background of participants', 'Design'],
 ['9', 'Restore the accompanying-persons passage — six adults for twenty-one minors, one per 3.5, and why the Greek flow carries two.', 'Measures field', 'Design'],
 ['10', 'Run the typographic list from the earlier review: 17 missing spaces, “twenty one”, “LEADERnetwork”, “O1 :”, the missing full stop in Impact.', 'Throughout', 'Management'],
 ['11', 'Reconsider the third topic. “Digital safety and data protection” is the weakest fit for what the text argues.', 'Topic', 'Relevance'],
 ['12', 'Ask ANPCDEFP what the financial guarantee requires, and check that GGD’s accession form is signed.', 'Outside the form', 'Eligibility'],
], widths=[0.8, 7.4, 4.4, 3.4], small=True)

H2('Two things I got wrong earlier, corrected')
P('The **Annexes section does carry a Timetable slot** — you were right and I was reading an export that did not show it. The timetable is uploaded (25 kB), alongside the '
  'Declaration on Honour (184 kB) and both accession forms. My earlier concern that the session codes D1.2, D4.1 and the rest were defined nowhere therefore falls away: they '
  'are defined in the annex, which is attached.')
P('The **preparatory visit at four funded persons is almost certainly the correct reading**, not an under-claim. The unit cost covers travel and subsistence, which the host '
  'organisation’s own local staff do not incur. The 2,720.00 now in the form matches the alternative figure flagged in the earlier review. It is the narrative that needs to '
  'follow the budget here, not the other way round.')

FLAG('Still undecided from earlier, and each worth money: the Turkish flow’s travel rate (+972.00), the travel days on all three flows (414.00 per person-day per flow), and '
     'inclusion support for participants. Taken together these are the difference between the 21,638.00 activity grant in the form and the 27,094.00 the content document '
     'computes. None of them affects the score directly; all of them affect what the project can actually pay for.')

E.doc.save('/home/user/UNIC-2/VERIFAI_Evaluation_Grid_Assessment.docx')
print('saved')
