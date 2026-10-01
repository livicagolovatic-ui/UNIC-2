# -*- coding: utf-8 -*-
"""Ședința 1 – „Cine sunt eu și ce am bun?” – scenariu complet + anexe de tipărit."""
import os
from lib_unic import *
from justificativ import fisa_activitate, metode, raport

OUT = os.path.join(HERE, 'Sedinta_1_Cine_sunt_eu_Scenariu_si_Anexe.docx')
D = UnicDoc('Proiect UNIC – cod MySMIS 352704   |   Atelier „Eu, punctele mele forte și ce mă motivează”   |   Ședința 1')
d = D.d

# =====================================================================  SCENARIU
D.banner('ATELIER DE DEZVOLTARE PERSONALĂ  •  ȘEDINȚA 1 DIN 2',
         'CINE SUNT EU ȘI CE AM BUN?',
         'Atelier „Eu, punctele mele forte și ce mă motivează”  •  60 de minute  •  Clasele a VII-a – a VIII-a  •  10–15 elevi',
         'Tema creativă: AGENȚIA SECRETĂ A PUNCTELOR FORTE')

fisa_activitate(D, 1, 'Cine sunt eu și ce am bun?', [
    'Ședința face parte dintr-un atelier de dezvoltare personală de 2 ședințe a câte 60 de minute, destinat elevilor din clasele a VII-a – '
    'a VIII-a. Scopul ședinței este dezvoltarea autocunoașterii prin identificarea punctelor forte și a resurselor personale, precum și '
    'exersarea oferirii și primirii feedbackului pozitiv.',
    'Activitatea a fost proiectată și realizată de facilitatorul comunitar: elaborarea scenariului detaliat și a 9 materiale-suport '
    '(Anexele 1–9), pregătirea logistică, facilitarea directă a ședinței cu grupul țintă, evaluarea și raportarea rezultatelor. '
    'Ședința cuprinde 7 secvențe de învățare experiențială (joc de energizare, exercițiu anonim, interviu în perechi, hartă colectivă '
    'a resurselor, studiu de caz, cerc de feedback, reflecție individuală), descrise la secțiunea 9.',
], [
    ('Documentare și proiectare', 'Analiza nevoilor grupului țintă; documentare privind metode de dezvoltare personală adaptate vârstei de 13–14 ani; '
     'elaborarea scenariului detaliat (obiective, etape, timp, replici, întrebări de reflecție, gestionarea situațiilor dificile).'),
    ('Elaborarea materialelor-suport', 'Conceperea și redactarea celor 9 anexe: ecusoane, bilețele „Dosar secret”, Fișa 1 – Detectivul, indicatoare, '
     'cartonașe „Misiunea imposibilă”, banca de complimente, Cardul de agent, Fișa 2 – Harta mea, bilet de ieșire.'),
    ('Pregătire logistică', 'Comunicarea cu unitatea de învățământ (stabilirea datei, a sălii și a grupului); multiplicarea și decuparea '
     'materialelor; pregătirea consumabilelor; amenajarea sălii.'),
    ('Desfășurarea activității cu grupul țintă', 'Facilitarea atelierului (60 de minute) conform scenariului; gestionarea listei de prezență; '
     'realizarea fotografiilor.'),
    ('Evaluare și raportare', 'Analiza biletelor de ieșire și a produselor elevilor; completarea raportului de desfășurare; centralizarea '
     'documentelor justificative; ajustarea planului pentru Ședința 2.'),
], [
    'Scenariul complet al Ședinței 1 (prezentul document), cu 9 materiale-suport (Anexele 1–9).',
    'Ședință de 60 de minute desfășurată cu elevi din clasele a VII-a – a VIII-a (numărul de participanți – conform listei de prezență).',
    'Produse ale elevilor: Fișa 1 – Detectivul, Harta echipei (afiș colectiv), Cardurile de agent, biletele de ieșire.',
    'Raportul privind desfășurarea activității (secțiunea 12).',
])

D.h('SCENARIUL ACTIVITĂȚII', 1)
D.h('1. Fundamentare și abordare metodologică')
D.p('La vârsta de 13–14 ani, elevii se raportează intens la ceilalți, iar comparația socială (inclusiv în mediul online) le poate diminua '
    'încrederea în propriile resurse. Mulți elevi formulează mai ușor ce nu le reușește decât ce le reușește. Atelierul răspunde acestei nevoi '
    'prin activități care îi ajută să-și identifice și să-și valorizeze punctele forte, într-un cadru sigur și fără evaluare școlară.',
    align='justify')
D.p('Pentru a crește implicarea, activitatea folosește **elemente de gamificare**, adaptate intereselor vârstei:', after=2)
D.b('**Ședința 1 – „Agenția Secretă a Punctelor Forte”:** elevii devin „agenți”, primesc ecuson și nume de cod și descoperă, prin probe și '
    'interviuri în perechi, punctele forte proprii și ale colegilor.')
D.b('**Ședința 2 – „Level Up”:** elevii explorează sursele de motivație, își aleg o „superputere” (un punct forte) și își stabilesc '
    'o provocare personală de 30 de zile.')
D.b('**Continuitatea între ședințe** este asigurată prin **Cardul de agent**, completat în Ședința 1 și finalizat în Ședința 2.')
D.p('Activitatea contribuie la scopul proiectului UNIC – incluziunea și continuitatea educației elevilor – prin dezvoltarea stimei de sine, '
    'a competențelor socio-emoționale și a motivației pentru învățare, factori care susțin participarea și menținerea elevilor în educație.',
    align='justify')

D.h('2. Scopul ședinței')
D.p('Dezvoltarea autocunoașterii prin identificarea punctelor forte, a abilităților și a resurselor personale, '
    'precum și prin exersarea oferirii și primirii feedbackului pozitiv.')

