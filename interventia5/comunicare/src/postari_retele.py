# -*- coding: utf-8 -*-
"""Postările pentru Facebook și LinkedIn (campania A2 online, L2–L3) și textul pentru secțiunea „Despre” a paginilor GAL.

Facebook: cele 5 postări săptămânale din postari_texte.py, joia la 10:00.
LinkedIn: aceleași 5 teme, rescrise pentru un public profesional (directori de școli, coordonatori de ONG-uri, primării,
alte GAL-uri, experți), marțea următoare la 09:00. Aceleași imagini 1080 × 1350 (4:5), potrivite pe ambele rețele.
Fiecare postare are la final mențiunea obligatorie (Anexa II C1.1-6, GIV V3 C-(1)); imaginile au bara de sigle cu emblema UE."""
import json, pathlib
from postari_texte import POSTARI as FB, MENTIUNE, HASHTAGS as HASHTAGS_FB

HASHTAGS_LI = '#LEADER #EducatiePentruMediu #DezvoltareRurala #PS2027 #GALNapocaPorolissum'
LINK_FEADR = 'https://agriculture.ec.europa.eu/cap-my-country/rural-development_ro'

LI = [
    dict(nr=1, data='marți, 20.10.2026, ora 09:00', tema='Prezentarea proiectului (de fixat sus pe pagină)', imagine=1,
         text="""Un GAL din vestul județului Cluj lansează o schemă de micro-granturi pentru educația de mediu în 14 comunități rurale.

GAL Napoca Porolissum implementează proiectul „Educație pentru mediu în teritoriul GAL Napoca Porolissum – micro-granturi pentru mediu”, finanțat prin intervenția „LEADER în verde” din Planul Strategic PAC 2023 – 2027.

Pe scurt:
• 138.643 € sprijin nerambursabil, din care 119.000 € ajung direct în comunități;
• 6 micro-granturi de până la 19.833,3 € fiecare;
• pentru grădinițe, școli, licee și ONG-uri de mediu din cele 14 localități ale teritoriului;
• un apel competitiv, lansat la începutul anului 2027, cu criterii publice și o comisie de evaluare cu membri interni și externi.

De ce: în teritoriul nostru sunt școli și organizații care vor să facă educație pentru mediu prin acțiuni concrete, dar inițiativele lor rămân sporadice din lipsă de resurse. Proiectul le oferă un mecanism local de finanțare și sprijin.

Ce urmărim: 6 proiecte de educație și protecție a mediului puse în practică în comunitățile noastre și un schimb de bune practici care să ducă mai departe ce funcționează.

Lucrați într-o școală sau într-un ONG din teritoriu, sau cunoașteți pe cineva care ar trebui să afle? Vă rugăm să distribuiți."""),
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

NOTE_FB = {
    1: 'Fixați postarea sus pe pagina de Facebook: ține loc de informarea „vizibilă în jumătatea de sus a primei pagini” cerută de GIV V3 B-(2).',
}
NOTE_LI = {
    1: 'Fixați postarea sus pe pagina de LinkedIn: ține loc de informarea „vizibilă în jumătatea de sus a primei pagini” cerută de GIV V3 B-(2).',
    2: 'Statistica PISA 2018 este cea din cererea de finanțare (Anexa 1, cap. 1).',
    4: 'Ultimul paragraf anunță căutarea de evaluatori externi. Scoateți-l dacă nu vreți încă să faceți anunțul public.',
}

DESPRE_SCURT = 'Proiecte cofinanțate de UE prin PS 2023–2027 (FEADR, LEADER). Detalii: napocaporolissum.ro'

DESPRE = f"""Proiect finanțat cu fonduri europene nerambursabile prin Planul Strategic PAC 2023 – 2027 (PS 2023 – 2027)

„Educație pentru mediu în teritoriul GAL Napoca Porolissum – micro-granturi pentru mediu”
Beneficiar: Asociația Grupul de Acțiune Locală Napoca Porolissum
Localizare: teritoriul GAL Napoca Porolissum, județul Cluj (Aghireșu, Beliș, Călățele, Căpușu Mare, Gilău, Huedin, Izvoru Crișului, Măguri-Răcătău, Mănăstireni, Mărgău, Mărișel, Râșca, Săcuieu, Sâncraiu)
Sprijin nerambursabil: 138.643 € · Perioada: 08.09.2026 – 08.06.2028

Prin proiect, GAL Napoca Porolissum finanțează, printr-un apel competitiv, 6 micro-granturi de până la 19.833,3 € pentru inițiative de educație și protecție a mediului ale unităților de învățământ și ONG-urilor din teritoriu. Rezultate urmărite: 6 sub-proiecte de mediu contractate și implementate, 2 campanii de informare și un schimb de bune practici.

{MENTIUNE}
Mai multe despre FEADR: {LINK_FEADR}"""


def fb_text(p):
    return f"{p['text']}\n\n—\n{MENTIUNE}\n\n{HASHTAGS_FB}"


def li_text(p):
    return f"{p['text']}\n\n—\n{MENTIUNE}\n\n{HASHTAGS_LI}"


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
           'Campania online A2, lunile L2–L3. Facebook: joia la 10:00. LinkedIn: marțea la 09:00. Aceleași imagini din `social/` '
           '(1080 × 1350 px), pe ambele rețele. Nicio postare nu se publică înainte de aprobare.\n',
           '## Secțiunea „Despre” a paginilor\n',
           f'**Text scurt** ({len(DESPRE_SCURT)} caractere; încape în „Intro” pe Facebook, max. 101):\n', '```text', DESPRE_SCURT, '```\n',
           '**Text detaliat** (LinkedIn: Despre noi → Prezentare, după textul existent al GAL, max. 2.000 de caractere în total; '
           'Facebook: în secțiunea Despre, dacă pagina are câmp pentru o descriere lungă; altfel ajunge postarea 1 fixată sus):\n',
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
