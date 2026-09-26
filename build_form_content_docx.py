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
        'Square brackets mark the few facts that do not exist yet — the accommodation unit in Beliș, the exact departure cities, and a handful of partner details. Everything else is final.',
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
P('We want young people who use artificial intelligence every single day to stop taking at face value whatever it hands them. In our own survey of 153 young people in the '
  'Napoca Porolissum territory, 96.9% of those aged 14–17 already use AI tools, yet they rate their own digital competence at 3.25 out of 5, and half of them build their picture of '
  'the world from social media. Nobody has taught them how to check any of it. VERIFAI turns twenty-one of them, from three peripheral European communities, into detectives: young '
  'people who can identify a source, check a date and a context, compare two independent sources, recognise a reused image and spot the signature of AI-generated content, and who '
  'then pass that on to others at home.')
P('From a youth work perspective the problem is not ignorance but untrained confidence. The Flash Eurobarometer “Youth Survey 2024” (EP013EP), carried out by Ipsos for the '
  'European Parliament among 25,863 young people aged 16–30 across all 27 Member States, found that more than three quarters of them had met disinformation in the previous seven '
  'days, while 70% were confident they could recognise it. Because confidence outruns competence, the method cannot be a lecture. Participants meet the false material and commit '
  'to a judgement before the verdict is revealed, and discover for themselves that they were wrong. That controlled moment of being wrong is the core of the non-formal learning '
  'approach of this exchange, and it only works in a genuinely international group, where a stereotype is very hard to defend with someone from the targeted community sitting at '
  'the same table.')
P('The project therefore pursues three objectives, referred to throughout this application as O1, O2 and O3 in the order given here.')
NUM([
 'By the end of the project, at least 17 of the 21 young participants aged 14–17 will improve their mean score on the assessment of online information verification competences by '
 'at least 30% compared with the initial assessment.',
 'By the end of the project, at least 17 of the 21 participants will correctly demonstrate, in a practical exercise, at least four verification techniques: identifying the source '
 'and the author, checking the date and the context, comparing with independent sources, and verifying images or claims.',
 'In the follow-up stage, the 21 participants will transfer the methods learned to at least 80 young people in the partner communities, through at least four local initiatives, '
 'and at least 70% of the beneficiaries of those initiatives will be able to apply at least two simple verification methods.',
])
P('Each of the three is measured with an instrument that already exists in writing. The first uses a fifteen-item, thirty-point practical test taken in month 2 and again in month '
  '18, with the same scoring method at both ends. The second uses a structured observation grid applied during the assessed session on Day 4 by observers trained and calibrated '
  'beforehand, which records what a participant actually does rather than what they can describe. The third uses a ten-minute exercise at the end of each local initiative, in '
  'which the young people reached name two checks, carry one out and draw a conclusion from what they find.')
P('The 30% threshold is confirmed once the baseline exists, and the rule for adjusting it is fixed now rather than later: below a group mean of 9 out of 30 the threshold rises to '
  '50%, above 18 out of 30 it falls to 20% with an absolute companion measure, and a participant who already scores 24 or more at the start meets the objective by holding 27 or '
  'more at the end. Writing this down in advance is what stops a threshold from quietly becoming a way of producing the answer we want.')
COUNT()

Q('What activities do you plan to implement? What is the number and profile of the participants involved?')
P('The project is built around one youth exchange of seven activity days plus two travel days, hosted in the Napoca Porolissum territory in the Apuseni Mountains, Romania, from 9 '
  'to 15 August 2027, inside the school summer holiday of all three countries. The programme moves from self-diagnosis in “My Digital Map” through the mechanics of manipulation in '
  '“Spot the Fake”, AI-generated content in “AI or human?”, a full fact-checking simulation in “Fact-checkers for a day”, a community and intercultural day in the host commune and a neighbouring village of the '
  'territory, media production in “Make It, Don’t Fake It”, and a public presentation with Youthpass reflection. Around the exchange sit four months of preparation, with four joint '
  'online sessions and a preparatory visit, and ten months of local application in which the participants run four local initiatives in their own communities.')
P('Twenty-one young people aged 14–17 take part — seven from Romania, seven from Türkiye and seven from Greece — accompanied by four group leaders and two facilitators, 27 people in '
  'all. They come from three peripheral communities: the rural mountain communes of the Napoca Porolissum territory in Cluj County, the İstanbul metropolitan periphery and the '
  'rural localities around it, and small islands of the South Aegean.')
P('They share the profile this project is built for. Almost all of them use AI tools and social media every day, and for a large part of them social media is the news, yet none has '
  'been taught how to check any of it. Their access to non-formal learning is thin and their access to international learning close to nil: at least 16 of the 21 will be taking '
  'part in a European mobility for the first time, and in our territory 31.3% of young people aged 14–17 have never taken part in any non-formal education activity at all. At '
  'least 13 of the 21 face documented barriers, whether geographical, economic or social. The group is built to be mixed in gender and in locality, and the '
  'Romanian group is deliberately mixed in language, because the language question is part of the subject matter.')
COUNT()

Q('What results and impact do you expect your project to have?')
P('The twenty-one participants end the project able to do something they could not do at the start, and with the evidence to show it: the same practical test taken at the beginning and at the end, an observation '
  'grid applied during the exchange, four short media products debunking real local myths that they made themselves, and Youthpass certificates built through daily reflection '
  'rather than handed out at the door. For most of them it is also a first international experience, which at fifteen, arriving from a mountain commune or a small island, is its '
  'own learning.')
P('Their communities gain four local initiatives reaching at least 80 more young people — two in the Romanian territory, one in Türkiye and one in the South Aegean — hosted in '
  'youth centres, libraries, community centres, the partner organisations’ own spaces and other public places young people can actually get to. Alongside them comes a “Digital '
  'Detectives” toolkit of worksheets, exercises, games and verification grids, tested during the exchange, rewritten on the basis of what happened in the field, published free of '
  'charge and handed to the youth workers, librarians and community educators who work with these young people week to week.')
P('The three organisations keep a working method that survives the project. The coordinator integrates it into the youth animation work it already runs across its 14 partner '
  'municipalities; GGD takes it into the volunteer network it trains every year; KEA takes it into its creative activity centre for children and young people and out to the 36 '
  'islands it serves. Together they end up with something none of them has now: a shared, evidenced answer to a problem all three of their communities have, in a form other '
  'peripheral territories can pick up. The results are published on the Erasmus+ Project Results Platform.')
P('We do not claim more than that. Twenty-one participants will not move a county-level statistic, still less a national one. The contribution is measurable change in twenty-one young '
  'people, documented extension to at least eighty more, and three instruments and one toolkit that stay in use in three organisations after the money stops.')
COUNT()

H1('Summary of participating organisations')
TBL([
 ['Organisation name', 'OID', 'Country', 'Role', 'Type of organisation'],
 ['ASOCIAȚIA GRUPUL DE ACȚIUNE LOCALĂ NAPOCA POROLISSUM', 'E10181755', 'Romania', 'Applicant organisation', 'Non-governmental organisation / association (non-profit)'],
 ['GENÇ GÖNÜLLÜLER DERNEĞI — Young Volunteers Association (GGD)', 'E10309307', 'Türkiye', 'Partner organisation', 'Non-governmental organisation / association (non-profit)'],
 ['KENTRO EREUNAS KAI ANAPTYXIS IERAS MHTROPOLIS SYROU (KEA IM Syrou)', 'E10151458', 'Greece', 'Partner organisation', 'Non-governmental organisation / association (non-profit)'],
], widths=[5.4, 2.2, 1.8, 3.4, 3.8], count=False)

H1('Summary of activities and participants')
TBL([
 ['Activity Type', 'No. of activities', 'No. of persons', 'Participants with fewer opportunities'],
 ['Youth exchanges', '1', '27', '13'],
 ['**Total**', '**1**', '**27**', '**13**'],
], widths=[5.0, 3.6, 3.6, 4.4], count=False)
SMALL('27 persons = 21 participants aged 14–17 + 4 group leaders + 2 facilitators, in three national groups of seven from Romania, Türkiye and Greece.')

# =====================================================================
H1('Project budget')
H3('Budget summary')
TBL([
 ['Budget item', 'Grant (EUR)', 'Basis of calculation'],
 ['Organisational support', '2,625.00', '125 × 21 participants'],
 ['Travel (green travel)', '8,010.00', 'Romania 9 persons × 56 (band 10–99 km); Türkiye 9 and Greece 9 persons × 417 (band 500–1,999 km)'],
 ['Individual support', '12,834.00', 'Romania 9 persons × 9 days × 46; Türkiye 9 and Greece 9 persons × 11 days × 46 (9 days plus the 2 additional days green travel over that distance makes eligible)'],
 ['Inclusion support for organisations', '1,625.00', '125 × 13 participants with fewer opportunities'],
 ['Inclusion support for participants', '2,000.00', 'Real costs, requested on separate dedicated lines and justified individually'],
 ['Preparatory visit', '3,400.00', '680 × 5 persons: 2 from each of the 2 sending organisations, one of them a young person, plus 1 staff member of the coordinating organisation'],
 ['**Total**', '**30,494.00**', 'Of which 27,094.00 is the Activity 01 grant and 3,400.00 the preparatory visit'],
], widths=[4.4, 2.2, 10.0], count=False)
SMALL('Figures built on the 2026 Programme Guide unit costs. The form produces the final amounts per flow once the distance calculator has been run for each place of origin. '
      'Organisational support is calculated here on the 21 young participants only; if the National Agency counts group leaders and facilitators as participants for this item, that line rises to 3,375.00 (125 × 27) and the totals with it. '
      '[TO CONFIRM: the exact departure cities and the resulting distance bands. Also to confirm: that a green-travel combination is available from Syros — ferry to Piraeus and then overland — since if it is not, the '
      'standard rate applies to the Greek flow and the travel line falls accordingly.]')

H3('Budget summary per activity type')
TBL([['Activity type', 'Grant (EUR)'], ['Youth exchanges', '27,094.00']], widths=[8.0, 8.6], count=False)
H3('Budget summary per activity')
TBL([['Activity id', 'Activity type', 'Grant (EUR)'], ['01', 'Youth exchanges', '27,094.00']], widths=[4.0, 6.0, 6.6], count=False)
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

Q('Please briefly present your organisation/the group')
P('We are Asociația Grupul de Acțiune Locală Napoca Porolissum, a non-governmental, non-profit association registered in Romania under Government Ordinance 26/2000, based in '
  'Gilău, Cluj County, in the Apuseni Mountains. Our registered main sector of activity is offering participation in youth-led events and youth participation activities.')
P('We were founded in 2011 as a Local Action Group under the LEADER programme, which makes us a public-private partnership rather than a single organisation. We have 43 members, '
  'listed and signed in the record of our General Assembly of 17 October 2023: 14 municipalities — Aghireșu, Beliș, Călățele, Căpușu Mare, Gilău, Huedin, Izvorul Crișului, '
  'Măguri-Răcătău, Mănăstireni, Mărgău, Mărișel, Rîșca, Săcuieu and Sâncraiu — one university, and 28 private companies, NGOs and authorised individuals, among them the '
  'professional social workers’ association PROSOCIAL. Our staff work across several projects at once and most of them speak English and French.')
P('Those 14 localities are our territory: a rural mountain area where young people live 40 to 80 kilometres from the nearest city, where the offer of youth activities is thin, '
  'and where community life runs in two languages, Romanian and Hungarian. Everything we do happens there, with the people who live there, and LEADER gives us one method we '
  'apply to all of it. We analyse the territory, ask the people affected what they need, design with them and measure what changed. Two Local Development Strategies have been '
  'built and implemented that way, and the current one, covering 2023 to 2027, has already launched calls that help rural young people develop skills, cooperate and start their '
  'own businesses. It is also how this project began, with a survey of 153 young people in our own communes rather than with a wish to run a mobility.')
P('On 17 October 2023 our General Assembly decided, unanimously, to establish a Youth Department inside the association and appointed Claudiu Iancu as its Coordinator. That '
  'decision matters more than it may look, because it means youth work here does not depend on whichever project happens to be running: it is a standing department with a named '
  'coordinator and a mandate from the members, including the 14 mayors who voted for it.')
P('Beyond projects, we are accredited as a social economy entrepreneur, and through a European Social Fund programme between 2021 and 2023 we trained 99 people from '
  'disadvantaged households in social entrepreneurship. Our Social Inclusion Centre and the UNIC — Porolissum project put us in weekly contact with vulnerable families, which is '
  'how we reach young people an online call never touches. We also run much of the cultural and educational infrastructure young people here actually have: Ruraliada, a '
  'three-day arts festival in Beliș funded by the National Recovery and Resilience Plan; The School — children’s painting, which brings artists into village schools; Christmas '
  'markets in Mărișel and Beliș; an annual Diversity Day; and educational camps at home and abroad.')
P('At European level we coordinate EMPOWER+ — Empowering Rural Youth: Establishing and Strengthening the Rural Youth Parliament in Sub-Saharan Africa (101243075), a Capacity '
  'Building project in which we lead nine organisations across seven countries, and we coordinated Rural Youth Parliament — tool for youth involvement in local communities '
  '(2021-1-RO01-KA220-YOU-000029265). We have been a partner in youth projects with coordinators in Ireland, Spain, Italy, France and Türkiye, including YOU PRO CLIMA '
  '(2023-1-IT03-KA220-YOU-000155348) and ALL4JOBS (2024-1-IT03-KA220-YOU-000248804), and in a youth-worker mobility project led from Türkiye '
  '(2025-1-TR01-KA153-YOU-000297756).')
P('What we have never done is host a youth exchange, and that is the deliberate next step, because hosting means owning the learning programme, the venue, the safety of twenty-one '
  'minors and the relationship with the host community. We have the territory, the venue network, the 14 municipalities, the Social Inclusion Centre, an in-house youth worker '
  'and trainer, and a Youth Department created for exactly this. What we do not yet have is KA152 experience, which is why we are doing it with partners who complement us, and '
  'why the learning programme, the safeguarding arrangements and the three measurement instruments were written before we asked for the money.')
COUNT()

Q('What are the activities and experience of the organisation in youth work? Please provide information on your organisation’s / group’s regular youth work activities. Please give information on the key staff/persons involved in this application and on the competences and previous experience that they will bring to the project.')
P('Youth work here has a named owner and a permanent home. On 17 October 2023 our General Assembly unanimously established a Youth Department inside the association and appointed '
  'Claudiu Iancu as its Coordinator, with the mayors of our 14 communes voting. What follows is what runs.')
P('The Rural Youth Parliament is the centre of it. We created it through the Erasmus+ project Rural Youth Parliament (2021-1-RO01-KA220-YOU-000029265) as an informal group of '
  'young people and youth workers, and we still coordinate it. It runs its own campaigns: every winter it collects and distributes gifts to children in low-income families, every August it runs “Full Backpack”, giving school supplies so '
  'children start the year with what they need, and through the year it organises tree-planting and clean-up actions, movie nights for younger children and blood donation drives. '
  'It also staffs every event we hold, including LINC and the community brunches.')
P('Alongside it we run environmental education at scale. Choose Green!, financed by the Environmental Fund Administration in 2024–2025, works with 510 young people aged 6 to 18 '
  'through 12 workshops and 36 awareness campaigns, two educational trips and an interactive learning application we built. Put the Green in Motion!, '
  'over the same period, reaches 520 young people across 14 localities through 12 workshops, a biodiversity camp, a field trip to the Rodna Mountains and 24 media campaigns. That '
  'is over a thousand young people in two years, in workshops we designed and ran.')
