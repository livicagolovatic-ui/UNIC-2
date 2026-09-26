# -*- coding: utf-8 -*-
"""VERIFAI timetable annex content, taken from the application content document."""

ORGS = (
    "Applicant and coordinator: ASOCIAȚIA GRUPUL DE ACȚIUNE LOCALĂ NAPOCA POROLISSUM (OID E10181755, Romania) — host, sending organisation, owner of the learning programme.\n"
    "Partner: GENÇ GÖNÜLLÜLER DERNEĞI — Young Volunteers Association / GGD (OID E10309307, Türkiye) — sending organisation; leads Day 3 (AI-generated content) and Day 6 (media production); designates one of the two facilitators.\n"
    "Partner: KENTRO EREUNAS KAI ANAPTYXIS IERAS MHTROPOLIS SYROU — KEA IM Syrou (OID E10151458, Greece) — sending organisation; leads the method of Day 5 (community dialogue) and the local-initiative template."
)

DURATION = (
    "7 activity days excluding travel: 09/08/2027 – 15/08/2027.\n"
    "2 travel days: arrival 08/08/2027, departure 16/08/2027. For the Turkish and Greek flows, green travel over 500–1,999 km makes 2 additional travel days eligible (11 days in all per flow).\n"
    "21 participants aged 14–17 (7 Romania + 7 Türkiye + 7 Greece), 4 group leaders, 2 facilitators — 27 persons."
)

CITY, COUNTRY, START, END = "Beliș (Cluj County)", "Romania", "09/08/2027", "15/08/2027"

