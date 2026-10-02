# -*- coding: utf-8 -*-
import os
import gal_docx as E
from gal_docx import TITLE, H1, H2, H3, P, SMALL, QUOTE, BUL, NUM, TBL, CALLOUT, IMG, PAGEBREAK, FOOTER

HERE = os.path.dirname(os.path.abspath(__file__))
FOOTER('Intervenția 5 – Comunicare și vizibilitate  ·  v1, 02.10.2026')

TITLE('Comunicare și vizibilitate – ce trebuie să respectăm')
SMALL('Proiectul „Educație pentru mediu în teritoriul GAL Napoca Porolissum – micro-granturi pentru mediu”, contract de finanțare '
      'C 36010804713061304413 / 08.09.2026. Analiză de conformitate, partea 1 din analiza Ghidului solicitantului pentru '
      'Intervenția 5 „LEADER în verde”, sesiunea 2/2026. Versiunea 1, 02.10.2026.')

CALLOUT('De făcut acum (octombrie 2026, finalul lunii L1)', [
    '**1. Placa informativă la sediul GAL.** Se pune de la începerea implementării (contractul e din 08.09.2026). Model AFIR '
    '„Placă FEADR LEADER” V3, 50 × 70 cm, completat cu datele din secțiunea 4.',
    '**2. Caseta informativă pe napocaporolissum.ro**, pe prima pagină, în jumătatea de sus, cu link către pagina Comisiei Europene '
    'despre FEADR. La verificarea din 02.10.2026, codul paginii principale nu conținea nicio mențiune despre proiect sau despre PS 2023-2027. '
    'Poate fi un conținut încărcat dinamic, deci merită o privire directă.',
    '**3. Informarea pe toate canalele social media ale GAL**: o mențiune vizibilă în partea de sus a fiecărui canal (copertă, postare '
    'fixată sau descriere) și o postare care prezintă finanțarea.',
    '**4. Graficul calendaristic actualizat, cu locurile și agenda activităților**, încărcat în platforma AFIR cu cel puțin 10 zile lucrătoare '
    'înaintea primului eveniment. De verificat dacă a fost transmis. E obligatoriu înaintea întâlnirilor din campania offline și a sesiunilor de informare.',
    '**5. O singură bară de sigle pentru toate materialele proiectului**, după regula AFIR din ianuarie 2026. Manualul GAL are altă ordine '
    '(secțiunea 5).',
], fill='FBEAEA', line='E0A0A0')

# ------------------------------------------------------------------ 1
H1('1. Ce documente se aplică și care are prioritate')
P('Ghidul solicitantului (p. 28) cere respectarea a două manuale: cel al AFIR și cel al GAL. Regulile de vizibilitate vin însă din mai multe '
  'documente, iar în câteva puncte se contrazic. Le-am citit pe toate și le-am aplicat în ordinea de mai jos.')
TBL([
    ['Nr.', 'Document', 'Ce reglementează', 'Statut'],
    ['1', 'Contractul de finanțare – Anexa II „Materiale și activități de informare de tip publicitar” (AFIR, Ed. I Rev. 1)',
     'placa, afișul, autocolantul, site-ul, social media, materialele tipărite, acțiunile publice', 'obligatoriu, face parte din contract'],
    ['2', 'Regulamentul de punere în aplicare (UE) 2022/129, Anexele II și III',
     'emblema UE și declarația de finanțare', 'obligatoriu'],
    ['3', 'Ghidul AFIR de utilizare a elementelor de identitate vizuală PS 2027, V3 (ianuarie 2026) și modelele „Materiale publicitare PS 2027 V3”',
     'ordinea siglelor, regulile LEADER, modelele editabile pentru placă, afiș, autocolant', 'modelele se folosesc întocmai („nu se aplică soluții creative”)'],
    ['4', 'Ghidul de implementare DR-36, Ed. I Rev. 3 (AFIR)',
     'evenimente, liste de prezență, chestionare, verificări pe teren, rapoarte de activitate', 'obligatoriu'],
    ['5', 'Ghidul solicitantului GAL – Intervenția 5, sesiunea 2/2026',
     'preia punctele 1 și 4 și adaugă manualul GAL', 'obligatoriu'],
    ['6', 'Manualul de identitate vizuală GAL Napoca Porolissum (2025)',
     'sigla GAL, culorile, fonturile, antetele', 'obligatoriu, cu excepția punctelor în care contrazice AFIR'],
    ['7', 'Cererea de finanțare, Anexa 1, Metodologia de selecție',
     'angajamentele de comunicare asumate: campanii, sesiuni, transparență', 'asumate prin contract'],
], widths=[1.0, 6.4, 5.6, 4.0])
P('**Regula de lucru:** unde manualul GAL contrazice documentele AFIR, aplicăm AFIR. AFIR este autoritatea contractantă, iar ghidul ei '
  'este mai nou (ianuarie 2026). Diferențele sunt listate în secțiunea 5.')

