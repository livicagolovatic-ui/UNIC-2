# -*- coding: utf-8 -*-
"""Textele celor 5 postări săptămânale (campania A2 de informare, lunile L2–L3)."""

MENTIUNE = ('Proiect finanțat cu fonduri europene nerambursabile prin Planul Strategic PAC 2023 – 2027 (PS 2023 – 2027). '
            'PS 2023 – 2027 este implementat de Agenția pentru Finanțarea Investițiilor Rurale, din subordinea Ministerului '
            'Agriculturii și Dezvoltării Rurale. PS 2023 – 2027 este finanțat de Uniunea Europeană și Guvernul României prin '
            'Fondul european agricol pentru dezvoltare rurală.')

HASHTAGS = '#GALNapocaPorolissum #EducatiePentruMediu #MicroGranturiPentruMediu #LEADER #PS2027 #FEADR #ApuseniiClujului'

POSTARI = [
    dict(nr=1, data='joi, 15.10.2026, ora 10:00', tema='Anunțul proiectului', model='Model A – anunț',
         fisier='Postarea1_anunt_proiect.png',
         text="""🌱 Avem o veste bună pentru școlile și ONG-urile din teritoriul nostru!

GAL Napoca Porolissum a pornit proiectul „Educație pentru mediu în teritoriul GAL Napoca Porolissum – micro-granturi pentru mediu”. Prin el vom finanța 6 inițiative locale de educație și protecție a mediului, cu până la 19.833,3 € fiecare, 100% nerambursabil.

👉 Cine poate aplica: grădinițe, școli, licee și ONG-uri de mediu din cele 14 localități ale teritoriului.
👉 Ce se poate face: plantări, ecologizări, reciclare, spectacole și ateliere, sport pentru natură, concursuri cu drone, echipamente pentru mediu.

Apelul se lansează la începutul anului 2027. Până atunci, în fiecare joi vă spunem aici tot ce trebuie să știți ca să vă pregătiți. 💚

Vreți să aflați primii când se deschide apelul? Scrieți-ne la contact@napocaporolissum.ro.""",
         alt='Card verde cu siglele finanțatorilor sus și titlul „Pornim micro-granturile pentru mediu!”. Text: 6 micro-granturi de până la '
             '19.833,3 €, 100% nerambursabile, pentru grădinițe, școli, licee și ONG-uri de mediu din teritoriul GAL Napoca Porolissum. '
             'Apelul se lansează la începutul anului 2027. Jos, dealuri cu brazi și logo-ul proiectului „Educație pentru mediu”.'),
    dict(nr=2, data='joi, 22.10.2026, ora 10:00', tema='Cine poate aplica', model='Model B – card informativ',
         fisier='Postarea2_cine_poate_aplica.png',
         text="""Cine poate primi un micro-grant pentru mediu? 🏫🌿

✅ grădinițele, școlile și liceele din teritoriul GAL Napoca Porolissum;
✅ ONG-urile active în educația pentru mediu, cu sediu, filială sau activitate dovedită în teritoriu.

Teritoriul nostru înseamnă 14 localități: Aghireșu, Beliș, Călățele, Căpușu Mare, Gilău, Huedin, Izvoru Crișului, Măguri-Răcătău, Mănăstireni, Mărgău, Mărișel, Râșca, Săcuieu și Sâncraiu.

Fiecare solicitant poate depune un singur proiect, iar activitățile se desfășoară în teritoriul GAL.

Cunoașteți o școală sau o asociație căreia i-ar folosi vestea asta? Dați-i tag! 👇""",
         alt='Card crem cu titlul „Cine poate aplica?”. Două casete: „Grădinițe, școli și licee din teritoriul GAL Napoca Porolissum” '
             'și „ONG-uri de mediu cu sediu, filială sau activitate dovedită în teritoriu”, apoi cele 14 localități ale teritoriului.'),
    dict(nr=3, data='joi, 29.10.2026, ora 10:00', tema='Ce idei pot primi finanțare', model='Model B – card informativ',
         fisier='Postarea3_ce_se_finanteaza.png',
         text="""Ce ați face pentru natură dacă ați avea un buget dedicat? 💡🌳

Micro-granturile pot finanța, de exemplu:
🌱 plantări de arbori și acțiuni de ecologizare;
♻️ reciclare și colectare selectivă;
🎭 spectacole de teatru, scenete, cluburi after-school și pictură în școli;
⚽ activități sportive legate de protecția mediului;
🚁 concursuri cu drone;
🧰 echipamente care sprijină protecția mediului.

Se finanțează și acțiuni de conștientizare despre aer, apă, păduri, biodiversitate, energie regenerabilă, schimbări climatice și transport cu emisii scăzute.

Spuneți-ne în comentarii: ce idee verde ar schimba ceva în comunitatea voastră?""",
         alt='Card crem cu titlul „Ce idei pot primi finanțare?” și șase iconițe: plantări și ecologizări, reciclare și colectare selectivă, '
             'teatru, scenete, pictură, sport pentru natură, concursuri cu drone, echipamente pentru mediu.'),
    dict(nr=4, data='joi, 05.11.2026, ora 10:00', tema='Cum se aleg proiectele', model='Model B – card informativ',
         fisier='Postarea4_cum_se_aleg_proiectele.png',
         text="""Cum se aleg cele 6 proiecte? Transparent, după criterii publice. 📊

Fiecare proiect primește un punctaj de la 0 la 100:
• ore de voluntariat – până la 25 de puncte;
• proiecte comunitare – până la 25 de puncte;
• calitatea planului de intervenție – până la 30 de puncte;
• interviul cu juriul – până la 20 de puncte (minimum 12).

Pragul minim de selecție este de 50 de puncte. Evaluează un juriu mixt, format din echipa GAL și experți externi, iar granturile se acordă în ordinea punctajului, până la epuizarea bugetului.

Toate detaliile vor fi în ghidul apelului, pe www.napocaporolissum.ro.""",
         alt='Card crem cu titlul „Cum se aleg proiectele?” și patru bare de punctaj: ore de voluntariat 25 p, proiecte comunitare 25 p, '
             'calitatea planului de intervenție 30 p, interviul cu juriul 20 p. Prag minim 50 din 100, juriu format din echipa GAL și experți externi.'),
    dict(nr=5, data='joi, 12.11.2026, ora 10:00', tema='Pregătește-te din timp', model='Model A – anunț',
         fisier='Postarea5_pregateste-te_din_timp.png',
         text="""Apelul se deschide la începutul lui 2027, dar pregătirea poate începe de azi. ⏳

1️⃣ Formați echipa care va duce proiectul.
2️⃣ Țineți evidența orelor de voluntariat (contracte și fișe de voluntariat): contează la punctaj.
3️⃣ Gândiți cel puțin două acțiuni comunitare, fiecare cu minimum 20 de participanți. Sunt obligatorii pentru proiectele câștigătoare.
4️⃣ Scrieți-ne la contact@napocaporolissum.ro cu numele instituției și vă anunțăm primii când se deschide apelul.

Aveți întrebări? Ne găsiți la 0728 146 123 sau la sediul din Gilău. Vă oferim gratuit informații și consiliere despre eligibilitate și apel; proiectul îl scrieți voi.""",
         alt='Card verde cu titlul „4 lucruri de făcut chiar de acum”: formați echipa, țineți evidența orelor de voluntariat, gândiți cel puțin '
             '2 acțiuni comunitare cu minimum 20 de participanți, scrieți-ne la contact@napocaporolissum.ro ca să vă anunțăm primii.'),
]


def text_complet(p):
    return f"{p['text']}\n\n—\n{MENTIUNE}\n\n{HASHTAGS}"


def markdown():
    out = ['# Postări săptămânale – „Educație pentru mediu” (micro-granturi)\n',
           'Se publică pe Facebook și Instagram (și pe celelalte canale ale GAL). La fiecare postare se încarcă imaginea din `social/`, '
           'textul de mai jos (cu mențiunea obligatorie la final) și textul alternativ.\n']
    for p in POSTARI:
        out += [f"\n## Postarea {p['nr']} – {p['tema']}\n", f"**Când:** {p['data']} · **Imagine:** `social/{p['fisier']}` ({p['model']})\n",
                '**Text:**\n', '```text', text_complet(p), '```\n', f"**Text alternativ (alt text):** {p['alt']}\n"]
    return '\n'.join(out)


if __name__ == '__main__':
    import pathlib
    root = pathlib.Path(__file__).resolve().parent.parent
    (root / 'social' / 'Postari_saptamanale_texte.md').write_text(markdown(), encoding='utf-8')
    print('ok')