D.h('3. Obiective')
D.p('La finalul ședinței, elevii vor putea:', after=2)
D.b('**O1** – să numească cel puțin 2–3 puncte forte personale;')
D.b('**O2** – să descopere cel puțin o calitate pe care colegii o observă la ei;')
D.b('**O3** – să explice, pe un exemplu, de ce o echipă are nevoie de oameni cu puncte forte diferite;')
D.b('**O4** – să formuleze un feedback pozitiv concret (despre ce face o persoană, nu despre cum arată).')

D.h('4. Elemente de proiectare')
metode(D, [
    ['Domeniul', 'Consiliere și dezvoltare personală – autocunoaștere, stimă de sine, relaționare pozitivă.'],
    ['Competențe vizate', ['- identificarea resurselor personale (calități, abilități, interese);',
                           '- oferirea și primirea feedbackului pozitiv;',
                           '- valorizarea diversității și a contribuției fiecăruia într-o echipă.']],
    ['Metode și procedee', 'Joc de energizare, joc de ghicire (exercițiu anonim), interviul în perechi, brainstorming pe categorii '
                           '(harta colectivă), studiu de caz („Misiunea imposibilă”), cercul de feedback, reflecția ghidată, gamificarea.'],
    ['Forme de organizare', 'Frontal, în perechi, pe grupe, individual.'],
    ['Resurse', 'Materiale: Anexele 1–9 și consumabile (secțiunea 5). Temporale: 60 de minute. Umane: 10–15 elevi, facilitatorul comunitar. '
                'Spațiale: sală de clasă cu scaune așezate în cerc.'],
    ['Evaluare', 'Observarea sistematică a participării; analiza produselor (Fișa 1, Harta echipei, Cardul de agent); '
                 'biletul de ieșire (autoevaluare și feedback).'],
])

D.h('5. Materiale necesare (listă de verificare)')
D.simple_table(['Material', 'Cantitate', 'Unde îl găsești', '✓'], [
    ['Ecusoane de agent', '1 / elev + 2 rezervă', 'Anexa 1', '☐'],
    ['Bandă adezivă de hârtie sau ace de siguranță (pentru ecusoane)', '1 rolă', '–', '☐'],
    ['Bilețele „Dosar secret”', '1 / elev', 'Anexa 2', '☐'],
    ['Cutie, plic mare sau pălărie = „Dosarul secret”', '1', '–', '☐'],
    ['Fișa 1 – Detectivul de puncte forte', '1 / elev', 'Anexa 3', '☐'],
    ['Indicatoarele pentru Harta echipei (6 zone)', '1 set', 'Anexa 4', '☐'],
    ['Cartonașe „Misiunea imposibilă”', '1 set', 'Anexa 5', '☐'],
    ['Banca de complimente (cartonașe)', '1 set', 'Anexa 6', '☐'],
    ['Cardul de agent', '1 / elev', 'Anexa 7', '☐'],
    ['Fișa 2 – Harta mea de puncte forte (opțional / pentru acasă)', '1 / elev', 'Anexa 8', '☐'],
    ['Biletul de ieșire', '1 / elev', 'Anexa 9', '☐'],
    ['Post-it-uri (ideal 3 culori)', '3 / elev + rezervă', '–', '☐'],
    ['Coli flipchart sau tablă + markere, carioci, pixuri', '2 coli', '–', '☐'],
    ['Minge moale (sau ghem de sfoară – vezi varianta de la Activitatea 5)', '1', '–', '☐'],
    ['Plic mare A4 pentru păstrarea cardurilor până la Ședința 2', '1', '–', '☐'],
    ['Telefon + boxă pentru muzică de fundal (opțional)', '1', '–', '☐'],
], [9.0, 3.6, 3.2, 1.2])

D.h('6. Pregătirea sălii (cu 10 minute înainte)')
D.b('Mută băncile lângă pereți; așază scaunele **în cerc** (câte un scaun pentru fiecare elev și unul pentru tine).')
D.b('Scrie pe tablă: **AGENȚIA SECRETĂ A PUNCTELOR FORTE – Misiunea de azi: descoperim ce avem bun.**')
D.b('Lipește pe tablă sau pe perete cele **6 indicatoare** (Anexa 4), lăsând loc pentru post-it-uri. Deasupra: **NOI – CE AVEM ÎN NOI**.')
D.b('Pregătește „Dosarul secret” (cutia/plicul), bilețelele, pixurile și post-it-urile pe o masă la îndemână.')
D.b('Pornește o muzică ritmată, potrivită vârstei, pentru momentul în care intră elevii (opțional, dar creează atmosferă).')

D.h('7. Principii pentru facilitator')
D.callout('REGULI DE AUR', [
    '- **Ritm alert, instrucțiuni scurte** (maximum 30 de secunde). Demonstrează tu primul fiecare exercițiu.',
    '- **Dreptul de a spune „pas”.** Nimeni nu e obligat să vorbească. Elevii spun despre ei atât cât doresc.',
    '- **Nu e interogatoriu.** Accentul cade pe resurse și pe lucruri concrete, observabile.',
    '- **Complimentele sunt despre ce face omul**, nu despre haine, corp sau aspect fizic.',
    '- **Fără clasamente și comparații** între elevi. Un punct forte nu înseamnă „cel mai bun din clasă”.',
    '- **Orice răspuns se poate transforma într-o resursă:** „mă joc mult” → strategie, reflexe, lucru în echipă; '
    '„vorbesc mult” → comunicare, curaj de a te exprima.',
    '- **Joacă rolul de „Șef(ă) al(a) agenției”** cu umor și energie, fără ironii la adresa elevilor.',
], C['lyellow'], C['yellow'], C['ink'])