# ------------------------------------------------------------------ 2
H1('2. Obligațiile GAL ca beneficiar al proiectului')
TBL([
    ['Ce', 'Cerința', 'Sursa', 'Ce facem și ce păstrăm ca dovadă', 'Când'],
    ['Placa informativă',
     'Obligatorie pentru finanțările de peste 50.000 € **și la sediile GAL**. Model AFIR A.2 „Placă FEADR LEADER” V3, completat doar cu datele '
     'proiectului. 50 × 70 cm (V3 acceptă 50–100 × 70–140 cm), policromie, fond alb, font Calibri, margine de siguranță 3 cm, material '
     'rezistent (PVC, tablă). Pe clădire, cu marginea de jos la 130–200 cm de sol, lângă intrare, vizibilă din toate punctele de acces public. '
     'Se înlocuiește dacă se degradează.',
     'Anexa II C1.1-(2); GIV V3 A-(2); Ghid GAL p. 28',
     'Comandă pe baza datelor din secțiunea 4. Fotografii datate la montare și periodic, factura. Acordul administratorului '
     'blocului pentru montarea pe fațadă.',
     'Acum. Rămâne expusă cel puțin până la finalul perioadei de monitorizare.'],
    ['Caseta informativă pe site',
     'Pe prima pagină a site-ului, în jumătatea de sus: o scurtă descriere a proiectului, scopul și rezultatele, cu sprijinul UE '
     'evidențiat și datele de pe placă. Link către pagina Comisiei Europene despre FEADR. Site-ul GAL prezintă mai multe proiecte, deci '
     'pe prima pagină pui o informare scurtă, iar detaliile finanțării merg pe o pagină dedicată proiectului.',
     'Anexa II C1.1-(5); GIV V3 B-(1)',
     'Textul din secțiunea 4. Capturi de ecran datate, lunar.\nLink: agriculture.ec.europa.eu/cap-my-country/rural-development_ro',
     'Acum; până la finalul monitorizării.'],
    ['Social media (Facebook, Instagram, TikTok, X, LinkedIn, YouTube)',
     'Pe fiecare canal, informația despre finanțarea PS 2027 trebuie să fie vizibilă în jumătatea de sus a primei pagini (copertă, postare fixată sau '
     'descriere). Mai e nevoie de o descriere „succintă și completă” a sprijinului, de exemplu imaginea afișului informativ cu un text scurt '
     'despre scop și rezultate. Orice postare despre proiect are cel puțin emblema UE cu „Cofinanțat de Uniunea Europeană”.',
     'Anexa II C1.1-(5); GIV V3 B-(2)',
     'O postare-tip și o imagine de copertă. Capturi de ecran datate.',
     'Acum; apoi la fiecare postare.'],
    ['Materiale tipărite și multimedia (afișul și pliantul apelului, ghidul, prezentări, comunicate, video)',
     'Trei mențiuni obligatorii (textul exact e mai jos), datele proiectului și bara de sigle în header.',
     'Anexa II C1.1-(6); GIV V3 C-(1) și cap. 3',
     'Câte un exemplar din fiecare material, la dosar și în raportul de activitate.',
     'La fiecare material.'],
    ['Acțiuni publice',
     'Participare benevolă la evenimente de prezentare media sau publică. Dacă proiectul e desemnat exemplu de bună practică, participare '
     'la diseminare.',
     'Anexa II C1.1-(7)', 'La invitația AFIR, MADR sau a rețelei rurale.', 'Pe toată durata.'],
    ['Siglele pe alte materiale',
     'Elementele de identitate vizuală se pot folosi pe alte materiale decât cele din Anexa II numai cu aprobarea scrisă a AFIR. '
     'Materialul trebuie să fie de interes public, gratuit și necomercial.',
     'Anexa II, prevederea 9',
     'Propun o adresă către OJFIR Cluj cu lista materialelor planificate (pliant, afiș pentru apel, roll-up, prezentări, eventuale obiecte '
     'promoționale), trimisă înainte de tipărire.',
     'Înaintea primului material tipărit.'],
    ['Autocolante',
     'Se aplică pe echipamentele cumpărate prin proiect. Bugetul GAL nu are echipamente; obligația revine beneficiarilor finali (secțiunea 7).',
     'Anexa II C1.1-(4)', '–', '–'],
], widths=[2.4, 5.6, 2.3, 4.2, 2.5])

