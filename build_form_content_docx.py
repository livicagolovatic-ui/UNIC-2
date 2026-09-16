# -*- coding: utf-8 -*-
"""VERIFAI — clean fill-in document, section by section per the KA152-YOU 2026 R2 form."""
from docx_engine import *

# ---------- cover ----------
p = doc.add_paragraph(); runs(p, 'ERASMUS+ · KA152-YOU · MOBILITY OF YOUNG PEOPLE — YOUTH EXCHANGES', size=9, color=BLUE, bold=True)
p = doc.add_paragraph(); runs(p, 'VERIFAI', size=30, color=BLUE, bold=True)
p.paragraph_format.space_after = Pt(0)
p = doc.add_paragraph(); runs(p, 'Young Detectives Against Digital Disinformation', size=15, color=INK)
p.paragraph_format.space_after = Pt(4)
p = doc.add_paragraph(); runs(p, 'Application content, ready to enter into the form', size=12, color=GREY)
p.paragraph_format.space_after = Pt(12)
SMALL('Call 2026, Round 2 · Form ID KA152-YOU-691C4B41 · Deadline 1 October 2026, 12:00 Brussels time\n'
      'Applicant and coordinator: ASOCIAȚIA GRUPUL DE ACȚIUNE LOCALĂ NAPOCA POROLISSUM (E10181755 — RO) · National Agency: RO01 — ANPCDEFP')

CALLOUT('What this document is.',
        'The completed content of the application, section by section and question by question, in the order of the 2026 Round 2 form. Each form question appears in a blue box; the text under it is the answer, ready to enter. '
        'The grey line after each answer is its character count. **The limits shown are assumptions, not facts read from the form** — 5,000 for the summary and short fields, 6,000 for the long narrative ones. '
        'Every answer here fits those assumptions, so if the live field turns out to be larger you have room to spare, and if one is smaller the count tells you immediately how much to cut.\n'
        'Square brackets mark the few facts that do not exist yet — the two island partners, the venue, the departure cities and the EMPOWER project reference. Everything else is final.',
        'E8EEF7', 'C7D6EA')
PAGEBREAK()

# =====================================================================
H1('Context')
TBL([
 ['Field', 'Entry'],
 ['Project title', 'VERIFAI: Young Detectives Against Digital Disinformation'],
 ['Project start date', '01/04/2027'],
 ['Project duration (months)', '18'],
 ['Project end date', '30/09/2028'],
 ['National Agency of the applicant organisation', 'RO01 — Agenția Națională pentru Programe Comunitare în Domeniul Educației și Formării Profesionale'],
 ['Language used to fill in the form', 'English'],
], widths=[5.5, 11.1], count=False)

# =====================================================================
H1('Project summary')

Q('What do you want to achieve by implementing the project? What are the objectives of your project? Please specify from the perspective of youth work practice.')
P('We want young people who use artificial intelligence every single day to stop taking at face value whatever it hands them. In our own survey of 153 young people in the Napoca Porolissum LAG territory, 96.9% of '
  'those aged 14–17 already use AI tools, yet they rate their own digital competence at 3.25 out of 5, and half of them build their picture of the world from social media. Nobody has taught them how to check any of '
  'it. VERIFAI turns twenty of them, from four peripheral European communities, into detectives: young people who can identify a source, check a date and a context, compare two independent sources, recognise a '
  'reused image and spot the signature of AI-generated content — and who then pass that on to others at home.')
P('From a youth work perspective the practice problem is not ignorance. It is untrained confidence. The Flash Eurobarometer “Youth Survey 2024” (EP013EP), carried out by Ipsos for the European Parliament among '
  '25,863 young people aged 16–30 across all 27 Member States, found that more than three quarters of them had met disinformation in the previous seven days, while 70% were confident they could recognise it. '
  'Confidence outruns competence — so the method cannot be a lecture. Participants meet the false material and commit to a judgement //before// the verdict is revealed, and discover for themselves that they were '
  'wrong. That controlled moment of being wrong is the core of the non-formal learning approach of this exchange, and it only works in a genuinely international group, where a stereotype is very hard to defend with '
  'someone from the targeted community sitting at the same table.')
P('The project has three objectives. Each names its target group, its threshold, the instrument that produces the number and the date by which it has to be true.')
P('**O1 — Measured competence.** By 30 September 2028, at least 16 of the 20 participants aged 14–17 increase their score on the project’s 15-item, 30-point practical verification test by at least 30% against their '
  'own baseline, measured in May 2027 with the equivalent form of the same instrument and the same formula at both ends.')
P('**O2 — Demonstrated competence.** By 15 August 2027, the last day of the youth exchange, at least 16 of the 20 participants demonstrate all four verification techniques — identifying the source and the author; '
  'checking the date and the context; comparing at least two independent sources; verifying an image or a claim, including the indicators of AI-generated content — scoring the full 2 points on each, in the structured '
  'observation grid applied during session D4.1 by six observers trained and calibrated beforehand.')
P('**O3 — Transfer to the community.** Between September 2027 and June 2028, the 20 participants reach at least 80 other young people through four local initiatives, one in each partner community, and at least 70% '
  'of the young people reached pass the ten-minute closing exercise: naming two distinct checks, actually carrying one of them out, and drawing a conclusion that follows from what they found.')
P('The 30% threshold is confirmed once the baseline exists, using relative growth with the same 30-point instrument at both ends. The recalibration rule is fixed in writing now, before any data exists: below a group '
  'mean of 9/30 the threshold rises to +50%, above 18/30 it falls to +20% with an absolute companion measure, and a participant scoring 24 or more at baseline meets O1 by holding 27 or more at the end. Fixing this '
  'in advance is what stops a threshold from becoming a way of producing the answer we want.')
COUNT()

Q('What activities do you plan to implement? What is the number and profile of the participants involved?')
P('One youth exchange of seven activity days plus two travel days, hosted in the Napoca Porolissum LAG territory in the Apuseni Mountains, Romania, from 9 to 15 August 2027 — inside the school summer holiday of all '
  'four countries. The programme moves from self-diagnosis (“My Digital Map”) through the mechanics of manipulation (“Spot the Fake”), AI-generated content (“AI or human?”), a full fact-checking simulation '
  '(“Fact-checkers for a day”), a community and intercultural day in a village of the territory, media production (“Make It, Don’t Fake It”) and a public presentation with Youthpass reflection. Around it: four '
  'months of preparation with four joint online sessions and a preparatory visit, and ten months of local application in which the participants run four local initiatives in their own communities.')
P('Twenty young people aged 14–17, five from each of the four organisations, plus four group leaders and two facilitators — 26 people in total. They come from four peripheral communities: the rural mountain communes '
  'of the LAG territory in Cluj County (Romania), the İstanbul metropolitan periphery (Türkiye), inland Corsica (France) and inner Sardinia (Italy).')
P('They share the profile this project is built for. Almost all of them use AI tools and social media every day, and for a large part of them social media is the news; none of them has been taught how to check any of '
  'it. Their access to non-formal learning is thin and their access to international learning is close to nil: at least 15 of the 20 will be taking part in a European mobility for the first time, and in our territory '
  '31.3% of young people aged 14–17 have never taken part in any non-formal education activity at all. At least 12 of the 20 face documented barriers — geographic (isolated mountain communes, two Mediterranean '
  'islands, a metropolitan periphery), economic, educational, linguistic or social. The group is built to be mixed in gender, in locality and, in the Romanian and island groups, in language.')
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
P('We do not claim more than that. Twenty participants will not move a county-level statistic, still less a national one. The contribution is exactly what it is: measurable change in twenty young people, documented '
  'extension to at least eighty more, and three instruments and one toolkit that stay in use in four organisations after the money stops.')
COUNT()
PAGEBREAK()

# =====================================================================
H1('Summary of participating organisations')
TBL([
 ['Organisation name', 'OID', 'Country', 'Role', 'Type of organisation'],
 ['ASOCIAȚIA GRUPUL DE ACȚIUNE LOCALĂ NAPOCA POROLISSUM', 'E10181755', 'Romania', 'Applicant organisation', 'Non-governmental organisation / association (non-profit)'],
 ['SINIRLARI AŞAN GENÇLIK DERNEĞI (YOBBA)', 'E10094576', 'Türkiye', 'Partner organisation', 'Non-governmental organisation / youth association (non-profit)'],
 ['[TO CONFIRM — partner in Corsica]', '[TO CONFIRM]', 'France', 'Partner organisation', '[TO CONFIRM]'],
 ['[TO CONFIRM — partner in Sardinia]', '[TO CONFIRM]', 'Italy', 'Partner organisation', '[TO CONFIRM]'],
], widths=[5.4, 2.2, 1.8, 3.4, 3.8], count=False)

H1('Summary of activities and participants')
TBL([
 ['Activity Type', 'No. of activities', 'No. of persons', 'Participants with fewer opportunities'],
 ['Youth exchanges', '1', '26', '12'],
 ['**Total**', '**1**', '**26**', '**12**'],
], widths=[5.0, 3.6, 3.6, 4.4], count=False)

# =====================================================================
H1('Project budget')
H3('Budget summary')
TBL([
 ['Budget item', 'Grant (EUR)', 'Basis of calculation'],
 ['Organisational support', '2,500.00', '125 × 20 participants'],
 ['Travel (green travel)', '8,315.00', 'Romania 7 persons × 56 (band 10–99 km); Türkiye 7, Corsica 6 and Sardinia 6 persons × 417 (band 500–1,999 km)'],
 ['Individual support', '12,512.00', '26 persons × 9 days × 46 = 10,764.00, plus 19 persons × 2 additional green-travel days × 46 = 1,748.00'],
 ['Inclusion support for organisations', '1,500.00', '125 × 12 participants with fewer opportunities'],
 ['Inclusion support for participants', '2,000.00', 'Real costs, requested on separate dedicated lines and justified individually'],
 ['Preparatory visit', '4,760.00', '680 × 7 persons: 2 from each of the 3 sending organisations, one of them a young person, plus 1 staff member of the coordinating organisation'],
 ['**Total**', '**31,587.00**', 'Of which 26,827.00 is the Activity 01 grant and 4,760.00 the preparatory visit'],
], widths=[4.4, 2.2, 10.0], count=False)
SMALL('Figures built on the 2026 Programme Guide unit costs. The form produces the final amounts per flow once the distance calculator has been run for each place of origin. [TO CONFIRM: distances, once the partners’ departure cities are known.]')

H3('Budget summary per activity type')
TBL([['Activity type', 'Grant (EUR)'], ['Youth exchanges', '26,827.00']], widths=[8.0, 8.6], count=False)
H3('Budget summary per activity')
TBL([['Activity id', 'Activity type', 'Grant (EUR)'], ['01', 'Youth exchanges', '26,827.00']], widths=[4.0, 6.0, 6.6], count=False)
PAGEBREAK()

# =====================================================================
H1('Participating organisations')
H2('Applicant — ASOCIAȚIA GRUPUL DE ACȚIUNE LOCALĂ NAPOCA POROLISSUM')
TBL([
 ['Field', 'Entry'],
 ['Organisation ID (OID) / PIC', 'E10181755 / 935151490'],
 ['Legal name', 'ASOCIAȚIA GRUPUL DE ACȚIUNE LOCALĂ NAPOCA POROLISSUM'],
 ['Country / Region', 'Romania / Nord-Vest, Cluj County'],
 ['City', 'Gilău'],
 ['Address', 'Eroilor Street, Building I1, Gilău, 407310, Cluj County'],
 ['Is the organisation a public body?', 'No'],
 ['Is the organisation a non-profit?', 'Yes'],
 ['Legal representative', 'Marius Gheorghe Dumitrescu, President'],
 ['Contact person', 'Alina Ioana Baba, Manager — manager@napocaporolissum.ro'],
], widths=[5.0, 11.6], count=False)

Q('What are the activities and experience of the organisation in youth work?')
P('LAG Napoca Porolissum is a public-private partnership founded in 2011 under the LEADER programme, with 43 partners: 14 municipalities, one university and 28 private-sector members. It employs 13 people and works '
  'across a rural mountain territory of 14 localities in the Apuseni Mountains, Cluj County. Its mandate is local development through a bottom-up approach, and youth work has become a permanent strand of that mandate '
  'rather than an occasional add-on.')
P('In the youth field specifically, the organisation was the coordinator of the Erasmus+ project //Rural Youth Parliament — tool for youth involvement in local communities// (2021-1-RO01-KA220-YOU-000029265), which '
  'created and ran youth parliament simulations across rural communities, and it coordinates the Rural Youth Parliament that came out of it. It is currently implementing //CONNECT-R — Connecting rural youth with the '
  'EU// under KA154-YOU (2025 ID KA154-YOU-62F63343), and has been a partner in //YouProClima// (2023-1-IT03-KA220-YOU-000155348), //ALL4JOBS// (KA220-YOU-70101DB1) and //SMART+CULTURE// (KA210-YOU-C68333FA).')
P('It also brings the experience of **EMPOWER** — [TO COMPLETE: full project title], implemented under [TO COMPLETE: action] with the reference [TO COMPLETE: project number], in which LAG Napoca Porolissum acted as '
  '[TO COMPLETE: coordinator / partner]. Its relevance to VERIFAI is direct: [TO COMPLETE, one sentence — what the project did with and for young people, and what the organisation took from it that this project uses].')
