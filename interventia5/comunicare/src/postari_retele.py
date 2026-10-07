# -*- coding: utf-8 -*-
"""Postările pentru Facebook și LinkedIn (campania A2 online, L2–L3) și textul pentru secțiunea „Despre” a paginilor GAL.

Toate sunt bilingve: textul în română, apoi „🇬🇧 English” și versiunea în engleză; la final mențiunea obligatorie în română
(textul exact cerut de AFIR) urmată de traducerea ei.

Facebook: cele 5 postări săptămânale din postari_texte.py, joia la 10:00.
LinkedIn: aceleași 5 teme, rescrise pentru un public profesional (directori de școli, coordonatori de ONG-uri, primării,
alte GAL-uri, experți), marțea următoare la 09:00. Aceleași imagini 1080 × 1350 (4:5), potrivite pe ambele rețele.
Fiecare postare are la final mențiunea obligatorie (Anexa II C1.1-6, GIV V3 C-(1)); imaginile au bara de sigle cu emblema UE."""
import json, pathlib
from postari_texte import POSTARI as FB, MENTIUNE, HASHTAGS as HASHTAGS_FB

HASHTAGS_LI = '#LEADER #EducatiePentruMediu #EnvironmentalEducation #RuralDevelopment #GALNapocaPorolissum'
HASHTAGS_FB_EN = '#EnvironmentalEducation'
LINK_FEADR = 'https://agriculture.ec.europa.eu/cap-my-country/rural-development_ro'