H3('Textul obligatoriu pe materialele tipărite și multimedia (Anexa II, C1.1-6)')
QUOTE('Proiect finanțat cu fonduri europene nerambursabile prin Planul Strategic PAC 2023 – 2027 (PS 2023 – 2027).\n'
      'PS 2023 – 2027 este implementat de Agenția pentru Finanțarea Investițiilor Rurale, din subordinea Ministerului Agriculturii și Dezvoltării Rurale.\n'
      'PS 2023 – 2027 este finanțat de Uniunea Europeană și Guvernul României prin Fondul european agricol pentru dezvoltare rurală.')
SMALL('La acestea se adaugă datele proiectului din secțiunea 4. Titulatura programului: „Planul Strategic PAC 2023 – 2027” pe materialele publicitare '
      'și pe social media („PS 2027” e acceptat informal); „Planul Strategic PAC 2023 – 2027 (PS 2023 – 2027)” în corespondență și pe site '
      '(GIV V3, nota 1).')

# ------------------------------------------------------------------ 3
H1('3. Ce ne-am asumat prin proiect')
TBL([
    ['Angajament', 'Unde e scris', 'Perioada (calendarul v2)', 'Dovezi necesare'],
    ['Campanie de informare și promovare, cu o componentă online și una offline; minimum 20 de potențiali beneficiari informați '
     '(unități de învățământ și ONG-uri de mediu)',
     'CF – A2; Anexa 1, cap. 3, 4, 10', 'L1–L5\n08.09.2026 – 07.02.2027',
     'Registrul potențialilor beneficiari informați (instituție, localitate, persoană de contact, dată, canal, confirmare); capturi, fotografii, liste.'],
    ['Lansarea apelului: 1 ghid, 1 apel publicat, 2 sesiuni de informare',
     'CF – A4', 'L5–L7', 'Anunțul publicat, ghidul pe site, agendele, listele de prezență, chestionarele, fotografiile.'],
    ['Consiliere pentru solicitanți, fizic sau online, fără consultanță la scrierea proiectelor',
     'Anexa 1, cap. 8; Metodologia', 'L5–L8', 'Registrul de consiliere.'],
    ['Transparența selecției: apelul, ghidul, criteriile și rezultatele publicate pe site; rezultatele transmise direct fiecărui solicitant',
     'Metodologia, cap. VIII și XI; Anexa 1, cap. 8', 'L5–L8', 'Capturi de ecran datate; e-mailurile de notificare.'],
    ['Raportul de activitate intermediar, cu documentația integrală a concursului, transmis la AFIR în max. 10 zile lucrătoare de la finalizarea selecției',
     'Ghid GAL p. 16 și 26', 'L8', 'Include toate materialele de comunicare de până atunci.'],
    ['Schimbul de bune practici: raportul, sinteza concluziilor, lista de recomandări și contacte',
     'Fundamentarea bugetului, cap. 2', 'L5–L8 (v2)', 'Dosarul evenimentului (secțiunea 6).'],
    ['Raportul final de activitate publicat', 'CF – A13', 'L21', 'Publicare pe site.'],
], widths=[5.6, 3.4, 2.8, 5.2])
SMALL('Campaniile nu au linie de buget proprie. Costurile cu placa și tipăriturile se acoperă din alte surse ale GAL, fără dublă finanțare.')

# ------------------------------------------------------------------ 4
H1('4. Datele pentru placă, site și postări')
TBL([
    ['Câmp pe model', 'Ce scriem', 'Observații'],
    ['Proiect finanțat ... (titlul)', 'Educație pentru mediu în teritoriul GAL Napoca Porolissum – micro-granturi pentru mediu', '–'],
    ['Cod proiect', 'C36010804713061304413',
     'Codul cererii de finanțare atribuit de AFIR. De confirmat că e același cu numărul contractului.'],
    ['Județ', 'Cluj', '–'],
    ['Localitate', 'Gilău, Aghireșu, Beliș, Călățele, Căpușu Mare, Huedin, Izvoru Crișului, Măguri-Răcătău, Mănăstireni, Mărgău, Mărișel, '
     'Râșca, Săcuieu, Sâncraiu',
     'Întâi localitatea cu ponderea cea mai mare (Gilău, 9% în CF; celelalte 13 au câte 7%), apoi celelalte.'],
    ['Beneficiar', 'Asociația Grupul de Acțiune Locală Napoca Porolissum', '–'],
    ['Valoarea totală eligibilă a proiectului', '138.643 euro', 'Din bugetul contractat.'],
    ['din care, finanțare nerambursabilă PS 2023-2027', '138.643 euro', '100% din eligibil.'],
    ['Proiectant / Executant', 'Proiectant: nu este cazul\nExecutant: Asociația GAL Napoca Porolissum',
     'Câmpurile sunt gândite pentru lucrări. Formularea trebuie confirmată cu OJFIR.'],
    ['Demarare', '08.09.2026', 'Data semnării contractului.'],
    ['Finalizare', '07.06.2028 (estimat, 21 de luni)', 'Se ia din contract.'],
], widths=[4.4, 6.8, 5.8])
IMG(os.path.join(HERE, 'img', 'model_placa_leader.png'), 13.5,
    'Modelul AFIR „Placă FEADR LEADER” V3, care se completează. Sursa: afir.ro – Identitatea vizuală – Materiale publicitare PS 2027 V3.')