P('Beyond the Programme, the organisation runs the cultural and educational infrastructure that young people in this territory actually have. //Ruraliada — Culture in the Mountains//, funded through the National '
  'Recovery and Resilience Plan and implemented in 2024, was a three-day festival of visual, digital and performing arts in Beliș commune — painting, ceramics and multimedia workshops, improvisational theatre, '
  'encounters with artists — designed to motivate rural young people and to push local authorities to widen what they offer. //The School — children’s painting// brought professional artists into village schools '
  'across the county. The organisation runs Christmas markets in Mărișel and Beliș, an annual Diversity Day, and educational camps in Romania and abroad for children from socially disadvantaged communities. Through '
  'its Social Inclusion Centre and the //UNIC — Porolissum// project it works directly with vulnerable families in the territory, which is how it reaches young people that a call published online would never touch.')
P('And, crucially for this application, the organisation carried out the needs analysis on which VERIFAI is built: a bilingual Romanian/Hungarian survey of 153 young people from 12 of the 14 localities of the '
  'territory, of whom 96 are aged 14–17 — the exact target group of this project.')
COUNT()

Q('Please describe the profile of each of the group members and what does each one bring to the project.')
TBL([
 ['Person and role in VERIFAI', 'Profile and contribution'],
 ['**Alina Ioana Baba**\nProject manager',
  'Two degrees (Legal Sciences; Public Administration), three master’s degrees (Public Management; Health Policy and Management; Rural Development) and a PhD in economics. More than twelve years in project management '
  'and rural development, with a strong record in animating local actors. Manager of the association for over ten years, responsible for a portfolio that includes Erasmus+ projects in youth, VET, school and adult '
  'education as well as transnational cooperation. Guest facilitator at workshops and conferences of the European Network for Rural Development. In VERIFAI she carries overall coordination, the relationship with the '
  'National Agency, the budget, reporting and risk decisions.'],
 ['**Claudiu Iancu**\nLearning Programme Coordinator (non-formal learning) and lead facilitator',
  'Youth worker and community facilitator, with a qualified Trainer certificate and five Europass mobility certificates. BSc in Economic Engineering in Agriculture, MSc in Rural Development. Around three years inside '
  'Local Action Groups, focused on rural development, social inclusion and non-formal education, after a background in adult education where he contributed as an expert to the training of over 1,000 adults. Directly '
  'involved in more than five Erasmus+ Youth projects; in the past three years he has organised and facilitated over 50 youth events. Coordinator of the Rural Youth Parliament and youth leader in YouProClima. In '
  'VERIFAI he owns the learning programme, the three measurement instruments, the facilitation team and the Youthpass process.'],
 ['**Livia Golovatic**\nActivity coordinator and Romanian group leader',
  'BA in International Relations and European Studies, currently in the first year of a master’s in European Affairs and Programme Management. Assistant manager on the implementation of the Local Development Strategy, '
  'with experience in strategic planning support. Involved in Erasmus+ Youth and VET projects, contributing to implementation, activity coordination and cooperation with international partners, with practical '
  'experience in non-formal education and youth participation, including in EMPOWER [TO CONFIRM: her exact role there]. In VERIFAI she leads the Romanian group, runs the four joint online preparation sessions and '
  'coordinates the four local initiatives.'],
 ['**Marilena Georgescu**\nInclusion and safeguarding lead',
  'Higher education in Social Assistance and Law, master’s in Project Management, with vocational qualifications in human resources management, public procurement, entrepreneurship, train-the-trainer and '
  'socio-educational animation. Fourteen years managing projects for the social inclusion of vulnerable groups, vocational training and labour-market integration, and educational and cultural projects. Coordinator of '
  'social service centres including a day centre for children. In VERIFAI she is the designated safeguarding focal point — deliberately a person outside the facilitation team — and she leads the recruitment of '
  'participants with fewer opportunities through the Social Inclusion Centre.'],
 ['**Iulia Fătu**\nFinancial and logistics officer',
  'Two bachelor’s degrees (Accounting; Agri-food Economy) and two master’s degrees (Agribusiness; Audit and Financial Management of European Funds). Working in European projects since 2014, responsible for procurement '
  'documentation, project evaluation and monitoring, and the implementation of social infrastructure projects. In VERIFAI she handles the budget, procurement, venue and transport contracting, insurance, the written '
  'venue risk assessment and financial reporting.'],
], widths=[4.2, 12.4])
P('The five roles are separated on purpose. The project manager decides; the Learning Programme Coordinator owns the learning; the safeguarding lead sits outside the facilitation chain, so that a participant can '
  'raise a concern about a facilitator; and the financial officer is not the person negotiating with participants or families. The team meets weekly during the preparation and mobility months and monthly otherwise, '
  'with a written action log in which every decision has an owner and a date.')
COUNT()

PAGEBREAK()
H2('Partner — SINIRLARI AŞAN GENÇLIK DERNEĞI / YOBBA (Türkiye)')
TBL([
 ['Field', 'Entry'],
 ['Organisation ID (OID) / PIC', 'E10094576 / 901841496'],
 ['Legal name', 'SINIRLARI AŞAN GENÇLIK DERNEĞI'],
 ['Country / City', 'Türkiye / İstanbul (Küçükçekmece)'],
 ['Address', 'İnönü Mahallesi, Hakan Caddesi, Öz Feza Sitesi A Blok Kat 2/10, Küçükçekmece, 34295, İstanbul'],
 ['Is the organisation a public body? / non-profit?', 'No / Yes'],
 ['Legal representative', 'Doğan Can Karabudak, President'],
 ['Contact person', 'Aysu Zeybel, Project Coordinator'],
], widths=[5.0, 11.6], count=False)

Q('What are the activities and experience of the partner organisation in youth work?')
P('YOBBA is a youth association based in Küçükçekmece, in the metropolitan periphery of İstanbul, working with a volunteer community of more than 150 young people a year. Its declared core expertise is digital media: '
  'it trains young people in media work, gives them professional skills and puts them into projects with social impact, and it delivers digital literacy training to beneficiaries of companies and civil-society '
  'institutions. In 2020 its team founded the //ErasmusPlus Türkiye// platform, which produces content about opportunities at home and abroad and disseminates Erasmus+ projects nationally, with a following of around '
  '250,000.')
P('Its work spans youth policy volunteering, civil-society development, non-formal education and the recognition of youth work, international cooperation, environmental initiatives, work with refugees and migrants, '
  'women’s rights and gender equality, and the social inclusion of people with disabilities. It has run digital skills training covering digital literacy and cyber-security, intercultural exchange programmes, '
  'entrepreneurship initiatives, and mental health and emotional resilience programmes delivered together with psychologists and counsellors. Activities with young people are designed and supervised with pedagogues '
  'and psychologists involved.')
P('**Experience in this Action specifically.** YOBBA has taken part in six KA152 youth exchanges as a partner organisation between 2022 and 2024, with coordinators in Hungary (2022-1-HU-01-KA152-45D10D09), Latvia '
  '(2023-LV02-KA152-YOU-000148179), Italy (2023-1-IT03-KA152-YOU-000147001; 2023-3-IT03-KA152-YOU-000183264; 2024-3-IT03-KA152-YOU-000282312) and Poland (2023-3-PL01-KA152-YOU-000183071).')
P('**What it brings, and where it does not overlap with the coordinator.** YOBBA teaches young people to //produce// digital content. It does not teach them to //verify// it. That gap is exactly what this project '
  'fills, and it is why the division of labour between the two experienced partners is clean rather than duplicated. YOBBA leads Day 6, the media production day, and contributes substantially to Day 3 on '
  'AI-generated content, where knowing how such content is made is precisely what allows a fifteen-year-old to recognise it. The coordinator leads the verification days. A young person who can edit a convincing video '
  'but cannot check a source is a more efficient vector of disinformation, not an antidote — the partnership is designed around closing that circle.')
P('**One of the two facilitators of the exchange is designated by YOBBA**, for the same reason: the sessions on AI-generated content, on the ethics of using AI in one’s own production and on media production need '
  'someone in the facilitation team who works with these tools professionally. That facilitator joins in month 4, takes part in the observer calibration exercise, and applies the observation grid on Day 4 alongside '
  'the facilitator designated by the coordinator. YOBBA also brings dissemination reach that none of the other partners has.')
COUNT()

Q('Please describe the profile of each of the group members and what does each one bring to the project.')
TBL([
 ['Person and role', 'Profile and contribution'],
 ['**Doğan Can Karabudak**\nLegal representative; lead on media production and AI content',
  'Computer engineer, founder of YOBBA, traveller and content creator. Alumnus of the Study of the United States Institutes programme (2014). Has organised and contributed to numerous EU projects and training courses '
  'as leader and as participant, and has delivered over 100 seminars and training sessions. In VERIFAI he leads sessions D3.1 (AI-generated content) and D3.4 (the ethics of AI use), co-leads Day 6, and secures '
  'dissemination through the platforms YOBBA operates.'],
 ['**Aysu Zeybel**\nProject coordinator; Turkish group leader',
  'Graduate in Economics, University of Karabük. Learned sign language at university and has worked on projects with people with disabilities. Completed a ten-month European Solidarity Corps project in Tușnad, '
  'Romania, running weekly activities with children with disabilities in kindergarten, after-school and middle-school settings — direct experience of intercultural life between Hungarian and Romanian communities, '
  'which is directly relevant to a project about how information travels inside language communities. In VERIFAI she leads the Turkish group, prepares it before departure, supervises it throughout, and observes one '
  'mixed team on Day 4.'],
 ['**Facilitator designated by YOBBA**\n[TO CONFIRM: name]',
  'A facilitator with professional practice in digital content production and in generative AI tools, and with experience of working with young people in non-formal settings. Joins the team in month 4, takes part in '
  'the observer calibration exercise, co-facilitates sessions D2.3 and D4.2, supports D3.1, D3.4 and Day 6, and carries out the independent second scoring of five participants on Day 4.'],
], widths=[4.2, 12.4])
COUNT()

H2('Partner — [TO CONFIRM], Corsica (France)')
P('**Profile.** [The partner’s own description replaces this paragraph once confirmed.] A youth NGO, socio-cultural centre, youth service, cooperative or Local Action Group based in Corsica, with documented current '
  'work with young people aged 14–17, reaching those who live in inland or rural communes rather than only in Ajaccio or Bastia, and anchored in a community where the Corsican language is part of daily life.', count=False)
P('**Why this partner is necessary and not decorative.** Around 11,000 young people aged 16–29 in Corsica are neither in employment nor in education or training — close to one in four of that age group — and the '
  'island records a higher share of inactive, unschooled and unemployed young people than the French national average. Access to mainland non-formal education is conditioned by the cost and the length of the journey: '
  'for a teenager from an inland commune, a learning activity in Marseille is effectively out of reach. And part of community communication happens in Corsican, on small local channels that no national fact-checker '
  'covers — which means false information circulating in that language almost never meets a correction.', count=False)
P('**Role and deliverables.** Sending organisation; thematic lead on Day 2 for the strand on how disinformation circulates in minority-language communities and small local media ecosystems; contributor to Day 5; one '
  'group leader who observes a mixed team on Day 4. Delivers: a local needs note with its own consultation data; five to eight documented cases of disinformation from its own community (month 4); recruitment and '
  'preparation of the French group; one local initiative in Corsica (by month 13); the French translation of the toolkit.', count=False)

H2('Partner — [TO CONFIRM], inner Sardinia (Italy)')
P('**Profile.** [The partner’s own description replaces this paragraph once confirmed.] A youth association, social cooperative or Local Action Group in inner Sardinia, working with young people aged 14–17 from small '
  'localities affected by depopulation, open to the Sardinian language and culture.', count=False)
P('**Why this partner is necessary.** 17.8% of young people aged 15–29 in Sardinia are not in employment, education or training, against an Italian average of 15.2% and a European average of around 11%. The inner '
  'areas of the island are among the Italian territories with the sharpest demographic decline: young people emigrate, birth rates fall, and the educational and cultural offer contracts along with the population — so '
  'non-formal learning opportunities become rarest exactly where young people have fewest alternatives. As in Corsica and in our own territory, part of community life is carried in a language of its own, on small '
  'local channels.', count=False)
P('**Role and deliverables.** Sending organisation; thematic lead for the preparation and moderation of Day 5, the community dialogue day, and for the methodology of the local initiatives; one group leader who '
  'observes a mixed team on Day 4. Delivers: a local needs note with its own consultation data; five to eight documented local cases (month 4); the local initiative model and its evaluation grid (month 5); '
  'recruitment and preparation of the Italian group; one local initiative in Sardinia (by month 13); the Italian translation of the toolkit.', count=False)
PAGEBREAK()

# =====================================================================
H1('Project rationale')
H2('Needs and objectives')

Q('Why do you want to carry out this project? Please describe the issues and needs you want to address and your project’s objectives.')
P('**The need, in one sentence.** Young people aged 14–17 in the Napoca Porolissum LAG territory and in the peripheral partner communities of Corsica, Sardinia and the İstanbul periphery consume digital content and '
  'use AI tools every day, but have not acquired the habit of checking the source, the author, the date and the context of a piece of information before believing it and passing it on.')
P('**How we know: our own data.** Between spring and summer 2026 we ran a bilingual Romanian/Hungarian survey among young people in our territory and received 153 responses from 12 of our 14 localities. Ninety-six '
  'respondents are aged 14–17, exactly the target group of this project. Of those 96: 96.9% already use AI tools (45.8% often, 51.0% occasionally); 20.8% rate their own digital competence as low, with a group mean of '
  '3.25 out of 5; 31.3% have never taken part in any non-formal education activity; 37.5% name lack of information as the first barrier to joining a mobility, 34.4% cost and 31.2% transport; they hear about '
  'opportunities from school (50.0%), social media (49.0%) and friends (38.5%), and from the municipality only 6.2% of the time; 68.1% say they learn through practical activities against 29.8% through a course; 58.5% '
  'want activities organised in or near their own locality; and 85.4% would take part in an Erasmus+ activity organised by the LAG.')