P('For three editions we also ran Green Campus with the University of Agricultural Sciences and Veterinary Medicine in Cluj-Napoca, bringing at least 150 high-school students and '
  'over 50 volunteers per edition onto a university campus, to show rural teenagers that higher education is for them. A separate programme for 185 students combined guidance and counselling, a workshop on equal opportunities and non-discrimination, internships with local employers '
  'and practice workshops abroad for 12 of them.')
P('We also ask young people what they need rather than assuming it. In spring and summer 2026 a bilingual Romanian/Hungarian survey brought 153 responses from 12 of our 14 '
  'communes, 96 of them from young people aged 14–17 — the evidence base of this application. We reach them through open calls in schools, NGOs and youth networks, through '
  'direct outreach by our own youth workers, and through youth groups that already exist.')
P('The work will be done by five people. **Claudiu Iancu**, Coordinator of our Youth Department and, in this project, Learning Programme Coordinator and lead facilitator, is a youth worker and community facilitator holding a Trainer qualification and five Europass mobility certificates, with a BSc in Economic Engineering in Agriculture and an '
  'MSc in Rural Development. He has around three years inside Local Action Groups on rural development, social inclusion and non-formal education, after work in adult '
  'education that trained over 1,000 adults. He managed a European Solidarity Corps project, has been involved in more than five Erasmus+ Youth projects, and in '
  'the past three years has organised and facilitated over 50 youth events. He coordinated the Rural Youth Parliament and was Youth Leader in YOU PRO CLIMA, and here he owns the learning programme, the three measurement instruments, the facilitation '
  'team and Youthpass.')
P('**Alina Ioana Baba**, project manager, holds two degrees in Legal Sciences and Public Administration, three master’s degrees and a PhD in economics. She has managed the '
  'association for over ten years and spent more than fifteen on social inclusion, vocational training and labour-market integration projects, and she carries coordination, the '
  'National Agency relationship, the budget, reporting and risk decisions. **Livia Golovatic**, activity coordinator and Romanian group leader, has a BA in International '
  'Relations and European Studies and is completing a master’s in European Affairs and Programme Management while working as assistant manager on our Local Development Strategy; '
  'she brings experience in Erasmus+ Youth and VET projects and in youth participation, and she runs the joint online preparation sessions, leads the Romanian group and '
  'coordinates the four local initiatives.')
P('**Marilena Georgescu**, inclusion and safeguarding lead, has higher education in Social Assistance and Law, a master’s in Project Management and qualifications in '
  'train-the-trainer and socio-educational animation, with fourteen years in social inclusion projects and experience coordinating social service centres including a day centre '
  'for children; she is the safeguarding focal point, deliberately outside the facilitation team. **Iulia Fătu**, responsible for finance and logistics, holds two bachelor’s and '
  'two master’s degrees including Audit and Financial Management of European Funds and has worked on European projects since 2014, handling the budget, procurement, contracting, '
  'insurance, the venue risk assessment and reporting.')
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
H2('Partner — GENÇ GÖNÜLLÜLER DERNEĞI / Young Volunteers Association (Türkiye)')
TBL([
 ['Field', 'Entry'],
 ['Organisation ID (OID) / PIC', 'E10309307 / 947709013'],
 ['Legal name (national language)', 'Genç Gönüllüler Derneği'],
 ['Legal name (Latin characters) / Acronym', 'Young Volunteers Association / GGD'],
 ['Country / Region / City', 'Türkiye / Marmara / İstanbul'],
 ['Address', 'Ayazağa Mh. 118. Sk. No: 1, Üzüm Apt. K:5 D:9, Sarıyer, 34397, İstanbul'],
 ['Website', 'www.gencgonulluler.org.tr · www.cocukhaklarioyunu.org'],
 ['Type of organisation', 'Non-governmental organisation / association'],
 ['Is the organisation a public body? / non-profit?', 'No / Yes'],
 ['Accreditation', 'None yet. The organisation has received EU grants before'],
 ['Legal representative', 'Eyüp Coşkun, Chairman of the Board of Directors'],
 ['Contact person', 'M. Talha Serenli — serenlimahmuttalha@gmail.com'],
], widths=[5.0, 11.6], count=False)

Q('What are the activities and experience of the partner organisation in youth work?')
P('Genç Gönüllüler Derneği — Young Volunteers Association — has worked in Türkiye since 2004 to increase young people’s participation in social, cultural and artistic life, and has implemented or partnered in more than '
  'a hundred projects in twenty years. It works through formal, non-formal and informal methods on the personal, social, emotional and professional development of young people and youth workers, and it targets '
  'disadvantaged and at-risk groups, working with public institutions, civil-society organisations and universities.')
P('What makes it unusual, and useful here, is the composition of its team. The organisation’s expert group — all of them contributing voluntarily — includes an adolescent health specialist, a paediatrician, a forensic '
  'medicine specialist, social workers, psychologists, a lawyer, a child development specialist, software developers, artists and academics. Among them is a **social media, cyber-security and artificial intelligence '
  'specialist**, which is the single competence this project most needs on the partner side and which a youth organisation almost never has in-house.')
P('In the areas this project works on, GGD has taken part in Erasmus+ KA1 and KA2 projects on children’s rights, climate change, youth worker mobility and human rights, with an emphasis on experiential '
  'learning and cross-cultural dialogue that built communication skills, environmental awareness and **digital literacy**. It has run digital skills programmes and campaigns against racism and hate speech, online and in '
  'the community. Most directly relevant: it convened a **workshop on developing an action plan to identify children’s digital content needs**, bringing together a hundred participants — educators, child development '
  'experts, digital media specialists and NGO representatives — and published the result as a guide for educators, parents and content creators. An organisation that has already had to think about what makes digital '
  'content appropriate and trustworthy for young people is starting this project from the right place.')
P('It also works where our own project works: GGD runs **rural youth empowerment programmes**, supported by the Turkish Ministry of Interior, that bring together young people from urban and rural areas, and it organises '
  'camps for children who have lost both parents. It has collaborated with the Kingdom of the Netherlands, the Embassy of Switzerland and the International Children’s Center, and with Turkish government institutions.')
P('One point deserves stating because it matters for a project with twenty-one minors in it. GGD’s declared practice in child-related projects is to limit public sharing in order to protect participants, while sharing '
  'method and technical detail openly with partner organisations. That is the same distinction VERIFAI draws in its own dissemination rules — participants produce the results, and nothing identifiable about a minor is '
  'published without consent — so the safeguarding culture does not have to be negotiated into the partnership; it is already there.')

H4('What GGD brings to VERIFAI, and where it does not overlap with the coordinator')
P('GGD brings the production and the technology side; the coordinator brings verification. The organisation knows how digital content for young people is made, what it is made with, and — through its AI and '
  'cyber-security specialist — how generated content works from the inside. That is what allows a fifteen-year-old to recognise it. The coordinator leads the verification days; GGD leads the day on AI-generated content, '
  'the session on the ethics of using AI in one’s own production, and the media production day. A young person who can edit a convincing video but cannot check a source is a more efficient vector of disinformation, not '
  'an antidote, and the division of labour is designed around closing that circle.')
P('For the same reason, **one of the two facilitators of the exchange is designated by GGD**: the sessions on AI-generated content and on media production need someone in the facilitation team who works with these '
  'tools professionally rather than someone who has read about them. That facilitator joins the team in month 4, takes part in the observer calibration exercise, and carries out independent second scoring on Day 4 '
  'alongside the facilitator designated by the coordinator.')
COUNT()

Q('Please describe the profile of each of the group members and what does each one bring to the project.')
TBL([
 ['Person and role', 'Profile and contribution'],
 ['**Eyüp Coşkun**\nPresident; legal representative',
  'More than twenty years in the field, specialist in EU project writing, and trainer for public institutions and NGOs on innovative methods in work with children and young people. Public relations expert with '
  'experience coordinating large-scale projects. In VERIFAI he carries GGD’s institutional commitment, signs the partnership agreement and the child protection undertakings, and oversees the Turkish group’s '
  'administrative and financial obligations.'],
 ['**M. Talha Serenli**\nContact person; Turkish group leader',
  'Twenty-three years old, studying International Relations at Ankara Hacı Bayram Veli University. Has taken part in and implemented local and international projects, worked in social responsibility initiatives '
  'including hippotherapy training with disadvantaged people, and has experience working with children as a coach and with several civil-society organisations. In VERIFAI he leads the Turkish group, prepares it before '
  'departure, accompanies it throughout, and observes one mixed team on Day 4. [TO CONFIRM: that he is the designated group leader.]'],
 ['**Tahsin Altay**\nSpecialist adviser — AI, social media and cyber-security',
  'Expertise in social media strategy, cyber-security and artificial intelligence. In VERIFAI he is the technical authority behind the Day 3 module: what generative tools can and cannot do, what traces they leave, and '
  'how to read them. He also advises on the digital safety rules the cohort applies to its own communication group, and on the security of project data.'],
 ['**Nursu Yüce**\nVolunteer management and collaboration programmes director',
  'Responsible for volunteer coordination and training at GGD, for the association and for other institutions. Her standing task is identifying and addressing digital and social skill gaps among volunteers, which is '
  'the same diagnostic work this project does with participants. In VERIFAI she runs the recruitment of the Turkish group through GGD’s volunteer network and carries the toolkit into that network afterwards.'],
 ['**Facilitator designated by GGD**\n[TO CONFIRM: name]',
  'A facilitator from GGD’s team with practice in digital content production and generative AI tools, and experience of non-formal work with young people. Joins in month 4, takes part in observer calibration, '
  'co-facilitates the debate session on Day 2 and the cross-examination on Day 4, supports the Day 3 and Day 6 modules, and independently second-scores five participants on Day 4.'],
 ['**Specialist support on call**',
  'GGD’s wider expert group is available to the project without being on its budget: an adolescent health specialist (Assoc. Prof. Dr Aylin Yetim Şahin) and a paediatrician (Prof. Dr Ayşe Kılıç) for questions of '
  'adolescent wellbeing, a child development specialist and general secretary (Tuğba Nur Saray), and a lawyer (Serhat Aydemir) with experience in KA154 youth projects. For an exchange in which every participant is a '
  'minor, having that range reachable in the partnership is a safeguarding asset rather than a line in a CV.'],
], widths=[4.2, 12.4])
COUNT()

H2('Partner — KEA IM Syrou (Greece)')
TBL([
 ['Field', 'Entry'],
 ['Organisation ID (OID)', 'E10151458'],
 ['Legal name', 'KENTRO EREUNAS KAI ANAPTYXIS IERAS MHTROPOLIS SYROU\nΚΕΝΤΡΟ ΕΡΕΥΝΑΣ & ΑΝΑΠΤΥΞΗΣ ΙΕΡΑΣ ΜΗΤΡΟΠΟΛΕΩΣ ΣΥΡΟΥ'],
 ['Acronym', 'KEA'],
 ['Country / Region / City', 'Greece / South Aegean / Syros'],
 ['Website', 'www.keaimsyrou.gr'],
 ['Type of organisation', 'Non-governmental organisation / association — main area of action: training, education and human resources development'],
 ['Is the organisation a public body? / non-profit?', 'No / Yes'],
 ['Legal representative', 'Bishop Dorotheos Polikandriotis, President'],
 ['Contact person', 'Prof. Nikos Chrysinis, General Director — info@keaimsyrou.gr'],
 ['Additional contact', 'Manolis Papamakarios, Project Manager'],
], widths=[5.0, 11.6], count=False)

Q('What are the activities and experience of the partner organisation in youth work?')
P('KEA IM Syrou is a non-profit organisation based on Syros, in the South Aegean, working on social and economic integration, on countering exclusion and on equal opportunities across **36 inhabited islands** of the '
  'region — the Cyclades and the Dodecanese. That reach is the point: it is not an organisation in one island town, it is the body that carries EU and Greek State programmes out to islands where nothing else arrives.')
P('Its standing services go well beyond project delivery: vocational counselling and career guidance, business plan development, individual psychological and social support, social and cultural integration programmes, '
  'informal education for adults and young people, and networking between local businesses, social institutions and municipalities for regional development. It also runs self-financed facilities — a hostel for people '
  'who are poor, disabled, refugees or immigrants; painting and iconography workshops; a **creative activity centre for children and young people**; a daycare centre for older people; and a family responsibility centre.')
P('In the areas this project works on, KEA manages large projects funded by ESF+, Interreg Greece–Cyprus, Erasmus+, national frameworks and LEADER/CLLD. Four strands matter here. First, **young people and '
  'NEETs**: it coordinated //PNAI ANERGOI// (South Aegean, ESF, 2022–2024, 415,350 EUR), training, counselling and certifying low-skilled young people including those with an immigrant background, and it took part in '
  '//AmuNEET// under the ALMA initiative on youth unemployment. Second, **children and adolescents in vulnerability**: it is currently implementing a two-year ESF+ //Local Action Plan for Tackling Child Poverty// in the '
  'island municipalities of Naxos and Kea (2026–2028), combining psychological assessment and social counselling with a voucher-based aid system, parental empowerment workshops, school dropout prevention seminars and '
  'professional orientation days for young people, all tracked on a digital monitoring platform. Third, **digital work**: it coordinated the digitisation of cultural and religious heritage and the creation of a digital '
  'museum (EPAnEK, 453,000 EUR). Fourth, **Erasmus+ specifically**: it coordinated //I.D.E.A.// (2019-1-EL01-KA204-063049), an interactive toolset helping adult educators boost entrepreneurship among NEETs, and was a '
  'partner in //Meta Skills// (2021-1-RO01-KA220-ADU-000028211).')
P('That last reference is worth noticing. //Meta Skills// was coordinated from Romania and contracted by this same National Agency, so the administrative conventions of RO01 are not new to KEA. For a consortium whose '
  'main risk is a partner meeting a set of rules for the first time, that is a real reduction in risk rather than a reassurance.')
P('KEA is a newcomer to this Action rather than to the Programme: it has not previously taken part in a KA152 youth exchange. Its Erasmus+ experience is in adult education partnerships, and its youth work has been delivered '
  'through national and ESF programmes rather than through Erasmus+ mobility. This project is therefore its first Erasmus+ youth mobility, undertaken alongside a coordinator that carries the financial and reporting '
  'load — which is one of the things the National Agency has said it wants to encourage.')

H4('What KEA brings to VERIFAI, and where it does not overlap')
P('KEA brings two things neither of the other partners has. The first is **reach into genuine island isolation**: through its work across 36 inhabited islands it can recruit young people from small island communities '
  'that no national programme reaches, and it can host a local initiative there afterwards. The second is **method for the community day and for the local initiatives**. The Day 5 dialogue — young people sitting down '
  'with residents and municipal representatives to find out what false information actually circulates in a place and who it hurts — is a facilitated social-work exercise before it is a media-literacy one, and KEA '
  'staffs it with a social worker and a counsellor who do this professionally. Its child-poverty action plan runs on exactly this kind of networking with municipal Community Centres and local services, which is also '
  'why it is the right partner to design the template the four local initiatives are built on.')
P('KEA also leads the Day 2 strand on **how information circulates in small island communities** — regional media, community pages and local channels spread across dozens of islands, which no national fact-checker in '
  'Athens covers. It is the same mechanism our Hungarian-language material shows in Cluj County, arriving by a different route.')
COUNT()