LI = [
    dict(nr=1, data='marți, 20.10.2026, ora 09:00', tema='Prezentarea proiectului (de fixat sus pe pagină)', imagine=1,
         text="""Un GAL din vestul județului Cluj lansează o schemă de micro-granturi pentru educația de mediu în 14 comunități rurale.

GAL Napoca Porolissum implementează proiectul „Educație pentru mediu în teritoriul GAL Napoca Porolissum – micro-granturi pentru mediu”, finanțat prin intervenția „LEADER în verde” din Planul Strategic PAC 2023 – 2027.

Pe scurt:
• 138.643 € sprijin nerambursabil, din care 119.000 € ajung direct în comunități;
• 6 micro-granturi de până la 19.833,3 € fiecare;
• pentru grădinițe, școli, licee și ONG-uri de mediu din cele 14 localități ale teritoriului;
• un apel competitiv la începutul anului 2027, cu criterii publice și o comisie de evaluare mixtă, cu experți externi.

De ce: în teritoriu sunt școli și organizații care vor să facă educație pentru mediu prin acțiuni concrete, dar inițiativele lor rămân sporadice din lipsă de resurse. Proiectul le oferă un mecanism local de finanțare și sprijin.

Ce urmărim: 6 proiecte de educație și protecție a mediului puse în practică în comunitățile noastre și un schimb de bune practici care să ducă mai departe ce funcționează.

Lucrați cu școli sau ONG-uri din teritoriu? Vă rugăm să distribuiți."""),
    dict(nr=2, data='marți, 27.10.2026, ora 09:00', tema='Pentru cine sunt micro-granturile', imagine=2,
         text="""80% dintre elevii români care au participat la testele PISA din 2018 spun că protejarea mediului e importantă pentru ei. 60% dintre ei se simt însă neputincioși să schimbe ceva.

Micro-granturile pentru mediu ale GAL Napoca Porolissum vor să le dea școlilor și ONG-urilor din teritoriu mijloacele de a trece de la intenție la acțiune.

Pot aplica:
• grădinițele, școlile și liceele din teritoriul GAL Napoca Porolissum;
• ONG-urile active în educația pentru mediu, cu sediu, filială sau activitate dovedită în teritoriu.

Teritoriul cuprinde 14 localități: Aghireșu, Beliș, Călățele, Căpușu Mare, Gilău, Huedin, Izvoru Crișului, Măguri-Răcătău, Mănăstireni, Mărgău, Mărișel, Râșca, Săcuieu și Sâncraiu.

Fiecare solicitant poate depune un singur proiect, iar activitățile se desfășoară în teritoriul GAL.

Cunoașteți un director de școală sau un coordonator de ONG din aceste localități? O distribuire îl poate ajuta să afle la timp."""),
    dict(nr=3, data='marți, 03.11.2026, ora 09:00', tema='Ce se poate finanța', imagine=3,
         text="""Copiii și adulții învață mai mult despre mediu atunci când fac ceva concret pentru locul în care trăiesc. În mediul rural, astfel de ocazii sunt puține.

De aceea, micro-granturile pentru mediu ale GAL Napoca Porolissum finanțează activități practice, de exemplu:
• plantări de arbori și acțiuni de ecologizare;
• reciclare și colectare selectivă;
• teatru, scenete, cluburi after-school și pictură în școli, pe teme de mediu;
• activități sportive legate de protecția mediului;
• concursuri cu drone;
• echipamente care sprijină protecția mediului.

Temele: aer, apă, păduri, biodiversitate, deșeuri, energie regenerabilă, schimbări climatice și transport cu emisii scăzute.

Lucrați la o idee de proiect? Echipa GAL oferă gratuit informații și consiliere privind eligibilitatea și apelul: contact@napocaporolissum.ro."""),
    dict(nr=4, data='marți, 10.11.2026, ora 09:00', tema='Selecția, transparent', imagine=4,
         text="""Cum alegi corect 6 proiecte din mai multe propuneri bune? Cu criterii publicate dinainte și o comisie mixtă.

Selecția micro-granturilor pentru mediu se face pe un punctaj de la 0 la 100:
• ore de voluntariat – până la 25 de puncte;
• proiecte comunitare – până la 25 de puncte;
• calitatea planului de intervenție – până la 30 de puncte;
• interviul cu juriul – până la 20 de puncte (minimum 12).

Pragul minim este de 50 de puncte, iar granturile se acordă în ordinea punctajului, până la epuizarea bugetului.

Evaluează o comisie de cel puțin 5 membri: 3 din echipa GAL și 2 experți externi, instruiți înainte de evaluare. Contestațiile au termene clare, iar rezultatele se publică pe www.napocaporolissum.ro.

Sunteți expert în educație pentru mediu și v-ar interesa rolul de evaluator extern? Urmăriți pagina: vom publica un anunț."""),
    dict(nr=5, data='marți, 17.11.2026, ora 09:00', tema='Pregătirea pentru apel', imagine=5,
         text="""Pentru directorii de școli și coordonatorii de ONG-uri din teritoriul GAL Napoca Porolissum: apelul pentru micro-granturile de mediu se deschide la începutul anului 2027. Iată ce puteți face de acum:

1. Stabiliți echipa care va scrie și va implementa proiectul.
2. Țineți evidența orelor de voluntariat, cu contracte și fișe de voluntariat. Contează la punctaj.
3. Planificați cel puțin două acțiuni comunitare, fiecare cu minimum 20 de participanți. Sunt obligatorii pentru proiectele selectate.
4. Scrieți-ne la contact@napocaporolissum.ro cu numele instituției și vă anunțăm primii când se deschide apelul.

Informațiile și consilierea privind eligibilitatea și apelul sunt gratuite, la 0728 146 123 sau la sediul din Gilău. Proiectul îl scrieți voi; noi vă ajutăm să înțelegeți regulile."""),
]

# ---------------------------------------------------------------- versiunile în engleză
SEP_EN = '🇬🇧 English'

MENTIUNE_EN = ('Project financed with non-reimbursable European funds through the CAP Strategic Plan 2023–2027 (PS 2023–2027). '
               'PS 2023–2027 is implemented by the Agency for Financing Rural Investments (AFIR), under the Ministry of Agriculture '
               'and Rural Development. PS 2023–2027 is financed by the European Union and the Government of Romania through the '
               'European Agricultural Fund for Rural Development (EAFRD).')