D.h('8. Agenda pe scurt')
D.simple_table(['Timp', 'Activitate', 'Ce urmărim', 'Materiale'], [
    ['0–5\'', '0. Recrutarea agenților', 'Siguranță, reguli, intrare în joc', 'Anexa 1'],
    ['5–12\'', '1. Schimbă locul dacă...', 'Energizare; „suntem diferiți”', '–'],
    ['12–20\'', '2. Dosarul secret (Ghicește talentul meu)', 'Primul punct forte, spus anonim', 'Anexa 2, cutie'],
    ['20–32\'', '3. Detectivii de puncte forte', 'Puncte forte văzute de un coleg', 'Anexa 3'],
    ['32–44\'', '4. Harta echipei + Misiunea imposibilă', 'Diversitatea resurselor într-o echipă', 'Anexele 4, 5, post-it'],
    ['44–52\'', '5. Mingea complimentelor', 'Feedback pozitiv dat și primit', 'Minge, Anexa 6'],
    ['52–60\'', '6. Cardul de agent + Biletul de ieșire', 'Integrare și reflecție', 'Anexele 7, 9'],
], [1.6, 5.6, 6.0, 3.8], bold_first=True)

D.h('9. Desfășurarea pas cu pas')

D.activity('0', 'Recrutarea agenților', '5 min', 'minutele 0–5', [
    ('SCOP', 'Elevii intră în atmosfera jocului și stabilim împreună regulile grupului.'),
    ('FĂ', ['- Primește elevii la ușă (cu muzică, dacă ai). Fiecare primește un **ecuson de agent** (Anexa 1) și se așază în cerc.',
            '- Cere-le să-și scrie pe ecuson un **nume de cod**: prenumele + un animal sau un obiect care îi reprezintă '
            '(ex.: „Andrei – Vulpea”, „Maria – Racheta”, „Ionuț – Bateria”). Ai la dispoziție 1 minut.',
            '- Scrie pe tablă **Codul agenției** (3 reguli) și cere acordul grupului.']),
    ('SPUNE', ['„Bine ați venit la Agenția Secretă a Punctelor Forte! Eu sunt șeful/șefa agenției, iar voi ați fost recrutați '
               'pentru o misiune specială: să descoperiți ce aveți bun – voi și colegii voștri. Nu e o oră de curs: nu se dau note '
               'și nu există răspunsuri greșite.”',
               '„Orice agenție are un cod. Al nostru are trei reguli: 1. Ce se spune aici rămâne aici. 2. Râdem împreună, nu unii de alții. '
               '3. Oricine poate spune «pas». Sunteți de acord? Arătați-mi degetul mare.”']),
    ('VARIANTĂ', 'Stabilește un **semnal de liniște**: când spui „Agenți, pe poziții!” și ridici mâna, toți îngheață și tac. '
                 'Exersați-l o dată – îl vei folosi după activitățile cu mișcare.'),
])

D.activity('1', 'Schimbă locul dacă...', '7 min', 'minutele 5–12', [
    ('SCOP', 'Energizare. Elevii observă că fiecare are preferințe și abilități diferite.'),
    ('FĂ', ['- Toată lumea stă pe scaune, în cerc. Citești o afirmație. Cei cărora li se potrivește se ridică și **schimbă locul** cu altcineva '
            'care s-a ridicat (nu cu vecinul direct). Nimeni nu este eliminat.',
            '- Crește treptat ritmul. Citește 3–4 afirmații din fiecare rundă, în funcție de energia grupului.']),
    ('SPUNE', '„Prima probă de agent: atenție și reflexe! Citesc o afirmație. Dacă vi se potrivește, vă ridicați și schimbați locul cu '
              'cineva care s-a ridicat. Nu cu vecinul!”'),
    ('AFIRMAȚII', ['# Runda 1 – Încălzire',
                   '- … îți place muzica.   - … ai un animal de companie.   - … joci jocuri video.',
                   '- … ai stat vreodată până târziu în noapte ca să termini un serial.',
                   '# Runda 2 – Ce știu să fac',
                   '- … ai învățat ceva singur/singură, de pe YouTube sau TikTok.',
                   '- … știi să gătești cel puțin un fel de mâncare.',
                   '- … îi faci pe alții să râdă.   - … ai reparat sau ai montat ceva.',
                   '- … te pricepi la telefon sau calculator mai bine decât adulții din casă.',
                   '- … ai ajutat pe cineva săptămâna aceasta.',
                   '# Runda 3 – Curaj și viitor',
                   '- … ai o activitate la care vrei să devii mai bun/bună.',
                   '- … ai încercat ceva nou, deși îți era puțin frică.',
                   '- … ai deja o idee despre ce ai vrea să faci în viitor.',
                   '- … crezi că există cel puțin un lucru la care te pricepi.',
                   '# Final (toată lumea se mișcă)',
                   '- … ești în sala aceasta astăzi!']),
    ('SPUNE', '„Ați observat? Niciodată nu s-au ridicat exact aceiași oameni. Suntem în aceeași grupă, dar avem lucruri diferite care ne plac '
              'și la care ne pricepem. Astăzi le dăm de urmă.”'),
    ('ATENȚIE', 'Dacă un elev **nu** se ridică la „crezi că există cel puțin un lucru la care te pricepi”, nu comenta în fața grupului. '
                'Reține și acordă-i atenție discretă la activitatea Detectivii.'),
])