H3('Propunere de text pentru caseta de pe prima pagină a site-ului')
QUOTE('**Proiect finanțat cu fonduri europene nerambursabile prin Planul Strategic PAC 2023 – 2027 (PS 2023 – 2027)**\n'
      '„Educație pentru mediu în teritoriul GAL Napoca Porolissum – micro-granturi pentru mediu” · Cod proiect C36010804713061304413 · '
      'Beneficiar: Asociația Grupul de Acțiune Locală Napoca Porolissum · Valoarea totală eligibilă: 138.643 euro, din care finanțare '
      'nerambursabilă PS 2023 – 2027: 138.643 euro · Perioada: 08.09.2026 – 07.06.2028.\n'
      'Prin acest proiect, GAL Napoca Porolissum finanțează 6 inițiative de educație pentru mediu, de până la 19.833,3 euro fiecare, propuse '
      'de școli și ONG-uri din cele 14 localități ale teritoriului și selectate printr-un concurs deschis și transparent. Scopul este ca '
      'protecția mediului să devină o preocupare concretă a comunităților noastre, prin activități practice cu copiii, tinerii și cetățenii.\n'
      'PS 2023 – 2027 este implementat de AFIR, din subordinea MADR, și este finanțat de Uniunea Europeană și Guvernul României prin '
      'Fondul european agricol pentru dezvoltare rurală. Află mai multe despre FEADR: [link Comisia Europeană].')

H3('Propunere de postare de prezentare (pentru toate canalele)')
QUOTE('🌱 GAL Napoca Porolissum lansează proiectul „Educație pentru mediu în teritoriul GAL Napoca Porolissum – micro-granturi pentru mediu”. '
      'În 2027, școlile și ONG-urile de mediu din teritoriu vor putea obține câte un micro-grant de până la 19.833,3 euro pentru inițiative '
      'de educație și protecție a mediului: plantări, ecologizări, reciclare, ateliere, spectacole, activități sportive cu temă ecologică. '
      'Detaliile apelului vor fi publicate pe napocaporolissum.ro.\n'
      'Proiect finanțat cu fonduri europene nerambursabile prin Planul Strategic PAC 2023 – 2027. Valoare eligibilă: 138.643 euro. '
      'Cofinanțat de Uniunea Europeană prin FEADR și de Guvernul României.')
SMALL('Postarea se însoțește de imaginea afișului informativ sau a plăcii completate, care conține deja emblema UE cu „Cofinanțat de Uniunea Europeană”.')

# ------------------------------------------------------------------ 5
H1('5. Bara de sigle și diferențele dintre manualul GAL și AFIR')
P('Regula AFIR (GIV V3, cap. 3): materialele proiectului au în header siglele în această ordine, de la stânga la dreapta: emblema UE cu '
  'declarația de finanțare, sigla MADR, sigla PS 2023-2027, sigla beneficiarului, sigla AFIR. Logo-ul LEADER se pune pe un rând separat. '
  'Toate siglele au aceeași înălțime.')