Q('Please describe the profile of each of the group members and what does each one bring to the project.')
TBL([
 ['Person and role', 'Profile and contribution'],
 ['**Prof. Nikos Chrysinis**\nGeneral Director; contact person',
  'Master’s degrees in Computer Science and in Human Studies and Adult Education. Adjunct instructor in computer sciences at the New York Institute of Technology (1986–1988) and assistant professor at the Technological '
  'Institute of Athens; from 1996 to 2015 Managing Director of the Unified Vocational Training Centre of the Cyclades, a non-profit founded by the Cyclades local authorities, where he designed and implemented strategic '
  'plans for the region’s municipalities. Responsible at KEA for coordinating and implementing EU-funded programmes. In VERIFAI he carries KEA’s institutional commitment and the relationship with the island '
  'municipalities that host the Greek local initiative. A partner whose director spent three decades between computer science and adult education is well placed to judge whether a digital-verification programme is '
  'sound.'],
 ['**Manolis Papamakarios**\nProject Manager',
  'Graduate of Product and Systems Design Engineering, University of the Aegean (Syros campus), and of Accounting at the School of Management and Economics, TEI of Larissa. More than ten years on European projects, '
  'with responsibility for awareness raising and dissemination locally and internationally, for networking and publicity, for workshops with young people, and for procurement, tendering, monitoring and financial '
  'reporting to EU standards. In VERIFAI he is KEA’s operational counterpart to the coordinator: deliverables, reporting, and the dissemination of results across the South Aegean.'],
 ['**Evgenia Kalogeropoulou**\nSocial worker; Greek group leader',
  'Social worker with a background in Social Anthropology (Panteion University) and Social Work (University of West Attica), with public-service experience and extensive practical training in supporting vulnerable '
  'groups. In VERIFAI she leads the Greek group — recruitment, preparation, accompaniment, the daily reflection in Greek — designs and facilitates the Day 5 community dialogue with KEA, and observes one mixed team on '
  'Day 4. The safeguarding counterpart for the Greek group is hers. [TO CONFIRM: that she travels as group leader.]'],
 ['**Ioulia Dialeisma**\nProject coordinator; career guidance and counselling',
  'University degree in Philosophy, Pedagogy and Psychology from the University of Athens. Career guidance and counselling specialist — career development, employment counselling, empowerment and entrepreneurship '
  'guidance for adults and for young people; from 1996 to 2015 responsible for counselling in the Job Placement Programme of the Unified Vocational Training Centre of the Cyclades, and since then project coordinator '
  'for KEA on national and international projects addressing youth unemployment. In VERIFAI she contributes the methodology of the local initiatives and the reflection design, and is the second accompanying adult for '
  'the Greek flow. [TO CONFIRM.]'],
], widths=[4.2, 12.4])
P('The Greek group travels with two adults because of the journey itself. Seven participants, all minors, travelling from a Cyclades island to the Apuseni Mountains — ferry to Piraeus, then overland — is the longest and most complex journey in '
  'this project, with at least one transfer where a group of fourteen-year-olds could be split. The Romanian and Turkish flows each carry a group leader and a facilitator; the Greek flow would otherwise carry one adult '
  'for seven minors. The National Call allows one group leader for every four young people, so four group leaders for twenty-one participants remains below that ceiling, and the Call makes explicit provision for '
  'well-justified cases involving minors. Six adults accompany twenty-one minors — one adult per 3.5 participants.')
COUNT()

PAGEBREAK()

# =====================================================================
H1('Project rationale')
H2('Needs and objectives')

Q('Why do you want to carry out this project? Please describe the issues and needs you want to address and your project’s objectives.')
P('Young people aged 14–17 in the Napoca Porolissum territory and in the peripheral partner communities of the İstanbul periphery and the South Aegean islands use digital content '
  'and AI tools every day, but have not acquired the habit of checking the source, the author, the date and the context of a piece of information before believing it and passing '
  'it on. That is the need, and it is measured rather than assumed.')
P('Between spring and summer 2026 we ran a bilingual Romanian/Hungarian survey among young people in our territory and received 153 responses from 12 of our 14 localities. '
  'Ninety-six respondents are aged 14–17, exactly the target group of this project. Among them, 96.9% already use AI tools and 20.8% rate their own digital competence as low, with '
  'a group mean of 3.25 out of 5; 31.3% have never taken part in any non-formal education activity; 37.5% name lack of information as the first barrier to joining a mobility, '
  '34.4% cost and 31.2% transport; 68.1% learn through practical activities against 29.8% through a course; 58.5% want activities organised in or near their own locality; and '
  '85.4% would take part in an Erasmus+ activity organised by us. Read together, those figures are the whole problem: use is universal, competence has not followed.')
P('The same picture appears in Greece, where KEA IM Syrou produced a needs analysis for the South Aegean. Greece scores 50.96 on the DESI index for basic digital competences, '
  '22nd of 27 Member States against an EU average of 60.40, and the deficit is sharpest in isolated island areas. In a 2025 nationwide survey Greek students named misinformation as a primary risk only fifth, behind data theft, excessive use and contact with strangers. The consequence is '
  'measurable: 80% of Greek students cannot distinguish a real article from a fake one or from a sponsored advertisement, and many report judging an article by the size of its '
  'photograph. Greek academic studies confirm the same gap we found, where self-reported confidence rarely matches performance in a structured assessment.')
P('Read against our own data the two territories line up almost exactly. Romania has the highest share of young people with low digital skills in the Union; Greece sits 22nd of '
  '27. Here, 96.9% of 14–17-year-olds use AI tools while rating their own competence barely above the midpoint; there, four fifths of students cannot tell a real article from a '
  'fake one while naming misinformation as only their fifth concern. The same overconfidence, in the two places in Europe least equipped to correct it, is the shared condition '
  'this partnership is built on. GGD completes the picture with the same ten-question consultation in its own community before submission, with at least 20–25 young people aged '
  '14–17 from the İstanbul periphery and the rural localities it works with, delivered as a one-page needs note. [TO CONFIRM: GGD’s findings.]')
P('European data points the same way. The Flash Eurobarometer “Youth Survey 2024” (EP013EP), carried out by Ipsos for the European Parliament among 25,863 respondents aged 16–30, '
  'found that more than three quarters of young Europeans believe they met disinformation in the previous week while 70% feel confident they can recognise it. Romania records the '
  'highest share in the Union of young people saying they encountered none at all, 19% against 1% in Cyprus, while 31% declare themselves very confident: Romanian young people '
  'are simultaneously the least likely in Europe to notice disinformation and among the most certain they would recognise it.')
P('That shapes the design. If the problem were a lack of confidence the answer would be encouragement; because it is untrained confidence, the answer is a controlled experience of '
  'being wrong. Day 1 starts with participants mapping their own media diet rather than with a presentation, and on Day 2 the false material is judged before the verdict is '
  'revealed. It is also why the project needs a genuinely international group: a stereotype is at its least defensible when a young person from the community it targets is in the '
  'room.')
P('The three communities do not look alike and we will not pretend they do, but what their young people share is narrow and exact. They are peripheral in three different ways — an '
  'isolated rural mountain area of 14 localities, a metropolitan periphery with the rural communities beyond it, and small islands scattered across a region of 36 — which produces '
  'the same result at the door of a European programme: a journey longer, costlier and harder to organise than from a capital city. Information reaches them through channels '
  'nobody corrects, since national fact-checkers work in the majority language on national subjects while community life here runs partly in Hungarian, in the İstanbul periphery '
  'through neighbourhood and family networks, and in the South Aegean through regional media and community pages across dozens of islands nobody in Athens monitors. And in all '
  'three, use has outrun competence. The practical offer that would fix this exists in none of them.')
P('Against that need the project sets three objectives, worded here exactly as they appear in the project summary and in the evaluation section.')
NUM([
 'By the end of the project, at least 17 of the 21 young participants aged 14–17 will improve their mean score on the assessment of online information verification competences by '
 'at least 30% compared with the initial assessment.',
 'By the end of the project, at least 17 of the 21 participants will correctly demonstrate, in a practical exercise, at least four verification techniques: identifying the source '
 'and the author, checking the date and the context, comparing with independent sources, and verifying images or claims.',
 'In the follow-up stage, the 21 participants will transfer the methods learned to at least 80 young people in the partner communities, through at least four local initiatives, '
 'and at least 70% of the beneficiaries of those initiatives will be able to apply at least two simple verification methods.',
])
COUNT(6000)

Q('How does your project link to the objectives of the Erasmus programme and those of Youth Exchanges?')
P('Digital transformation is the substance of this project rather than its label. VERIFAI builds the part of digital competence that use alone never produces, because our '
  'participants can already operate the tools but cannot find out where something came from. The project develops three things in order: using digital and AI tools responsibly '
  'and with their limits understood; checking sources, meaning who published an item, who wrote it, when, in what original context, and whether any independent source says the '
  'same; and recognising false, manipulated or artificially generated content, including content they could produce themselves. That priority defines the need, the participant '
  'profile, every method in the agenda, the four media products, the toolkit and the two instruments that measure whether it worked. It also matches what the National Agency has '
  'said it is looking for in 2026, since among projects addressing digital transformation priority goes to those that tackle disinformation and promote digital literacy.')
P('Checking a claim is also a precondition of taking part in democratic life, because without it a vote, a public argument or a civic initiative rests on false premises. Our '
  'participants are 14 to 17 now, which means most of them will cast their first ballot within four to six years of this project, and the point is that by the time they get there '
  'forming an opinion on information they have actually checked is a habit rather than an effort. In the meantime they practise the civic half of it for real: through the four '
  'local initiatives they step out of the learning room and into their own communities, working with youth organisations, libraries, community centres and local authorities, and '
  'taking responsibility for an activity that other young people attend.')
P('Inclusion runs through the design rather than alongside it, and each barrier our participants face is answered by a concrete measure. The exchange is hosted inside our own '
  'territory and transport is paid from each participant’s own front door, which answers the geographic barrier; there is no participation fee of any kind, stated in writing from '
  'the day the call is published, which answers the economic one; and preparation runs over four months rather than four weeks, with a parents’ meeting in each country before consents are '
  'signed and a stated right to leave a session without giving a reason, which answers the social one. English is not a selection criterion and A2 is accepted, with a glossary '
  'built in four languages, so that language is never a filter for anyone. At least 13 of the 21 participants face documented barriers and at least 16 travel on a '
  'European mobility for the first time. The measures are set out in full under Participants with fewer opportunities.')
P('The Action’s own objectives are addressed directly. Youth Exchanges exist to encourage intercultural dialogue and learning and a sense of being European, to develop young '
  'people’s competences and attitudes, to strengthen European values and break down prejudice and stereotypes, and to raise awareness of socially relevant subjects. VERIFAI meets '
  'each of these, and the third structurally, because the working material of Day 2 includes real content that feeds ethnic, gender and migration stereotypes, analysed in mixed '
  'teams in which young people from the targeted communities are present.')
P('Within the EU Youth Strategy the project addresses Goal 4, Information and Constructive Dialogue, which is its very object; Goal 6, Moving Rural Youth Forward, since the '
  'activity takes place in a rural mountain territory and the multiplication happens in the participants’ own localities; and Goal 9, Space and Participation for All, since '
  'participants co-design the programme, choose the subjects to be verified and lead their own local initiatives. In the Strategy’s “Connecting” field of action it creates '
  'exactly the link the Strategy looks for, with young people from three European peripheries discovering that they have the same problem and working on it together.')
P('Common EU values are anchored in three concrete places rather than declared. Disinformation attacks human dignity through dehumanising content, equality through algorithmically '
  'amplified stereotypes, and the rule of law by eroding trust in institutions. Against that, the ground rule of the exchange is that any claim made in debate must be verifiable '
  'and it applies to facilitators exactly as to participants; the group agreement negotiated by the participants on Day 1 includes non-discrimination and respect for every '
  'language and identity present, Romanian, Hungarian, Turkish and Greek; and the analysis of stereotype-bearing content is deliberately done in the presence of the people it '
  'targets.')
COUNT()

H2('Impact')
Q('How will your project benefit the young participants involved in the project, during and after the project lifetime?')
P('Every participant takes the same fifteen-item practical verification test in month 2 and its equivalent in month 18, and we expect at least seventeen of the twenty-one to improve '
  'their score by at least 30%. During the mobility an observation grid records whether each of them actually performs four named techniques in the Day 4 simulation, rather than '
  'whether they can describe them. That distinction matters here more than it would elsewhere, because our starting point is a group that already believes it can spot a fake, so '
  'the gain has to be documented rather than asserted.')
P('For most of them this is also a first European experience. At least 16 of the 21 will be taking part in a European mobility for the first time, and in our territory 31.3% of '
  'young people aged 14–17 have never taken part in any non-formal education activity at all. For those participants the gain is not only thematic, because working in a mixed '
  'international team, in English, with people they have never met, is itself the learning — and it is what they asked for, since 60.4% of the 14–17 group named foreign languages '
  'and intercultural communication as what they most want out of a European mobility.')
P('The project also gives them something to do afterwards. Each participant leaves the mobility with a written commitment and a role in one of the four local initiatives, which '
  'they design and lead themselves while the group leader supports rather than directs. This is where a fifteen-year-old moves from “I learned something” to “I taught twenty '
  'people”, and in our experience it is the part that changes how they see themselves.')
P('What they learn, they can name, document and use. Youthpass is worked on from Day 1 through a learning diary and daily reflection groups, held in the national group and in the '
  'participant’s own language first and then in plenary, and closed on Day 7 in a dedicated session. The value lies in the process rather than the paper, because it teaches a '
  'sixteen-year-old to identify what they actually learned, document it with evidence they can point to, and present it in a form someone else understands. That is what makes the '
  'certificate usable afterwards, in the next learning activity they join, in volunteering, in a civic initiative in their own community, and in the next international mobility '
  'they apply for.')
P('Six months after the exchange a follow-up questionnaire asks what they still use. The honest expectation is not that all twenty-one become fact-checkers, but that they have '
  'acquired a reflex — the pause before sharing — and that the four local initiatives have given at least some of them a taste for organising something in their own community.')
COUNT()

Q('How will your project benefit the organisations or the groups of young people implementing the project, during and after the project lifetime?')
P('For the coordinator this is a deliberate step in the organisation’s development. LAG Napoca Porolissum has run youth projects as partner and as coordinator, but never as '
  'hosting organisation for a youth exchange, and hosting means owning the learning programme, the venue, the safety of twenty-one minors and the relationship with the host '
  'community. It converts a network of 43 members and 14 municipalities from a rural-development asset into a youth-work asset, and the organisation ends the project with a '
  'tested non-formal learning programme, three measurement instruments it did not have, and a child protection policy that will apply to everything it does afterwards.')
P('Genç Gönüllüler Derneği brings production and technology expertise and gains the verification methodology it currently lacks. For an organisation that already convened a '
  'hundred specialists to work out what children need from digital content, and that has an artificial intelligence and cyber-security specialist on its team, a structured '
  'approach to source verification is the missing half of what it teaches. GGD takes the toolkit into the volunteer network it trains every year and into the rural youth '
  'programme it runs with the Turkish Ministry of Interior.')
P('For KEA IM Syrou this is a first Erasmus+ youth mobility. Its Erasmus+ experience is in adult education partnerships and its youth work has run through national and ESF '
  'programmes, so it gains a first structured experience of KA152 alongside a coordinator that carries the financial and reporting load. It also gains a tested method it can put '
  'into its creative activity centre for children and young people and carry out to the 36 islands it already serves, where the alternative is nothing at all, and one that sits '
  'naturally inside the child-poverty action plan it is currently implementing in Naxos and Kea, which already includes school dropout prevention and professional orientation.')
P('Together the three produce something none of them has separately: an evidenced answer to a problem all three communities share, in a form other peripheral territories can pick '
  'up. In month 17 they formally assess whether to continue, and with what — either a second exchange hosted by another partner, or a youth participation project on dialogue with '
  'local decision-makers — and the decision is minuted either way, including if it is not to continue.')
COUNT()

Q('What would be the impact of your project beyond the participants and participating organisations, at local, regional, national, if any European level?')
P('Locally, at least 80 young people are reached directly through the four local initiatives, hosted in youth centres, libraries, community centres, the partner organisations’ '
  'own spaces and other accessible public places. In Romania the results are also presented across the 14 localities of the territory through the community events the '
  'organisation already runs every year, so that young people who did not take part still meet the material and the four media products circulate where the myths they debunk '
  'actually circulate.')