D.activity('2', 'Dosarul secret – Ghicește talentul meu', '8 min', 'minutele 12–20', [
    ('SCOP', 'Fiecare elev numește un prim punct forte, în siguranță (anonim).'),
    ('FĂ', ['- Împarte bilețelele „Dosar secret” (Anexa 2). Fiecare scrie, **fără nume**, un lucru la care se pricepe + un mic indiciu, '
            'apoi pliază bilețelul și îl pune în „Dosarul secret” (cutie/plic). Timp: 2 minute.',
            '- Amestecă bilețelele. Extrage **6–8** dintre ele și citește-le ca un prezentator TV. Grupul are 3 încercări să ghicească agentul. '
            'Autorul poate confirma sau poate rămâne „sub acoperire”.',
            '- Păstrează bilețelele necitite: le poți citi la Harta echipei sau le poți lipi direct pe hartă.']),
    ('SPUNE', '„Misiunea a doua este top secret. Scrieți, fără nume, un singur lucru la care vă pricepeți. Poate fi orice: sport, desen, '
              'să faci glume, să repari o bicicletă, să-ți asculți prietenii, să construiești în Minecraft, să ai grijă de frații mai mici. '
              'Nu trebuie să fiți cei mai buni din lume la asta.”'),
    ('ÎNTREABĂ', ['- „A fost ușor sau greu să vă gândiți la ceva la care vă pricepeți?”',
                  '- „De ce credeți că ne vine mai ușor să spunem ce NU ne iese decât ce ne iese?”',
                  '- „Cum ne dăm seama că suntem buni la ceva?” (ne place, ne iese, ne cer alții ajutorul, progresăm)']),
    ('MESAJ-CHEIE', '**Un punct forte nu înseamnă să fii cel mai bun. Este ceva ce faci bine, o calitate sau ceva care te ajută să te descurci.**'),
    ('ATENȚIE', 'Dacă pe un bilețel scrie „nimic”, citește-l cu căldură: „Agentul acesta e foarte modest. Până la finalul misiunii '
                'aflăm noi ce ascunde!” Nu încerca să ghicești cine l-a scris.'),
])

D.activity('3', 'Detectivii de puncte forte', '12 min', 'minutele 20–32', [
    ('SCOP', 'Elevii descoperă calități pe care un coleg le observă la ei și exersează întrebările deschise.'),
    ('FĂ', ['- Formează perechi (de exemplu, după culoarea ecusonului sau numărând 1–2). Împarte **Fișa 1 – Detectivul** (Anexa 3).',
            '- Rolul A este **detectivul**, rolul B este **martorul**. Detectivul pune întrebările de pe fișă și notează răspunsurile și o **dovadă** '
            '(un exemplu concret). După **4 minute** dă semnalul de schimbare a rolurilor.',
            '- În ultimele 3 minute, 4–5 detectivi voluntari prezintă „raportul”: '
            '„L-am investigat pe agentul ___. Punctul lui forte este ___. Dovada: ___.”']),
    ('SPUNE', '„Acum lucrați ca detectivi. Un detectiv nu ghicește: pune întrebări și caută dovezi. Aveți 4 minute să descoperiți cel puțin '
              'un punct forte al partenerului. Apoi schimbați rolurile.”'),
    ('ÎNTREABĂ', ['- Întrebările de pe fișă: Ce îți place să faci în timpul liber? La ce îți cer alții ajutorul? Ce ai făcut în ultima vreme '
                  'și ai fost mulțumit(ă) de tine? Ce faci când ceva nu îți iese? Ce spun prietenii că faci bine?',
                  '- La final: „Cum a fost să auzi ce a descoperit detectivul despre tine?”']),
    ('ATENȚIE', ['- Încurajează formulări **concrete și respectuoase**: în loc de „e de treabă” → „e răbdător: își ajută fratele la teme”.',
                 '- La număr impar de elevi, formează un grup de 3 sau intră tu în pereche.',
                 '- Dacă o pereche se blochează, dă-le un indiciu: „Întreabă-l ce ar face dacă ar avea o zi liberă și bani nelimitați.”']),
])

D.activity('4', 'Harta echipei + Misiunea imposibilă', '12 min', 'minutele 32–44', [
    ('SCOP', 'Elevii văd că grupul are resurse diferite și că diferențele sunt utile într-o echipă.'),
    ('FĂ', ['# Pasul 1 – Harta (5 min)',
            '- Fiecare elev primește **3 post-it-uri**. Scrie pe fiecare câte o abilitate sau o calitate (poate folosi ce a aflat de la detectiv) '
            'și le lipește în zona potrivită: CREATIVITATE, COMUNICARE, SPORT/MIȘCARE, GÂNDIRE/IDEI, PERSEVERENȚĂ, ECHIPĂ/AJUTOR.',
            '# Pasul 2 – Privire de ansamblu (2 min)',
            '- Grupul se adună în fața hărții. Citește câteva post-it-uri cu voce tare.',
            '# Pasul 3 – Misiunea imposibilă (5 min)',
            '- Un voluntar extrage un cartonaș din Anexa 5 (ex.: „Aveți două săptămâni să organizați cel mai tare festival din istoria școlii”). '
            'Grupul decide: de ce zone ale hărții avem nevoie? Cine din grup ar face ce? Elevii arată post-it-urile sau zonele.']),
    ('ÎNTREABĂ', ['- „Unde avem cele mai multe puncte forte? Unde avem mai puține?”',
                  '- „Avem puncte forte diferite? Ce s-ar întâmpla dacă toți am fi buni la același lucru?”',
                  '- „Dacă am rezolva misiunea împreună, cum ne-ar ajuta aceste calități?”']),
    ('MESAJ-CHEIE', '**Nu trebuie să fim buni la aceleași lucruri. O echipă bună are oameni diferiți, cu puncte forte diferite. '
                    'Diferențele dintre noi sunt resurse.**'),
    ('ATENȚIE', '**Fotografiază harta** (sau păstreaz-o): o folosești la începutul Ședinței 2. Dacă rămâi fără timp, discutați o singură misiune, 2 minute.'),
])