# (day label, [(AM activity, AM method), ...], [(PM activity, PM method), ...])
DAYS = [
 ("ARRIVAL DAY — Sunday 08/08/2027 (travel day, not counted in the 7 activity days)",
  [("Arrival of the three groups in Beliș. Reception by the coordinator's team, room allocation (minors with minors, group leaders on their groups' floors), handover of the practical pack in four languages.",
    "Informal welcome; peer buddying between the national groups."),
   ("The Greek group arrives in the late afternoon, after the inter-island ferry and the flight; headcount at every boarding, confirmed by its two group leaders.",
    "—")],
  [("D0.1 Guided safety tour of the venue and its surroundings, with an evacuation drill: assembly point shown to every participant, emergency contact chain, the night-duty rota, the rule that at least one adult is awake and reachable at all times.",
    "Guided tour; practical drill; demonstration rather than instruction."),
   ("Welcome dinner with local seasonal food from producers of the territory; first informal contact between the three groups; the week explained by the participants' own timetable.",
    "Informal intercultural contact; shared meal as a first group experience.")]),

 ("DAY 1 — Monday 09/08/2027 · Who we are and what we consume · Objectives O1, O2 · AIM: form the group and make it look at its own habits before anyone teaches",
  [("D1.1 Mixed-team formation. The 21 participants are divided into four mixed teams of five or six, each containing members of all three national groups; name games, energisers and trust exercises inside the new teams.",
    "Icebreakers; energisers; name games; team-building exercises; deliberate mixing so no national group works alone."),
   ("D1.2 The group agreement. Participants negotiate and write their own rules for the week; non-discrimination and respect for every language present are non-negotiable clauses, everything else is theirs to decide.",
    "Facilitated negotiation; consensus building; a written group contract signed by the participants.")],
  [("D1.3 “My Digital Map”. Each participant maps one ordinary day of their own media diet: what they saw, where, from whom, what they shared and why. Kept sealed until Day 7.",
    "Individual visual mapping; sharing in pairs; gallery walk; self-observation before any teaching."),
   ("D1.4 Safety, safeguarding, digital-conduct and Youthpass briefing; each participant sets two personal learning targets. D1.5 First daily reflection, in the national group in the participant's own language and then in plenary; learning diaries opened.",
    "Briefing with open questions; individual goal setting; structured reflection groups; learning diary.")]),

 ("DAY 2 — Tuesday 10/08/2027 · Spot the Fake · Objectives O1, O2 · AIM: break untrained confidence and replace it with named mechanics",
  [("D2.1 The controlled-error exercise. Teams commit in writing to a verdict on a mixed set of real and false items — two misleading statistics and a manipulated graph among them — before the answer key is revealed. The facilitators commit too, and get some items wrong, visibly and on purpose.",
    "Learning through controlled error; team decision under time pressure; deliberate surprise as the instrument that works on overconfidence; plenary debrief."),
   ("D2.2 The mechanics of manipulation — emotional headlines, cropped context, borrowed authority, numbers quoted without their population or year — worked on the real cases the three groups documented during preparation, including content carrying ethnic, gender and migration stereotypes. KEA leads the strand on how information travels in island communities.",
    "Case analysis in mixed teams; guided discovery; comparison of the same mechanism across three countries; analysis with someone from the targeted community in the room.")],
  [("D2.3 “The information tribunal” — a structured debate on where opinion ends and falsehood begins, under one rule: every claim must be evidenced, facilitators included.",
    "Role play / simulated tribunal; structured argumentation; the evidence rule applied to adults as well as to participants."),
   ("The four teams produce the manipulation grid in four languages (Romanian, Hungarian, Turkish, Greek). D2.4 Daily reflection, national group then plenary; what comes out of it changes the next day's programme visibly.",
    "Collaborative writing; multilingual peer work; reflection groups; learning diary; a visible feedback loop.")]),

 ("DAY 3 — Wednesday 11/08/2027 · AI or human? · Objectives O1, O2 · AIM: understand generated content from the inside, which is what makes it recognisable · Led by GGD",
  [("D3.1 Participants generate AI text, images and audio themselves and try to fool the other teams with it; they then write their own recognition sheet of indicators. Led by GGD's facilitator, who works with these tools professionally.",
    "Learning by doing; peer challenge as a game; a resource written by the participants rather than given to them."),
   ("D3.2 Peer teaching. Four teams each take one free verification tool — reverse image search, metadata, geolocation, claim databases — learn it, and teach it to the others.",
    "Peer-to-peer teaching; hands-on practice; rotating stations; each team responsible for the others' learning.")],
  [("D3.3 Escape room on digital traces and privacy: what a phone reveals about its owner, solved against the clock in mixed teams.",
    "Escape room; gamification; problem solving under time pressure."),
   ("D3.4 The group writes its own rule on using AI honestly, which binds their own Day 6 productions. D3.5 Daily reflection, national group then plenary.",
    "Facilitated consensus; a rule authored by the participants and applied to themselves; reflection groups; learning diary.")]),

 ("DAY 4 — Thursday 12/08/2027 · Fact-checkers for a day — the assessed day · Objective O2 · AIM: have every participant perform the four verification techniques under observation",
  [("D4.1 The verification newsroom. Three hours in which the mixed teams take real viral claims through the full route to a documented verdict — source and author, date and original context, two independent sources, the image or claim itself — with facilitators intervening only when asked.",
    "Simulation of a real professional practice; non-interventionist facilitation; individual performance observed rather than self-reported."),
   ("The observation grid for O2 is applied here: each of the four group leaders observes one mixed team; Facilitators 1 and 2 independently double-score five participants each, ten of the twenty-one scored twice; the Learning Programme Coordinator moderates and does not score. Each verdict is written up with its sources so another person can check it.",
    "Structured observation on four techniques scored 0–2; independent double scoring; documented written output with source referencing.")],
  [("D4.2 Cross-examination. Each team's verdict is challenged by another team and must be defended with evidence.",
    "Peer review; adversarial questioning; evidence-based defence."),
   ("D4.3 Collective analysis of the day's errors, the facilitators' own included. D4.4 Mid-point review: each participant returns to the two learning targets set on Day 1 and says where they stand.",
    "Error-centred debrief; facilitators modelling fallibility; individual goal review; reflection groups; learning diary.")]),

 ("DAY 5 — Friday 13/08/2027 · Community and intercultural day · Objective O3 · AIM: see what disinformation does to a real place and to real people · Method led by KEA",
  [("D5.1 Visit in and around Beliș — the commune, Lake Fântânele and the village rebuilt higher up after the old one was submerged in the 1970s — guided by residents. Participants collect what is said about the place and by whom.",
    "Field visit; guided observation; informal interviews; outdoor learning; local memory as primary source."),
   ("Preparation of the afternoon dialogue in mixed teams: the questions they want to ask, who asks what, who records.",
    "Mixed-team preparation; question design; distribution of roles decided by the participants.")],
  [("D5.2 Facilitated dialogue with residents and representatives of the municipality on what false information actually circulates locally and who it is hurting. The record of the dialogue becomes the working material of Day 6. Facilitated by KEA's social worker and career counsellor.",
    "Facilitated intergenerational dialogue; active listening; structured note-taking; community-based learning; a social-work method applied to a media-literacy subject."),
   ("D5.3 Intercultural evening. The three groups present their communities, languages, food and music; the Hungarian-language material of the territory is part of it, not an appendix to it.",
    "Intercultural exchange; peer presentation; experiential cultural learning.")]),

 ("DAY 6 — Saturday 14/08/2027 · Make It, Don't Fake It · Objective O3 · AIM: turn what they can check into something other people will watch · Led by GGD, initiative template by KEA",
  [("D6.1 How a short video or an infographic is built to be clear, honest and watchable: structure, framing, sound, and the ethics of editing. Led by GGD, whose expert group includes a social media, cyber-security and artificial intelligence specialist.",
    "Practical workshop led by a media professional; demonstration and critique; applied learning."),
   ("D6.2 Production. Each team debunks one myth recorded on Day 5, under the group's own AI-use rule written on Day 3.",
    "Media production as applied learning; teamwork with roles defined by the team; a self-imposed ethical constraint.")],
  [("D6.3 In parallel, the national groups plan their four local initiatives on the common template supplied by KEA: date, venue, audience, partner, responsibilities, indicator. Two initiatives in different communes of the Romanian territory, one in Türkiye, one in the South Aegean.",
    "Project planning in national groups; template-guided design; peer feedback between groups; the group leader supports rather than coordinates."),
   ("The four media products are finished in English plus a local language. D6.4 Daily reflection, national group then plenary.",
    "Collaborative production; multilingual adaptation; reflection groups; learning diary.")]),

 ("DAY 7 — Sunday 15/08/2027 · Presentation, evaluation, Youthpass · Objectives O1, O2, O3 · AIM: close the learning in public and in writing",
  [("D7.1 Public presentation by the participants to guests from Beliș, the neighbouring communes, the partner municipalities and the local press: the four media products, the manipulation grid and what the week produced. The participants present; the adults answer only if asked.",
    "Public presentation by participants; audience questions; dissemination as a learning activity rather than a communication task."),
   ("D7.2 Youthpass session. Each participant re-reads the “My Digital Map” they sealed on Day 1 against their learning diary and names, with evidence, what changed; the eight key competences are worked through one at a time with a facilitator.",
    "Structured self-assessment; evidence-based reflection; individual Youthpass dialogue; Youthpass as a process running from Day 1 rather than a certificate handed out at the door.")],
  [("D7.3 Participatory evaluation of the whole week by the participants: what worked, what did not, what the next edition should change. Feeds the final report.",
    "Participatory evaluation; anonymous and visual feedback; plenary synthesis; participants as evaluators rather than beneficiaries."),
   ("D7.4 The written, public commitments to the four local initiatives are read out, signed and dated. Youthpass certificates handed over — 21 for participants and 4 for the group leaders. Farewell evening.",
    "Public commitment witnessed by peers and by the host community; celebration and closure.")]),

 ("DEPARTURE DAY — Monday 16/08/2027 (travel day, not counted in the 7 activity days)",
  [("Departure of the three groups. Headcount at every boarding, confirmed by each group leader; domestic transport from the point of arrival to each participant's own home is organised and paid by the project, including the Greek group's inter-island ferry legs.",
    "—"),
   ("The cohort communication group stays open and becomes the working space for the four local initiatives of months 6–15.",
    "Continuity of the peer group as a follow-up method.")],
  []),
]