P('Regionally, the “Digital Detectives” toolkit is offered free of charge to the youth organisations, libraries and community centres of the territory, with a presentation '
  'session for the youth workers and librarians who will use it, and the 14 partner municipalities receive the evaluation report and a short set of recommendations. Romania has '
  'no coordinated national media-literacy strategy and its policies in this area are fragmented across separate legal frameworks, so a tested, free, ready-to-use set of materials '
  'in the hands of people who already work with rural young people has a value out of proportion to the size of this project.')
P('Nationally and at European level the results are published on the Erasmus+ Project Results Platform. GGD disseminates through its own channels and volunteer network, and KEA '
  'through a website with more than 12,000 unique visitors a month, a newsletter of 800 recipients and a working relationship with more than 80 regional media outlets across the '
  'South Aegean. The coordinator shares the method through the LEADER and ELARD networks, where it already has transnational cooperation experience, reaching Local Action Groups '
  'across rural Europe — an audience that rarely encounters media-literacy tools at all. The target is at least four organisations outside the partnership confirming in writing '
  'that they use the toolkit.')
P('We state the limits of this as plainly as the ambitions. Twenty-one participants will not move a county-level statistic. The contribution is measurable change in twenty-one young '
  'people, documented extension to at least eighty more, and instruments that stay in use in three organisations after the project ends.')
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
 ['01', 'Youth exchanges', 'VERIFAI: Young Detectives Against Digital Disinformation', '21', '27', '27,094.00'],
 ['', '', '**Total**', '**21**', '**27**', '**27,094.00**'],
], widths=[1.2, 2.6, 6.0, 2.4, 2.0, 2.4], count=False)

H3('Participant contribution and fees')
Q('Are you planning to ask for any contributions from participants?')
P('**No** — and this is a decision rather than an omission. In our survey, cost is the second barrier young people aged 14–17 name to taking part in a mobility (34.4%) and transport is the third (31.2%). A fee of any size would '
  'filter out precisely the young people this project exists for, and a family deciding whether to let a fourteen-year-old leave the country for nine days should not also be deciding whether they can afford it. Since '
  'at least 13 of our 21 participants are participants with fewer opportunities, from whom the Programme does not permit fees in any case, a fee would also have to be charged to some participants and not others — '
  'inside a group of twenty-one who spend nine days together. The rule is therefore written into the local call in all three countries from the day it is published: travel, accommodation, meals, insurance, materials and '
  'transport from the participant’s own front door are covered in full, and nothing is asked of the participant or the family at any point.')
COUNT(2000)

H2('Activity 01 — description')
TBL([
 ['Field', 'Entry', 'Field', 'Entry'],
 ['Id.', '01', 'Total no. of participants', '21'],
 ['Activity Type', 'Youth exchanges', 'Of which, with fewer opportunities', '13'],
 ['Activity Title', 'VERIFAI: Young Detectives Against Digital Disinformation', 'No. of group leaders', '4'],
 ['Start date', '09/08/2027', 'No. of facilitators', '2'],
 ['End date', '15/08/2027', 'No. of accompanying persons', '0'],
 ['Duration excluding travel', '7 days', 'Total no. of persons', '27'],
 ['Travel days', '08/08/2027 arrival\n16/08/2027 departure', 'Total Activity grant', '**27,094.00 EUR**'],
], widths=[3.6, 4.7, 3.6, 4.7], count=False)

H3('Flows summary (Activity 01)')
TBL([
 ['Flow', 'Place of origin', 'Participants', 'Group leaders', 'Facilitators', 'Persons', 'Fewer opport.', 'Distance band', 'Travel', 'Days'],
 ['1', 'Cluj County, Romania\n[TO CONFIRM: departure city]', '7', '1', '1', '**9**', '5', '10–99 km', 'Green', '9'],
 ['2', 'İstanbul, Türkiye', '7', '1', '1', '**9**', '4', '500–1,999 km', 'Green', '11'],
 ['3', 'Syros, South Aegean, Greece\n[TO CONFIRM: departure point]', '7', '2', '—', '**9**', '4', '500–1,999 km', 'Green', '11'],
 ['', '**Total**', '**21**', '**4**', '**2**', '**27**', '**13**', '', '', ''],
], widths=[0.9, 3.4, 1.6, 1.5, 1.5, 1.3, 1.5, 1.9, 1.3, 1.0], small=True, count=False)
SMALL('City of venue for all three flows: Beliș, Cluj County, Romania — a commune of the Napoca Porolissum territory in the Apuseni Mountains [TO CONFIRM: the accommodation unit]. Start 09/08/2027 and end 15/08/2027 for all three. '
      '“Days” counts the 7 activity days plus 2 travel days, and for flows 2 and 3 the 2 additional days that green travel over that distance makes eligible. The three groups are split into separate flows because they '
      'sit in two distance bands and two durations — which is what the form’s own definition of a flow requires. The Greek flow carries two group leaders: see the note under the Greek partner’s staff.')

H3('Budget per flow and activity budget summary')
TBL([
 ['Flow', 'Travel', 'Individual support', 'Flow total'],
 ['1 — Romania (9 persons)', '9 × 56 = 504.00', '9 × 9 × 46 = 3,726.00', '4,230.00'],
 ['2 — Türkiye (9 persons)', '9 × 417 = 3,753.00', '9 × 11 × 46 = 4,554.00', '8,307.00'],
 ['3 — Greece (9 persons)', '9 × 417 = 3,753.00', '9 × 11 × 46 = 4,554.00', '8,307.00'],
 ['**Subtotal, flows**', '**8,010.00**', '**12,834.00**', '**20,844.00**'],
 ['Organisational support', '', '125 × 21', '2,625.00'],
 ['Inclusion support for organisations', '', '125 × 13', '1,625.00'],
 ['Inclusion support for participants', '', 'real costs, separate lines', '2,000.00'],
 ['**Total Activity grant**', '', '', '**27,094.00**'],
], widths=[5.6, 3.6, 3.8, 3.6], count=False)
SMALL('The preparatory visit (3,400.00 EUR) sits at project level, not inside the activity, which is why the project total is 30,494.00 and the activity grant 27,094.00.')
PAGEBREAK()

Q('Please describe the background of the participants in each participating group and how each group was formed. Please also provide information on the group leaders, the age of the participants and how country balance is ensured. If necessary, explain how the gender balance is respected.')
P('The Romanian group brings seven young people aged 14–17 and one group leader, drawn from the rural mountain communes of the territory — Săcuieu, Gilău, Huedin, Mărișel, '
  'Căpușu Mare, Mărgău, Măguri-Răcătău, Călățele, Beliș, Mănăstireni, Aghireșu and Izvorul Crișului — communities with a thin offer of youth activities and information '
  'circulating in two languages. From our survey of this exact population, 96.9% already use AI tools, 20.8% rate their digital competence as low, 31.3% have never taken part in '
  'a non-formal activity, and lack of information is the first barrier they name. The group is deliberately mixed linguistically, with at least one Hungarian-speaking '
  'participant, because the language question is part of the subject matter.')
P('The Turkish group brings seven young people aged 14–17 and one group leader from the İstanbul metropolitan periphery — the Sarıyer district and around it, dense and diverse, '
  'including families with migrant and refugee backgrounds — and from the rural localities GGD reaches through the rural youth programme it runs with the Turkish Ministry of '
  'Interior. In both, information travels through neighbourhood, family and community networks that national fact-checking never reaches. GGD recruits through the volunteer '
  'network it trains every year, prioritising young people who have never taken part in an international activity, and its standing work identifying digital skill gaps among '
  'those volunteers is how it knows where to look. [TO CONFIRM: the urban/rural composition, the localities, and GGD’s consultation data.]')
P('The Greek group brings seven young people aged 14–17 and two group leaders from small islands of the South Aegean, recruited through the network KEA operates across 36 '
  'inhabited islands of the Cyclades and the Dodecanese. Their isolation is not metaphorical: for a fourteen-year-old on a small island any learning activity means a ferry, and '
  'what exists in Athens does not reach them. The national data behind this group is in the needs section, where Greece sits 22nd of 27 on basic digital competences and 80% of '
  'students cannot tell a real article from a fake one. The group travels with two accompanying adults because of the length of the journey. [TO CONFIRM: the islands and the '
  'departure point.]')
P('All three partners form their groups on one common recruitment backbone, published simultaneously in month 1 with the same criteria translated into Romanian, Hungarian, '
  'Turkish and Greek, aiming for at least 63 applications for the 21 places. Selection is by a commission of at least two people per organisation, on a written form plus a short '
  'conversation, with the outcome and the reasons given to every candidate. The criteria are identical in all three countries: age 14–17 at the start date, which is eliminatory; '
  'motivation and willingness to run a local initiative afterwards, weighted 30%; first participation in a European mobility or any non-formal activity, weighted 25% with a '
  'target of 16 of 21; a situation limiting access to opportunities, declared voluntarily and confidentially, weighted 25% with a target of 13 of 21; and gender and locality '
  'balance, weighted 20%. English is not among them, and A2 is accepted, because the programme is built on visual and practical methods, pair work and linguistic support from '
  'the group leaders so that language does not become a social filter — a language test at the door would convert the 12.5% who name lack of self-confidence into exclusion.')
P('All twenty-one participants are aged 14 to 17 at the start date, and the band is deliberately tight. They share the same need, since the survey evidence behind this project '
  'describes exactly this age group, and they are at a similar stage of development, so one register of language and one set of expectations about autonomy works for the whole '
  'room instead of two. That also lets us use one coherent set of non-formal methods — visual, practical, game-based, built on small mixed teams and peer teaching — that fits '
  'all of them. A band crossing into legal adulthood would put minors and adults in the same accommodation, which is a safeguarding problem before it is a learning one.')
P('Country balance is held by three equal groups of seven, one from Romania, one from Türkiye and one from Greece, so that no national group is larger than another and none holds a majority of the twenty-one. '
  'The balance is enforced where it matters, in the working teams: the cohort is '
  'divided into four mixed teams of five or six, each containing members of all three national groups, recomposed daily, so every participant works with every nationality repeatedly '
  'rather than once. Gender balance is binding at group level rather than an aspiration at project level, with each national group including at least 40% of each gender — three '
  'in every group of seven — and the team of four group leaders itself gender-balanced. Participants who do not identify within that binary are counted by '
  'their own declaration and are not required to declare anything, and the activity coordinator checks both rules at selection and at final confirmation.')
P('Four group leaders accompany the groups, all aged 18 or over, experienced in youth work and in accompanying minors, staying with their groups throughout including at night: '
  'one for Romania, one for Türkiye and two for Greece. We propose Livia Golovatic for Romania, M. Talha Serenli for Türkiye, and for Greece Evgenia Kalogeropoulou, a social '
  'worker trained in supporting vulnerable groups, with Ioulia Dialeisma as second accompanying adult. [TO CONFIRM with the partners.] Each is responsible for safeguarding, the '
  'daily reflection in the group’s own language, attendance, the code of conduct, observing one mixed team on Day 4, and afterwards the group’s local initiative. Four leaders for '
  'twenty-one participants is below the National Call’s ceiling of one per four, and with the two facilitators it gives six adults for twenty-one minors. All four take the two-day '
  'leaders’ briefing in month 4.')
COUNT(6000)

Q('Please describe the role and involvement of the participants from each participating group in all phases (planning before, during and follow-up).')
P('The subject of this project was not chosen by the coordinator’s staff. It came from 153 young people in the territory who answered our survey, and it was then put back to them for checking. Three '
  'things in this application exist because they asked for them. They told us where to hold it: 58.5% asked for learning activities in or near their own locality, so the exchange is hosted inside the LAG territory '
  'rather than in a comfortable host city, and the host community became part of the programme on Day 5 instead of being scenery. They told us what stops them: cost and transport are the second and third barriers they '
  'name, so there is no participation fee of any kind and transport is paid from each participant’s own front door. And they told us how they learn: 68.1% through practical activities against 29.8% through a course, '
  'so there are no lectures in this programme and every session produces an output or a decision taken by the participants themselves. A validation meeting with 8–10 young people from the territory, held before '
  'submission, confirms the wording of the need, reviews the objectives in plain language, and produces the first list of the claims and rumours they want checked — a list that becomes the working material of Day 2.')
P('In the planning phase, months 1 to 4, participants do not simply wait for August. Four online sessions of 90 minutes each bring the three groups together in mixed national composition, not country by country. '
  'Session 1: meeting each other and negotiating the first draft of the group agreement. Session 2: participants choose the local disinformation cases that will be analysed during the mobility — each group brings '
  'five to eight documented real cases from its own community, and the participants themselves decide which ones make the working set. Session 3: distribution of roles for the mobility — photo and video '
  'documentation, activity diary, energisers, mediation, contact with the host community, timekeeping — and preparation of the intercultural evening. Session 4: safety, digital rules, practical arrangements, and '
  'questions answered live by the group leaders. Between sessions a moderated communication group keeps the cohort in contact. A separate online meeting is held with the parents, in each country and in its own language.')
P('During the mobility, every day has a host team of the day: a mixed team of three participants, one from each country, who open the day, keep the timing, run the energisers and close the day. Seven days at three hosts a day comes to exactly twenty-one, so every participant leads once and nobody is only an audience. The four working '
  'teams are recomposed daily so that every participant works with every nationality repeatedly. The daily reflection groups — first in the national group and in the participant’s own language, then in plenary — feed '
  'directly into adjusting the next day’s programme, and the adjustments are made visibly, so participants see their feedback change something rather than disappear into a form. On Day 6 the participants plan their '
  'own local initiatives: date, venue, audience, partners, who does what.')
P('In the follow-up phase, months 6 to 18, four local initiatives are designed and led by the participants, with the group leader in a support role rather than a coordinating one: **two in the Romanian territory, in different '
  'communes, one in Türkiye and one in the South Aegean.** The Romanian group has seven participants drawn from twelve localities and a coordinator with fourteen partner municipalities, so a single event in one '
  'commune would reach the wrong young people; two smaller initiatives in different communes is more faithful to the territory and reaches further into it. Each initiative reaches at least 20 young people and is '
  'hosted in a youth centre, a library, a community centre, the partner organisation’s own space or another accessible public place in the participants’ own community. In month 17 the participants take '
  'part in a participatory evaluation session that feeds the final report — so they close the project as evaluators rather than as beneficiaries. The cohort communication group stays open throughout, and all four '
  'organisations involve the twenty-one as peer trainers in their later activities.')
COUNT(6000)

Q('What will the participants learn about the chosen topic of the activity? Which learning outcomes or competences (i.e. knowledge, skills and attitudes/behaviours) are to be acquired/improved by participants in the activity?')
P('What the participants learn is written here as what they will be able to do afterwards, because that is the only form of learning we can actually check. The framework is the '
  'eight European key competences for lifelong learning, the one Youthpass uses, and behind every claim below there is a session that builds it and a piece of evidence that '
  'records it. The rule runs in both directions: no session in the programme is without a learning outcome, and no competence appears here without a session and evidence.')
P('The centre of it is **digital competence (KC4)**, and it is built in an order rather than all at once. A participant arrives fluent at using a phone and untrained at '
  'interrogating what appears on it. On Day 1 they map one ordinary day of their own media diet, which for most is the first time anyone has asked them to look at it. '
  'By the end of Day 2 they can name the mechanics that were used on them — the emotional headline, the cropped context, the borrowed authority, the number quoted without its '
  'population or its year — because they have just been taken in by them in front of their team. On Day 3 they generate AI content themselves, try to fool the others with it, '
  'and then write the sheet of indicators they will use afterwards to recognise it. By Day 4 they carry out four techniques on a real viral claim without being prompted: '
  'finding the source and the author, checking the date and the original context, comparing against two independent sources, and testing an image or a claim, reverse image '
  'search included. The evidence is the practical test taken in month 2 and again in month 18, the observation grid applied on Day 4, the AI-recognition sheet they wrote and '
  'the four media products.')