P('Two of those figures, read together, are the whole problem. Almost every young person in our territory already uses AI, and almost half of them build their picture of the world from social media — while rating '
  'their own digital competence at barely above the midpoint. Use is universal; competence has not followed it.')
P('**How we know: the same need in the other three communities.** All four partners run the same short consultation before submission — a ten-question instrument built from our own survey, translated locally, with at '
  'least 20–25 young people aged 14–17 from the partner’s own community, plus a short focus group where numbers are small. Each partner delivers a one-page needs note with the method, the number and profile of the '
  'young people consulted, and the three main findings. [TO CONFIRM: YOBBA’s findings; the two island partners’ findings once they are confirmed.]')
P('**How we know: European data.** The Flash Eurobarometer “Youth Survey 2024” (EP013EP), carried out by Ipsos for the European Parliament among 25,863 respondents aged 16–30 across all 27 Member States, fieldwork '
  '25 September – 3 October 2024, found that more than three quarters of young Europeans believe they were exposed to disinformation in the previous seven days, while 70% feel confident they can recognise it. '
  'Confidence outruns competence. Young people in rural areas are less confident (68%) than those in large cities (73%). And Romania records the highest share in the Union of young people saying they encountered no '
  'disinformation at all in the past week — 19%, against 1% in Cyprus — while 31% of Romanian respondents declare themselves very confident. Romanian young people are simultaneously the least likely in Europe to '
  'notice disinformation and among the most certain they would recognise it.')
P('**What follows for the design.** If the problem were a lack of confidence, the answer would be encouragement. Because the problem is untrained confidence, the answer is a controlled experience of being wrong. '
  'Day 1 therefore starts with participants mapping their own media diet rather than with a presentation. On Day 2 the false material is judged before the verdict is revealed. And this is why the project needs a '
  'genuinely international group and cannot be run at home: a stereotype is at its least defensible when a young person from the community it targets is sitting in the room.')
P('**Why these four communities.** They do not look alike, and we are not going to pretend they do. A mountain commune in the Apuseni, a district on the edge of İstanbul, a village in inland Corsica and a small town '
  'in inner Sardinia have different histories, languages, economies and problems. What their young people have in common is narrower and more exact. Information reaches them through channels nobody corrects — '
  'Hungarian in part of our territory, which is why our survey had to be bilingual; Corsican; Sardinian; neighbourhood and community networks in the İstanbul periphery — and national fact-checkers work in the '
  'majority language on subjects of national interest. The practical media-literacy offer that exists elsewhere does not reach them: not one of the four communities has a standing activity where a fifteen-year-old '
  'can be taught, hands on, how to check an image or a source. And getting to any international activity is harder and more expensive from where they live. That overlap is what the project works on, and it is why a '
  'young person from each of the four recognises the other three within an hour of meeting them.')
P('**Objectives.** **O1:** by 30 September 2028, at least 16 of the 20 participants improve their score on the 15-item, 30-point practical verification test by at least 30% against their own May 2027 baseline, same '
  'instrument and same formula at both ends. **O2:** by 15 August 2027, at least 16 of the 20 demonstrate all four verification techniques at full marks each, in the structured observation grid applied during session '
  'D4.1 by six calibrated observers, with 25% of participants double-scored independently. **O3:** between September 2027 and June 2028, the 20 participants reach at least 80 other young people through four local '
  'initiatives, and at least 70% of those reached pass the ten-minute exercise — naming two distinct checks, carrying one out, and drawing a conclusion that follows.')
COUNT(6000)

Q('How does your project link to the objectives of the Erasmus programme and those of Youth Exchanges?')
P('**Digital transformation — the substance, not the label.** VERIFAI builds the part of digital competence that use alone never produces. Our participants can already operate the tools; what they cannot do is find '
  'out where something came from. The project develops three things, in this order: using digital tools and AI tools responsibly and with their limits understood; checking sources — who published it, who wrote it, '
  'when, in what original context, and whether any independent source says the same; and recognising false, manipulated or artificially generated content, including content they could produce themselves. That is the '
  'priority and it is also the whole project — it defines the need, the participant profile, every method in the agenda, the four media products, the toolkit and the two instruments that measure whether it worked. It '
  'also matches what the National Agency has said it is looking for in 2026: among projects addressing digital transformation, priority goes to those that tackle disinformation and promote digital literacy.')
P('**Participation in democratic life, common values and civic engagement.** Checking a claim is a precondition of taking part: without it, a vote, a public argument or a civic initiative rests on false premises. Our '
  'participants are 14 to 17 now, which means most of them will cast their first ballot within four to six years of this project. The point is that by the time they get there, forming an opinion on information they '
  'have actually checked is a habit rather than an effort. In the meantime they practise the civic half of it for real: through the four local initiatives they step out of the learning room and into their own '
  'communities, working with youth organisations, libraries, community centres and local authorities, and taking responsibility for an activity that other young people attend.')
P('**Inclusion and diversity.** The barriers our participants face are concrete, and each is answered by a concrete measure: geographic — the exchange is hosted inside our own territory and transport is paid from '
  'each participant’s own front door; economic — no participation fee of any kind, stated in writing from the day the call is published; linguistic — English is not a selection criterion and A2 is accepted, with a '
  'glossary built in five languages; social and educational — four months of preparation rather than four weeks, a parents’ meeting in each country before consents are signed, and the stated right to leave a session '
  'without giving a reason. At least 12 of the 20 participants face documented barriers and at least 15 travel on a European mobility for the first time. The measures are set out in full under Participants with '
  'fewer opportunities.')
P('**Objectives of the Action.** Youth Exchanges exist to encourage intercultural dialogue and learning and a sense of being European, to develop young people’s competences and attitudes, to strengthen European '
  'values and break down prejudice and stereotypes, and to raise awareness of socially relevant subjects. VERIFAI addresses each of these directly, and the third structurally: the working material of Day 2 includes '
  'real content that feeds ethnic, gender and migration stereotypes, analysed in mixed teams in which young people from the targeted communities are present.')
P('**EU Youth Strategy and the European Youth Goals.** The project addresses Goal 4, //Information and Constructive Dialogue//, which is its very object; Goal 6, //Moving Rural Youth Forward//, since the activity '
  'takes place in a rural mountain territory and the multiplication happens in the participants’ own localities; and Goal 9, //Space and Participation for All//, since participants co-design the programme, choose the '
  'subjects to be verified and lead their own local initiatives. Within the “Connecting” field of action it creates exactly the link the Strategy looks for: young people from four European peripheries discovering '
  'that they have the same problem, and working on it together.')
P('**Common EU values.** Disinformation attacks human dignity through dehumanising content, equality through algorithmically amplified stereotypes, and the rule of law by eroding trust in institutions. Three concrete '
  'anchors rather than a declaration: the ground rule of the exchange is that any claim made in debate must be verifiable, and it applies to facilitators exactly as to participants; the group agreement negotiated by '
  'the participants on Day 1 includes non-discrimination and respect for every language and identity present — Romanian, Hungarian, Turkish, Corsican, Sardinian, Italian, French; and the analysis of stereotype-bearing '
  'content is deliberately done in the presence of the people it targets.')
COUNT()

H2('Impact')
Q('How will your project benefit the young participants involved in the project, during and after the project lifetime?')
P('**A competence they did not have, measured rather than asserted.** Every participant takes the same 15-item practical verification test in month 2 and its equivalent in month 18, and the target is a 30% '
  'improvement for at least 16 of the 20. During the mobility an observation grid records whether each participant actually performs four named techniques in the Day 4 simulation — not whether they can describe them. '
  'That distinction matters here more than it would elsewhere, because our starting point is a group that already believes it can spot a fake.')
P('**A first European experience, for most of them.** At least 15 of the 20 will be taking part in a European mobility for the first time, and in our territory 31.3% of young people aged 14–17 have never taken part '
  'in any non-formal education activity at all. For those participants the gain is not only thematic: working in a mixed international team, in English, with people they have never met, is itself the learning. It is '
  'also what they asked for — 60.4% of the 14–17 group named foreign languages and intercultural communication as what they most want out of a European mobility.')
P('**Something to do afterwards.** The project does not end when they get off the bus. Each participant leaves the mobility with a written commitment and a role in one of the four local initiatives, which they design '
  'and lead themselves, with the group leader supporting rather than directing. This is where a fifteen-year-old moves from “I learned something” to “I taught twenty people”, and in our experience it is the part that '
  'changes how they see themselves.')
P('**Learning they can name, document and use.** Youthpass is worked on from Day 1 through a learning diary and daily reflection groups — in the national group and in the participant’s own language first, then in '
  'plenary — and closed on Day 7 in a dedicated session. The value is in the process, not the paper: it teaches a sixteen-year-old to identify what they actually learned, to document it with evidence they can point '
  'to, and to present it in a form someone else understands. That is a transferable skill in itself, and it is what makes the certificate usable afterwards — in the next learning activity they join, in volunteering, '
  'in a civic initiative in their own community, and in the next international mobility they apply for.')
P('**Six months later.** A follow-up questionnaire in month 12 asks what they still use. The honest expectation is not that all twenty become fact-checkers. It is that they have acquired a reflex — the pause before '
  'sharing — and that the four local initiatives have given at least some of them a taste for organising something in their own community.')
COUNT()

Q('How will your project benefit the organisations or the groups of young people implementing the project, during and after the project lifetime?')
P('**For the coordinator.** LAG Napoca Porolissum has run youth projects as partner and as coordinator, but this is its first project as hosting organisation for a youth exchange. That is a deliberate step in the '
  'organisation’s development. Hosting means owning the learning programme, the venue, the safety of twenty minors and the relationship with the host community, and it converts a network of 43 partners and 14 '
  'municipalities from a rural-development asset into a youth-work asset. The organisation ends the project with a tested non-formal learning programme, three measurement instruments it did not have, and a child '
  'protection policy that will apply to everything it does afterwards.')
P('**For YOBBA.** The partner brings production expertise and gains the verification methodology it currently lacks. For an organisation whose core business is training young people to make digital content, and whose '
  'platform reaches around 250,000 followers, acquiring a structured approach to source verification changes what it can responsibly teach. YOBBA takes the toolkit into its own volunteer programme of more than 150 '
  'young people a year.')
P('**For the two island partners.** Both are expected to be newcomers to this Action or less experienced in it. They gain a first structured experience of KA152 alongside a coordinator that carries the administrative '
  'and financial load, a method adapted to communities that have a language of their own, and a documented local initiative they can show to their own municipalities and funders. [TO CONFIRM once the partners are known.]')
P('**For all four.** The partnership produces something none of them has separately: an evidenced answer to a problem all four communities share, in a form other peripheral territories can pick up. In month 17 the '
  'four organisations formally assess whether to continue — either with a second exchange hosted by another partner, or with a youth participation project focused on dialogue with local decision-makers. The decision '
  'is minuted either way, including if it is not to continue.')
COUNT()

Q('What would be the impact of your project beyond the participants and participating organisations, at local, regional, national, if any European level?')
P('**Local.** At least 80 young people reached directly through the four local initiatives, hosted in youth centres, libraries, community centres, the partner organisations’ own spaces and other accessible public '
  'places. In Romania, the results are also presented across the 14 localities of the LAG territory through the community events the organisation already runs every year, so that young people who did not take part '
  'still meet the material, and so that the four media products circulate where the myths they debunk actually circulate.')
P('**Regional.** The “Digital Detectives” toolkit is offered free of charge to the youth organisations, libraries and community centres of the territory, with a presentation session for the youth workers and '
  'librarians who will use it. The 14 partner municipalities receive the evaluation report and a short set of recommendations. Romania has no coordinated national media-literacy strategy and its policies in this area '
  'are fragmented across separate legal frameworks; in that context, a tested, free, ready-to-use set of materials in the hands of people who already work with rural young people has a value out of proportion to the '
  'size of this project.')
P('**National and European.** Results are published on the Erasmus+ Project Results Platform. YOBBA disseminates through the ErasmusPlus Türkiye platform. The coordinator shares the method through the LEADER and '
  'ELARD networks, where it already has transnational cooperation experience — a channel that reaches Local Action Groups across rural Europe, an audience that rarely encounters media-literacy tools at all. The '
  'target is at least four organisations outside the partnership confirming in writing that they use the toolkit.')
P('**What we do not claim.** Twenty participants will not move a county-level statistic. The contribution is stated as it is: measurable change in twenty young people, documented extension to at least eighty more, '
  'and instruments that stay in use in four organisations after the project ends.')
COUNT()

H2('Topic')
Q('Please select up to three topics addressed by your project')
BUL(['Digital skills and competences', 'Critical thinking and media literacy', 'Youth participation and civic engagement'], count=False)
SMALL('Closed dropdown — pick the closest available equivalents from the live list. If a topic mentions disinformation explicitly, take it: it is the national priority for 2026.')
PAGEBREAK()

# =====================================================================
H1('Project details')
H3('Activity list')
TBL([
 ['Id.', 'Activity Type', 'Activity Title', 'No. of participants', 'No. of persons', 'Total grant (EUR)'],
 ['01', 'Youth exchanges', 'VERIFAI: Young Detectives Against Digital Disinformation', '20', '26', '26,827.00'],
 ['', '', '**Total**', '**20**', '**26**', '**26,827.00**'],
], widths=[1.2, 2.6, 6.0, 2.4, 2.0, 2.4], count=False)