CALLOUT('Bara de sigle propusă pentru proiect', [
    '**Rândul 1:** UE „Cofinanțat de Uniunea Europeană” · Guvernul României – MADR · PS 2023-2027 · GAL Napoca Porolissum · AFIR',
    '**Rândul 2:** LEADER – „Dezvoltarea locală plasată sub responsabilitatea comunității”',
    '**Excepție, paginile web:** emblema UE cu mențiunea „Uniunea Europeană” stă pe același rând cu logo-ul LEADER (GIV V3, cap. 2.G).',
    '**Placa, afișul și autocolantul nu folosesc bara:** modelul AFIR se folosește exact cum este. Pe aceste modele nu există loc pentru sigla GAL.',
], fill='EAF3EA', line='9FC49F')
TBL([
    ['Aspect', 'Manualul GAL (2025)', 'AFIR (Anexa II + GIV V3, ian. 2026)', 'Ce aplicăm'],
    ['Ordinea siglelor', 'UE, MADR, AFIR, PS, GAL (exemplele de la p. 14–17); la LEADER: UE, FEADR, MADR, PS',
     'UE, MADR, PS, beneficiar, AFIR', 'AFIR'],
    ['Declarația de lângă emblema UE', '„Cofinanțat” la LEADER, dar exemplul pentru PS folosește „Finanțat de Uniunea Europeană”, iar cel pentru AFIR doar „Uniunea Europeană”',
     'La LEADER: „Cofinanțat de Uniunea Europeană”; pe web: „Uniunea Europeană”', '„Cofinanțat de Uniunea Europeană”'],
    ['Poziția siglelor LEADER și GAL', 'Ambele pe rândul al doilea', 'GAL pe rândul principal, înaintea AFIR; LEADER separat', 'AFIR'],
    ['Sigla FEADR', 'Inclusă în setul LEADER', 'Opțională', 'O omitem, pentru o bară mai aerisită'],
    ['Fonturi', 'Montserrat în antet', 'Calibri pe materialele publicitare; declarația UE doar în Arial, Calibri, Garamond, Trebuchet, Tahoma, Verdana sau Ubuntu',
     'Montserrat doar pentru numele GAL din antet; în rest, Calibri'],
    ['Dimensiuni și spațiere', 'Sigla GAL: min. 25 mm lățime (print), 150 px (digital); între sigle, 1/5 din înălțime',
     'Sigla AFIR: min. 13 mm înălțime; spațiu de siguranță 1/5 din înălțime sau min. 20 mm; emblema UE la fel de mare ca celelalte sigle; declarația la 1–4 mm de emblemă',
     'Le respectăm pe toate'],
], widths=[3.0, 4.6, 5.2, 4.2])
P('**Recomandare:** o erată scurtă la manualul GAL. Ghidul trimite și beneficiarii finali la ambele manuale, iar fără erată școlile și '
  'ONG-urile primesc două reguli diferite.')

# ------------------------------------------------------------------ 6
H1('6. Evenimentele: reguli și dovezi')
P('Sunt vizate sesiunile de informare, întâlnirile din campania offline și schimbul de bune practici. Pentru proiectele de servicii, '
  'OJFIR verifică pe teren tocmai activitățile cu grup țintă.')
BUL([
    '**Graficul calendaristic actualizat**, cu locul și agenda, se încarcă în platformă cu cel puțin 10 zile lucrătoare înaintea primului eveniment '
    '(Ghid GAL p. 25). Recomand să fie actualizat înaintea fiecărui eveniment și la orice schimbare de dată sau loc. OJFIR poate anunța vizita '
    'cu cel mult 24 de ore înainte și poate veni și neanunțat.',
    '**La vizita OJFIR** participă obligatoriu un reprezentant al GAL cu calitate oficială în proiect, iar toate documentele trebuie să fie la '
    'îndemână. O activitate neavizată pe teren nu se plătește. Dacă e ultima activitate din grafic, se consideră neavizată în întregime.',
    '**Lista de prezență se face pentru fiecare zi:** nume și prenume, adresă, telefon, e-mail și semnătură, plus durata și locul evenimentului. '
    'Datele sunt confidențiale și se transmit doar beneficiarului și AFIR. Adăugăm și localitatea, pentru că grupul țintă trebuie să lucreze '
    'sau să locuiască în teritoriul GAL (criteriul EG11).',
    '**Fiecare participant semnează o declarație pe propria răspundere** că nu a participat la alte evenimente cu aceeași tematică, inclusiv în '
    'proiecte din 2014-2020 (Ghid GAL p. 26). Atenție: GAL a avut deja proiecte de mediu (AFM „Alege Verde!” și „Pune verdele în mișcare!”, '
    'PNDR „Children and youth camp”, Erasmus+ YouProclima și BEYOND). Tematica evenimentelor trebuie formulată precis, ca informare '
    'despre apelul de micro-granturi, ca să nu se suprapună.',
    '**Chestionare de evaluare** la acțiunile de informare. Dacă peste 50% dintre chestionare au note sub 3, activitatea nu se avizează. '
    'Folosim o scală de la 1 la 5 și împărțim chestionarele la final, înainte să plece participanții.',
    '**Dosarul fiecărui eveniment:** agenda, prezentarea, fotografiile, comunicatul sau postarea, listele de prezență, declarațiile, '
    'chestionarele, nota de informare GDPR și acordurile pentru fotografii. Toate se anexează la raportul de activitate.',
    '**Numărul minim de participanți:** ghidurile nu fixează unul. Formularul notei de modificare (C3.1L) pomenește 10/20 de participanți pe grupă '
    'la acțiunile de informare. De confirmat cu OJFIR; până atunci, ne propunem minimum 10 participanți pe sesiune.',
    '**Fotografiile cu copii:** e nevoie de acordul scris al părinților pentru fotografiere și publicare (GDPR, Legea 272/2004). Contează la '
    'evenimentele din școli.',
])