P('The same days build **literacy (KC1)** in a way that school rarely reaches. Participants learn to separate what a text states from what it implies and from what its author '
  'merely believes, to see framing as a choice someone made, and then to do the harder thing: write a verdict on a claim that another person can follow, check and disagree '
  'with, sources named. The manipulation grid they produce on Day 2 and the four written verdicts of Day 4 are what show it.')
P('The competence we care about most is also the least comfortable. **Personal, social and learning-to-learn competence (KC5)** is built by being wrong in public and surviving '
  'it: on Day 2 every team commits to a judgement before the answer is revealed, and the facilitators get some items wrong too, on purpose and visibly. A sixteen-year-old who '
  'has said out loud “I was sure and I was wrong” has learned something that no lecture on media literacy delivers. Around it sit the ordinary skills of working in a team '
  'nobody chose — a group of seven from a mountain commune, seven from the İstanbul periphery and seven from small Aegean islands, recomposed daily so no one settles into a '
  'national corner. Each participant re-reads their Day 1 digital map on Day 7 against their own learning diary and names, with evidence, what changed; that comparison and '
  'Youthpass are the record.')
P('**Citizenship competence (KC6)** is where the topic stops being about phones. Participants come to be able to say why verification is a condition of taking part in '
  'democratic life rather than a technical hobby, to argue a position with evidence and accept being refuted by it, and to sit down with adults who are not their teachers: on '
  'Day 5 with residents of the host commune and municipal representatives, asking what false information actually circulates there and who it hurts. Then they design and lead '
  'something themselves. The group agreement they negotiate on Day 1, the Day 5 record and the four local initiative plans are the evidence, and the initiatives themselves '
  'are the proof.')
P('Two competences grow because of how the group is composed rather than because of a session. **Multilingual competence (KC2)** develops through seven days of working in '
  'English at a functional level with people whose English is also imperfect, interpreting for each other, and discovering that information circulates differently inside a '
  'minority language — a point our Hungarian-speaking participants can make from experience and the Greek group recognises at once. '
  '**Cultural awareness and expression (KC8)** grows from analysing, in mixed teams, how a stereotype about their own community is built and passed on, with someone from that '
  'community in the room, and then from making something: a short video or an infographic that has to be clear, honest and watchable. The manipulation grid in four languages, '
  'the intercultural evening and the four media products carry it.')
P('The follow-up carries **entrepreneurship competence (KC7)**: turning an idea into a plan with a date, a venue, an audience, partners and named responsibilities, then '
  'running it and reporting on what happened, which is a different skill from having the idea. **Mathematical and technological competence (KC3)** is developed in one narrow '
  'but useful direction — reading a statistic critically, asking who was measured, when and how many, what the figure does not say, and recognising a graph built to mislead.')
P('Attitudes are the part we can shape but not certify. What we are aiming at is a reflex, the two seconds of hesitation before sharing; a tolerance for finding out you were '
  'mistaken; the habit of asking who is telling me this and why now; and the confidence of a fifteen-year-old from a village who has stood in front of their own community and '
  'explained something the adults there did not know. We measure the first through the test and the grid and we report the rest as what participants say and do, not as a '
  'number we invented.')
P('We are careful about what we claim. Seven days do not produce expert fact-checkers, and we will not write that they do. What seven days produce is that pause before '
  'sharing, four techniques a participant can actually perform under observation, and one local initiative each has led — which is exactly what objective O2 measures and what '
  'the observation grid records.')
COUNT(6000)
Q('What are the basic elements of the activity? Please describe at the very least the venue(s), non formal learning methods used, aims of the session etc.')
P('The activity is hosted in **Beliș, Cluj County** — one of the 14 communes of the Napoca Porolissum territory, high in the Apuseni Mountains on the shore of Lake Fântânele. '
  'The choice is not convenience. In our survey 58.5% of the young people asked for activities in or near their own locality, so the exchange happens '
  'inside the territory and the host community joins the programme on Day 5. We already work in Beliș — our LINC arts festival and one of our Christmas markets are held there '
  '— so the municipality relationship and the practical arrangements are known quantities. And Beliș suits the subject: '
  'the old village was submerged in the 1970s for the Fântânele reservoir and rebuilt higher up, so what people there say about their own past '
  'already comes in layers.')
P('Practically the venue must provide 30 places in rooms that keep minors with minors and leaders on their groups’ floors, a plenary room for 27, four small-team spaces, '
  'accessibility, and internet that holds — a programme about checking things online cannot run on a connection that drops mid-session, so connectivity is measured on site '
  'during the preparatory visit in month 3. [TO CONFIRM: the unit in Beliș, with a written offer and a connection test.]')
P('The central non-formal method is learning through controlled error: participants receive the false material, commit to a judgement, and only then learn the verdict — the '
  'surprise is what works on overconfidence, and it comes on Day 2 before any teaching. Around it: mixed teams of five or six recomposed daily; simulation and role play (the '
  'newsroom D4.1, the tribunal D2.3, the escape room D3.3); structured debate where every claim must be evidenced, facilitators included; peer teaching (D3.2); '
  'media production on Day 6; daily reflection in the national group in the participant’s own language and then in plenary, with a learning diary, where what comes out visibly '
  'changes the next day; and outdoor activities. There are no lectures: every session ends in an output or a decision taken by the participants themselves.')
P('The programme runs over seven activity days, with 8 and 16 August as travel days. Day 0 is arrival, accommodation and the guided safety tour with an evacuation drill (D0.1).')
P('**Day 1 — who we are and what we consume.** O1, O2. Aim: form the group and make it look at its own habits before anyone teaches. Mixed-team formation (D1.1); the group '
  'agreement the participants negotiate themselves, non-discrimination and respect for all languages present being non-negotiable (D1.2); “My Digital Map”, one ordinary day of '
  'each participant’s media diet (D1.3); the safety, safeguarding and Youthpass briefing (D1.4).')
P('**Day 2 — Spot the Fake.** O1, O2. Aim: break untrained confidence and replace it with named mechanics. Teams commit to a verdict on a mixed set of real and false items '
  'before the answer key is revealed (D2.1); then the mechanics of manipulation, worked on real cases from their own communities, including content carrying ethnic, '
  'gender and migration stereotypes (D2.2); and a debate on where opinion ends and falsehood begins (D2.3). KEA leads the strand on how information travels in island '
  'communities.')
P('**Day 3 — AI or human?** O1, O2. Aim: understand generated content from the inside, which is what makes it recognisable. Participants generate AI content and try to fool '
  'each other, then write their own recognition sheet (D3.1); four teams each test a free verification tool and teach it to the others (D3.2); an escape room '
  'on digital traces (D3.3); the group writes its own rule on using AI honestly (D3.4). Led by GGD.')
P('**Day 4 — fact-checkers for a day, the assessed day.** O2. Aim: have every participant perform the four techniques under observation. A three-hour verification newsroom '
  'takes mixed teams through the full route to a documented verdict, facilitators intervening only when asked (D4.1); the observation grid is applied here — each group '
  'leader observes one team, the two facilitators independently double-score ten of the twenty-one, and the Learning Programme Coordinator moderates without scoring; then '
  'cross-examination of each verdict (D4.2) and a collective analysis of the day’s errors, the facilitators’ included (D4.3).')
P('**Day 5 — community and intercultural day.** O3. Aim: see what disinformation does to a real place and to real people. A visit in and around Beliș (D5.1); a facilitated '
  'dialogue with residents and municipal representatives on the rumours that circulate there and who gets hurt (D5.2), whose record is the working material for Day 6; '
  'the intercultural evening (D5.3). Method led by KEA’s social worker and counsellor.')
P('**Day 6 — Make It, Don’t Fake It.** O3. Aim: turn what they can check into something other people will watch. Led by GGD: how a short video or infographic is built to be '
  'clear and honest (D6.1); production, each team debunking a Day 5 myth under the group’s own AI-use rule (D6.2); and in parallel the groups plan their local '
  'initiatives on KEA’s template — date, venue, audience, partner, responsibilities, indicator (D6.3).')
P('**Day 7 — presentation, evaluation, Youthpass.** O1, O2, O3. Aim: close the learning in public and in writing. A public presentation to guests from '
  'Beliș, the neighbouring communes and the press (D7.1); the Youthpass session, where each re-reads their Day 1 digital map against their learning diary and names, with '
  'evidence, what changed (D7.2); a participatory evaluation (D7.3); and the written, public commitments to the four local initiatives (D7.4).')
P('Every output belongs to the participants: the group agreement, 21 digital maps, the manipulation grid in four languages, the AI-recognition sheet and AI-use rule, four '
  'documented verdicts, four media products in English plus a local language, four initiative plans with named owners, and 25 Youthpass '
  'certificates. The full programme is annexed as the project timetable, where each session carries its objective, method, competences, output and the person responsible, and '
  'the session codes above match it exactly.')
COUNT(6000)
Q('How will the groups of participants cooperate and communicate between them to prepare and follow-up on the Youth Exchange?')
P('Before the exchange, the groups work together in four joint online sessions of 90 minutes in months 3 and 4, in mixed national composition rather than country by country, so the teams that will work together in August have already met. A shared '
  'workspace holds the documents, the case files and the templates; a moderated messaging group, with clear rules and no sharing of personal data, keeps day-to-day contact going. Between sessions each group has a '
  'concrete deliverable for the others: five to eight documented cases of disinformation from its own community, uploaded to the shared space, which the whole cohort then reviews. The group leaders hold their own '
  'separate channel and a two-day online briefing.')
P('During the exchange, cooperation is built into the structure of each day: mixed teams recomposed daily, the host team of the day, the reflection cycle running from the '
  'national group into the plenary, and a visible feedback loop, where changes requested one evening appear in the next day’s programme.')
P('After the exchange, the cohort communication group stays open for the whole 18 months and becomes the working space for the four local initiatives: each group posts its plan and the others comment before it happens. A '
  'joint online meeting is held after the first two initiatives, in month 10, so that the two groups that have not yet run theirs learn from what went wrong rather than repeating it. A follow-up questionnaire in month '
  '12 and a participatory evaluation session in month 17 close the cycle. The four media products and the toolkit circulate through all three organisations’ channels, and each group is expected to disseminate the '
  'other groups’ products, not only its own.')
COUNT()
PAGEBREAK()

# =====================================================================
H1('Project design')
H2('Preparation, support and follow-up')

Q('How will you prepare the participants before the start of the activity (e.g. intercultural, linguistic, risk-prevention etc.) and how will you support them during and after the activity?')
P('Preparation runs over four months rather than four weeks, because 31.3% of the young people in our target population have never taken part in any non-formal education '
  'activity and 12.5% name lack of self-confidence as a barrier. For a fourteen-year-old leaving the country for the first time, the preparation is the inclusion measure.')
P('It begins in month 2 with the baseline, when all 21 participants take the fifteen-item practical verification test before any learning activity, together with a short '
  'questionnaire on media habits. That establishes the starting value for the first objective and tells the facilitators what the group actually cannot do, which is not always '
  'what they say they cannot do. Four joint online sessions of 90 minutes follow in months 3 and 4, held in mixed national teams: meeting each other and drafting the group '
  'agreement, choosing the local cases to be analysed, distributing roles and preparing the intercultural evening, and finally safety, digital rules and practical arrangements.')
P('Linguistic preparation produces a “detective’s glossary” of about 60 working terms in four languages — English, Romanian with Hungarian equivalents, Turkish and Greek — built '
  'with the participants rather than handed to them, plus two light conversation sessions inside the online meetings. The aim is functional confidence rather than language '
  'teaching, since A2 is enough and the programme is built so that it is. Interculturally, each group prepares a short presentation of its own community for the intercultural '
  'evening, including its language, and group leaders run a session on expectations and stereotypes before departure, deliberately, since the project itself works on stereotypes.')
P('On risk prevention and safeguarding, each participant and each parent receives a participant pack containing the programme, house rules, code of conduct, contact chain, '
  'emergency numbers, the safeguarding focal point’s name and direct contact, and the media and consent rules. An online meeting is held with the parents in each country and in '
  'its own language, where questions are answered live. Alongside this run the practical arrangements: parental consents, travel and medical insurance, medical information '
  'sheets, dietary and accessibility requirements and travel bookings, with the visa procedure for the Turkish group starting in month 3. The group leaders take a two-day online '
  'briefing in month 4 on safeguarding, the escalation chain, facilitating reflection and the calibrated use of the observation grid across four different observers. Where a '
  'participant needs support beyond the standard arrangements, it is identified here, in the preparation phase, costed on a separate line and justified by what it makes possible, '
  'rather than requested as a lump sum and explained afterwards.')
P('During the exchange each national group stays with its own group leader throughout, including at night. The daily reflection happens first in the national group and in the '
  'participant’s own language, which is where a participant who is struggling is most likely to say so, and only then in plenary. The safeguarding focal point is present, is '
  'introduced in person on Day 1 and is available for individual conversations every day, and she is deliberately not part of the facilitation team so that a concern about a '
  'facilitator can be raised at all. A buddy system pairs participants across countries for language and social support, and any participant may leave a session without giving a '
  'reason, a rule stated on Day 1 and repeated before the sessions that work with distressing content.')
P('Support does not stop when they get off the bus. The cohort communication group stays open for 18 months, and each participant leaves with a written commitment and a role in a '
  'local initiative that the group leader supports them through: the initiative is theirs to run, but they are not left alone to run it. A joint online meeting in month 10 lets '
  'the groups that have already delivered pass on what they learned, a follow-up questionnaire in month 12 and the final test in month 18 close the loop, and the participatory '
  'evaluation session in month 17 brings the twenty-one back into the project as evaluators rather than beneficiaries.')
COUNT(6000)

Q('What measures will you put in place to ensure the safety and protection of participants?')
P('All twenty-one participants are minors, so the measures below are specific rather than reassuring, and they meet the requirements the National Call sets for the mobility of '
  'minors: adequate preparation before departure with the parents involved, and group leaders selected for their competence in working with minors and in preventing and handling '
  'conflict, bullying and abuse, who prepare alongside the young people and commit in writing to the rules.')
P('The venue is assessed before it is contracted. A written risk assessment covers fire safety certification and evacuation routes, the state of the electrical installations and '
  'heating, the security of doors, windows and balconies, lighting of outdoor areas, separation of participant accommodation from any unrelated guests, distance and travel time '
  'to the nearest medical facility and hospital, mobile signal coverage across the whole site, and the suitability of the outdoor spaces used. The logistics officer then verifies '
  'all of it on site during the preparatory visit in month 3, together with representatives of the sending organisations, and the venue is not confirmed until it has been seen. '
  'On arrival an evacuation drill is held on Day 0 with the assembly point shown to every participant, and the guided safety tour is a scheduled session rather than an '
  'informality. Rooms are allocated by gender and by age with minors accommodated only with minors, the group leaders sleep on the same floors as their groups, and a night-duty '
  'rota keeps at least one adult awake and reachable at all times. Activity spaces are checked daily, a first-aid kit sits in the plenary room and another travels on every '
  'off-site activity, and at least one member of the team holds a valid first-aid qualification. [TO CONFIRM: who, and the certificate’s validity date.] For the off-site activity '
  'on Day 5 transport is by a licensed carrier, with a written route and timing, a headcount at every boarding and one adult per group at all times.')