H3('Participant contribution and fees')
Q('Are you planning to ask for any contributions from participants?')
P('**No.** This is a decision, not an omission. In our survey, cost is the second barrier young people aged 14–17 name to taking part in a mobility (34.4%) and transport is the third (31.2%). A fee of any size would '
  'filter out precisely the young people this project exists for, and a family deciding whether to let a fourteen-year-old leave the country for nine days should not also be deciding whether they can afford it. Since '
  'at least 12 of our 20 participants are participants with fewer opportunities, from whom the Programme does not permit fees in any case, a fee would also have to be charged to some participants and not others — '
  'inside a group of twenty who spend nine days together. The rule is therefore written into the local call in all four countries from the day it is published: travel, accommodation, meals, insurance, materials and '
  'transport from the participant’s own front door are covered in full, and nothing is asked of the participant or the family at any point.')
COUNT(2000)

H2('Activity 01 — description')
TBL([
 ['Field', 'Entry', 'Field', 'Entry'],
 ['Id.', '01', 'Total no. of participants', '20'],
 ['Activity Type', 'Youth exchanges', 'Of which, with fewer opportunities', '12'],
 ['Activity Title', 'VERIFAI: Young Detectives Against Digital Disinformation', 'No. of group leaders', '4'],
 ['Start date', '09/08/2027', 'No. of facilitators', '2'],
 ['End date', '15/08/2027', 'No. of accompanying persons', '0'],
 ['Duration excluding travel', '7 days', 'Total no. of persons', '26'],
 ['Travel days', '08/08/2027 arrival\n16/08/2027 departure', 'Total Activity grant', '**26,827.00 EUR**'],
], widths=[3.6, 4.7, 3.6, 4.7], count=False)

H3('Flows summary (Activity 01)')
TBL([
 ['Flow', 'Place of origin', 'Participants', 'Group leaders', 'Facilitators', 'Persons', 'Fewer opport.', 'Distance band', 'Travel', 'Days'],
 ['1', 'Cluj County, Romania\n[TO CONFIRM: city]', '5', '1', '1', '**7**', '3', '10–99 km', 'Green', '9'],
 ['2', 'İstanbul, Türkiye', '5', '1', '1', '**7**', '3', '500–1,999 km', 'Green', '11'],
 ['3', 'Corsica, France\n[TO CONFIRM: city]', '5', '1', '—', '**6**', '3', '500–1,999 km', 'Green', '11'],
 ['4', 'Sardinia, Italy\n[TO CONFIRM: city]', '5', '1', '—', '**6**', '3', '500–1,999 km', 'Green', '11'],
 ['', '**Total**', '**20**', '**4**', '**2**', '**26**', '**12**', '', '', ''],
], widths=[0.9, 3.1, 1.6, 1.5, 1.5, 1.3, 1.5, 1.9, 1.3, 1.0], small=True, count=False)
SMALL('City of venue for all four flows: the accommodation unit in the Napoca Porolissum LAG territory, Apuseni Mountains, Cluj County, Romania [TO CONFIRM]. Start 09/08/2027 and end 15/08/2027 for all four. '
      '“Days” counts the 7 activity days plus 2 travel days, and for flows 2–4 the 2 additional days that green travel over that distance makes eligible. The four groups are split into separate flows because they sit '
      'in two distance bands and two durations — which is what the form’s own definition of a flow requires.')

H3('Budget per flow and activity budget summary')
TBL([
 ['Flow', 'Travel', 'Individual support', 'Flow total'],
 ['1 — Romania (7 persons)', '7 × 56 = 392.00', '7 × 9 × 46 = 2,898.00', '3,290.00'],
 ['2 — Türkiye (7 persons)', '7 × 417 = 2,919.00', '7 × 11 × 46 = 3,542.00', '6,461.00'],
 ['3 — France / Corsica (6 persons)', '6 × 417 = 2,502.00', '6 × 11 × 46 = 3,036.00', '5,538.00'],
 ['4 — Italy / Sardinia (6 persons)', '6 × 417 = 2,502.00', '6 × 11 × 46 = 3,036.00', '5,538.00'],
 ['**Subtotal, flows**', '**8,315.00**', '**12,512.00**', '**20,827.00**'],
 ['Organisational support', '', '125 × 20', '2,500.00'],
 ['Inclusion support for organisations', '', '125 × 12', '1,500.00'],
 ['Inclusion support for participants', '', 'real costs, separate lines', '2,000.00'],
 ['**Total Activity grant**', '', '', '**26,827.00**'],
], widths=[5.6, 3.6, 3.8, 3.6], count=False)
SMALL('The preparatory visit (4,760.00 EUR) sits at project level, not inside the activity, which is why the project total is 31,587.00 and the activity grant 26,827.00.')
PAGEBREAK()

Q('Please describe the background of the participants in each participating group and how each group was formed. Please also provide information on the group leaders, the age of the participants and how country balance is ensured. If necessary, explain how the gender balance is respected.')
P('**Romania — LAG Napoca Porolissum, 5 young people aged 14–17 plus 1 group leader.** Young people from the rural mountain communes of the LAG territory — Săcuieu, Gilău, Huedin, Mărișel, Căpușu Mare, Mărgău, '
  'Măguri-Răcătău, Călățele, Beliș, Mănăstireni, Aghireșu, Izvorul Crișului — communities with a thin offer of youth activities and with information circulating in two languages, Romanian and Hungarian. From our '
  'survey of this exact population: 96.9% already use AI tools, 20.8% rate their digital competence as low, 31.3% have never taken part in a non-formal activity, and lack of information is the first barrier they '
  'name. The group is deliberately built to be linguistically mixed, with at least one Hungarian-speaking participant, because the language question is part of the subject matter.')
P('**Türkiye — YOBBA, 5 young people aged 14–17 plus 1 group leader.** Young people from Küçükçekmece and the surrounding İstanbul periphery, a dense and diverse district that includes families with migrant and '
  'refugee backgrounds, where information travels through neighbourhood, family and community networks that national fact-checking never reaches. YOBBA recruits from its volunteer community of over 150 young people '
  'a year, prioritising those who have never taken part in an international activity. [TO CONFIRM: YOBBA’s consultation data.]')
P('**France — [Corsica partner], 5 young people aged 14–17 plus 1 group leader.** Young people from inland and rural communes of Corsica, with limited access to the mainland non-formal education offer because of the '
  'cost and the length of the journey, and living in communities where part of daily communication happens in Corsican, on small local channels with no fact-checking coverage. Around one in four young people aged '
  '16–29 on the island is neither in employment nor in education or training. [TO CONFIRM: partner data and localities.]')
P('**Italy — [Sardinia partner], 5 young people aged 14–17 plus 1 group leader.** Young people from small localities of inner Sardinia affected by depopulation, where the educational and cultural offer contracts as '
  'the population falls. 17.8% of young people aged 15–29 in Sardinia are not in employment, education or training, against 15.2% nationally and around 11% across Europe. [TO CONFIRM: partner data and localities.]')
P('**How the groups are formed.** All four partners use one common recruitment backbone, published simultaneously in month 1 with the same criteria translated into four languages. Target: at least 60 applications '
  'for the 20 places. Selection is by a commission of at least two people per organisation, on a written form plus a short conversation, with the outcome and the reasons communicated to every candidate. The published '
  'criteria are identical across the four countries: age 14–17 at the start date (eliminatory); motivation to work on information verification and willingness to run a local initiative afterwards (30%); first '
  'participation in a European mobility or any non-formal activity (25%, target at least 15 of 20); a situation limiting access to opportunities, declared voluntarily and confidentially (25%, target at least 12 of '
  '20); and gender and locality balance within the national group (20%).')
P('**English is not a selection criterion** and A2 is accepted: the programme is built on visual and practical methods, pair work and linguistic support from the group leaders, precisely so that language does not '
  'become a social filter. A language test at the door would convert the 12.5% who name lack of self-confidence as a barrier into exclusion.')
P('**Age.** All twenty participants are aged 14 to 17 at the start date. The band is deliberately tight, for three reasons that point the same way. They share the same need — the survey evidence behind this project '
  'describes exactly this age group. They are at a similar stage of development, so one register of language and one set of expectations about autonomy works for the whole room instead of two. And it lets us use one '
  'coherent set of non-formal methods — visual, practical, game-based, built on small mixed teams and peer teaching — that genuinely fits all of them. A band crossing into legal adulthood would also put minors and '
  'adults in the same accommodation and the same group dynamic, which is a safeguarding problem before it is a learning one.')
P('**Country and gender balance.** Country balance is exact: five participants and one group leader from each of the four countries, so no national group can dominate the dynamic, and every mixed team of five has one '
  'member from each country. Gender balance is a binding rule at group level, not an aspiration at project level: each national group must include at least 40% of each gender — in a group of five, at least two — and '
  'the team of four group leaders is itself gender-balanced. Participants who do not identify within that binary are counted according to their own declaration and are not required to declare anything. The rule is '
  'checked twice, at selection and at final confirmation, by the activity coordinator.')
P('**Group leaders.** Each national group has one group leader aged 18 or over, experienced in youth work and in accompanying minors, who travels with the group and stays with it throughout, including at night. Group '
  'leaders are responsible for safeguarding and wellbeing, for the daily reflection in the national group in its own language, for attendance and the code of conduct, for observing one mixed team on Day 4, and '
  'afterwards for supporting their group’s local initiative. Confirmed: Livia Golovatic (Romania) and Aysu Zeybel (Türkiye), who has completed a ten-month European Solidarity Corps placement working weekly with '
  'children in Romania. [TO CONFIRM: group leaders for Corsica and Sardinia.] All four take part in a two-day online leaders’ briefing in month 4 covering safeguarding, the escalation chain, facilitating '
  'reflection, and the calibrated use of the observation grid.')
COUNT(6000)

Q('Please describe the role and involvement of the participants from each participating group in all phases (planning before, during and follow-up).')
P('**Where this project came from.** The subject was not chosen by the coordinator’s staff. It came from 153 young people in the territory who answered our survey, and it was then put back to them for checking. Three '
  'things in this application exist because they asked for them. They told us where to hold it: 58.5% asked for learning activities in or near their own locality, so the exchange is hosted inside the LAG territory '
  'rather than in a comfortable host city, and the host community became part of the programme on Day 5 instead of being scenery. They told us what stops them: cost and transport are the second and third barriers they '
  'name, so there is no participation fee of any kind and transport is paid from each participant’s own front door. And they told us how they learn: 68.1% through practical activities against 29.8% through a course, '
  'so there are no lectures in this programme and every session produces an output or a decision taken by the participants themselves. A validation meeting with 8–10 young people from the territory, held before '
  'submission, confirms the wording of the need, reviews the objectives in plain language, and produces the first list of the claims and rumours they want checked — a list that becomes the working material of Day 2.')
P('**Planning, months 1–4.** Once selected, participants do not simply wait for August. Four online sessions of 90 minutes each bring the four groups together in mixed national composition, not country by country. '
  'Session 1: meeting each other and negotiating the first draft of the group agreement. Session 2: participants choose the local disinformation cases that will be analysed during the mobility — each group brings '
  'five to eight documented real cases from its own community, and the participants themselves decide which ones make the working set. Session 3: distribution of roles for the mobility — photo and video '
  'documentation, activity diary, energisers, mediation, contact with the host community, timekeeping — and preparation of the intercultural evening. Session 4: safety, digital rules, practical arrangements, and '
  'questions answered live by the group leaders. Between sessions a moderated communication group keeps the cohort in contact. A separate online meeting is held with the parents, in each country and in its own language.')
P('**During the mobility.** Every day has a host team of the day: a mixed team of four participants, one from each country, who open the day, keep the timing, run the energisers and close the day. Teams are '
  'recomposed daily so that every participant works with every nationality at least once. The daily reflection groups — first in the national group and in the participant’s own language, then in plenary — feed '
  'directly into adjusting the next day’s programme, and the adjustments are made visibly, so participants see their feedback change something rather than disappear into a form. On Day 6 the participants plan their '
  'own local initiatives: date, venue, audience, partners, who does what.')
P('**Follow-up, months 6–18.** The four local initiatives are designed and led by the participants, with the group leader in a support role rather than a coordinating one. Each initiative reaches at least 20 young '
  'people and is hosted in a youth centre, a library, a community centre, the partner organisation’s own space or another accessible public place in the participants’ own community. In month 17 the participants take '
  'part in a participatory evaluation session that feeds the final report — so they close the project as evaluators rather than as beneficiaries. The cohort communication group stays open throughout, and all four '
  'organisations involve the twenty as peer trainers in their later activities.')
COUNT(6000)

Q('What will the participants learn about the chosen topic of the activity? Which learning outcomes or competences will be developed?')
P('The learning outcomes are expressed against the eight European key competences for lifelong learning, the framework Youthpass uses, and each is tied to the sessions that build it and to the evidence that documents '
  'it. The rule is strict in both directions: no session exists in the programme without an entry here, and no competence is claimed without a session and a piece of evidence behind it.')