# ------------------------------------------------------------------ 7
H1('7. Ce transmitem beneficiarilor finali')
P('Obligațiile de mai jos intră în ghidul sub-proiectelor și în contractul de grant. GAL le verifică la cele două vizite pe teren.')
BUL([
    '**Afișul informativ A2**, după modelul AFIR A.3 „Afiș FEADR LEADER” V3. Cel puțin 2 afișe, pe suprafețe diferite, la locul de implementare, '
    'cu marginea de jos la 130–200 cm. Hârtie lucioasă rezistentă la apă și UV, 100–150 g/m²; recomandat circa 9 exemplare, ca rezervă. '
    'Rămân expuse de la începerea implementării până la finalul monitorizării.',
    '**Ce date intră pe afișul unui sub-proiect** (cod, valoare, beneficiar) trebuie stabilit cu OJFIR. Sub-proiectele nu au cod AFIR propriu. '
    'Propun un text unic, completat de GAL pentru toți cei 6 beneficiari.',
    '**Autocolante de 15 × 21 cm** (model A.4 LEADER) pe toate echipamentele cumpărate, inclusiv drone. Cel puțin 2 pe fiecare echipament, '
    'aplicate în maximum 20 de zile de la recepție.',
    '**Site și social media:** casetă pe site și informare pe social media, dacă beneficiarul le are. Pe materialele tipărite și multimedia, '
    'cele trei mențiuni obligatorii.',
    '**Strategia de promovare** este element obligatoriu al planului de intervenție (Anexa 2 AFIR; Metodologia, cap. IV). Le dăm un model '
    'cu cerințele minime.',
    '**Costurile de vizibilitate** (afișe, autocolante) pot fi eligibile în bugetul sub-proiectelor, prin derogarea LEADER: Reg. (UE) 2022/129, '
    'Anexa III pct. 2 lit. a, b, e, preluată în Ghidul de implementare DR-36. Trebuie scris explicit în ghid.',
    '**Dovezi pentru tranșa a II-a:** fotografiile afișelor și ale autocolantelor, capturi de ecran, câte un exemplar din materiale.',
    '**Participarea** la schimbul de bune practici și la evenimentele de diseminare ale GAL.',
    '**Acordul părinților** pentru fotografiile cu copii.',
])
IMG(os.path.join(HERE, 'img', 'model_afis_leader.png'), 7.5, 'Modelul AFIR „Afiș FEADR LEADER” V3 (A2, vertical).')

# ------------------------------------------------------------------ 8
H1('8. Calendarul comunicării')
TBL([
    ['Perioada', 'Ce', 'Cine'],
    ['L1–L2 (până la 07.11.2026)', 'Placa; caseta pe site; informarea pe social media; bara de sigle și antetul documentelor; adresa către OJFIR cu '
     'lista materialelor; verificarea graficului calendaristic din platformă', 'Expertul de animare locală și managerul'],
    ['L1–L5 (până la 07.02.2027)', 'Campania online și offline; registrul potențialilor beneficiari informați (≥ 20)', 'Expertul de animare locală'],
    ['L5 (ianuarie 2027)', 'Lansarea apelului: anunțul, ghidul și metodologia pe site; comunicat de presă; postări', 'Toată echipa'],
    ['L5–L7', '2 sesiuni de informare (grafic actualizat cu 10 zile lucrătoare înainte); consiliere', 'Expertul de animare și expertul de coordonare'],
    ['L7–L8', 'Publicarea rapoartelor de selecție (intermediar, contestații, final); notificarea fiecărui solicitant', 'Managerul'],
    ['L8', 'Raportul de activitate intermediar (în 10 zile lucrătoare), cu dosarul complet al concursului', 'Managerul'],
    ['L8–L10', 'Schimbul de bune practici, dacă se mută după selecție (vezi analiza calendarului)', 'Echipa'],
    ['L9', 'Contractele de grant: comunicat și postări; kitul de vizibilitate predat beneficiarilor', 'Expertul de animare locală'],
    ['L9–L20', 'Verificarea vizibilității la cele 2 vizite pe proiect; postări despre activitățile sub-proiectelor', 'Expertul de coordonare și expertul de animare'],
    ['L21', 'Raportul final publicat; postare de încheiere cu rezultatele', 'Managerul'],
    ['După L21', 'Placa și caseta rămân până la finalul perioadei de monitorizare', 'GAL'],
], widths=[3.6, 9.4, 4.0])