D.activity('5', 'Mingea complimentelor', '8 min', 'minutele 44–52', [
    ('SCOP', 'Exersarea feedbackului pozitiv: a-l oferi și, la fel de important, a-l primi.'),
    ('FĂ', ['- Toată lumea stă în cerc. Pune în mijloc cartonașele din **Banca de complimente** (Anexa 6). Cine se blochează poate lua unul ca început de frază.',
            '- Începi tu: spui un compliment concret unui elev și îi arunci mingea. Cine primește mingea spune „Mulțumesc”, apoi '
            'oferă un compliment altcuiva și aruncă mingea acelei persoane.',
            '- Cine a primit deja mingea își încrucișează brațele, ca să știm cine mai urmează. **Fiecare primește mingea o singură dată.**']),
    ('SPUNE', '„Ultima probă de agent este, pentru mulți oameni, cea mai grea: să spui cu voce tare ceva bun despre altcineva și – și mai greu – '
              'să primești un compliment. Regula: când primești un compliment, spui doar «Mulțumesc». Fără «nu e adevărat» sau «ei, lasă».”'),
    ('ÎNTREABĂ', ['- „Ce a fost mai ușor: să dați sau să primiți un compliment? De ce?”',
                  '- „Cum v-ați simțit când ați auzit ceva bun despre voi?”']),
    ('ATENȚIE', ['- Complimentul este despre **ce face sau cum se poartă** persoana (a avut o idee bună, a fost curajos, m-a făcut să râd, a ajutat), '
                 '**nu** despre haine sau aspect fizic.',
                 '- Urmărește discret să nu rămână nimeni fără compliment. Dacă cineva este ocolit, cere tu mingea și oferă-i un compliment sincer și concret.',
                 '- Nu forța elevii care nu vor să vorbească: pot alege un cartonaș și îl pot citi, completându-l cu un cuvânt.']),
    ('VARIANTĂ', ['- **Pânza de păianjen:** în locul mingii, folosește un ghem de sfoară. Fiecare ține de fir și aruncă ghemul mai departe. '
                  'La final, arată pânza: „Suntem conectați. Dacă unul lasă firul, se simte în toată pânza.”',
                  '- **Grup foarte timid:** fiecare are o foaie lipită pe spate. Colegii scriu pe ea complimente, în liniște, pe fundal muzical (5 min).']),
])

D.activity('6', 'Cardul de agent + Biletul de ieșire', '8 min', 'minutele 52–60', [
    ('SCOP', 'Integrarea a ceea ce au descoperit elevii și legătura cu Ședința 2.'),
    ('FĂ', ['- Împarte **Cardul de agent** (Anexa 7). Elevii completează: numele de cod, un simbol sau un avatar desenat, '
            '**3 abilități speciale** (punctele forte descoperite azi) și un compliment primit. Partea „Nivelul 2” rămâne goală. Timp: 4 minute.',
            '- Împarte **Biletul de ieșire** (Anexa 9). Elevii îl completează în 2 minute și ți-l predau la ieșire.',
            '- Invită 3–4 voluntari să încheie verbal, cu una dintre formulele: „Astăzi am descoperit că eu...” / '
            '„Un lucru bun pe care îl am este...” / „Mi-a plăcut...”.',
            '- Strânge cardurile în plicul mare: le păstrezi tu până la Ședința 2.']),
    ('SPUNE', ['„În jocuri, fiecare personaj are abilități diferite. Niciunul nu le are pe toate la maximum și tocmai de aceea fac echipă. '
               'Completați-vă cardul cu abilitățile descoperite azi.”',
               '„Misiune îndeplinită, agenți! Data viitoare primim misiunea LEVEL UP: vedem ce ne pune în mișcare, cum ne folosim superputerile '
               'și alegem un pas mic pentru ceva ce vrem să dezvoltăm. Cardurile rămân la mine, în siguranță, și le primiți înapoi data viitoare.”']),
    ('ATENȚIE', 'Nu cere nimănui să vorbească. Biletul de ieșire scris îi ajută pe elevii timizi și îți oferă ție informații pentru Ședința 2.'),
])

D.h('10. Situații dificile – ce faci dacă...')
D.simple_table(['Situația', 'Ce poți face'], [
    ['Un elev spune „nu sunt bun la nimic”.',
     'Nu-l contrazice imediat. Întreabă: „Ce faci în timpul liber? Cine te cheamă când are nevoie de ajutor? Ce ai învățat singur?” '
     'Reformulează răspunsul ca abilitate. Poți întreba grupul: „Cine a observat ceva bun la colegul nostru?”'],
    ['Apar glume sau ironii la adresa unui coleg.',
     'Oprește calm activitatea, amintește regula 2 („râdem împreună, nu unii de alții”) și continuă. Nu umili pe nimeni în fața grupului; '
     'dacă situația se repetă, vorbește cu elevul la final.'],
    ['Grupul este prea agitat.',
     'Folosește semnalul „Agenți, pe poziții!”. Scurtează activitățile cu mișcare și treci mai repede la lucrul în perechi.'],
    ['Un elev nu vrea să participe.',
     'Oferă-i un rol: cronometror, „prezentatorul” bilețelelor, fotograful hărții. Respectă dreptul la „pas”, dar invită-l din nou mai târziu.'],
    ['Cineva nu primește niciun compliment.',
     'Cere mingea și oferă-i tu un compliment sincer și concret, bazat pe ce ai observat în ședință.'],
    ['Rămâi fără timp.',
     'Scurtează Misiunea imposibilă la o discuție de 2 minute. Fișa 2 (Harta mea) poate fi dată pentru acasă. Nu sări peste încheiere.'],
    ['Un elev spune ceva îngrijorător (violență, abuz, autovătămare).',
     'Nu aprofunda subiectul în grup. Mulțumește-i, continuă activitatea și discută cu el individual după ședință. '
     'Urmează procedura școlii și a proiectului (consilierul școlar, dirigintele, coordonatorul proiectului).'],
], [5.2, 11.8], bold_first=True)

D.h('11. Lista anexelor și numărul de exemplare de tipărit')
D.p('Recomandare: fișele de lucru se pot tipări alb-negru; indicatoarele (Anexa 4) și cardurile (Anexa 7) arată mai bine color.',
    italic=True, color=C['grey'])