TBL([
 ['Key competence', 'What the participant will be able to do', 'Sessions', 'Evidence'],
 ['**KC4 Digital** //primary//',
  'Identify the source and the author of an online item; check its date and its original context; run a reverse image search; compare a claim against at least two independent sources; recognise the indicators of '
  'AI-generated text, image, audio and video; use AI tools in their own production ethically and with attribution.',
  'D1.3, D2.1, D2.2, D3.1, D3.2, D3.3, D4.1, D4.2, D6.1',
  'Baseline and final practical test; Day 4 observation grid on four named techniques; the AI-recognition sheet; the four media products.'],
 ['**KC1 Literacy** //primary//',
  'Distinguish fact from opinion and from inference in a text; identify emotional framing, cropped context and false authority; construct a documented verdict in writing that another person can follow and check.',
  'D2.1, D2.2, D2.3, D4.1, D4.2, D4.3',
  'The manipulation-techniques grid produced by the participants; four written verdicts with their sources.'],
 ['**KC6 Citizenship** //primary//',
  'Explain why verification is a precondition of democratic participation; argue a position with evidence and accept being refuted by evidence; take part in dialogue with community members and local institutions; '
  'design and run an activity that serves their own community.',
  'D1.2, D2.3, D5.1, D5.2, D6.3, D7.1',
  'The group agreement; the Day 5 record of local rumours; the four local initiative plans and the initiatives themselves.'],
 ['**KC5 Personal, social, learning to learn** //primary//',
  'Assess their own media habits and name their own weak points; recognise that they were wrong about a claim and say so; work in a mixed international team; set a learning target and evaluate their progress against it.',
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
  'D6.3 and the four local initiatives, months 6–15',
  'The four initiative plans with owners and deadlines; the reports on the initiatives held.'],
 ['**KC3 Mathematical, science and technology** //secondary//',
  'Read a statistic critically: check the population measured, the year, the sample and what the figure does not say; recognise a graph designed to mislead.',
  'D2.1, D4.1',
  'The statistics exercise inside D2.1; the verdicts, where numerical claims appear.'],
], widths=[3.0, 6.6, 3.0, 4.0], small=True)
P('**What we do not claim.** Seven days do not produce expert fact-checkers. What they produce is a reflex — the pause before sharing — and four techniques the participant can actually perform, which is what '
  'objective O2 measures and what the observation grid records.')
COUNT(6000)

Q('What are the basic elements of the activity? Please describe at the very least the venue(s), non-formal learning methods and the daily programme.')
P('**Venue.** An accommodation unit inside the Napoca Porolissum LAG territory, in the Apuseni Mountains, Cluj County — not a neutral host city: 58.5% of the young people we surveyed asked for activities in or '
  'near their own locality, and the host community is itself part of the programme on Day 5. Requirements: capacity for at least 30 people, a plenary room, four separate spaces for small-team work, stable '
  'internet, accessibility. [TO CONFIRM: the unit, with a written offer.]')
P('**Non-formal learning methods.** Learning through controlled error is the central method: participants receive the false material, commit to a judgement, and only then learn the verdict — the surprise is the '
  'instrument that works on overconfidence, and it is used on Day 2 before any teaching. Around it: mixed international teams recomposed daily; simulation and role play (the verification newsroom D4.1, the '
  'information tribunal D2.3, the escape room D3.3); structured debate under the rule that every claim must be evidenced, facilitators included; peer-to-peer teaching (D3.2); media production as applied learning '
  'on Day 6; daily reflection in the national group in the participant’s own language, then in plenary, with an individual learning diary, and what comes out of it visibly changes the next day (D1.5, D2.4, D3.5, '
  'D4.4, D6.4); and outdoor activities in the territory. There are no lectures: every session produces an output or a decision taken by the participants — 68.1% of the young people we surveyed learn through practical activities, 29.8% through a course.')
P('**Daily programme.** Travel days 8 and 16 August. Day 0 carries arrival, accommodation and a guided safety tour with an evacuation drill (D0.1).')
P('**Day 1 — who we are and what we consume.** O1, O2. The group forms itself and looks at its own habits before anyone teaches: mixed-team formation (D1.1), the group agreement the participants negotiate '
  'themselves, with non-discrimination and respect for all languages present as non-negotiable clauses (D1.2), “My Digital Map”, in which each participant maps one ordinary day of their own media diet (D1.3), and the '
  'safety, safeguarding and Youthpass briefing (D1.4). Outputs: four mixed teams, a signed group agreement, 20 digital maps kept for Day 7. Claudiu Iancu and Marilena Georgescu with Facilitator 1.')
P('**Day 2 — Spot the Fake.** O1, O2. The controlled-error day: teams commit to a verdict on a mixed set of real and false items, including two misleading statistics and a manipulated graph, before the answer key is '
  'revealed (D2.1); then the mechanics of manipulation — emotional headlines, cropped context, false authority, numbers out of context — worked on the real cases their own communities brought, including content '
  'carrying ethnic, gender and migration stereotypes (D2.2); and a debate on where opinion ends and falsehood begins (D2.3). Output: the manipulation-techniques grid in five languages. Claudiu Iancu '
  'with Facilitators 1 and 2; the Corsican partner leads the minority-language strand.')
P('**Day 3 — AI or human?** O1, O2. Participants generate AI content themselves and try to fool each other, then write their own recognition sheet (D3.1); four teams each test a free verification tool and teach it '
  'to the others (D3.2); the verification route is drilled as an escape room until automatic (D3.3); the group writes the AI-use rule it will apply on Day 6 (D3.4). Outputs: the AI-recognition sheet, an annotated '
  'tool list with one national resource per country, the group’s AI-use rule. Doğan Can Karabudak (YOBBA) with Claudiu Iancu and Livia Golovatic.')
P('**Day 4 — fact-checkers for a day. The assessed day.** O2. A three-hour verification newsroom in which mixed teams take real viral claims through the full route to a documented verdict, facilitators '
  'intervening only when asked (D4.1). This is where the observation grid for O2 is applied: each group leader observes one mixed team, Facilitators 1 and '
  '2 independently double-score five participants each, the Learning Programme Coordinator moderates without scoring. Then cross-examination of each verdict (D4.2) and a collective analysis of the day’s errors, '
  'the facilitators’ included (D4.3). Outputs: four documented verdicts with sources, and per-participant data on all four techniques.')
P('**Day 5 — community and intercultural day.** O3. A visit to a village of the territory (D5.1) and a facilitated dialogue with residents and municipal representatives about the rumours that circulate '
  'there, through which channels and who gets hurt (D5.2) — that record becomes the working material for Day 6. The intercultural evening closes the day (D5.3). Method led by the Sardinian partner.')
P('**Day 6 — Make It, Don’t Fake It.** O3. Led by YOBBA: how a short video or infographic is built to be clear and honest (D6.1), then production, each team debunking a Day 5 myth under the AI-use rule the '
  'group wrote on Day 3 (D6.2). In parallel the national groups plan their local initiatives on a common template — date, venue, audience, partner, responsibilities, indicator (D6.3). Outputs: four media products '
  'in English plus a local language, four initiative plans with named owners and deadlines.')
P('**Day 7 — presentation, evaluation, Youthpass.** O1, O2, O3. A public presentation by the participants to guests from the community, the municipalities and the press (D7.1); the Youthpass session, where each '
  'participant re-reads their Day 1 digital map against their learning diary and names, with evidence, what changed (D7.2); a participatory evaluation (D7.3); and the written, public commitments to the four local '
  'initiatives (D7.4). Outputs: 20 Youthpass certificates plus 4 for the group leaders, four signed commitments with dates.')
P('The full programme is annexed as the project timetable, where every session carries five attributes: the objective it serves, the non-formal method, the key competences it builds, the output it produces and '
  'the person responsible. The session codes above match the competence matrix and the timetable exactly.')
COUNT(6000)

Q('How will the groups of participants cooperate and communicate between them to prepare and follow-up on the Youth Exchange?')
P('**Before.** Four joint online sessions of 90 minutes in months 3 and 4, in mixed national composition rather than country by country, so the teams that will work together in August have already met. A shared '
  'workspace holds the documents, the case files and the templates; a moderated messaging group, with clear rules and no sharing of personal data, keeps day-to-day contact going. Between sessions each group has a '
  'concrete deliverable for the others: five to eight documented cases of disinformation from its own community, uploaded to the shared space, which the whole cohort then reviews. The group leaders hold their own '
  'separate channel and a two-day online briefing.')
P('**During.** Mixed teams recomposed daily; the host team of the day; the daily reflection cycle running from the national group into the plenary; and a visible feedback loop, where changes requested one evening '
  'appear in the next day’s programme.')
P('**After.** The cohort communication group stays open for the whole 18 months and becomes the working space for the four local initiatives: each group posts its plan and the others comment before it happens. A '
  'joint online meeting is held after the first two initiatives, in month 10, so that the two groups that have not yet run theirs learn from what went wrong rather than repeating it. A follow-up questionnaire in month '
  '12 and a participatory evaluation session in month 17 close the cycle. The four media products and the toolkit circulate through all four organisations’ channels, and each group is expected to disseminate the '
  'other three groups’ products, not only its own.')
COUNT()
PAGEBREAK()

# =====================================================================
H1('Project design')
H2('Preparation, support and follow-up')

Q('How will you prepare the participants before the start of the activity (e.g. intercultural, linguistic, risk-prevention etc.) and how will you support them during and after the activity?')
P('**Before.** Preparation runs over four months, not four weeks, because 31.3% of the young people in our target population have never taken part in any non-formal education activity and 12.5% name lack of '
  'self-confidence as a barrier. For a fourteen-year-old leaving the country for the first time, the preparation is the inclusion measure.')
BUL([
 '**Baseline, month 2.** The 15-item practical verification test is taken by all 20 participants before any learning activity, with a short questionnaire on media habits. It establishes the starting value for O1 and tells the facilitators what the group actually cannot do — which is not always what they say they cannot do.',
 '**Four joint online sessions, months 3–4**, 90 minutes each, in mixed national teams: meeting each other and drafting the group agreement; choosing the local cases to be analysed; distributing roles and preparing the intercultural evening; safety, digital rules and practical arrangements.',
 '**Linguistic preparation.** A “detective’s glossary” of about 60 working terms in five languages, produced with the participants rather than handed to them, plus two light conversation sessions inside the online meetings. The aim is functional confidence, not language teaching: A2 is enough, and the programme is built so that it is.',
 '**Intercultural preparation.** Each group prepares a short presentation of its own community for the intercultural evening, including its language. Group leaders run a session on expectations and stereotypes before departure — deliberately, since the project itself works on stereotypes.',
 '**Risk prevention and safeguarding.** Each participant and each parent receives a participant pack: programme, house rules, code of conduct, contact chain, emergency numbers, the safeguarding focal point’s name and direct contact, and the media and consent rules. An online meeting is held with the parents, in each country in its own language, where questions are answered live.',
 '**Practical.** Parental consents, travel and medical insurance, medical information sheets, dietary and accessibility requirements, travel bookings. For the Turkish group the visa procedure starts in month 3.',
 '**Group leaders’ briefing, month 4:** two online half-days on safeguarding, the escalation chain, facilitating reflection, and the calibrated use of the observation grid across six different observers.',
 '**Inclusion support, prepared individually.** Where a participant needs support beyond the standard arrangements, it is identified here, in the preparation phase, costed on a separate line, and justified by what it makes possible — not requested as a lump sum and explained afterwards.',
])
P('**During.** Each national group stays with its own group leader throughout, including at night. The daily reflection happens first in the national group and in the participant’s own language, which is where a '
  'participant who is struggling is most likely to say so, and only then in plenary. The safeguarding focal point is present, is introduced in person on Day 1 and is available for individual conversations every day; '
  'she is deliberately not part of the facilitation team, so that a concern about a facilitator can be raised at all. A buddy system pairs participants across countries for language and social support. And any '
  'participant may leave a session without giving a reason — a rule stated on Day 1 and repeated before the sessions that work with distressing content.')
P('**After.** Support does not stop at the bus. The cohort communication group stays open for 18 months. Each participant leaves with a written commitment and a role in a local initiative, and the group leader '
  'supports them through it: the initiative is theirs to run, but they are not left alone to run it. A joint online meeting in month 10 lets the two groups that have already delivered pass on what they learned. A '
  'follow-up questionnaire in month 12 and the final test in month 18 close the loop, and the participatory evaluation session in month 17 brings the twenty back into the project as evaluators rather than beneficiaries.')
COUNT(6000)

Q('What measures will you put in place to ensure the safety and protection of participants?')
P('All twenty participants are minors. The measures below are specific, and they meet the requirements the National Call sets for the mobility of minors: adequate preparation before departure with the parents '
  'involved, and group leaders selected for their competence in working with minors and in preventing and handling conflict, bullying and abuse, who prepare alongside the young people and commit in writing to the rules.')
P('**Safety of the accommodation and of the activity spaces.** A written risk assessment of the venue before contracting, covering fire safety certification and evacuation routes; the state of electrical '
  'installations and heating; the security of doors, windows and balconies; lighting of outdoor areas; separation of participant accommodation from any unrelated guests; distance and travel time to the nearest medical '
  'facility and hospital; mobile signal coverage across the whole site; and the suitability of the outdoor spaces used. Verification on site during the preparatory visit in month 3, by the logistics officer with '
  'representatives of the sending organisations — the venue is not confirmed until it has been seen. An evacuation drill on Day 0, immediately after arrival, with the assembly point shown to every participant; the '
  'guided safety tour is a scheduled session (D0.1), not an informality. Room allocation by gender and by age, minors accommodated only with minors; the four group leaders sleep on the same floors as their groups; a '
  'night-duty rota so that at least one adult is awake and reachable at all times. Activity spaces checked daily by the logistics officer; a first-aid kit in the plenary room and one carried on every off-site '
  'activity; at least one member of the team holding a valid first-aid qualification [TO CONFIRM: who, and the certificate’s validity date]. For the off-site activity on Day 5: transport by a licensed carrier, a '
  'written route and timing, a headcount at every boarding, and one adult per group at all times.')