EN_FB = {
    1: """🌱 Good news for schools and NGOs in our area!

The Napoca Porolissum Local Action Group (LAG) has started the project “Environmental education in the Napoca Porolissum LAG territory – micro-grants for the environment”. Through it we will fund 6 local environmental education and protection initiatives, with up to €19,833.30 each, 100% non-reimbursable.

👉 Who can apply: kindergartens, schools, high schools and environmental NGOs from the 14 localities of our territory.
👉 What can be funded: tree planting, clean-ups, recycling, shows and workshops, sport for nature, drone competitions, environmental equipment.

The call opens in early 2027. Until then, every Thursday we will share here what you need to know to get ready. 💚

Want to be the first to know when the call opens? Write to us at contact@napocaporolissum.ro.""",
    2: """Who can get an environmental micro-grant? 🏫🌿

✅ kindergartens, schools and high schools in the Napoca Porolissum LAG territory;
✅ NGOs active in environmental education, with their headquarters, a branch or proven activity in the territory.

Our territory covers the 14 localities listed above. Each applicant may submit one project, and the activities take place in the LAG territory.

Know a school or an association that should hear this? Tag them! 👇""",
    3: """What would you do for nature with a dedicated budget? 💡🌳

The micro-grants can fund, for example:
🌱 tree planting and clean-up actions;
♻️ recycling and separate waste collection;
🎭 theatre, sketches, after-school clubs and painting in schools;
⚽ sports activities linked to environmental protection;
🚁 drone competitions;
🧰 equipment that supports environmental protection.

Awareness actions on air, water, forests, biodiversity, renewable energy, climate change and low-emission transport can also be funded.

Tell us in the comments: what green idea would make a difference in your community?""",
    4: """How will the 6 projects be chosen? Transparently, using public criteria. 📊

Each project gets a score from 0 to 100:
• volunteering hours – up to 25 points;
• community projects – up to 25 points;
• quality of the intervention plan – up to 30 points;
• interview with the jury – up to 20 points (minimum 12).

The minimum selection threshold is 50 points. A mixed jury of LAG staff and external experts evaluates the projects, and grants are awarded in order of score until the budget runs out.

All details will be in the call guide at www.napocaporolissum.ro.""",
    5: """The call opens in early 2027, but you can start preparing today. ⏳

1️⃣ Build the team that will run the project.
2️⃣ Keep records of volunteering hours (volunteer contracts and timesheets): they count towards your score.
3️⃣ Plan at least two community actions, each with at least 20 participants. They are mandatory for the winning projects.
4️⃣ Write to us at contact@napocaporolissum.ro with the name of your institution and we will let you know first when the call opens.

Questions? Call us at +40 728 146 123 or visit our office in Gilău. We offer free information and advice on eligibility and the call; you write the project yourselves.""",
}