D.simple_table(['Anexa', 'Conținut', 'De tipărit (pentru 15 elevi)'], [
    ['Anexa 1', 'Ecusoane de agent (8 pe pagină)', '2 pagini'],
    ['Anexa 2', 'Bilețele „Dosar secret” (10 pe pagină)', '2 pagini'],
    ['Anexa 3', 'Fișa 1 – Detectivul de puncte forte', '15 exemplare'],
    ['Anexa 4', 'Indicatoare pentru Harta echipei (6 zone, 2 pe pagină)', '1 set (3 pagini), de preferință color'],
    ['Anexa 5', 'Cartonașe „Misiunea imposibilă” (6)', '1 pagină'],
    ['Anexa 6', 'Banca de complimente (18 cartonașe)', '1 pagină'],
    ['Anexa 7', 'Cardul de agent (2 pe pagină)', '8 pagini, de preferință color'],
    ['Anexa 8', 'Fișa 2 – Harta mea de puncte forte (opțional / acasă)', '15 exemplare'],
    ['Anexa 9', 'Biletul de ieșire (4 pe pagină)', '4 pagini'],
], [2.2, 9.6, 5.2], bold_first=True)

raport(D, 12, ['O1 – numește cel puțin 2–3 puncte forte personale', 'O2 – descoperă o calitate observată de colegi',
              'O3 – explică de ce o echipă are nevoie de puncte forte diferite', 'O4 – formulează un feedback pozitiv concret'],
       'De ex.: nr. de fișe „Detectivul” completate, Harta echipei (fotografie), Cardurile de agent, biletele de ieșire.')

# =====================================================================  ANEXE
# ---- Anexa 1 – Ecusoane
D.annex_title('ANEXA 1', 'Ecusoane de agent')
scissors_note(d)


def ecuson(cell, i):
    cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
    para(cell, 'AGENȚIA SECRETĂ A PUNCTELOR FORTE', 8, True, color=C['purple'], align='center', after=0)
    para(cell, '★  ECUSON DE AGENT  ★', 14, True, color=C['ink'], align='center', after=2)
    field(cell, [('Nume de cod:', 7.6)], 11, before=8)
    field(cell, [('Agent(ă):', 7.6)], 11, before=8)
    para(cell, 'Nivel de acces: TOP SECRET', 8, italic=True, color=C['grey'], align='center', before=6, after=0)


cut_grid(d, 8, 2, 8.5, 5.4, ecuson)

# ---- Anexa 2 – Dosar secret
D.annex_title('ANEXA 2', 'Bilețele „Dosar secret”')
scissors_note(d, '✂  Decupează pe linia punctată. Elevii scriu fără nume, pliază bilețelul și îl pun în „Dosarul secret”.')


def dosar(cell, i):
    p = para(cell, '', after=2)
    r = p.add_run('  DOSAR SECRET  ')
    r.bold = True
    r.font.size = Pt(9.5)
    r.font.color.rgb = rgb(C['white'])
    rPr = r._r.get_or_add_rPr()
    sh = OxmlElement('w:shd'); sh.set(qn('w:val'), 'clear'); sh.set(qn('w:color'), 'auto'); sh.set(qn('w:fill'), C['purple'])
    rPr.append(sh)
    r2 = p.add_run('   nr. ______      TOP SECRET')
    r2.font.size = Pt(8)
    r2.font.color.rgb = rgb(C['grey'])
    field(cell, [('Un lucru la care mă pricep:', 7.7)], 10, before=5)
    lines(cell, 1, 7.7, 10, before=7)
    field(cell, [('Indiciu (fără nume!):', 7.7)], 10, before=7)


cut_grid(d, 10, 2, 8.5, 4.3, dosar)

# ---- Anexa 3 – Fișa 1 Detectivul
D.annex_title('ANEXA 3', 'FIȘA 1 – Detectivul de puncte forte')
field(d, [('Detectivul (numele meu):', CONTENT_W)], 10.5, before=0)
field(d, [('Martorul (colegul/colega pe care îl investighez):', CONTENT_W)], 10.5, before=8, after=6)
D.callout('MISIUNEA', 'Astăzi sunt detectiv. Pun întrebări, ascult cu atenție și caut **dovezi** (exemple concrete) pentru punctele forte '
          'ale colegului meu. Am 4 minute.', C['lav'], C['purple'])
qs = ['1. Ce îți place să faci în timpul liber?',
      '2. La ce îți cer alții ajutorul?',
      '3. Ce ai făcut în ultima vreme și ai fost mulțumit(ă) de tine?',
      '4. Ce faci când ceva nu îți iese?',
      '5. Ce spun prietenii sau familia că faci bine?']
for q in qs:
    para(d, q, 10.5, True, color=C['purple'], before=6, after=0, keep=True)
    lines(d, 2, CONTENT_W, 10.5, before=10)
para(d, 'Bifează ce ai observat la colegul tău:', 10.5, True, before=10, after=3)
checkbox_grid(d, ['curajos/curajoasă', 'creativ(ă)', 'vesel(ă)', 'răbdător/răbdătoare',
                  'de încredere', 'comunicativ(ă)', 'atent(ă) la alții', 'muncitor/muncitoare',
                  'descurcăreț/descurcăreață', 'bun(ă) la sport', 'amuzant(ă)', 'altceva: ________'], 3, CONTENT_W, 10)
spacer(d, 6)
t = table(d, 1, 1, [CONTENT_W], borders=('single', 12, C['purple']), lr=0.3, tb=0.15)
cell = t.cell(0, 0)
shade(cell, C['lyellow'])
para(cell, 'RAPORTUL DETECTIVULUI', 11, True, color=C['purple'], after=0)
field(cell, [('L-am investigat pe agentul/agenta', 16.2)], 10.5, before=8)
field(cell, [('Punctul lui/ei forte este:', 16.2)], 10.5, before=8)
field(cell, [('Dovada (un exemplu concret):', 16.2)], 10.5, before=8)
field(cell, [('Dacă ar avea o superputere, cred că ar fi:', 16.2)], 10.5, before=8, after=4)