P('**Protection of participants.** A child protection policy of the coordinating organisation, signed by every adult involved — staff, facilitators, group leaders — and presented to the participants on Day 1 [TO '
  'CONFIRM: the policy must be adopted before submission]. A designated safeguarding focal point, Marilena Georgescu, outside the facilitation team, introduced in person on Day 1, whose contact details go to '
  'participants and parents before departure, with a named counterpart in each partner organisation. Written parental consents for participation, travel, emergency medical care and use of images, obtained before '
  'departure and notarised where national law requires it, as is expected for the Turkish group. A code of conduct negotiated with the participants themselves on Day 1 (D1.2) rather than imposed, including '
  'non-discrimination, respect for all languages present, and explicit rules on harassment and bullying. Insurance — health, accident and civil liability — for all 26 people for the whole travel period, arranged and '
  'verified centrally by the coordinator rather than left to each sending organisation. An emergency protocol: a 24/7 contact chain, the full list of parents’ contacts held by the coordinator and by each group '
  'leader, a designated reference medical facility identified during the preparatory visit, and an interpreter reachable for the Turkish and French groups. Every group leader signs the child protection policy and the '
  'house rules before departure and prepares alongside the young people of their own group. Digital protection and data: explicit consent for photographs and video; no publication of identifiable images of minors '
  'without consent; no personal data of third parties in the material produced; a two-step review before anything is published, with the safeguarding focal point approving; all data processed under the GDPR, stored '
  'in restricted folders and anonymised in the supporting file.')
P('**Protocol for sensitive content.** Working with real disinformation exposes participants to violent, discriminatory or distressing material — about war, health, migration. The measures are specific rather than '
  'reassuring. All working material is pre-screened by the facilitators and explicit content is excluded. Every analysis session ends with a short decompression sequence (D2.4). Participants have a stated right to '
  'leave a session without justifying it. And an adult outside the facilitation team is available for an individual conversation every day. These rules are announced on Day 1, together with the group agreement, and '
  'repeated before Day 2.')
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
  'is the point at which the competence becomes theirs. The toolkit is left with the youth workers, librarians and community educators who see them week to week, so the method does not leave with us. Youthpass gives '
  'them a way to name and evidence what they gained, so they can use it in whatever they apply for next — another learning activity, a volunteering placement, a civic initiative, another mobility. And the twenty '
  'continue as peer trainers in the four organisations’ later activities. The project does not run alongside their learning and then stop; it leaves a competence, a document that describes it, and a place to keep using it.')
COUNT(6000)

H2('Recognition of learning outcomes')
Q('How will you support participants to be aware of what they have learned and which competences they have developed or improved? Please remember to include the methods that support reflection and documentation of the learning outcomes in the daily timetable of each activity.')
P('The methods that support reflection and documentation are scheduled sessions in the timetable, not good intentions. **D1.4** introduces the eight key competences, the learning diary and Youthpass, and each '
  'participant sets two personal learning targets. **D1.5, D2.4, D3.5, D4.4 and D6.4** are the daily reflection cycle — national group in the participant’s own language first, then plenary. **D4.4** is the mid-point '
  'review of each participant’s own learning targets. **D7.2** is the closing Youthpass session. All six appear in the annexed timetable with their objective, method, competences, output and named responsible person.')
P('**Awareness of learning is built into the structure rather than added at the end,** in three concrete ways. First, the Day 1 digital map is kept and returned on Day 7: participants compare their own description of '
  'their media habits before and after, which turns an abstract competence gain into something they can see. Second, the observation grid applied on Day 4 records whether each participant actually performed each of '
  'four named techniques, so the conversation is about evidence rather than impression — and participants are told on Day 1 that this observation happens, what is observed and why, because it is their learning data '
  'and concealed assessment of minors is neither necessary nor acceptable. Third, the baseline and final test gives each participant a personal figure, communicated to them individually in month 18, not only '
  'aggregated for the report.')
P('**What the process is for.** Youthpass here teaches a transferable skill in its own right: identifying what you learned, documenting it with evidence you can point to, and presenting it in a form someone else '
  'understands. That is what makes the certificate useful to a sixteen-year-old afterwards — in the next learning activity they join, in volunteering, in a civic initiative in their own community, and in the next '
  'international mobility they apply for. The competence matrix above is the reference document for the whole process: every competence claimed is tied to the sessions that build it and to the evidence that documents '
  'it, and facilitators work from that same matrix when supporting participants to write their Youthpass.')
COUNT()

Q('The Erasmus Programme promotes the use of instruments/certificates like Youthpass or Europass, to validate the competences acquired by the participants during their experiences abroad. Will your project make use of such European instruments/certificates?')
P('Yes — **Youthpass**, for all 20 participants and all 4 group leaders. It is used as a process running from Day 1 to Day 7, as described above, and not as a certificate handed out at the door. Europass is not used '
  'in this project: our participants are 14 to 17 and are not in a mobility that produces a Europass Mobility document, so claiming it would be decoration. We would rather name one instrument we genuinely use well '
  'than two we use loosely. Alongside Youthpass, the coordinating organisation issues its own certificate of participation in Romanian and English, stating that the young person took part and naming the competences '
  'they developed through non-formal learning, with the evidence behind them — and that is all it claims. Participants and parents are told plainly what it is and what it is not, so that nobody is given an '
  'expectation the document cannot carry.')
COUNT(3000)

H2('Participants with fewer opportunities')
Q('Are participants involved in activities facing challenges that hinder their participation?')
P('**Yes. At least 12 of the 20 participants — 60%.**')
COUNT(500)

Q('What type of challenges are these participants facing? How will you reach out to them, and what specific measures will you implement to support their participation?')
P('**The challenges.** //Geographical// — the principal one, affecting essentially the whole group: isolated rural mountain communes, two Mediterranean islands, and a metropolitan periphery. Living in a remote or '
  'rural region, on a small island or in a peripheral, less-served area is recognised as an obstacle to participation, and all four groups qualify on that ground alone. //Economic// — 34.4% of the young people aged '
  '14–17 in our survey name cost as a barrier and 31.2% name transport; in these households the first 80 kilometres are a real obstacle, not a detail. //Educational// — 31.3% have never taken part in any non-formal '
  'education activity, and some come from households with no experience of European programmes at all; for them the difficulty is not only getting there, it is knowing that such a thing exists and is meant for them. '
  '//Linguistic// — part of our own territory communicates in Hungarian, inland Corsica in Corsican, inner Sardinia in Sardinian; a young person whose community life happens in a minority language has less access to '
  'information in the majority language, and none at all to correction of what circulates in their own. //Social// — 12.5% name lack of self-confidence and 10.4% say their family would not agree; among the '
  'respondents there are young people reached through the social worker, young people with childcare responsibilities and young people from Roma communities, and two wrote about exclusion directly: “There shouldn’t '
  'be differences of class or gender — if you’re in the 12th grade you should be able to go on Erasmus too” and “The right to study; Roma don’t put an emphasis on school.” //Health or disability// — not known before '
  'selection; the specific-needs sheet allows it to be declared confidentially, and the support that follows is costed individually rather than assumed.')
P('**How we reach them.** The first barrier these young people name is not money. It is information: 37.5% say the reason opportunities pass them by is that they never hear about them. So outreach is a project '
  'activity with its own indicator — a target of at least 60 applications for 20 places — not an administrative formality. We work through the youth networks the four organisations already run, including the Rural '
  'Youth Parliament and the participants of previous activities, because those are the people who can say what an exchange is actually like; peer-to-peer, since friends are the channel for 38.5% of them; through '
  'social media (49.0%), in a format adapted to the age group and produced with young people already active in the organisations rather than written by staff and posted at them; through libraries, community centres '
  'and local youth spaces, where the call is presented in person rather than pinned up; through the LAG’s Social Inclusion Centre and the UNIC — Porolissum project, which work directly with vulnerable households and '
  'reach young people who would never see an online call — six of our survey respondents did in fact hear about opportunities through a social worker; and, as an information channel only, through the schools of the '
  'territory, because that is where half of these young people say they hear about opportunities. Not through municipal noticeboards, which reach 6.2% of this age group: the 14 partner municipalities are used for '
  'validating the need and hosting activities, not for recruitment. Saying that plainly is what our own data requires.')
P('**The measures.** //Informational// — the outreach plan above, the call translated into four languages, and a plain-language version written for parents rather than for funders. //Economic// — no contribution of '
  'any kind is asked of participants; travel, accommodation, meals, insurance and materials are covered in full, and the rule is stated in writing from the day the call is published, because that is what allows a '
  'family to let a child apply at all. //Transport// — organised and paid from the participant’s home to the point of departure, through the inclusion support category, on a dedicated budget line: a young person from '
  'Măguri-Răcătău or from an inland Corsican commune does not have to solve the first 80 kilometres alone. //Educational and linguistic// — English is not a selection criterion, A2 is accepted, the detective’s '
  'glossary is built in five languages, methods are visual and practical, work is done in pairs, group leaders interpret on request, and cross-language support is built deliberately into the mixed teams. //Social and '
  'confidence// — the preparatory visit includes one young person from each sending organisation, so a participant arrives in August already knowing someone who has been there; the cohort communication group is '
  'active two months before departure; there is an online meeting with parents; the group leader accompanies throughout the journey; and the right to leave a session is stated. //Health or disability// — the '
  'specific-needs sheet allows confidential declaration, the venue is chosen to be accessible, and additional inclusion support at real cost is requested where needed, on its own line with its own justification. '
  '//Family reluctance// — named by 10.4%: the parents’ online meeting is held in each country in the local language, with the safeguarding focal point present and the full programme, supervision arrangements and '
  'contact chain explained, and parental consent is obtained after that meeting, not before it.')
COUNT(6000)

H2('Virtual learning / Blended activities and use of virtual components')
Q('Do you foresee Virtual/Blended activities and/or the use of any virtual component, before, during or after the activity?')
P('**Yes**, before and after the physical activity. Approximately 26 persons take part: 20 participants, 4 group leaders and 2 facilitators.')
COUNT(500)

Q('If yes, please describe them.')
P('**Before, months 3–4.** Four joint online sessions of 90 minutes each, in mixed national teams. A shared online workspace holds the documents, the case files uploaded by each group, and the templates. A moderated '
  'messaging group with explicit rules keeps day-to-day contact. A separate online meeting with parents in each country, and a two-day online briefing for the group leaders that includes the observer calibration '
  'exercise. The baseline test is administered online.')
P('**After, months 6–18.** The cohort communication group remains the working space for preparing the four local initiatives: each group posts its plan and the others comment before it happens. A joint online review '
  'meeting in month 10; the follow-up questionnaire in month 12; the participatory evaluation session in month 17, held online across the four countries; and the final test in month 18.')
P('**Why this is not decoration.** Two reasons, both from the data. First, for a group in which 31.3% have never taken part in a non-formal activity and 12.5% name lack of confidence as a barrier, the virtual phase '
  'lowers the threshold: they arrive in August having already met the people they will be working with, which is a different thing from arriving among strangers. Second, the subject of this project is the digital '
  'environment, so the way the project itself uses digital tools is part of the message. The rules the cohort applies in its own communication group — consent, no personal data of third parties, no sharing of '
  'unverified content — are the rules the project teaches.')
COUNT()

H2('Environmental friendly practices')
Q('Will you include sustainable and environmental-friendly practices in your activities?')
P('**Yes.** //Green travel// — for each group the low-emission option is analysed (train, coach, ferry, to the extent each qualifies as green travel under the rules of the applicable call), including the additional '
  'eligible travel days, and the option chosen and the reason are documented; the budget is built on the green rates for all four flows. //Food from the territory// — meals are mostly local and seasonal, sourced from '
  'producers in the LAG territory through the short supply chains the organisation itself developed in its rural-development work. That is not a gesture: it is the organisation’s own infrastructure, and it lets '
  'participants see a short supply chain instead of hearing about one. No individually packaged portions. //Materials// — no folders, no printed handouts; worksheets are digital; workshop materials are reusable; '
  'waste is separated at the venue; participants are asked to bring reusable bottles. //Local movement// on foot or by a single group transport. //Awareness through the content itself// — one of the categories of '
  'disinformation analysed on Day 2 is environmental and climate content. Participants work on real examples of misleading environmental claims, which for this particular group is a far more durable environmental '
  'lesson than a briefing on recycling, and it is consistent with the method of the whole project: they learn to distrust the slogan, including the green one.')
COUNT(4000)
PAGEBREAK()

# =====================================================================
H1('Project management')
Q('How will you manage the project (agreements with partners etc.) and make sure that it is done in line with the Erasmus Youth Quality Standards? You will find the quality standards further down in the application form.')
P('**Roles, separated on purpose.** Alina Ioana Baba (coordinator) is project manager: overall coordination, the relationship with the National Agency, budget, reporting, risk decisions and the partnership '
  'agreements. Claudiu Iancu is Learning Programme Coordinator for non-formal learning: the learning programme, the three measurement instruments, observer calibration and moderation, the facilitation team and the '
  'Youthpass process. Livia Golovatic is activity coordinator and Romanian group leader: the four joint online preparation sessions, the coordination of the four local initiatives, and the gender and locality balance '
  'checks. Marilena Georgescu is the safeguarding focal point: she receives and handles concerns and approves publication of content, and she sits outside the facilitation chain by design, so that a participant can '
  'raise a concern about a facilitator. Iulia Fătu handles finance and logistics: budget execution, procurement, venue, transport, insurance, financial reporting and the written venue risk assessment. YOBBA leads '
  'media production and AI content and designates one of the two facilitators. Each of the four organisations provides one group leader aged 18 or over.')