P('Protection of the participants rests on a child protection policy of the coordinating organisation, signed by every adult involved and presented to the participants on Day 1. '
  '[TO CONFIRM: the policy must be adopted before submission.] Marilena Georgescu is the designated safeguarding focal point, sits outside the facilitation team, is introduced in '
  'person on Day 1, and her contact details go to participants and parents before departure, with a named counterpart in each partner organisation. Written parental consents for '
  'participation, travel, emergency medical care and use of images are obtained before departure and notarised where national law requires it, as is expected for the Turkish '
  'group. The code of conduct is negotiated with the participants themselves on Day 1 rather than imposed, and includes non-discrimination, respect for all languages present and '
  'explicit rules on harassment and bullying. Insurance for health, accident and civil liability covers all 27 people for the whole travel period and is arranged and verified '
  'centrally by the coordinator rather than left to each sending organisation. An emergency protocol provides a 24/7 contact chain, the full list of parents’ contacts held by the '
  'coordinator and by each group leader, a designated reference medical facility identified during the preparatory visit, and an interpreter reachable for the Turkish and Greek '
  'groups. On data and digital protection, consent for photographs and video is explicit, no identifiable image of a minor is published without it, no personal data of third '
  'parties appears in the material produced, every piece of content goes through a two-step review with the safeguarding focal point approving, and all data is processed under '
  'the GDPR, stored in restricted folders and anonymised in the supporting file.')
P('Working with real disinformation also exposes participants to violent, discriminatory or distressing material about war, health and migration, so a sensitive-content protocol '
  'applies. All working material is pre-screened by the facilitators and explicit content is excluded, every analysis session ends with a short decompression sequence, '
  'participants have a stated right to leave a session without justifying it, and an adult outside the facilitation team is available for an individual conversation every day. '
  'These rules are announced on Day 1 together with the group agreement, and repeated before Day 2.')
COUNT(6000)

Q('What activities are foreseen after the end of the Youth Exchange? How will the participants follow-up on the activity?')
P('Between months 6 and 15 the participants run four local initiatives: two in the Romanian territory, in different communes, one in Türkiye and one in the South Aegean. The '
  'Romanian group has seven participants drawn from twelve localities and a coordinator with fourteen partner municipalities, so a single event in one commune would reach the '
  'wrong young people, and two smaller initiatives in different communes is both more faithful to the territory and further into it. Each initiative reaches at least 20 young '
  'people and is hosted in a youth centre, a library, a community centre, the partner organisation’s own space or another accessible public place. The participants design and '
  'lead them while the group leader supports, and each one uses the “Digital Detectives” toolkit, screens the four media products made during the mobility, and ends with the '
  'ten-minute exercise that measures whether the young people reached can apply two simple verification methods. Two initiatives are due by month 10 and two by month 15, so that '
  'the later ones benefit from the earlier ones.')
P('In month 10 the three groups meet online to review what worked and what did not, and the toolkit is revised on the basis of real use rather than intentions. Month 12 brings '
  'the follow-up questionnaire at six months after the mobility, asking what they still use and what they have done with it. In months 16 and 17 the final version of “Digital '
  'Detectives” is published, translated by the partners and presented to the youth workers, librarians and community educators of the territory, with results presented across the '
  '14 localities and at the community events the organisation already runs, and with participants co-presenting. Month 17 also brings a participatory evaluation session feeding '
  'the final report, and month 18 the final test, the comparison with the baseline, the evaluation report and the reporting back to participants, parents, community partners and '
  'the National Agency.')
P('The follow-up is built so that the learning has somewhere to go. The local initiatives put the participants in front of other young people in their own community, which is the '
  'point at which the competence becomes theirs. The toolkit is left with the youth workers, librarians and community educators who see them week to week, so the method does not '
  'leave with us. Youthpass gives them a way to name and evidence what they gained, so they can use it in whatever they apply for next. And the twenty-one continue as peer trainers '
  'in the three organisations’ later activities, which means the project does not run alongside their learning and then stop: it leaves a competence, a document that describes it, '
  'and a place to keep using it.')
COUNT(6000)

H2('Recognition of learning outcomes')
Q('How will you support participants to be aware of what they have learned and which competences they have developed or improved? Please remember to include the methods that support reflection and documentation of the learning outcomes in the daily timetable of each activity.')
P('The methods that support reflection and documentation are scheduled sessions in the timetable rather than good intentions. Session D1.4 introduces the eight key competences, '
  'the learning diary and Youthpass, and each participant sets two personal learning targets. Sessions D1.5, D2.4, D3.5, D4.4 and D6.4 are the daily reflection cycle, held in the '
  'national group first and then in plenary. D4.4 is the mid-point review of each participant’s own learning targets, and D7.2 is the closing Youthpass session. All of them '
  'appear in the annexed timetable with their objective, method, competences, output and named responsible person.')
P('Awareness of learning is built into the structure in three concrete ways rather than added at the end. The digital map each participant draws on Day 1 is kept and returned on '
  'Day 7, so they compare their own description of their media habits before and after, which turns an abstract competence gain into something they can see. The observation grid '
  'applied on Day 4 records whether each participant actually performed each of four named techniques, so the conversation is about evidence rather than impression — and '
  'participants are told on Day 1 that this observation happens, what is observed and why, because it is their learning data and concealed assessment of minors is neither '
  'necessary nor acceptable. And the baseline and final test gives each participant a personal figure, communicated to them individually in month 18 rather than only aggregated '
  'for the report.')
P('The purpose of all this is a transferable skill in its own right: identifying what you learned, documenting it with evidence you can point to, and presenting it in a form '
  'someone else understands. That is what makes the certificate useful to a sixteen-year-old afterwards, in the next learning activity they join, in volunteering, in a civic '
  'initiative in their own community, and in the next international mobility they apply for. The competence matrix above is the reference document for the whole process, since '
  'every competence claimed is tied to the sessions that build it and to the evidence that documents it, and facilitators work from that same matrix when supporting participants '
  'to write their Youthpass.')
COUNT()

Q('The Erasmus Programme promotes the use of instruments/certificates like Youthpass or Europass, to validate the competences acquired by the participants during their experiences abroad. Will your project make use of such European instruments/certificates?')
P('Yes — **Youthpass**, for all 21 participants and all 4 group leaders. It is used as a process running from Day 1 to Day 7, as described above, and not as a certificate handed out at the door. Europass is not used '
  'in this project: our participants are 14 to 17 and are not in a mobility that produces a Europass Mobility document, so claiming it would be decoration. We would rather name one instrument we genuinely use well '
  'than two we use loosely. Alongside Youthpass, the coordinating organisation issues its own certificate of participation in Romanian and English, stating that the young person took part and naming the competences '
  'they developed through non-formal learning, with the evidence behind them — and that is all it claims. Participants and parents are told plainly what it is and what it is not, so that nobody is given an '
  'expectation the document cannot carry.')
COUNT(3000)

H2('Participants with fewer opportunities')
Q('Are participants involved in activities facing challenges that hinder their participation?')
P('**Yes. At least 13 of the 21 participants — 62%.**')
COUNT(500)

Q('How will you reach out to these participants?')
P('The first barrier these young people name is not money. In our survey 37.5% say the reason opportunities pass them by is that they never hear about them, so outreach is '
  'treated as a project activity with its own indicator — at least 63 applications for 21 places — and not as an administrative step before the real work starts.')
P('The call is published simultaneously in all three countries in month 1, in Romanian, Hungarian, Turkish and Greek, with the same criteria everywhere and a plain-language '
  'version written for parents rather than for funders. One rule is stated in it from the first day: nothing is asked of the participant or the family at any point, no fee and '
  'no pay-now-claim-later. That sentence is what allows a family to let a fourteen-year-old apply at all, so it belongs in the call and not in a later clarification.')
P('We then go where these young people actually are, and we chose the channels from our own data rather than from habit. Social media reaches 49.0% of them, so the material is '
  'made with young people already active in the three organisations, in their format, instead of being written by staff and posted at them. Friends are the channel for 38.5%, '
  'which is why members of the Rural Youth Parliament and participants of our previous activities do the talking: each organisation names two young people who have already been '
  'on a mobility to answer questions in person, because they are the only ones who can say what an exchange is really like. Around half say they hear about opportunities at '
  'school, so the call is carried into the schools of the territory — as an information channel only, with no school selecting anyone. We do not use municipal noticeboards, '
  'which reach 6.2% of this age group: the 14 partner municipalities validate the need and host activities, and saying plainly that they are not a recruitment channel is what '
  'our own figures require.')
P('Alongside that, each organisation opens the door it alone can open. In the Romanian territory the Social Inclusion Centre and the UNIC — Porolissum project work directly with '
  'vulnerable households, so the social worker puts the call into the hands of families who would never see an online post, and our own youth workers visit the communes in '
  'person — Beliș, Mărișel, Măguri-Răcătău, Săcuieu and the others — because a call presented face to face in a village of 400 people is worth more than any campaign. GGD '
  'recruits through the volunteer network it trains every year and through the rural youth programme it runs with the Turkish Ministry of Interior, prioritising young people who '
  'have never taken part in an international activity. KEA recruits through the network it operates across 36 inhabited islands of the Cyclades and the Dodecanese and through '
  'the municipal Community Centres it already works with on its ESF+ child-poverty action plan in Naxos and Kea.')
P('Applying is made as easy as we can make it. The form is short, it can be completed on a phone, help filling it in is offered by name and phone number, no English is required '
  'at any stage, and a young person may declare a situation limiting their access to opportunities confidentially — or not declare anything at all and still be selected. '
  'Selection is by a commission of at least two people per organisation, on the written form plus a short conversation, and every candidate is told the outcome and the reasons, '
  'including those not taken.')
P('We also say in advance what we will do if this does not work. The application register is checked against the target during the call, and if fewer than 63 applications have '
  'arrived two weeks before the deadline the call is extended, the peer channel is reinforced with additional in-person visits, and the social worker is asked for direct '
  'referrals. The composition targets — at least 13 of 21 participants with fewer opportunities and at least 16 of 21 taking part in a European mobility for the first time — are '
  'verified at selection and again at final confirmation by the activity coordinator. If they are not met, the call is reopened rather than the target quietly lowered.')
COUNT()

Q('What type of challenges are these participants facing?')
P('Three types, declared here because they are the three we can evidence: **geographical, economic and social obstacles**.')
P('**Geographical obstacles** affect very nearly the whole group, and they are the reason this consortium exists in this shape. The Romanian participants come from the mountain '
  'communes of the Apuseni — Beliș, Mărișel, Măguri-Răcătău, Săcuieu, Mărgău and the others — where the offer of youth activities is thin and the nearest city is a journey '
  'rather than a bus ride. The Greek participants come from small islands of the South Aegean, where for a fourteen-year-old any learning activity begins with a ferry and what '
  'exists in Athens simply does not arrive. The Turkish participants come from the İstanbul metropolitan periphery and from the rural localities behind it, peripheral in a '
  'different way but peripheral all the same. Living in a remote or rural area, on a small island or in a peripheral, less-served region is recognised in the Programme as an '
  'obstacle to participation, and all three groups qualify on that ground alone. What it produces is measurable: 31.3% of the young people aged 14–17 in our territory have never '
  'taken part in any non-formal education activity, and 37.5% say opportunities pass them by because they never hear that they exist.')
P('**Economic obstacles** come next and they are named by the young people themselves: 34.4% give cost as a barrier to taking part in a mobility and 31.2% give transport — the '
  'second and third obstacles on their own list. In these households the first eighty kilometres are a real problem and not a detail, and a scheme in which a family pays first '
  'and is reimbursed afterwards excludes exactly the young people it claims to include. Some of our participants come from households supported through our own Social Inclusion '
  'Centre, and between 2021 and 2023 we trained 99 people from disadvantaged households in social entrepreneurship, so these are families we already know by name.')
P('**Social obstacles** are the least visible and the most decisive. In our survey 12.5% name lack of self-confidence as what stops them and 10.4% say their family would not '
  'agree. Among the respondents there are young people reached through the social worker, young people with caring responsibilities at home, and young people from Roma '
  'communities; two of them wrote about exclusion in their own words — “There shouldn’t be differences of class or gender — if you’re in the 12th grade you should be able to go '
  'on Erasmus too” and “The right to study; Roma don’t put an emphasis on school.” In the İstanbul periphery the group includes young people from families with migrant and '
  'refugee backgrounds. And part of our own territory lives its community life in Hungarian: a young person whose information arrives in a minority language has less access to '
  'reliable reporting and almost no access to the correction of what circulates around them, which in this project is not a side note but the subject itself.')
P('The three overlap inside the same person more often than they separate. At least 13 of the 21 participants declare at least one, geography applies to almost all of them, and '
  'declaration is voluntary, confidential and never required of anyone. We do not declare disability or health obstacles in advance, because we do not know them before '
  'selection: the confidential specific-needs sheet lets a participant declare one afterwards, and the support that follows is then costed individually at real cost rather than '
  'assumed now.')
COUNT()

Q('What specific measures (e.g., accompanying persons, reinforced mentorship, accessibility measures) will you implement to support their participation?')
P('Each of the three obstacles is answered by measures that cost money and appear in the budget, not by good intentions.')
P('**Against geographical obstacles the project moves the participants and, where it can, moves itself.** Transport is organised and paid from each participant’s own front door '
  'to the point of departure, through the inclusion support category on a dedicated budget line, so that a young person from Măguri-Răcătău, or one who must take an '
  'inter-island ferry before reaching an airport, does not have to solve the first leg alone. **Accompanying persons** are set by the journey rather than by the minimum: four '
  'group leaders and two facilitators, six adults for twenty-one minors, one adult per 3.5 participants, below the National Call’s ceiling of one leader per four young people. '
  'The Greek flow carries two accompanying adults because its route — ferry to Piraeus, flight, then overland to the Apuseni — is the longest in the project and has at least one '
  'transfer where a group of fourteen-year-olds could be split. Every group is accompanied from its own departure point to Beliș and back and is never handed over mid-route. '
  'Two additional travel days are eligible for the Turkish and Greek flows under green travel, and we use them so that no minor travels overnight to save a '
  'day. And the activity itself is held in Beliș, inside the territory, because 58.5% of the young people we surveyed asked for activities in or near their own locality: the '
  'geography is designed around instead of ignored.')
P('**Against economic obstacles, nothing is asked of the participant or the family at any point.** Travel, accommodation, meals, insurance, materials and local transport are '
  'covered in full; there is no fee of any size and no reimbursement model in which a family pays first. The rule is in the call from the day it is published. Inclusion support '
  'for organisations, 125 EUR for each of the 13 concerned, pays for what reaching them costs: the in-person visits, the four-language call, the parents’ version and the extra '
  'preparation time. Inclusion support for participants is requested at real cost on separate dedicated lines, each justified individually, for a documented need such as an '
  'extra ferry leg, additional domestic transport or an accessibility cost. Nothing in the programme requires a young person to own anything: devices are provided at the venue, every exercise has a '
  'low-bandwidth version, and there is nothing to print or buy.')
P('**Against social obstacles the central measure is reinforced mentorship, and it is a named person rather than a procedure.** From selection until month 18 each participant '
  'has one adult from their own sending organisation — their group leader — who makes the pre-departure call with the family, travels with them, runs the daily reflection in '
  'their own language, is on the same floor at night, and afterwards supports the local initiative they lead without taking it over. The family is dealt with directly, because '
  '10.4% said the family would not agree: an online meeting is held in each country in the local language, with the safeguarding focal point present, explaining the full '
  'programme, the supervision arrangements and the contact chain — and parental consent is asked after that meeting, not before it. Nobody arrives among strangers: the '
  'preparatory visit takes one young person from each sending organisation, who then tells their own group what they saw; the cohort communication group is active two '
  'months before departure; and the four online preparation sessions are held in mixed national composition, so the team a participant will work with in August has already met '
  'them. Language is deliberately kept out of the door: English is not a selection criterion, A2 is accepted, the glossary is built in four languages, methods are visual and '
  'practical, and group leaders interpret on request — a test at the door would simply convert the '
  '12.5% who name lack of self-confidence into exclusion. During the week, the right to leave a session without giving a reason is written into the group agreement the '
  'participants negotiate themselves; the safeguarding focal point is available individually every day and sits outside the facilitation chain by design; the sensitive-content '
  'protocol means the material carrying ethnic, gender and migration stereotypes is pre-screened and nobody from a targeted community is made the example.')