# ------------------------------------------------------------------ 9
H1('9. Întrebări de lămurit')
NUM([
    'Ce versiune a Anexei II este atașată la contract? Pe afir.ro este Ed. I Rev. 1; vreau să confirm că nu există diferențe.',
    'Codul proiectului de pe placă este același cu numărul contractului (C36010804713061304413)?',
    'Cum se completează „Proiectant / Executant” la un proiect de servicii? (de întrebat la OJFIR)',
    'Există deja la sediu o placă pentru alt proiect GAL, de exemplu DR-36F? Ghidul AFIR permite o singură placă, pe modelul multifond, '
    'dacă mai multe operațiuni au loc în același loc. Trebuie confirmat cu OJFIR dacă se aplică aici.',
    'A fost încărcat în platformă graficul calendaristic actualizat, cu locații și agendă?',
    'Ce s-a făcut deja în campania A2 din luna L1 (postări, întâlniri)? Dovezile trebuie strânse de acum.',
    'Ce date intră pe afișul unui sub-proiect (cod, valoare)?',
    'În alte proiecte, AFIR a cerut GAL-ului aprobare scrisă pentru pliante și afișe? Chiar dacă nu, aș trimite adresa către OJFIR, din prudență.',
])

# ------------------------------------------------------------------ 10
H1('10. Ce pregătesc mai departe – pachetul de comunicare')
NUM([
    '**Planul de comunicare și vizibilitate (A2):** campaniile online și offline, mesajele, canalele, calendarul, indicatorii și responsabilii.',
    '**Fișa de date pentru placă** și indicațiile pentru tipografie.',
    '**Textele pentru site:** caseta de pe prima pagină și pagina proiectului.',
    '**Postările-tip** pentru fiecare canal și imaginea de copertă.',
    '**Antetul Word al documentelor proiectului**, cu bara de sigle.',
    '**Afișul și pliantul apelului** (texte și machetă).',
    '**Comunicatul de presă** pentru lansarea proiectului și a apelului.',
    '**Kitul de eveniment:** agenda, lista de prezență, declarația participantului, chestionarul, nota GDPR, acordul pentru fotografii.',
    '**Registrele:** potențiali beneficiari informați și consiliere.',
    '**Ghidul de vizibilitate pentru beneficiarii finali**, cu clauzele din contractul de grant și fișa de verificare de la vizita pe teren.',
    '**Adresa către OJFIR:** graficul actualizat și lista materialelor.',
])