P('**Agreements and governance.** A written partnership agreement is signed with each partner in month 1, before any expenditure, setting out tasks and deliverables with dates, the exact budget share and the '
  'conditions and timing of transfers, recruitment and selection obligations, safeguarding obligations, adherence to the Erasmus Youth Quality Standards, data protection, reporting duties, visibility rules, and what '
  'happens if a partner does not deliver. The agreement is not a formality — it is the document that makes the deliverables enforceable. Coordination meetings are held online monthly in months 1–5 and every two '
  'months thereafter, with a standard agenda, a written minute circulated within 48 hours and a rotating chair. A shared action log records every decision with an owner and a deadline, and the risk register is '
  'reviewed at every meeting.')
P('**Alignment with the Quality Standards.** //Basic principles// — inclusion and diversity, environmental sustainability, digital transformation and participation all appear as design decisions traceable to '
  'evidence, and the correlation between each survey finding and the decision it produced is documented in the supporting file. //Fair and transparent selection// — published criteria identical across four countries, '
  'a commission of at least two people per organisation, and the outcome communicated with reasons to every candidate, including those not selected. //Preparation of participants// — four months, four joint online '
  'sessions, a preparatory visit, linguistic and intercultural components, a parents’ meeting in each country, and a baseline that tells the facilitators what the group actually cannot do. //Definition, assessment '
  'and recognition of learning outcomes// — the competence matrix tied to sessions and evidence, the baseline and final test, the observation grid with calibrated observers, and Youthpass as a process from Day 1. '
  '//Protection and safety// — child protection policy, a safeguarding focal point outside the facilitation team, a written venue risk assessment verified on site, parental consents, central insurance, an emergency '
  'protocol and a sensitive-content protocol. //Sharing results and knowledge of the Programme// — the toolkit published free of charge, results on the Erasmus+ Project Results Platform, dissemination through the '
  'LEADER and ELARD networks, and a Day 1 session telling participants what else the Programme offers them after this project.')
COUNT(6000)

Q('How will you organise the practical and logistical part of the project (e.g. travel, accommodation, insurance, visa, social security, mentoring and support, preparatory meetings with partners etc.)?')
P('**Preparatory visit, month 3.** Held in the LAG territory, with two people from each of the three sending organisations — one of them a young person — plus one staff member from the coordinating organisation, '
  'seven people in total. That staff member has two concrete tasks: contributing to the on-site verification of the logistical and safety arrangements, and finalising the mobility programme with the partners while '
  'everyone is in the same room. The visit as a whole verifies the venue and its safety in person, settles the division of the thematic days, meets the host community, and lets a young person from each group see '
  'where they will be coming. It is requested and justified on three grounds: all twenty participants are minors, two of the four partners are new to us, and a venue’s suitability cannot be assessed from photographs.')
P('**Travel.** Booked centrally by the coordinator for all four flows, so that no sending organisation carries a cash-flow burden and so that green options are compared on the same basis. Distances are confirmed with '
  'the European Commission distance calculator once departure cities are known. Domestic transport from participants’ homes to the point of departure is organised and paid by the project.')
P('**Accommodation and meals.** One venue inside the LAG territory, contracted after a written risk assessment and an on-site check during the preparatory visit. Rooms allocated by gender and age, minors with minors, '
  'group leaders on the same floors. Meals mostly local and seasonal from producers in the territory; dietary requirements collected in month 4 and confirmed with the venue in writing.')
P('**Insurance.** Health, accident and civil liability for all 26 people for the whole travel period, contracted centrally by the coordinator and verified before departure, rather than left to each partner to arrange.')
P('**Visas — the principal logistical risk.** Romania has applied the Schengen acquis in full, land borders included, since 1 January 2025, and Turkish nationals holding ordinary passports are subject to the Schengen '
  'short-stay visa requirement. For minors that means notarised parental authorisations, invitation letters, proof of accommodation and insurance, and consulate appointments booked well ahead. The procedure therefore '
  'begins in month 3, five months before the activity: invitation letters issued by the coordinator, a complete file checked by the coordinator before submission to the consulate, and reserve participants prepared in '
  'parallel with their own files ready. This is not a theoretical risk, and we treat it as the item most likely to cost the project a participant.')
P('**Mentoring and support.** Each participant has a group leader throughout, a cross-country buddy, and access to the safeguarding focal point. The cohort communication group is active from two months before '
  'departure until the end of the project.')
P('**Risk management.** The main risks and their responses: visas not obtained for the Turkish group (high likelihood, high impact) — procedure from month 3, documents prepared in advance, appointments booked early, '
  'reserve participants with complete files; withdrawal of participants — a reserve list of at least 2 young people per national group, prepared alongside the main group and kept informed; a partner failing to '
  'deliver on time — deliverables with dates in the partnership agreement, a monthly action log, then a reminder, a joint problem-solving call and documented reallocation; low English level blocking participation — '
  'the five-language glossary, visual methods, interpreting by group leaders, deliberately balanced mixed teams; a medical or safety incident — insurance, emergency protocol, a reference medical facility identified '
  'during the preparatory visit, a first-aid trained staff member and a night-duty rota; a participant distressed by the working content — the sensitive-content protocol, pre-screened material, the right to leave a '
  'session, daily individual availability of the safeguarding focal point; observers unable to apply the grid consistently — the month 4 calibration exercise with an 80% agreement target, and if it is not reached the '
  'grid is simplified before the mobility and the decision is minuted, never after seeing the results; bad weather for outdoor sessions — an indoor alternative planned for every outdoor session; and one of the four '
  'local initiatives not delivered — written commitments made publicly on Day 7, an interim reporting deadline in month 10, and methodological support from the partner leading that component.')
COUNT(6000)

H2('Partnerships')
Q('How and why did you choose your project partners? What experiences and competences will they bring to the project?')
P('The partnership is built around one shared structural condition, not around geographical variety. All four territories are peripheral, and each has its own linguistic bubble — Hungarian in part of our territory, '
  'Corsican in Corsica, Sardinian in inner Sardinia, neighbourhood and community networks in the İstanbul periphery — and content circulating in those languages and networks is not covered by national fact-checkers, '
  'who work in the majority language on subjects of national interest. Each partner has the same problem in a different form, and each brings a distinct competence to it. That is why the project cannot be delivered '
  'by one organisation, and why swapping a partner for a more convenient one elsewhere would weaken it rather than simplify it.')
P('**LAG Napoca Porolissum** (Romania — applicant, coordinator, host, sending) owns the evidence base of 153 young people surveyed, the territory, the venue, the relationship with 14 municipalities and a network of '
  '43 partners, and an in-house youth worker and trainer. Its own survey identified the problem. It leads overall coordination, budget, reporting, risk, the learning programme, local logistics, safety, the '
  'relationship with the host community and evaluation, and delivers the partnership agreements (M1), the verification test and observation grid piloted and locked (M1–M2), the baseline and final test (M2, M18), the '
  'programme and worksheets (M4), venue and services (M4), the evaluation report (M18) and the final toolkit (M17). It leads sessions D1.2, D1.3, D1.4, D2.1, D2.2, D3.2, D3.3, D4.1, D4.3, D5.1 and D7.2.')
P('**YOBBA** (Türkiye — sending) is the only partner with declared and demonstrated core expertise in digital media, a volunteer community of over 150 young people a year, and six KA152 youth exchanges as a partner '
  'between 2022 and 2024. It teaches production; it does not teach verification — which is exactly the complementarity this project needs. It leads the media production module (D6.1, D6.2), the AI-content session '
  '(D3.1) and the ethics-of-AI session (D3.4), provides pre-departure digital preparation, and designates one of the two facilitators. It delivers the production module and technical guide (M4), recruitment and '
  'preparation of the Turkish group (M2–M4), the local initiative in Küçükçekmece (by M12) and dissemination through its platforms (M5–M17).')
P('**[Corsica partner]** (France — sending) is sought for direct current work with young people aged 14–17 in inland or rural communes of the island, in a community where the Corsican language is in daily use and the '
  'local media ecosystem is small. It would lead the Day 2 strand on how disinformation circulates in minority-language communities, contribute to Day 5 and observe one mixed team on Day 4, and deliver its own local '
  'needs note with consultation data (M2), five to eight documented local cases (M4), recruitment and preparation of the French group, the local initiative in Corsica (by M13) and the French translation of the '
  'toolkit. [TO CONFIRM]')
P('**[Sardinia partner]** (Italy — sending) is sought for work with young people aged 14–17 in small depopulating localities of inner Sardinia and for experience of dialogue with local institutions. It would lead the '
  'preparation and method of Day 5 and the methodology of the local initiatives (D6.3) and observe one mixed team on Day 4, and deliver its own local needs note with consultation data (M2), five to eight documented '
  'local cases (M4), the local initiative model and its evaluation grid (M5), recruitment and preparation of the Italian group, the local initiative in Sardinia (by M13) and the Italian translation of the toolkit. '
  '[TO CONFIRM]')
P('We deliberately avoid the formulation that all partners contribute to all activities. Each partner leads named sessions and delivers named products by named dates, and the partnership agreement is what makes that '
  'enforceable.')
COUNT(6000)

Q('How will you communicate with them?')
P('**Formal coordination and accountability** run through email and a shared document workspace: all decisions, deliverables and versions live there, response time is three working days, and nothing that binds a '
  'partner exists only in a chat. **Coordination meetings** are video calls, monthly in months 1–5 and every two months thereafter, with a standard agenda, a written minute within 48 hours and a rotating chair. '
  '**Fast operational contact** happens in a closed messaging group of the core team only, during the preparation and mobility weeks, with no personal data of participants. **Group leaders** have their own separate '
  'channel plus the two-day online briefing in month 4 covering safeguarding, escalation, reflection facilitation and the calibrated use of the observation grid. **Participants** have the moderated cohort group and '
  'the four joint online sessions, active from month 3 to month 18, with explicit rules and facilitators moderating. **Parents** have an online meeting per country in the local language, plus the written participant '
  'pack, in months 3–4, before parental consents are signed.')
COUNT(3000)

Q('How will you monitor and coordinate their contribution?')
P('Each partner has deliverables with dates written into the partnership agreement, and those same deliverables appear in the shared action log with an owner. At every coordination meeting the log is reviewed line by '
  'line: delivered, in progress, or late. Escalation is defined in advance and is proportionate — a reminder from the project manager; then a joint problem-solving call with the relevant leads; then, only if '
  'necessary, a documented reallocation of the task, recorded in the action log. Payments to partners are staged against deliverables rather than against the calendar.')
P('Because the four organisations are of genuinely different kinds — a rural Local Action Group, a media-focused youth association in a metropolitan periphery, and two island organisations — monitoring uses one '
  'common backbone with partner-specific expectations: the same reporting template and the same dates for everyone, but the content of what each is asked for follows the role they actually hold. Quality is monitored '
  'as well as delivery: the Learning Programme Coordinator reviews the local cases each partner submits in month 4 against a common standard, because those cases are the working material of the whole mobility and a '
  'weak set from one country would quietly degrade Day 2 for everyone.')
COUNT(3000)

Q('Which other actors (organisations or individuals) will be involved and how?')
P('**Youth organisations and youth structures in the four territories** carry the call to young people in their own networks, host local initiatives, and take the toolkit into their own standing activity afterwards. '
  '**Libraries and community centres** host the local initiatives and the presentation of the toolkit, and are where it stays available afterwards. **Local authorities** — the 14 partner municipalities of the LAG '
  'territory and their counterparts in the other three countries — validate the need, host the Day 5 community dialogue, provide spaces for the local initiatives and receive the evaluation report and its '
  'recommendations; they are not used for recruitment, because our data shows they reach only 6.2% of this age group. **The LAG’s Social Inclusion Centre and the UNIC — Porolissum project** carry outreach to young '
  'people from vulnerable households, and are the channel through which the inclusion targets are actually met rather than hoped for. **Local producers of the territory** supply meals through short supply chains and '
  'take part in the intercultural evening. **Residents of the host village** are interlocutors in the Day 5 dialogue — participants in the learning, not scenery: the record of local rumours they help produce becomes '
  'the working material of Day 6. **Local press** is invited to the Day 7 public presentation. **National fact-checking and verification resources in the four countries** are used as reference material in the Day 3 '
  'tool laboratory, one per partner country, so that participants leave with a resource usable at home in their own language [TO CONFIRM: the final list, checked for being free of charge and appropriate for minors]. '
  'And **the LEADER and ELARD networks** carry the method to Local Action Groups across rural Europe, an audience that rarely encounters media-literacy tools at all.')
COUNT(4000)