P('**Accessibility measures** are verified rather than promised. Accessibility is a condition in the venue specification and it is checked on site during the preparatory visit '
  'in month 3, not read off a booking page, together with the connection test, the evacuation arrangements and the distance to the nearest medical facility. After '
  'selection, the confidential specific-needs sheet allows a participant to declare a health, dietary or accessibility need; the venue check is then repeated against that '
  'need, and the support is requested at real cost on its own line.')
COUNT()
H2('Virtual learning / Blended activities and use of virtual components')
Q('Do you foresee Virtual/Blended activities and/or the use of any virtual component, before, during or after the activity?')
P('**Yes**, before and after the physical activity. Approximately 27 persons take part: 21 participants, 4 group leaders and 2 facilitators.')
COUNT(500)

Q('If yes, please describe them.')
P('Before the exchange, in months 3 and 4, four joint online sessions of 90 minutes each bring the groups together in mixed national teams. A shared online workspace holds the '
  'documents, the case files uploaded by each group and the templates, while a moderated messaging group with explicit rules keeps day-to-day contact going. A separate online '
  'meeting is held with parents in each country, and the group leaders take a two-day online briefing that includes the observer calibration exercise. The baseline test is '
  'administered online.')
P('After the exchange, from month 6 to month 18, the cohort communication group remains the working space for preparing the four local initiatives, with each group posting its '
  'plan and the others commenting before it happens. A joint online review meeting follows in month 10, the follow-up questionnaire in month 12, the participatory evaluation '
  'session in month 17 held online across the three countries, and the final test in month 18.')
P('None of this is decoration, for two reasons that come from the data. For a group in which 31.3% have never taken part in a non-formal activity and 12.5% name lack of '
  'confidence as a barrier, the virtual phase lowers the threshold, because they arrive in August having already met the people they will be working with, which is a different '
  'thing from arriving among strangers. And since the subject of this project is the digital environment, the way the project itself uses digital tools is part of the message: '
  'the rules the cohort applies in its own communication group — consent, no personal data of third parties, no sharing of unverified content — are the rules the project teaches.')
COUNT()

H2('Environmental friendly practices')
Q('Will you include sustainable and environmental-friendly practices in your activities?')
P('Yes. For each group the low-emission option is analysed — train, coach, ferry, to the extent each qualifies as green travel under the rules of the applicable call — including '
  'the additional eligible travel days, and the option chosen and the reason are documented; the budget is built on the green rates for all three flows. Meals are mostly local '
  'and seasonal, sourced from producers in the territory through the short supply chains the organisation itself developed in its rural-development work, which is not a gesture '
  'but its own infrastructure, and it lets participants see a short supply chain instead of hearing about one. There are no individually packaged portions, no folders and no '
  'printed handouts; worksheets are digital, workshop materials reusable, waste separated at the venue, and participants are asked to bring reusable bottles. Movement inside the '
  'territory is on foot or by a single group transport.')
P('The most durable environmental lesson, though, comes through the content itself. One of the categories of disinformation analysed on Day 2 is environmental and climate '
  'content, and participants work on real examples of misleading environmental claims. For this particular group that does more than a briefing on recycling would, and it is '
  'consistent with the method of the whole project: they learn to distrust the slogan, including the green one.')
COUNT(4000)

PAGEBREAK()

# =====================================================================
H1('Project management')
Q('How will you manage the project (agreements with partners etc.) and make sure that it is done in line with the Erasmus Youth Quality Standards? You will find the quality standards further down in the application form.')
P('The roles are separated on purpose. Alina Ioana Baba, as project manager, carries overall coordination, the relationship with the National Agency, the budget, reporting, risk '
  'decisions and the partnership agreements. Claudiu Iancu, Coordinator of our Youth Department, owns the learning programme, the three measurement instruments, observer '
  'calibration and moderation, the facilitation team and the Youthpass process. Livia Golovatic runs the joint online preparation sessions, leads the Romanian group, coordinates '
  'the four local initiatives and checks the gender and locality balance. Marilena Georgescu receives and handles safeguarding concerns and approves the publication of content, '
  'and she sits outside the facilitation chain by design, so that a participant can raise a concern about a facilitator. Iulia Fătu handles budget execution, procurement, venue, '
  'transport, insurance, financial reporting and the written venue risk assessment. GGD leads media production and AI content and designates one of the two facilitators, while '
  'KEA leads the community dialogue method and the local-initiative methodology. Romania and Türkiye each provide one group leader aged 18 or over, and Greece two.')
P('A written partnership agreement is signed with each partner in month 1, before any expenditure. It sets out tasks and deliverables with dates, the exact budget share and the '
  'conditions and timing of transfers, recruitment and selection obligations, safeguarding obligations, adherence to the Erasmus Youth Quality Standards, data protection, '
  'reporting duties, visibility rules, and what happens if a partner does not deliver. It is not a formality: it is the document that makes the deliverables enforceable. '
  'Coordination meetings are held online monthly in months 1 to 5 and every two months thereafter, with a standard agenda, a written minute circulated within 48 hours and a '
  'rotating chair, while a shared action log records every decision with an owner and a deadline and the risk register is reviewed at every meeting.')
P('Alignment with the Quality Standards runs through the design rather than beside it. The four basic principles — inclusion and diversity, environmental sustainability, digital '
  'transformation and participation — all appear as design decisions traceable to evidence, and the correlation between each survey finding and the decision it produced is '
  'documented in the supporting file. Selection is fair and transparent, with published criteria identical across three countries, a commission of at least two people per '
  'organisation, and the outcome communicated with reasons to every candidate including those not selected. Preparation of participants runs over four months, with four joint '
  'online sessions, a preparatory visit, linguistic and intercultural components, a parents’ meeting in each country, and a baseline that tells the facilitators what the group '
  'actually cannot do. Learning outcomes are defined, assessed and recognised through the competence matrix tied to sessions and evidence, the baseline and final test, the '
  'observation grid with calibrated observers, and Youthpass as a process from Day 1. Protection and safety rest on the child protection policy, a safeguarding focal point '
  'outside the facilitation team, a written venue risk assessment verified on site, parental consents, central insurance, an emergency protocol and a sensitive-content protocol. '
  'And results and knowledge of the Programme are shared through the toolkit published free of charge, the Erasmus+ Project Results Platform, the LEADER and ELARD networks, and a '
  'Day 1 session telling participants what else the Programme offers them after this project.')
COUNT(6000)

Q('How will you organise the practical and logistical part of the project (e.g. travel, accommodation, insurance, visa, social security, mentoring and support, preparatory meetings with partners etc.)?')
P('A preparatory visit is held in the territory in month 3, with two people from each of the two sending organisations — one of them a young person — plus one staff member from '
  'the coordinating organisation, five people in total. That staff member contributes to the on-site verification of the logistical and safety arrangements and finalises the '
  'mobility programme with the partners while everyone is in the same room. The visit as a whole verifies the venue and its safety in person, settles the division of the thematic '
  'days, meets the host community and lets a young person from each group see where they will be coming. It is requested on three grounds: all twenty-one participants are minors, '
  'both sending partners are new working relationships for us, and a venue’s suitability cannot be assessed from photographs.')
P('Travel is booked centrally by the coordinator for all three flows, so that no sending organisation carries a cash-flow burden and green options are compared on the same basis, '
  'with distances confirmed through the European Commission distance calculator once departure cities are known. Domestic transport from participants’ homes to the point of '
  'departure is organised and paid by the project, which for the Greek group includes the inter-island ferry legs before the group is even assembled, and is the reason that flow '
  'is planned with two accompanying adults and four eligible travel days.')
P('Accommodation is a single venue in Beliș, inside the territory, contracted after the written risk assessment and the on-site check during the preparatory visit, with rooms allocated by '
  'gender and age, minors with minors and group leaders on the same floors. Meals are mostly local and seasonal from producers in the territory, and dietary requirements are '
  'collected in month 4 and confirmed with the venue in writing. Insurance for health, accident and civil liability covers all 27 people for the whole travel period and is '
  'contracted centrally by the coordinator and verified before departure, rather than left to each partner to arrange.')
P('Visas are the principal logistical risk. Romania has applied the Schengen acquis in full, land borders included, since 1 January 2025, and Turkish nationals holding ordinary '
  'passports are subject to the Schengen short-stay visa requirement. For minors that means notarised parental authorisations, invitation letters, proof of accommodation and '
  'insurance, and consulate appointments booked well ahead, so the procedure begins in month 3, five months before the activity: invitation letters issued by the coordinator, a '
  'complete file checked before submission to the consulate, and reserve participants prepared in parallel with their own files ready. This is not a theoretical risk and we treat '
  'it as the item most likely to cost the project a participant.')
P('Greek participants need no visa, but their journey needs planning: a ferry from the participant’s island to Piraeus and then an overland leg north, with at least one transfer '
  'where a group of six fourteen-year-olds could be split. Timings are fixed with KEA during the preparatory visit, the whole route is written down and given to parents, a '
  'headcount is taken at every boarding, and the two accompanying adults are on the same tickets as the group throughout. Throughout the project each participant has a group '
  'leader, a cross-country buddy and access to the safeguarding focal point, and the cohort communication group is active from two months before departure until the end.')
P('The main risks are managed as follows. Visas not obtained for the Turkish group is the high-likelihood, high-impact case, answered by starting in month 3, preparing documents '
  'in advance, booking appointments early and holding reserve participants with complete files. Withdrawal of participants is answered by a reserve list of at least two young '
  'people per national group, prepared alongside the main group and kept informed. A partner failing to deliver on time is answered by deliverables with dates in the partnership '
  'agreement and a monthly action log, then a reminder, a joint problem-solving call and documented reallocation. Low English level blocking participation is answered by the '
  'four-language glossary, visual methods, interpreting by group leaders and deliberately balanced mixed teams. A medical or safety incident is answered by insurance, the '
  'emergency protocol, a reference medical facility identified during the preparatory visit, a first-aid trained staff member and a night-duty rota. A participant distressed by '
  'the working content is answered by the sensitive-content protocol, pre-screened material, the right to leave a session and daily individual availability of the safeguarding '
  'focal point. A missed ferry or transfer connection on the Greek route is answered by timings fixed during the preparatory visit, a written route given to parents, a headcount '
  'at every boarding, two accompanying adults and a margin day in the travel plan. Observers unable to apply the grid consistently is answered by the month 4 calibration exercise '
  'with an 80% agreement target, after which the grid is simplified before the mobility if needed and the decision is minuted, never after seeing the results. Bad weather is '
  'answered by an indoor alternative planned for every outdoor session, and a local initiative not delivered by the written commitments made publicly on Day 7, an interim '
  'reporting deadline in month 10 and methodological support from KEA.')
COUNT(6000)

H2('Partnerships')
Q('How and why did you choose your project partners? What experiences and competences will they bring to the project?')
P('The partnership is built around one shared structural condition rather than around geographical variety. All three territories are peripheral in different ways, information '
  'reaches young people there through channels no national fact-checker covers, and in all three the use of digital tools has outrun the competence to judge them — measurably so, '
  'in the two EU countries that sit at the bottom of the youth digital-skills rankings. Each partner has the same problem in a different form, and each brings a competence the '
  'others do not have, which is why the project cannot be delivered by one organisation and why swapping a partner for a more convenient one elsewhere would weaken it rather '
  'than simplify it.')
P('LAG Napoca Porolissum, as applicant, coordinator, host and sending organisation, owns the evidence base of 153 young people surveyed, the territory, the venue, the '
  'relationship with 14 municipalities and a network of 43 members, and an in-house youth worker and trainer; its own survey identified the problem in the first place. It leads '
  'overall coordination, budget, reporting, risk, the learning programme, local logistics, safety, the relationship with the host community and evaluation, and it delivers the '
  'partnership agreements in month 1, the verification test and observation grid piloted and locked in months 1 and 2, the baseline and final test in months 2 and 18, the '
  'programme and worksheets and the venue and services in month 4, the final toolkit in month 17 and the evaluation report in month 18. It leads sessions D1.2, D1.3, D1.4, D2.1, '
  'D2.2, D3.2, D3.3, D4.1, D4.3, D5.1 and D7.2.')
P('Genç Gönüllüler Derneği was chosen for one competence and one reach. The competence is technical, since among the professionals who work with GGD voluntarily is a social '
  'media, cyber-security and artificial intelligence specialist, and the organisation has already convened a hundred educators and digital-media experts to work out what '
  'children need from digital content, publishing the result as a guide; it knows how digital content for young people is made but does not teach how to verify it, which is '
  'exactly the complementarity this project needs. The reach is into both halves of Turkish peripherality: a volunteer network it trains every year in the İstanbul periphery, '
  'and a rural youth programme supported by the Turkish Ministry of Interior. It leads the media production module in D6.1 and D6.2, the AI-content session D3.1 and the '
  'ethics-of-AI session D3.4, provides pre-departure digital preparation, and designates one of the two facilitators. It delivers the production module and technical guide and '
  'its own local needs note, recruits and prepares the Turkish group, runs the local initiative in Türkiye by month 12 and disseminates through its channels.')
P('KEA IM Syrou was chosen for reach and for method. The reach is into real island isolation, since KEA carries EU and Greek State programmes out to 36 inhabited islands of the '
  'Cyclades and the Dodecanese, which means it can recruit young people from small islands that no national programme touches and host a local initiative there afterwards. The '
  'method is social work before it is media work: the Day 5 dialogue, in which participants sit down with residents and municipal representatives to find out what false '
  'information circulates in a place and who it hurts, is a facilitated community exercise, and KEA staffs it with a social worker and a career counsellor who do this '
  'professionally. Its current ESF+ child-poverty action plan in Naxos and Kea runs on exactly this kind of networking with municipal services, which is also why it designs the '
  'template the four local initiatives are built on. It leads the preparation and method of Day 5, the local-initiative methodology in D6.3 and the Day 2 strand on how '
  'information circulates in small island communities, and delivers its own local needs note — already produced for the South Aegean — the documented local cases, the initiative '
  'model and its evaluation grid, the recruitment and preparation of the Greek group, the local initiative in the South Aegean by month 13 and the Greek translation of the '
  'toolkit.')
P('KEA has not run a KA152 exchange before, and we say so plainly, but two things reduce that risk. It has coordinated Erasmus+ projects of its own, including I.D.E.A. '
  '(2019-1-EL01-KA204-063049), and managed budgets an order of magnitude larger than this one under ESF+ and Interreg. And it has already been a partner in an Erasmus+ project '
  'coordinated from Romania and contracted by this same National Agency, Meta Skills (2021-1-RO01-KA220-ADU-000028211), so the administrative conventions of RO01 are not new to '
  'it either.')
P('We deliberately avoid the formulation that all partners contribute to all activities. Each partner leads named sessions and delivers named products by named dates, and the '
  'partnership agreement makes that enforceable. Three organisations is also a deliberate size: with two sending partners the coordinator can hold a real working relationship '
  'with each, and every partner leads something visible rather than being carried.')
COUNT(6000)