PV_LINK = "01 — Youth exchange “VERIFAI: Young Detectives Against Digital Disinformation”, Beliș (Cluj County), Romania, 09/08/2027 – 15/08/2027"
PV_ORGS = (
    "5 persons in total: 2 from GENÇ GÖNÜLLÜLER DERNEĞI (OID E10309307, Türkiye) and 2 from KEA IM Syrou (OID E10151458, Greece) — one of the two from each being a young person who will take part in the exchange — plus 1 staff member of ASOCIAȚIA GRUPUL DE ACȚIUNE LOCALĂ NAPOCA POROLISSUM (OID E10181755, Romania), the coordinating and hosting organisation.\n"
    "Requested on three grounds: all 21 participants are minors; both sending partners are new working relationships for the coordinator; and a venue's suitability cannot be assessed from photographs."
)
PV_DURATION = "2 days on site, in month 3 of the project: 16/06/2027 – 17/06/2027 [TO CONFIRM with the partners]."

PV_DAYS = [
 ("DAY 1 — Wednesday 16/06/2027 · The venue and the programme",
  ["On-site verification of the venue against the written risk assessment: fire safety certification and evacuation routes; the state of the electrical installations and heating; security of doors, windows and balconies; lighting of outdoor areas; separation of participant accommodation from any unrelated guests; the rooms in which minors will be accommodated only with minors, with group leaders on the same floors.",
   "Measured test of the internet connection in the plenary room and in the four small-team spaces, because the whole programme depends on it; mobile signal coverage tested across the site; distance and travel time to the nearest medical facility and hospital checked in person; the reference medical facility and the first-aid arrangements identified and written down."],
  ["Working session with the partners on the division of the thematic days: GGD confirms what it leads on Day 3 and Day 6 and which of its staff will be Facilitator 2; KEA confirms the Day 5 dialogue method and the local-initiative template; the coordinator confirms Days 1, 2, 4 and 7. The daily timetable is finalised session by session, in the same room and in one sitting.",
   "The three measurement instruments are agreed: the fifteen-item practical test (Form A and Form B), the observation grid of four techniques scored 0–2, and the beneficiary exercise for the local initiatives; the observer calibration exercise of month 4 is scheduled. Safeguarding arrangements, the night-duty rota, the emergency protocol and the sensitive-content protocol are agreed in writing."]),

 ("DAY 2 — Thursday 17/06/2027 · The host community and the practical arrangements",
  ["Visit to the sites of the Day 5 community day in and around Beliș; meeting at the mayor's office and with residents who have agreed to take part in the dialogue; the route, the timing and the group transport are agreed on the spot.",
   "The young person from each sending organisation sees the venue, the village and the rooms, and their observations are written into the final programme — which is the reason they travel rather than a courtesy."],
  ["Practical arrangements settled: meals and dietary requirements with the local producers; insurance for all 27 persons; the visa file and its timetable for the Turkish group, starting five months before the activity; the ferry and flight timings for the Greek group and its four eligible travel days; the domestic transport plan from each participant's own home.",
   "Written minutes with decisions, owners and deadlines; signature of the partnership agreement annexes on safeguarding and on the division of tasks; the four joint online preparation sessions of months 3 and 4 fixed in the calendar, in mixed national composition."]),
]