# ---- Anexa 4 – Indicatoare
ZONE = [
    ('CREATIVITATE', 'Ce idei sau lucruri creative pot face?', 'desenez • compun muzică • editez video • inventez jocuri • gătesc • decorez • scriu povești', C['purple'], C['lav']),
    ('COMUNICARE', 'Cu ce fel de oameni mă descurc bine?', 'ascult • explic • conving • fac glume • fac ușor cunoștință • vorbesc în public', C['blue'], C['lblue']),
    ('SPORT / MIȘCARE', 'Ce activitate fizică îmi place sau îmi reușește?', 'fotbal • dans • bicicletă • înot • rezistență • reflexe • coordonare', C['green'], C['lgreen']),
    ('GÂNDIRE / IDEI', 'La ce fel de probleme găsesc soluții?', 'matematică • strategie în jocuri • reparații • logică • curiozitate • calculatorul', 'B07A00', C['lyellow']),
    ('PERSEVERENȚĂ', 'Când nu renunț ușor?', 'mă antrenez • încerc din nou • termin ce încep • am răbdare • nu mă las', C['orange'], C['lorange']),
    ('ECHIPĂ / AJUTOR', 'Cum îi ajut pe ceilalți?', 'ajut la teme • am grijă de frați • împart • sunt de încredere • organizez • încurajez', '2C6E6A', 'E0F0EE'),
]
for k in range(3):
    D.annex_title('ANEXA 4', 'Indicatoare pentru Harta echipei  (%d / 3)' % (k + 1))
    for j in range(2):
        name, q, ex, col, light = ZONE[k * 2 + j]
        t = table(d, 1, 1, [CONTENT_W], borders=('single', 24, col), lr=0.5, tb=0.3)
        row_setup(t.rows[0], 10.4, exact=True)
        cell = t.cell(0, 0)
        shade(cell, light)
        cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
        para(cell, 'ZONA %d' % (k * 2 + j + 1), 12, True, color=col, align='center', after=0)
        para(cell, name, 46, True, color=col, align='center', after=6, line=1.0)
        para(cell, q, 18, italic=True, color=C['ink'], align='center', after=10)
        para(cell, 'de exemplu: ' + ex, 12, color=C['grey'], align='center', after=0)
        if j == 0:
            spacer(d, 10)

# ---- Anexa 5 – Misiunea imposibilă
D.annex_title('ANEXA 5', 'Cartonașe „Misiunea imposibilă”')
scissors_note(d, '✂  Decupează. Un voluntar extrage un cartonaș; grupul decide ce puncte forte de pe hartă sunt necesare și cine ce ar face.')
MIS = [
    ('FESTIVALUL ȘCOLII', 'Aveți 2 săptămâni să organizați cel mai tare festival de talente din istoria școlii: scenă, afișe, prezentatori, muzică, public.'),
    ('NAUFRAGIAȚII', 'Grupul vostru a naufragiat pe o insulă pustie timp de 3 zile. Trebuie să construiți un adăpost, să găsiți mâncare și să trimiteți un semnal.'),
    ('CANALUL CLASEI', 'Lansați un canal video al clasei, cu un mesaj pozitiv despre școala voastră, care să ajungă la 1.000 de urmăritori în o lună.'),
    ('ESCAPE ROOM', 'Sunteți închiși într-o cameră cu 10 lacăte, ghicitori și coduri ascunse. Aveți 45 de minute să ieșiți – împreună.'),
    ('ADĂPOSTUL DE ANIMALE', 'Un adăpost de animale din oraș are nevoie de ajutor. Aveți o lună să strângeți hrană și să găsiți stăpâni pentru 10 cățeii.'),
    ('ROBOTUL CAMPION', 'Echipa voastră participă la un concurs de robotică. Trebuie să construiți un robot, să-l programați și să-l prezentați juriului.'),
]


def mis(cell, i):
    title, txt = MIS[i]
    shade(cell, C['lav'] if i % 2 == 0 else C['lyellow'])
    para(cell, 'MISIUNEA IMPOSIBILĂ #%d' % (i + 1), 9, True, color=C['grey'], after=0)
    para(cell, title, 15, True, color=C['purple'], after=4)
    para(cell, txt, 11, after=6)
    para(cell, 'De ce puncte forte are nevoie echipa? Cine ce ar face?', 9.5, True, italic=True, color=C['green'], after=0)


cut_grid(d, 6, 2, 8.5, 7.0, mis)

# ---- Anexa 6 – Banca de complimente
D.annex_title('ANEXA 6', 'Banca de complimente')
scissors_note(d, '✂  Decupează cartonașele și pune-le în mijlocul cercului. Cine se blochează alege unul și îl completează.')
COMP = ['Am observat că tu...', 'Mi-a plăcut când tu...', 'Ești bun/bună la...', 'Mă faci să râd când...',
        'Te admir pentru că...', 'Azi ai avut o idee bună când...', 'Ai fost curajos/curajoasă când...', 'Se vede că știi să...',
        'Mi-a plăcut cum ai ajutat...', 'Cu tine e ușor să...', 'Ai răbdare când...', 'Te poți baza pe tine pentru că...',
        'Îmi place cum explici...', 'Ai fost un detectiv bun pentru că...', 'Cred că ai talent la...', 'M-ai surprins plăcut când...',
        'Echipa are nevoie de tine pentru că...', 'Un lucru pe care l-aș învăța de la tine este...']