Q('How will you communicate with them?')
P('Formal coordination and accountability run through email and a shared document workspace, where all decisions, deliverables and versions live, with a response time of three '
  'working days and a rule that nothing binding a partner exists only in a chat. Coordination meetings are video calls, monthly in months 1 to 5 and every two months thereafter, '
  'with a standard agenda, a written minute within 48 hours and a rotating chair. Fast operational contact happens in a closed messaging group of the core team only, during the '
  'preparation and mobility weeks, and carries no personal data of participants. The group leaders have their own separate channel plus the two-day online briefing in month 4 on '
  'safeguarding, escalation, reflection facilitation and the calibrated use of the observation grid. Participants have the moderated cohort group and the four joint online '
  'sessions, active from month 3 to month 18, with explicit rules and facilitators moderating. And parents have an online meeting per country in the local language, plus the '
  'written participant pack, in months 3 and 4, before parental consents are signed.')
COUNT(3000)

Q('How will you monitor and coordinate their contribution?')
P('Each partner has deliverables with dates written into the partnership agreement, and those same deliverables appear in the shared action log with an owner. At every coordination meeting the log is reviewed line by '
  'line: delivered, in progress, or late. Escalation is defined in advance and is proportionate — a reminder from the project manager; then a joint problem-solving call with the relevant leads; then, only if '
  'necessary, a documented reallocation of the task, recorded in the action log. Payments to partners are staged against deliverables rather than against the calendar.')
P('Because the three organisations are of genuinely different kinds — a rural Local Action Group in the Carpathians, a multidisciplinary youth association in a metropolitan periphery, and an island development centre '
  'serving 36 islands — monitoring uses one '
  'common backbone with partner-specific expectations: the same reporting template and the same dates for everyone, but the content of what each is asked for follows the role they actually hold. Quality is monitored '
  'as well as delivery: the Learning Programme Coordinator reviews the local cases each partner submits in month 4 against a common standard, because those cases are the working material of the whole mobility and a '
  'weak set from one country would quietly degrade Day 2 for everyone.')
COUNT(3000)

Q('Which other actors (organisations or individuals) will be involved and how?')
P('Youth organisations and youth structures in the three territories carry the call to young people in their own networks, host local initiatives, and take the toolkit into their '
  'own standing activity afterwards. Libraries and community centres host the local initiatives and the presentation of the toolkit, and are where it stays available. Local '
  'authorities — the 14 partner municipalities of our territory and their counterparts in the other two countries — validate the need, host the Day 5 community dialogue, provide '
  'spaces for the local initiatives and receive the evaluation report and its recommendations, though they are not used for recruitment, because our data shows they reach only '
  '6.2% of this age group. The Social Inclusion Centre and the UNIC — Porolissum project carry outreach to young people from vulnerable households, and are the channel through '
  'which the inclusion targets are actually met rather than hoped for.')
P('Closer to the exchange itself, local producers of the territory supply the meals through short supply chains and take part in the intercultural evening, and residents of the '
  'host village are interlocutors in the Day 5 dialogue — participants in the learning rather than scenery, since the record of local rumours they help produce becomes the '
  'working material of Day 6. Local press is invited to the Day 7 public presentation. National fact-checking and verification resources in the three countries, Romanian, Turkish '
  'and Greek, are used as reference material in the Day 3 tool laboratory, one per partner country, so that participants leave with a resource usable at home in their own '
  'language. [TO CONFIRM: the final list, checked for being free of charge and appropriate for minors.] And the LEADER and ELARD networks carry the method to Local Action Groups '
  'across rural Europe, an audience that rarely encounters media-literacy tools at all.')
COUNT(4000)

H2('Evaluation')
Q('How will you evaluate your project’s success? Which activities will you carry out in order to assess whether, and to what extent, your project has reached its objectives and results?')
P('The three instruments that judge this project exist in writing now, at application stage, rather than being invented once the results are in. Every indicator we use has a '
  'baseline, a target, an instrument, a named owner and a fixed moment of measurement.')
P('The first instrument is a practical verification test of fifteen items worth thirty points, taken online on a closed device: Form A in month 2, before any learning activity, '
  'and the equivalent Form B in month 18, scored by the same formula at both ends. It is what tells us whether objective O1 was met — a rise of at least 30% in the mean score for '
  'at least 17 of the 21 participants. The second is an observation grid on which four named techniques are scored 0 to 2 each: identifying the source and the author, checking '
  'the date and the original context, comparing against two independent sources, and testing an image or a claim. It is applied in session D4.1 on Day 4 by six calibrated '
  'observers — the four group leaders and the two facilitators — with ten of the twenty-one double-scored independently and the Learning Programme Coordinator moderating but not '
  'scoring; it is what tells us whether O2 was met, again for at least 17 of 21. The third is a ten-minute exercise at the close of each of the four local initiatives: a young '
  'person who attended names two distinct checks, carries one out and draws a conclusion that follows from it. All three conditions, or it does not count. That is how O3 is '
  'judged — at least 80 young people reached, at least 20 per community, and at least 70% of them able to apply two simple methods.')
P('Two further measures matter more to us than the headline scores, because they go to the actual problem. The test carries a separate four-point sub-score on the two items that '
  'depend on overconfidence rather than knowledge, and we expect it to move proportionally more than the total; and an unscored question asking how good participants believe '
  'they are is converted onto the test scale, so the distance between believed and actual ability is reported as a number in month 2 and again in month 18. Our starting point is '
  'a group that already thinks it can spot a fake, so a project that raised the score while leaving that gap untouched would have missed the point.')
P('Neither instrument is used on the cohort untested. Before month 2 both are piloted with five to eight young people aged 14–17 from the territory who are not project '
  'participants, and any item that more than 80% or fewer than 10% of them answer correctly is rewritten, because an item everyone gets right and an item nobody gets '
  'right tell us nothing. The baseline is then taken in month 2 and the recalibration rule applied once, on the group mean, with the decision written down at the time. In month 4 '
  'all six observers score the same recorded sequence independently and compare, targeting exact agreement on at least 80% of judgements; if that is not reached the grid is '
  'simplified before the mobility and the decision minuted — before anyone has seen a result, never after.')
P('A second set of checks at selection is as binding as the learning ones: at least 63 applications for the 21 places, at least 16 of the 21 taking part in a European '
  'mobility for the first time, at least 13 with fewer opportunities, and at least 40% of each gender in every national group, verified by the activity coordinator '
  'at selection and again at final confirmation.')
P('During the week the evaluation is continuous and visible to the participants. The daily reflection groups run first in the national group in the participant’s own language and '
  'then in plenary, and what comes out of them visibly changes the next day’s programme — a learning method and our best early warning at once. The Day 4 grid is moderated '
  'immediately after the session, while the observers still remember what they saw, and at the mid-point each participant returns to the two learning targets they set on Day 1. '
  'On Day 7 there is a participatory evaluation run with the participants rather than on them, an anonymous questionnaire in which we look for at least 80% positive '
  'without leaning on it, the Youthpass session, and the comparison of each sealed Day 1 digital map with what its author can now say about their own habits.')
P('After the mobility the measurement follows the participants. Each local initiative produces an attendance record, a short report and the ten-minute exercise. In month 10 the '
  'four groups meet online to review what actually worked, and that review is what revises the toolkit, not a desk edit. A follow-up questionnaire in month 12 asks what '
  'they still use, with at least 16 of the 21 expected to be applying something six months on. In month 17 the participants take part in a participatory evaluation session that '
  'feeds the final report, and the three organisations hold their own evaluation meeting. In month 18 the final test is taken, compared with the baseline and written up. '
  'Externally we count one thing: at least four organisations outside the partnership confirming in writing that they use the toolkit. Results are communicated individually to '
  'every participant and collectively to parents, community partners, the 14 municipalities and the National Agency.')
P('We have built these instruments so that failure is visible rather than comfortable. A practical test can come back showing no improvement. An observation grid can record, '
  'participant by participant, that a technique was not performed. A participant who does not take both forms is excluded from the calculation and reported as '
  'excluded, not quietly removed from the denominator. We prefer that to a satisfaction questionnaire that always comes back positive. And we will describe the instruments '
  'honestly: fifteen items and twenty-one participants do not make a validated psychometric instrument and we will not call it one. It is fit for tracking change inside this '
  'cohort and for telling the team where the learning worked and where it did not; the final report will say both.')
COUNT(6000)
H2('Sustainability of the results')
Q('What will you do to make sure that your project continues to have effects also after it ends?')
P('Four things stay behind when the funding stops, and each one has a person responsible for it.')
P('The first is the toolkit. We call it “Digital Detectives” and it is not a report about the project. It is the material we actually used: worksheets, exercises, games, '
  'verification grids, the manipulation grid the participants wrote in four languages, and the AI-recognition sheet they made themselves. We test it during the exchange, then we '
  'fix it in month 10 using what really worked in the four local initiatives and what did not. It is published free of charge in month 17 in English and Romanian, and GGD and KEA '
  'translate it into Turkish and Greek. Any youth worker can download it and run a session with it the same week.')
P('The second is where that toolkit goes next, because a published file that nobody picks up is not a result. Our association already runs youth activities across its 14 partner '
  'municipalities and holds community events every year, and the toolkit becomes part of that work. GGD puts it into the volunteer network it trains every year and into its rural '
  'youth programme. KEA takes it into its creative activity centre for children and young people and out to the 36 islands it serves. In the partnership agreement each '
  'organisation writes down the name of the person who is responsible for it after the project ends — a name, not a department.')
P('The third is the twenty-one participants. They do not stop being part of this when they get home. Each of them has already planned and led a local activity for other young '
  'people, so the three organisations keep them on as peer trainers in what they do next. That is cheaper than finding a new group and it works better, because a sixteen-year-old '
  'listens differently to another sixteen-year-old. The group chat stays open for the whole 18 months and is not closed when the report is submitted.')
P('The fourth is the three instruments: the practical test, the observation grid, and the short exercise we use with the young people the participants reach afterwards. All three '
  'can be used again. At the end of this project our association owns three ways of measuring what young people actually learned, which it did not have before, and that changes '
  'what we can honestly write in the next project we apply for.')
P('In month 17 the three organisations sit down and decide whether to carry on together, and with what. Two ideas are already on the table: a second exchange, hosted next time by '
  'GGD or KEA, or a youth participation project where young people talk directly to local decision-makers. We write the decision down either way, including if the answer is no.')
COUNT(5000)

Q('Are you planning measures to make sure that the results produced are used and beneficial to others beyond the project’s lifetime? If yes, which ones?')
P('Yes. We prefer to name who gets what, rather than promise to share widely.')
P('Youth organisations, libraries and community centres in our own territory get the toolkit free, and in month 17 we sit down with the youth workers, librarians and community '
  'educators who will actually use it and go through it with them. This matters more here than it would elsewhere. Romania has no single national plan for media literacy and the '
  'rules are spread across different laws, so a tested set of free materials in the hands of people who already work with rural young people fills a gap that nobody else is '
  'filling.')
P('Youth organisations elsewhere in Europe get it through the Erasmus+ Project Results Platform and through our partners’ own channels. KEA reaches more than 80 regional media '
  'outlets, a website with over 12,000 visitors a month and a newsletter with 800 subscribers. GGD reaches the volunteers it trains every year. We also use the LEADER and ELARD '
  'rural networks, where our association already works internationally. The target is simple and checkable: at least four organisations outside this partnership confirm in '
  'writing that they have used the toolkit.')
P('Local institutions get the evaluation report and a short list of recommendations — what worked, what we would do differently, and what a municipality can do with very little '
  'money. It goes to our 14 partner municipalities and to the partner institutions in Türkiye and Greece.')
P('The communities get the four media products, which stay online on all three organisations’ channels after the project closes. A two-minute video that takes apart a rumour '
  'people in the village actually heard gets watched. A report does not.')
P('None of this needs new funding. Everything listed here happens inside activities the three organisations already run and already pay for.')
COUNT(4000)

H2('Dissemination of project results')
Q('How will you make your project visible outside your organisation and partner organisations? How will you share its results and success? With whom will you share the results?')
P('We share the results with five groups. For each one we know the channel, what they get, who is responsible and how we will know it happened.')
P('Young people in the three communities come first, because they are the ones the project is for. They get the four local initiatives the participants run themselves, the four '
  'media products on the organisations’ social media, and the toolkit through youth centres, libraries and community centres. At least 80 young people are reached directly, and '
  'the group leaders are responsible for that number.')
P('The communities of our territory come next. The 14 partner municipalities help us spread the word, we use the community events our association holds every year, and we work '
  'with the local press. What they see is the public presentation the participants give on Day 7 in Beliș, and a “Digital Detectives” stand at two of our community events. The '
  'target is two community events and three items in the local press, and the communication officer owns it.')
P('Parents and guardians are a special case, and we say plainly what they are: not a target group of the project, but the people who have to inform, support and protect '
  'participants who are minors. Each country holds a parents’ meeting before consents are signed, every family receives the participant pack, and parents are invited to the local '
  'initiative and to the Day 7 presentation, where they hear it from their own child instead of from us.')
P('Youth organisations and youth workers across Europe get the toolkit. We publish it on the Erasmus+ Project Results Platform, and it travels through KEA’s regional media '
  'network, website and newsletter, through GGD’s volunteer network, and through the LEADER and ELARD rural networks. What we count is the toolkit published and freely '
  'downloadable, and at least four organisations outside the partnership confirming that they use it.')
P('Local institutions and decision-makers get the evaluation report and the recommendations, in direct meetings and in presentations to local councils. At least four institutions '
  'informed, and the project manager is responsible.')
P('Two rules apply to everything we publish. Every product — toolkit, videos, presentations, press releases — carries the European Union emblem and the funding statement, as the '
  'Programme requires. And because all our participants are minors, nothing goes out until two people have seen it: the participant responsible for documentation prepares it, and '
  'the safeguarding focal point approves it. No recognisable photo of a minor is published without written consent, no personal data of other people appears, and we never publish '
  'where a minor lives or can be found. That rule is written into the group agreement on Day 1, and understanding why it exists is part of the learning.')
P('On Day 1 the participants also get a short session on what Erasmus+ actually is and what stays open to them afterwards — the European Solidarity Corps, DiscoverEU, other '
  'exchanges — so that this project is not the last time they hear the word.')
COUNT(5000)

Q('How will you involve participants in such activities?')
P('The participants are the ones doing the disseminating. They are not the subject of it.')
P('They make the four media products. They design and lead the four local initiatives, choosing the date, the place, the audience and who does what. They present in public on '
  'Day 7 to guests from Beliș, the neighbouring communes and the local press, and the adults in the room speak only if someone asks them a question. In months 16 and 17 they '
  'present the results again across the localities of the territory. And from month 3 each of them holds a real job in the project — photo and video, the activity diary, contact '
  'with the host community, energisers, timekeeping — assigned before the mobility and kept throughout.')
P('There is a practical reason for working this way and not only a principled one. When a fifteen-year-old stands in front of a room of other young people and shows them how to '
  'check whether a photograph is really what it claims to be, they are believed. It is also the moment the learning stops belonging to us and starts belonging to them.')
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
 ['**Accession forms** (if the slot is present)', 'One per partner, signed by each legal representative. Due at the latest before the signature of the grant agreement, and a condition for signing it.', 'GGD and KEA — to be collected'],
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
 'It fulfils the eligibility criteria listed in the Programme Guide — 21 participants aged 14–17, three groups from three countries (7 + 7 + 7), four group leaders, two facilitators, seven activity days excluding travel, activity in the country of the applicant and of the National Agency.',
 'All relevant fields in the application form have been completed — every [TO CONFIRM] in this document is a field still open.',
 'You have chosen the correct National Agency — RO01, ANPCDEFP.',
], count=False)

SMALL('Prepared 16 September 2026 for the KA152-YOU application of Asociația GAL Napoca Porolissum, Call 2026 Round 2, deadline 1 October 2026, 12:00 Brussels time.')

import os
out = '/home/user/UNIC-2/VERIFAI_KA152_Form_Content_EN.docx'
doc.save(out)
print('saved', out, os.path.getsize(out), 'bytes')