H2('Evaluation')
Q('How will you evaluate your project’s success? Which activities will you carry out in order to assess whether, and to what extent, your project has reached its objectives and results?')
P('Every indicator has a baseline, a target, an instrument, an owner and a moment of measurement, and the three main instruments exist in writing before submission.')
TBL([
 ['Indicator', 'Baseline', 'Target', 'Instrument', 'When and who'],
 ['Mean score on the practical verification test (O1)', 'Month 2', '+30% or more, for at least 16 of 20', '15-item, 30-point practical test, Form A and Form B, online, closed-device', 'Months 2 and 18; Learning Programme Coordinator'],
 ['Participants applying 4 verification techniques (O2)', '0 at selection', 'At least 16 of 20', 'Observation grid, 4 techniques scored 0–2, six calibrated observers, 25% double-scored', 'Day 4, and in short form at the local initiatives; facilitators and group leaders'],
 ['Young people reached through local initiatives (O3)', '0', 'At least 80, at least 20 per community', 'Attendance lists, short activity reports, photographs with consent', 'After each initiative, months 6–15; group leaders'],
 ['Beneficiaries able to apply 2 simple methods (O3)', '3 entry questions per workshop', 'At least 70%', 'The 10-minute exercise at the end of each local initiative', 'At each initiative; group leader'],
 ['Overconfidence sub-score (items 9 and 14)', 'Month 2', 'Moves proportionally more than the total', 'Same test, reported as a separate 4-point sub-score', 'Months 2 and 18; Learning Programme Coordinator'],
 ['Confidence gap (believed minus actual ability)', 'Month 2', 'Narrower at month 18', 'Unscored confidence question converted to the test scale', 'Months 2 and 18; Learning Programme Coordinator'],
 ['First-time participants in a European mobility', '—', 'At least 15 of 20', 'Selection form', 'Month 2; selection commission'],
 ['Participants with fewer opportunities', '—', 'At least 12 of 20', 'Selection form and specific-needs sheet', 'Month 2; selection commission'],
 ['Gender balance', '—', 'At least 40% of each gender in every national group', 'Participant list', 'Month 2 and final confirmation; activity coordinator'],
 ['Applications received', '0', 'At least 60 for 20 places', 'Application register', 'Month 2; each partner for its own group'],
 ['Satisfaction and perceived learning', '—', 'At least 80% positive', 'End-of-mobility questionnaire and daily reflection records', 'Daily and on Day 7; facilitators'],
 ['Retention at 6 months', '—', 'At least 15 of 20 still applying something', 'Follow-up questionnaire', 'Month 12; activity coordinator'],
 ['External uptake of the toolkit', '0', 'At least 4 organisations outside the partnership', 'Written confirmations', 'Months 16–18; communication officer'],
], widths=[3.6, 2.4, 3.2, 4.0, 3.4], small=True)
P('**Evaluation activities, in order.** Before month 2, both instruments are piloted with 5–8 young people aged 14–17 from the territory who are not project participants; any item that more than 80% or fewer than 10% '
  'of the pilot group answers correctly is rewritten, and neither instrument is used on the cohort untested. In month 2 the baseline is taken and the threshold recalibration rule is applied once, on the group mean, '
  'with the decision recorded in writing. In month 4 all six observers score the same recorded sequence independently and compare, targeting exact agreement on at least 80% of judgements; if it is not reached the '
  'grid is simplified before the mobility and that decision is minuted. During the mobility: daily reflection groups whose output visibly adjusts the next day’s programme, facilitator observation, the Day 4 grid with '
  'moderation immediately afterwards, and a mid-week check of individual learning targets. On Day 7: participatory evaluation, an anonymous written questionnaire, the Youthpass reflection, and the comparison of each '
  'participant’s Day 1 digital map with their Day 7 reflection. After each local initiative: attendance, a short report and the ten-minute exercise. Month 10: joint online review feeding a revision of the toolkit. '
  'Month 12: follow-up questionnaire. Month 17: participatory evaluation with participants plus a consortium evaluation meeting. Month 18: final test, comparison with baseline, evaluation report, and results '
  'communicated individually to each participant and collectively to parents, community partners, the 14 municipalities and the National Agency.')
P('**On honesty in evaluation.** The instruments are designed so that failure is visible. A practical test can show no improvement; an observation grid can record that a participant did not perform a technique; a '
  'participant who does not take both forms is excluded from the calculation and reported as excluded, rather than quietly dropped from the denominator. We prefer that to a satisfaction questionnaire that always '
  'comes back positive. Fifteen items and twenty participants is not a validated psychometric instrument and we will not describe it as one: it is fit for tracking change inside this cohort and for telling the team '
  'where the learning worked, and the final report will say what was achieved and what was not.')
COUNT(6000)

H2('Sustainability of the results')
Q('What will you do to make sure that your project continues to have effects also after it ends?')
P('**Something concrete stays behind, and someone owns it.** The “Digital Detectives” toolkit — worksheets, exercises, games, verification grids, the manipulation-techniques grid produced by the participants and the '
  'AI-recognition sheet they wrote themselves — is tested during the mobility, revised in month 10 on the basis of what actually worked in the four local initiatives, and published free of charge in month 17 in '
  'English and Romanian, with French, Italian and Turkish translations delivered by the partners. It is not a report about the project. It is a set of materials a youth worker can pick up and use on a Tuesday afternoon.')
P('**It enters standing activity, not an archive.** The coordinator integrates the toolkit into the youth animation work it already runs across its 14 partner municipalities and into the community events it holds '
  'every year. YOBBA takes it into a volunteer programme of more than 150 young people annually. The two island partners integrate it into their own youth work. Each organisation names, in the partnership agreement, '
  'the person who owns it afterwards — a named person, not a department.')
P('**The twenty stay.** Participants are not released at the end. They have each already run a local initiative; the organisations then involve them as peer trainers, which is both cheaper and more effective than '
  'recruiting a new cohort from scratch. The cohort communication group remains open.')
P('**The instruments stay too.** The verification test, the observation grid and the beneficiary exercise are reusable, and the coordinator ends the project owning three measurement instruments it did not have before '
  '— which changes what it can honestly claim in every youth project it writes afterwards.')
P('**The partnership decides its own future.** In month 17 the four organisations formally assess whether to continue, and with what: a second exchange hosted by another partner, or a youth participation project on '
  'dialogue with local decision-makers. The decision is minuted either way, including if it is not to continue.')
COUNT(5000)

Q('Are you planning measures to make sure that the results produced are used and beneficial to others beyond the project’s lifetime? If yes, which ones?')
P('Yes. Four measures, each with an addressee rather than a general intention. **To youth organisations, libraries and community centres in the territory:** the toolkit offered free, with a presentation session in '
  'month 17 for the youth workers, librarians and community educators who will actually use it. Romania has no coordinated national media-literacy strategy and its policies in this area are fragmented across separate '
  'legal frameworks; in that context a free, tested set of materials in the hands of people who already work with rural young people has value out of proportion to the size of this project. **To youth organisations '
  'across Europe:** publication on the Erasmus+ Project Results Platform, dissemination through YOBBA’s platforms, and dissemination through the LEADER and ELARD networks, where the coordinator already has '
  'transnational cooperation experience; target, at least four organisations outside the partnership confirming in writing that they use the toolkit. **To local institutions:** the evaluation report and a short set '
  'of recommendations delivered to the 14 partner municipalities and to the partner institutions in the other three countries. **To the communities themselves:** the four media products remain in circulation on the '
  'organisations’ channels — unlike a report, they are the kind of thing people actually watch.')
COUNT(4000)

H2('Dissemination of project results')
Q('How will you make your project visible outside your organisation and partner organisations? How will you share its results and success? With whom will you share the results?')
TBL([
 ['Audience', 'Channel', 'Product', 'Indicator and owner'],
 ['Young people in the four communities', 'The four local initiatives; the organisations’ social media; youth centres, libraries and community centres', 'Workshops, the four media products, the toolkit', 'At least 80 young people reached directly; group leaders'],
 ['Communities of the LAG territory', 'The 14 partner municipalities; the community events the organisation runs annually; local press', 'The Day 7 public presentation; a “Digital Detectives” stand at two community events', 'At least 2 community events and 3 items in local press; communication officer'],
 ['Parents and legal guardians of the participants', 'The parents’ meetings in each country; the participant pack; the local initiatives and the Day 7 presentation', 'Information on the programme, the supervision arrangements and the contact chain; presentations by the participants themselves', 'One meeting per country before consents are signed; 100% of families reached with the pack; group leaders. Parents are involved in informing, supporting and protecting participants who are minors — they are not a target group of the project'],
 ['Youth organisations and youth workers in Europe', 'Erasmus+ Project Results Platform; the partners’ networks; YOBBA’s platforms; LEADER and ELARD', 'The “Digital Detectives” toolkit', 'Toolkit published and freely downloadable; at least 4 external organisations confirm use'],
 ['Local institutions and decision-makers', 'Direct meetings; presentations in local councils', 'Evaluation report; short recommendations', 'At least 4 institutions informed; project manager'],
], widths=[3.2, 4.2, 4.2, 5.0], small=True)
P('**Visibility of the Programme.** All materials produced — toolkit, media products, presentations, press releases — carry the European Union emblem and the funding statement, in line with the Programme’s rules. On '
  'Day 1 participants have a short session on what Erasmus+ is and what stays open to them afterwards — the European Solidarity Corps, DiscoverEU, other exchanges — so that this project is not the end of their '
  'contact with the Programme.')
P('**Safeguarding in dissemination.** Because all participants are minors, every piece of content goes through a two-step review: the participant responsible for documentation prepares it, and the safeguarding focal '
  'point approves it before publication. No identifiable images of minors without written consent; no personal data of third parties; no location details for minors. This rule is written into the group agreement on '
  'Day 1, and it is itself part of the learning.')
COUNT(5000)

Q('How will you involve participants in such activities?')
P('Participants are the producers of the disseminated results, not their subject. They make the four media products; they design and lead the four local initiatives; they present publicly on Day 7 to guests from the '
  'community, the municipalities and the press; they co-present the results across the localities of the territory in months 16–17; and defined documentation roles — photo and video, activity diary, contact with the '
  'host community — are assigned in month 3 and held throughout. A fifteen-year-old explaining to a room of other young people how to check whether a photograph is what it claims to be is a more effective '
  'dissemination instrument than any press release the organisation could write — and it is also the moment the learning stops being ours and becomes theirs.')
COUNT(3000)
PAGEBREAK()

# =====================================================================
H1('Erasmus Youth Quality Standards')
SMALL('Open the linked document (erasmus-youth-quality-standards_en.pdf), read it, then confirm the three statements. The second binds the co-beneficiaries as well, which is why adherence to the standards is written into the partnership agreement signed with each partner in month 1.')
BUL([
 'I have read the above Erasmus Youth quality standards — **confirm**',
 'I confirm that I, my organisation and the co-beneficiaries (where applicable) adhere to the Erasmus Youth quality standards — **confirm**',
 'I understand and agree that Erasmus Youth quality standards will be used as part of the criteria for evaluation of the activities implemented under this project — **confirm**',
], count=False)

H1('Annexes')
TBL([
 ['Slot', 'What to upload', 'Status'],
 ['**Declaration on Honour**', 'Downloaded from the form, printed, signed by the legal representative, attached.', 'To prepare'],
 ['**Timetable**', 'The timetable of the youth exchange and of the preparatory visit, in the form’s template. This carries the full daily programme — all 24 sessions with their objective, method, competences, output and named responsible person.', 'Ready — to be transferred into the template'],
 ['**Accession forms** (if the slot is present)', 'One per partner, signed by each legal representative. Due at the latest before the signature of the grant agreement, and a condition for signing it.', 'YOBBA expected; the two island partners outstanding'],
 ['**Other Documents** (if the slot is present)', 'In priority order: the measurement-instruments pack; the youth survey instrument and analysis; the partners’ one-page needs notes. Only what is short and relevant.', 'To assemble'],
], widths=[3.4, 10.2, 3.0], small=True, count=False)

H1('Application conditions')
H3('EU values')
BUL([
 'I confirm that I, my organisation and the co-beneficiaries (where applicable) adhere to the EU values mentioned in Article 2 of the TEU and Article 21 of the EU Charter of Fundamental Rights — **confirm**',
 'I understand and agree that EU values will be used as part of the criteria for evaluation of the activities implemented under this project — **confirm**',
], count=False)
H3('EU sanctions and restrictive measures')
BUL([
 'I confirm that I / my organisation / project partners are NOT included on the list of persons or entities subject to EU sanctions — **confirm**, after checking the applicant and all three partners against the EU Sanctions Map',
 'I / my organisation / project partners are not established in Russia, nor are any of our proprietary rights directly or indirectly owned for more than 50% by a legal person, entity or body established in Russia — **confirm**. The four organisations are established in Romania, Türkiye, France and Italy; each partner confirms ownership as well as establishment in writing',
 'The alternative declaration, for organisations established in Russia or more than 50% Russian-owned — **not applicable, do not tick**',
], count=False)
H3('Original content and authorship')
BUL([
 'I confirm that this application contains original content authored by the applicant organisation — **confirm**. No passage is reused from the previous application: ANPCDEFP runs anti-plagiarism software and treats passages identical or similar to another application, including one’s own from a previous deadline, as double funding',
 'I confirm that no other organisations or individuals external to the applicant organisation have been paid or otherwise compensated for drafting the application — **confirm if true of your situation**',
], count=False)
H3('Protection of personal data and other acknowledgments')
BUL(['Acknowledgment that information concerning the organisation, the application, the capacity assessments and the implementation may be made accessible to authorised persons of the European Commission, EACEA and the National Agencies — **confirm**, after reading the linked privacy statement'], count=False)
H3('Pre-submission checklist')
BUL([
 'It fulfils the eligibility criteria listed in the Programme Guide — 20 participants aged 14–17, four groups from four countries, 5 per group, one group leader per group, two facilitators, seven activity days excluding travel, activity in the country of the applicant and of the National Agency.',
 'All relevant fields in the application form have been completed — every [TO CONFIRM] in this document is a field still open.',
 'You have chosen the correct National Agency — RO01, ANPCDEFP.',
], count=False)

SMALL('Prepared 16 September 2026 for the KA152-YOU application of Asociația GAL Napoca Porolissum, Call 2026 Round 2, deadline 1 October 2026, 12:00 Brussels time.')

import os
out = '/home/user/UNIC-2/VERIFAI_KA152_Form_Content_EN.docx'
doc.save(out)
print('saved', out, os.path.getsize(out), 'bytes')