EN_LI = {
    1: """A Local Action Group in western Cluj County is launching a micro-grant scheme for environmental education in 14 rural communities.

The Napoca Porolissum LAG is implementing the project “Environmental education in the Napoca Porolissum LAG territory – micro-grants for the environment”, funded through the “LEADER in Green” intervention of Romania’s CAP Strategic Plan 2023–2027.

In short:
• €138,643 in non-reimbursable support, of which €119,000 goes directly to communities;
• 6 micro-grants of up to €19,833.30 each;
• for kindergartens, schools, high schools and environmental NGOs in the 14 localities of the territory;
• a competitive call in early 2027, with public criteria and a mixed evaluation committee.

Our goal: 6 environmental projects carried out in our communities and a good-practice exchange to spread what works.

Working with schools or NGOs in the area? Please share.""",
    2: """80% of Romanian students who took the 2018 PISA tests say protecting the environment matters to them, yet 60% feel powerless to change anything.

The Napoca Porolissum LAG’s environmental micro-grants aim to give schools and NGOs in our territory the means to move from intention to action.

Eligible applicants:
• kindergartens, schools and high schools in the Napoca Porolissum LAG territory;
• NGOs active in environmental education, with their headquarters, a branch or proven activity in the territory (the 14 localities listed above).

Each applicant may submit one project, carried out in the LAG territory.

Know a school principal or an NGO coordinator in these localities? A share can help them hear about it in time.""",
    3: """Children and adults learn more about the environment when they do something concrete for the place they live in. In rural areas, such opportunities are scarce.

That is why the Napoca Porolissum LAG’s environmental micro-grants fund hands-on activities, such as:
• tree planting and clean-ups;
• recycling and separate collection;
• theatre, sketches, after-school clubs and painting in schools, on environmental themes;
• sports activities linked to environmental protection;
• drone competitions;
• equipment that supports environmental protection.

Themes: air, water, forests, biodiversity, waste, renewable energy, climate change and low-emission transport.

Working on a project idea? The LAG team offers free information and advice on eligibility and the call: contact@napocaporolissum.ro.""",
    4: """How do you fairly choose 6 projects out of many good proposals? With criteria published in advance and a mixed committee.

Projects are scored from 0 to 100:
• volunteering hours – up to 25 points;
• community projects – up to 25 points;
• quality of the intervention plan – up to 30 points;
• interview with the jury – up to 20 points (minimum 12).

The minimum threshold is 50 points, and grants are awarded in order of score until the budget runs out.

The evaluation committee has at least 5 members: 3 LAG staff and 2 external experts, trained before the evaluation. Appeals follow clear deadlines, and results are published at www.napocaporolissum.ro.

Are you an environmental education expert interested in serving as an external evaluator? Follow our page: we will publish a call.""",
    5: """For school principals and NGO coordinators in the Napoca Porolissum LAG territory: the call for environmental micro-grants opens in early 2027. Here is what you can do now:

1. Set up the team that will write and implement the project.
2. Keep records of volunteering hours, with volunteer contracts and timesheets. They count towards the score.
3. Plan at least two community actions, each with at least 20 participants. They are mandatory for the selected projects.
4. Write to us at contact@napocaporolissum.ro with your institution’s name and we will let you know first when the call opens.

Information and advice on eligibility and the call are free: +40 728 146 123 or at our office in Gilău. You write the project; we help you understand the rules.""",
}

NOTE_FB = {
    1: 'Fixați postarea sus pe pagina de Facebook: ține loc de informarea „vizibilă în jumătatea de sus a primei pagini” cerută de GIV V3 B-(2).',
}
NOTE_LI = {
    1: 'Fixați postarea sus pe pagina de LinkedIn: ține loc de informarea „vizibilă în jumătatea de sus a primei pagini” cerută de GIV V3 B-(2).',
    2: 'Statistica PISA 2018 este cea din cererea de finanțare (Anexa 1, cap. 1).',
    4: 'Ultimul paragraf anunță căutarea de evaluatori externi. Scoateți-l dacă nu vreți încă să faceți anunțul public.',
}

DESPRE_SCURT = 'Cofinanțat de UE prin PS 2023–2027 · Co-funded by the EU (EAFRD, LEADER) · napocaporolissum.ro'

DESPRE = f"""„Educație pentru mediu în teritoriul GAL Napoca Porolissum – micro-granturi pentru mediu”
Beneficiar: Asociația Grupul de Acțiune Locală Napoca Porolissum · Localizare: teritoriul GAL Napoca Porolissum, județul Cluj (Aghireșu, Beliș, Călățele, Căpușu Mare, Gilău, Huedin, Izvoru Crișului, Măguri-Răcătău, Mănăstireni, Mărgău, Mărișel, Râșca, Săcuieu, Sâncraiu) · Sprijin nerambursabil: 138.643 € · 08.09.2026 – 08.06.2028
Prin apel competitiv, GAL finanțează 6 micro-granturi de până la 19.833,3 € pentru inițiative de educație și protecție a mediului ale școlilor și ONG-urilor din teritoriu. Rezultate urmărite: 6 sub-proiecte de mediu contractate și implementate, 2 campanii de informare, un schimb de bune practici.
{MENTIUNE}

{SEP_EN}
“Environmental education in the Napoca Porolissum LAG territory – micro-grants for the environment”
Beneficiary: Napoca Porolissum Local Action Group Association · Location: the LAG territory, Cluj County, Romania (14 localities) · Non-reimbursable support: €138,643 · 08.09.2026 – 08.06.2028
Through a competitive call, the LAG funds 6 micro-grants of up to €19,833.30 for environmental education and protection initiatives of schools and NGOs in the territory. Expected results: 6 environmental sub-projects contracted and implemented, 2 information campaigns, a good-practice exchange.
{MENTIUNE_EN}

FEADR / EAFRD: {LINK_FEADR}"""