# ------------------------------------------------------------------ 11
H1('11. Alte constatări din ghid și metodologie')
P('Nu țin de comunicare, dar le-am găsit citind integral ghidul, metodologia și documentele AFIR la care trimit. Le tratăm în etapele următoare.')
TBL([
    ['Constatare', 'Sursa', 'Ce facem'],
    ['**Avansul la proiectele umbrelă** e de maximum 50% din valoarea activităților GAL de sprijin pentru solicitanți. Dacă intră doar schimbul de bune practici (8.740 €), '
     'avansul e de circa 4.370 €; dacă intră și cheltuielile cu personalul (19.643 €), e de circa 9.821 €. În ambele variante, nu poate finanța granturile. '
     'Tranșa I (80% × 119.000 = 95.200 €) se plătește din fonduri proprii sau din credit și se recuperează prin cereri de plată.',
     'Ghidul de implementare DR-36 Rev. 3, secțiunea despre avans', 'Plan de flux de numerar înainte de L9.'],
    ['**Juriul trebuie să aibă un număr impar de membri**, inclusiv reprezentanți ai domeniului din județ sau regiune. Metodologia spune doar „minimum 3 + minimum 2”.',
     'Ghid GAL p. 23; Anexa 2 AFIR', 'Componență fixă de 5. Un membru care iese din cauza unui conflict de interese se înlocuiește; juriul nu coboară la 4.'],
    ['**Criteriile de selecție ale proiectului GAL nu pot fi afectate prin modificări.** Criteriul 2: peste 2 angajați GAL în juriu. Criteriul 1: peste 3 sub-proiecte. '
     'Deci trebuie păstrați minimum 3 angajați GAL în juriu și contractate minimum 4 sub-proiecte (ținta e 6).',
     'Ghid GAL p. 7 și 22', 'Campania trebuie să aducă destule aplicații eligibile.'],
    ['**Incompatibilitate:** echipa de proiect, asociații și angajații GAL nu pot fi angajați sau asociați ai entităților finanțate (de exemplu, un angajat GAL care '
     'predă la școala solicitantă). Metodologia acoperă doar o parte.',
     'Ghid GAL p. 24', 'De scris explicit în ghidul sub-proiectelor.'],
    ['**GAL nu poate încheia contracte de servicii sau de furnizare** cu beneficiarii granturilor din același proiect.', 'Ghid GAL p. 24',
     'Contează și la alegerea furnizorului pentru schimbul de bune practici.'],
    ['**Tranșele:** cea inițială de maximum 90%; cea finală de minimum 10%, după realizarea a cel puțin 90% din acțiuni (proiecte sociale). '
     'Fundamentarea vorbește despre „obiectivele din Planul de afaceri”.',
     'Ghid GAL p. 24', 'Contractul de grant: 80/20, cu „90% din acțiunile din planul de intervenție”.'],
    ['**Plafonul pe sub-proiect este de maximum 19.833,3 €** (ghidul), deci 6 × 19.833,30 = 118.999,80 €, nu 119.000 €.',
     'Ghid GAL p. 9 și 23', 'Plafonul din ghidul sub-proiectelor: 19.833,30 €.'],
    ['**Calendarul din metodologie** (cap. IX) e cel inițial, cu lansarea în L2.', 'Metodologia',
     'Actualizare prin decizia Consiliului Director, publicată pe site.'],
    ['**Formulări neclare în metodologie:**\n'
     '• criteriul „proiecte comunitare” (25 p.) nu spune dacă punctează experiența anterioară sau angajamentul;\n'
     '• criteriul „calitatea planului” (30 p.) nu are punctaje pe subcriterii;\n'
     '• departajarea trimite la „coerența prezentării”, dar grila interviului are „coerența planului de intervenție”.',
     'Metodologia, cap. VI', 'De clarificat în ghid și în grila de evaluare.'],
    ['**Cheltuieli neeligibile care contează la sub-proiecte:** echipamente second-hand; mijloace de transport pentru uz personal sau pentru persoane '
     '(atenție la biciclete pentru „transport cu emisii scăzute”); cheltuieli făcute înainte de contractul de grant; TVA recuperabil; dublă finanțare.',
     'Ghid GAL p. 6', 'Lista intră în ghidul sub-proiectelor.'],
    ['**Indicatorul R.27:** ghidul îi dă valoarea 2 și cere ca numărul de obiective să apară în documentele proiectului. CF-ul și Anexa 1 nu dau un număr.',
     'Ghid GAL p. 5 și 10', 'De urmărit în raportul final.'],
    ['**Contractul de grant** trebuie să conțină prevederile minime stabilite de AFIR (anexă la Manualul de procedură DR-36).', 'Anexa 2 AFIR',
     'Trebuie procurat modelul AFIR.'],
    ['**Raportul de activitate intermediar:** AFIR răspunde în 6 zile lucrătoare și permite o singură retransmitere, în 5 zile lucrătoare. Contractele de grant se semnează doar după avizare.',
     'Ghid GAL p. 16', 'Calendar strâns în L8–L9.'],
], widths=[9.0, 3.6, 4.4])

SMALL('Surse: Ghidul solicitantului Intervenția 5, sesiunea 2/2026 (GAL, 19.01.2026); Metodologia de selecție a sub-proiectelor, sesiunea 2/2026; '
      'Ghid de identitate vizuală GAL Napoca Porolissum (2025); AFIR – Anexa II C1.1 la contractul de finanțare, Ed. I Rev. 1; AFIR – Ghid de '
      'utilizare a elementelor de identitate vizuală PS 2027, V3, ianuarie 2026, și modelele V3; AFIR – Ghid de implementare DR-36, Ed. I Rev. 3; '
      'AFIR – Anexa 2 „Detalii privind proiectele umbrelă”; Reg. (UE) 2022/129. Textele extrase sunt în interventia5/surse/.')

out = os.path.join(HERE, 'Int5_Comunicare_si_vizibilitate_analiza.docx')
E.doc.save(out)
print('saved', out)