def comp(cell, i):
    cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
    shade(cell, [C['lav'], C['lyellow'], C['lgreen']][(i // 3 + i) % 3])
    para(cell, '♥', 12, True, color=C['purple'], align='center', after=0)
    para(cell, COMP[i], 12, True, color=C['ink'], align='center', after=0, line=1.0)


cut_grid(d, 18, 3, 5.66, 3.55, comp)

# ---- Anexa 7 – Cardul de agent
D.annex_title('ANEXA 7', 'Cardul de agent')
scissors_note(d, '✂  Decupează. Se completează la finalul Ședinței 1; partea „Nivelul 2” se deblochează în Ședința 2.')


def agent_card(doc):
    W1, W2 = 5.6, CONTENT_W - 5.6
    t = table(doc, 4, 2, [W1, W2], borders=('single', 18, C['purple']), inside=('single', 4, C['lav2']), lr=0.25, tb=0.08)
    for r, h in zip(t.rows, (0.85, 4.5, 2.3, 3.2)):
        row_setup(r, h, exact=True)
    top = t.cell(0, 0).merge(t.cell(0, 1))
    shade(top, C['purple'])
    top.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
    p = para(top, '', after=0)
    p.paragraph_format.tab_stops.add_tab_stop(Cm(16.4), WD_TAB_ALIGNMENT.RIGHT)
    runs(p, '★  AGENȚIA SECRETĂ A PUNCTELOR FORTE', 11, True, color=C['white'])
    runs(p, '\tCARD DE AGENT  •  NIVELUL 1', 10, True, color=C['yellow'])
    a = t.cell(1, 0)
    para(a, 'SIMBOLUL / AVATARUL MEU', 8, True, color=C['grey'], align='center', after=0)
    para(a, '(desenează-l aici)', 7.5, italic=True, color=C['grey'], align='center', after=0)
    b_ = t.cell(1, 1)
    para(b_, 'ABILITĂȚI SPECIALE – punctele mele forte', 10, True, color=C['purple'], after=0)
    for k in range(3):
        p = para(b_, '', before=9, after=0)
        p.paragraph_format.tab_stops.add_tab_stop(Cm(8.0), WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.LINES)
        p.paragraph_format.tab_stops.add_tab_stop(Cm(10.8), WD_TAB_ALIGNMENT.RIGHT)
        runs(p, '%d.\t' % (k + 1), 10.5, True)
        runs(p, '\t☆☆☆☆☆', 13, color='B58A00')
    para(b_, 'Colorează stelele: cât de mult folosesc deja abilitatea.', 7.5, italic=True, color=C['grey'], before=4, after=0)
    c1 = t.cell(2, 0)
    field(c1, [('Nume de cod:', 5.0)], 9.5, before=4)
    field(c1, [('Agent(ă):', 5.0)], 9.5, before=8)
    c2 = t.cell(2, 1)
    para(c2, 'Un compliment primit azi:', 9.5, True, after=0)
    lines(c2, 2, 10.8, 9.5, before=8)
    bot = t.cell(3, 0).merge(t.cell(3, 1))
    shade(bot, C['lav'])
    para(bot, '▶  NIVELUL 2 – se deblochează în Ședința 2', 9.5, True, color=C['purple'], after=0)
    field(bot, [('Combustibilul meu (ce mă motivează):', 16.3)], 9.5, before=5)
    field(bot, [('Superputerea mea:', 16.3)], 9.5, before=6)
    field(bot, [('Quest-ul meu de 30 de zile:', 16.3)], 9.5, before=6)


agent_card(d)
spacer(d, 14)
agent_card(d)

# ---- Anexa 8 – Fișa 2 Harta mea
D.annex_title('ANEXA 8', 'FIȘA 2 – Harta mea de puncte forte')
field(d, [('Numele meu:', 10)], 10.5, before=0)
para(d, 'Scrie câte un lucru bun despre tine în fiecare zonă. Nu trebuie să fii cel mai bun – este suficient să fie ceva ce faci bine sau care te ajută.',
     10, italic=True, color=C['grey'], before=4, after=6)
t = table(d, 3, 2, [8.5, 8.5], borders=('single', 6, C['lav2']), inside=('single', 6, C['lav2']), lr=0.3, tb=0.15)
for i, (name, q, ex, col, light) in enumerate(ZONE):
    cell = t.cell(i // 2, i % 2)
    row_setup(t.rows[i // 2], 5.2)
    shade(cell, light)
    para(cell, name, 13, True, color=col, after=0)
    para(cell, q, 9.5, italic=True, after=2)
    lines(cell, 3, 7.9, 10.5, before=10)
spacer(d, 8)
t = table(d, 1, 1, [CONTENT_W], borders=('single', 12, C['yellow']), lr=0.3, tb=0.15)
cell = t.cell(0, 0)
field(cell, [('Un punct forte pe care ceilalți îl observă la mine:', 16.3)], 10.5, before=4)
field(cell, [('Zona în care am cele mai multe puncte forte:', 16.3)], 10.5, before=10)
field(cell, [('O zonă în care aș vrea să cresc:', 16.3)], 10.5, before=10, after=4)

# ---- Anexa 9 – Bilet de ieșire
D.annex_title('ANEXA 9', 'Biletul de ieșire')
scissors_note(d)


def bilet(cell, i):
    shade(cell, 'FFFFFF')
    para(cell, 'BILET DE IEȘIRE – Misiunea 1', 11, True, color=C['purple'], after=0)
    para(cell, 'Agenția Secretă a Punctelor Forte', 8, italic=True, color=C['grey'], after=2)
    para(cell, 'Astăzi am descoperit că eu...', 10, True, before=4, after=0)
    lines(cell, 2, 7.9, 10, before=9)
    para(cell, 'Un lucru bun pe care îl am:', 10, True, before=6, after=0)
    lines(cell, 1, 7.9, 10, before=9)
    para(cell, 'Mi-a plăcut cel mai mult:', 10, True, before=6, after=0)
    lines(cell, 1, 7.9, 10, before=9)
    para(cell, 'Cum m-am simțit azi? (încercuiește)', 9.5, True, before=8, after=2)
    para(cell, '1      2      3      4      5', 13, True, color=C['purple'], align='center', after=0)
    p = para(cell, '', after=0)
    p.paragraph_format.tab_stops.add_tab_stop(Cm(7.9), WD_TAB_ALIGNMENT.RIGHT)
    runs(p, 'deloc bine\tfoarte bine', 8, italic=True, color=C['grey'])


cut_grid(d, 4, 2, 8.5, 10.7, bilet)

D.save(OUT)
print('OK', OUT)