LIMITA_LI = 3000


def bilingv(ro, en, hashtags):
    return f"{ro}\n\n{SEP_EN}\n\n{en}\n\n—\n{MENTIUNE}\n\n{MENTIUNE_EN}\n\n{hashtags}"


def fb_text(p):
    return bilingv(p['text'], EN_FB[p['nr']], f'{HASHTAGS_FB} {HASHTAGS_FB_EN}')


def li_text(p):
    t = bilingv(p['text'], EN_LI[p['nr']], HASHTAGS_LI)
    n = len(t.encode('utf-16-le')) // 2          # LinkedIn numără unități UTF-16 (un steag = 4)
    assert n <= LIMITA_LI - 50, f"LinkedIn {p['nr']}: {n} caractere, limita e {LIMITA_LI}"
    return t


def toate():
    """Lista postărilor în ordinea publicării, cu id stabil (fb1…fb5, li1…li5)."""
    out = []
    for p in FB:
        out.append(dict(id=f"fb{p['nr']}", retea='Facebook', nr=p['nr'], data=p['data'], tema=p['tema'],
                        imagine=p['fisier'], text=fb_text(p), alt=p['alt'], nota=NOTE_FB.get(p['nr'], '')))
    for p in LI:
        f = FB[p['imagine'] - 1]
        out.append(dict(id=f"li{p['nr']}", retea='LinkedIn', nr=p['nr'], data=p['data'], tema=p['tema'],
                        imagine=f['fisier'], text=li_text(p), alt=f['alt'], nota=NOTE_LI.get(p['nr'], '')))
    return out


def markdown():
    out = ['# Postări Facebook și LinkedIn – „Educație pentru mediu” (micro-granturi)\n',
           'Campania online A2, lunile L2–L3. Facebook: joia la 10:00. LinkedIn: marțea la 09:00. Fiecare postare e bilingvă: română, apoi engleză. '
           'Aceleași imagini din `social/` '
           '(1080 × 1350 px), pe ambele rețele. Nicio postare nu se publică înainte de aprobare.\n',
           '## Secțiunea „Despre” a paginilor\n',
           f'**Text scurt** ({len(DESPRE_SCURT)} caractere; încape în „Intro” pe Facebook, max. 101):\n', '```text', DESPRE_SCURT, '```\n',
           f'**Text detaliat** ({len(DESPRE)} de caractere; Facebook: în secțiunea Despre, dacă pagina are câmp pentru o descriere lungă. '
           'Pe LinkedIn nu încape: secțiunea Prezentare are max. 2.000 de caractere, deci acolo adăugați textul scurt și fixați postarea LinkedIn 1):\n',
           '```text', DESPRE, '```\n']
    for retea in ('Facebook', 'LinkedIn'):
        out.append(f'\n## {retea}\n')
        for p in [q for q in toate() if q['retea'] == retea]:
            out += [f"\n### {retea} {p['nr']} – {p['tema']}\n", f"**Când:** {p['data']} · **Imagine:** `social/{p['imagine']}`\n"]
            if p['nota']:
                out.append(f"**Notă:** {p['nota']}\n")
            out += ['```text', p['text'], '```\n', f"**Text alternativ:** {p['alt']}\n"]
    return '\n'.join(out)


if __name__ == '__main__':
    root = pathlib.Path(__file__).resolve().parent.parent
    (root / 'social' / 'Postari_Facebook_LinkedIn.md').write_text(markdown(), encoding='utf-8')
    build = root / 'src' / '_build'; build.mkdir(exist_ok=True)
    (build / 'postari_retele.json').write_text(json.dumps(dict(postari=toate(), despre=DESPRE, despre_scurt=DESPRE_SCURT),
                                                          ensure_ascii=False, indent=1), encoding='utf-8')
    for p in toate():
        print(p['id'], len(p['text']), p['data'])
