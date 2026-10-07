# -*- coding: utf-8 -*-
"""Raportul de progres nr. 1 – proiect UNIC, cod SMIS 352704 (PEO 2021-2027).

Rulare:  python3 build_rp1_docx.py
Produce: RP1_UNIC_352704_Raport_de_progres.docx  (document de lucru, cu note MP)
         RP1_UNIC_352704_text_MySMIS.txt          (doar textele de copiat în MySMIS)
"""
import os, re
import rp1_engine as E
from rp1_engine import (H1, H2, H3, H4, P, SMALL, BUL, FLAG, CALLOUT, TBL,
                        PAGEBREAK, SECT, FIELD)

HERE = os.path.dirname(os.path.abspath(__file__))

# Limitele din formularul MySMIS2021 – Raport de progres (contorul „Caractere rămase”
# din capturile Manualului de utilizare MySMIS2021 FO – Raport de progres, v2, sept. 2024).
L_LUNG = 10500      # Rezumat, Progres, Abateri, Recepții, Dificultăți, Ajutor de stat,
                    # Comunicare, fiecare principiu orizontal, Observații
L_SCURT = 3500      # Rezultat obținut, Descriere modificare contract, Stadiu achiziție,
                    # Resurse umane, Recomandări vizite, Justificare/Măsuri/Abateri ind. etapă
L_PRESUPUS = 3500   # câmpuri pe care manualul nu le arată (de verificat la editare)

# =====================================================================================
# PARTEA A – NOTA MANAGERULUI DE PROIECT
# =====================================================================================
H1('Raport de progres nr. 1 – proiect UNIC (cod SMIS 352704)')
P('**„UNIC – Uniți pentru Nevoile Incluzive și Continuitatea Educației Elevilor”** · Contract de finanțare nr. 11205/16.06.2026 · '
  'PEO 2021-2027, P8, ESO4.6, acțiunile 8.f.1–8.f.3 · Beneficiar: Asociația Grupul de Acțiune Locală Napoca Porolissum')
P('**Perioada de raportare:** 01.07.2026 – 30.09.2026 (L1–L3) · **Versiune de lucru:** 05.10.2026 · **Întocmit de:** Managerul de proiect')
SMALL('Documentul are trei părți: A – nota managerului de proiect (ce trebuie rezolvat înainte de transmitere); B – textul raportului, câmp cu câmp, '
      'în ordinea din MySMIS2021, cu numărul de caractere față de limita fiecărui câmp; C – documentele de încărcat, cu denumirile fișierelor. '
      'Textul evidențiat cu galben «...» este o informație care trebuie confirmată sau completată din documente înainte de copierea în MySMIS. '
      'Casetele roșii sunt note interne și nu se copiază.')

H2('A1. Surse folosite și cum a fost construit raportul')
BUL([
    '**Cererea de finanțare – versiunea 12** (FormularDepunere_352704_2026-09-16, depusă cu Notificarea nr. 4 din 15.09.2026), comparată integral cu versiunea 11 (N3): '
    'singura diferență este poziția Cadru didactic 3 (Anderco Claudia-Maria în locul Boaru Mariana-Dorina). Contractul 11205/16.06.2026 cu anexele (Plan de monitorizare, grafic CR).',
    '**Manualul beneficiarului PEO/PIDS, versiunea 5 (decembrie 2025)**: §4.1.1 (RP), §4.1.2 (GT și formulare), Anexa 8 (pontaj), Anexa 10 (raport de activitate), '
    'Anexa 11 (documentele RP și denumirea fișierelor), Anexa 12 (planificare lunară), Anexa 13 (lista experților), Anexa 14 (centralizator livrabile), Anexa 18 (vizibilitate).',
    '**Ghidul solicitantului – condiții specifice 8.F** (consolidat cf. Corrigendum 2) și **condiții generale PEO** (cf. Corr. 4); definițiile indicatorilor EECO06+07, 5SO14 și 5SR09 '
    'sunt cele din GSCS §3.8. Ghidul de monitorizare a indicatorilor de program nu se află în Drive – fișele oficiale trebuie verificate separat.',
    '**Manualul de utilizare MySMIS2021 Front Office – Raport de progres** (v2, sept. 2024): de aici sunt luate limitele de caractere (tabelul A3).',
    '**Modelul RP 8 (alt proiect)**: s-au preluat doar structura, formulările, modul de cuantificare, denumirea fișierelor și aspectele asupra cărora atrage atenția '
    '(persoana a III-a, perfect compus, „În perioada de raportare…”, organizare pe luni și pe funcții, fără nume în secțiunea 4, formula de „neimpact” la modificări, '
    'documentarea fiecărei afirmații). Nu s-a preluat nicio informație de fond.',
    '**Documentele de implementare din Drive** (rapoarte de activitate și pontaje iulie–septembrie, Anexa 12, registrul GT la 04.10.2026, dosarele GT, minutele ședințelor, '
    'dosarele de achiziție, dosarele de personal, metodologiile, procedurile și planurile V2).',
])

H2('A2. Termene')
TBL([
    ['Obligație', 'Termen', 'Sursa'],
    ['Transmiterea RP 1 în MySMIS2021', '**cel târziu 30.10.2026** (30 de zile de la finalul perioadei)', 'MB §4.1.1; Contract, Anexa 4 art. 4 lit. b'],
    ['RP 1 transmis cu ≥10 zile lucrătoare înaintea CR 1', 'CR 1 planificată 25.10.2026 (duminică → 23.10.2026) ⇒ **RP 1 până la 09.10.2026**', 'MB §4.1.1, §3.2.1 pct. 8; Plan raportare UNIC-PL-02'],
    ['Răspuns la clarificări RP', 'max. 10 zile lucrătoare cumulat', 'MB §4.1.1'],
    ['Anexa 12 – planificarea lunară', 'până pe 25 ale lunii, pentru luna următoare', 'MB §4.2'],
    ['Formularul 11 – reconciliere contabilă', 'lunar, până pe 20', 'Contract, Anexa 4 art. 4 lit. b'],
], widths=[5.5, 6.5, 5.0])
FLAG('Dacă data CR 1 se amână, graficul de rambursare din MySMIS se actualizează (notificare fără aprobare). Dacă RP 1 nu este depus cu 10 zile lucrătoare înaintea CR 1, '
     'CR 1 este returnată (MB §4.1.1).')

H2('A3. Limitele de caractere din MySMIS2021 folosite la redactare')
TBL([
    ['Secțiune MySMIS (pct. din export)', 'Câmp', 'Limită'],
    ['1. Rezumatul proiectului', 'Rezumat proiect', '10.500'],
    ['2. Modificări ale contractului', 'Descriere (pe fiecare modificare)', '3.500'],
    ['4. Activități și rezultate (pe fiecare subactivitate)', 'Progres în perioada de raportare / Rezultat obținut / Abateri-riscuri', '10.500 / 3.500 / 10.500'],
    ['5. Indicatori', 'Informații valoare raportată', '3.500 (nefigurat în manual – presupus)'],
    ['7. Grafic și stadiu achiziții', 'Stadiu (pe fiecare achiziție)', '3.500'],
    ['8. Contracte achiziții semnate', 'Descriere', '3.500 (presupus)'],
    ['9. Documente recepție', 'Avize, recepții, execuție / Dificultăți și întârzieri', '10.500 / 10.500'],
    ['12. Resurse umane implicate', 'Descriere (pe fiecare persoană)', '3.500'],
    ['13. Ajutor de stat / 14. Comunicare / 15. Principii orizontale (fiecare)', 'text', '10.500'],
    ['16. Recomandări vizite', 'Descriere', '3.500'],
    ['17. Indicatori de etapă', 'Justificare / Măsuri de remediere / Abateri-întârzieri', '3.500 fiecare'],
    ['19. Observații pentru succesul proiectului', 'Descriere', '10.500'],
], widths=[6.3, 7.2, 3.5])
SMALL('Sursa: capturile de ecran din Manualul de utilizare MySMIS2021 FO – Raport de progres (contorul „Caractere rămase: x/10500” sau „x/3500”). '
      'Textele de mai jos rămân sub 95% din limită, pentru că editorul MySMIS poate număra și formatarea (liste, aldine).')

H2('A4. Ce trebuie rezolvat ÎNAINTE de transmiterea RP 1 (blocante)')
SMALL('Fiecare punct de mai jos poate genera clarificări sau tăieri la verificare. Ordinea este în funcție de impact.')
TBL([
    ['Nr.', 'Problema constatată în documente', 'Ce trebuie făcut / decizia necesară'],
    ['1', '**Grupul țintă nu este introdus în MySMIS2021** (0 participanți în foaia „Stare elevi”), deși registrul de la 04.10.2026 are 96 de elevi cu dată de intrare în operațiune; '
          'doar 24 de formulare de înregistrare (FIP) sunt semnate (17 în folderul GT).',
     'Indicatorii se raportează numai pentru participanții înregistrați în MySMIS, cu formularul generat din sistem și semnat (MB §4.1.2) și asociați la RP 1. '
     'Toate cifrele «...» din secțiunile 4, 5 și 17 se aliniază la numărul real de participanți asociați.'],
    ['2', '**Nu există Raportul de selecție și validare (Anexa 11 la metodologia GT)**, obligatoriu pentru validare; activitățile cu elevii au început la 15.09.2026.',
     'Emiterea rapoartelor de selecție (provizoriu/final) pe școli și serii, datate, avizate MP; data intrării în operațiune = prima activitate.'],
    ['3', '**Vizibilitate – ce există și ce lipsește.** Există: subpagina proiectului pe site (https://napocaporolissum.ro/unic-porolissum-2/, creată la 02.07.2026, actualizată la 30.07.2026), '
          'cu anunțul de începere a proiectului și cele două metodologii publicate la 16.07.2026; pagina de Facebook „UNIC: Viitor prin Educație” (588 de urmăritori). '
          'Lipsesc din Drive: fotografiile afișului A3 la sediu și în școli, dovada autocolantelor pe echipamentele IT, lista și capturile postărilor de pe Facebook '
          '(Facebook nu a putut fi citit automat – cere autentificare).',
     'Capturi de ecran cu data și URL pentru subpagină și pentru fiecare postare de pe Facebook din iul.–sept.; fotografiile afișelor și autocolantelor. '
     'Pe subpagină de corectat: „Cofinanțare UE: … intensitate 100%” → valoarea cofinanțării UE (5.879.540,52 lei FSE+, 85%); „acordarea de subvenții” → masă caldă (după AA1).'],
    ['4', '**Documente de resurse umane lipsă:** RA (Anexa 10) septembrie – Expert GT 1; RA + pontaj septembrie – Facilitator comunitar 2 (folder gol); '
          'pontajele RF iulie–august (Dumitrescu); pontajele MP doar ca Google Sheet, nesemnate.',
     'Completare și semnare. Fără ele, experții nu pot fi trecuți la pct. 12 și în Anexa 13 (care trebuie să fie identice).'],
    ['5', '**Pontajul MP din septembrie arată 8 h/zi în UNIC** și ore în proiectul PIDS 329335; bugetul UNIC este de 93 h/lună pentru MP.',
     'Pontajul trebuie să reflecte orele efective în limita bugetului și maximum 12 h/zi și 60 h/săptămână, cumulat PEO+PIDS (Anexa 8).'],
    ['6', '**Procedurile, planurile și metodologiile V2 nu sunt semnate/datate** (Elaborat/Avizat/Aprobat necompletate; metodologia GT V2 „__/__/2026”); '
          'CF cere planurile „finalizate până la finalul lunii 3”.',
     'Semnare (avizare MP, aprobare reprezentant legal) și trecerea în raport a datei reale.'],
    ['7', '**Minutele ședințelor din 18.09 (online) și 25.09.2026 (fizic)** lipsesc (folderul „6. Întâlniri/3. Septembrie” este gol).',
     'Minute + liste de prezență/capturi. Altfel, rezultatul 2 = 3 întâlniri, nu 5.'],
    ['8', '**Dosare de personal lipsă** pentru Cadrele didactice 1–3 și Responsabilul financiar Fekete; Facilitatorul comunitar 1 (Sotnic, aprobat prin N1) nu are nicio activitate documentată.',
     'Completare dosare. Pentru FC1: confirmați dacă a fost angajat; în RP se explică lipsa activității (OM verifică experții notificați).'],
    ['9', '**Neconcordanțe de cifre** între rapoartele de activitate și registru (fizică 20 vs. 26 elevi la 22.09; română LTR 20 vs. 18 la 30.09; consiliere 16 vs. 17 elevi); '
           '8 CNP-uri invalide și date imposibile în registru (ex. 30.09.3036).',
     'O singură sursă de cifre (registrul corectat), folosită identic în secțiunile 4, 5, 12, 15, 17 și în anexe.'],
    ['10', '**Liceul Tehnologic Energetic Cluj-Napoca** – întâlnire 28.09, fără acord de colaborare.',
     'Elevii unei școli se înscriu în GT numai după acordul de colaborare (GSCS §5.1.4, Anexa 7).'],
], widths=[0.8, 8.0, 8.2])

H2('A5. Alte aspecte la care atrag atenția')
BUL([
    '**Notificarea nr. 4 – aprobată** prin Informarea OIR PECU Nord-Vest nr. 17371/17.09.2026. Cadrul didactic 3 are CIM din aceeași zi (17.09.2026), deci activitatea ei '
    'din septembrie este acoperită de aprobare. Versiunea de proiect pentru RP 1 este 12.',
    '**Cadrele didactice formate (GT, SA5.2) sunt aceleași cu Cadrele didactice 1–4 ale echipei** (Tiron, Pleșoiu, Anderco, Arkosi). Nu am găsit nicio interdicție în GSCS 8.F, '
    'GSCG sau Manualul beneficiarului. Metodologia GT V2 (§20 și §24) cere doar ca ei să fie **evidențiați distinct** ca participanți GT față de resursele umane și prevede chiar '
    'că „Cadrele didactice contractate ulterior pentru activități remediale se evidențiază separat ca resursă umană”. De verificat: (a) dosar GT complet pentru fiecare '
    '(Anexele 2, 4, 7, 9 + adeverință de angajat ÎPT); (b) orele de curs din 10–18.09 să **nu** fie pontate ca ore lucrate în proiect (altfel aceeași oră ar fi plătită ca salariu '
    'și ar fi și formare GT); (c) prin acțiunea 8.f.1 se raportează și ei.',
    '**Numele programului:** peste tot „Programul Educație și Ocupare 2021-2027 (PEO)”. Cererea de finanțare menționează eronat „Programul Incluziune și Demnitate Socială” '
    'la descrierea anunțului de demarare – nu se preia în materiale.',
    '**Metodologia GT V2** menționează încă subvenția echivalentă bursei sociale (eliminată prin AA1) și perioada „24.07.2026 – 30.06.2029” (corect: 01.07.2026). Se corectează.',
    '**Ponderi urmărite cumulat la fiecare RP:** min. 70% elevi de clasa a IX-a la A5 (8.f.3); min. 50% elevi din clasele VII–VIII la A4 (8.f.2); min. 81 de elevi romi; '
    'procentul de elevi vulnerabili asumat în CF. Registrul nu are încă o coloană de etnie/vulnerabilitate completată pentru toți – trebuie introdusă.',
    '**Numărarea pe acțiuni (GSCS §3.7):** un elev poate fi înregistrat de 1–3 ori (câte un formular pentru fiecare acțiune 8.f.1/8.f.2/8.f.3). În raport se dau și înregistrările '
    'pe acțiune, și numărul de elevi unici. Interpretarea țintei (444 minim în ghid / 500 în CF – persoane sau înregistrări) se confirmă cu OM.',
    '**Planul de monitorizare (Anexa 2)** are termenul „30.06.2026” la indicatorul de etapă pentru părinți (eroare materială – înaintea începerii proiectului). Se explică la pct. 17 '
    'și se corectează la prima notificare. Tot ca erori materiale: CR 11 datată 24.04.2028 (după CR 10 din 2029); „14” vs. „13” dosare de personal în CF.',
    '**Responsabil financiar:** în iulie–august, poziția a fost ocupată de reprezentantul legal (Dumitrescu Marius-Gheorghe), care semna și contractele de achiziție; '
    'situația a fost rezolvată prin N3. Pontajele lui din iul.–aug. sunt necesare pentru CR 1.',
    '**Garanția echipamentelor IT:** procedura de achiziții UNIC-PO-04 cere minim 24 de luni, iar contractul dă 12 luni pentru 3 din 4 tipuri de produse – de verificat înaintea CR 1.',
    '**Fișa postului consilierului psihologic** (anexată la Anexa 10) conține cerințe dintr-un alt proiect („psihologia vârstei a treia”) – se înlocuiește.',
    '**Anexa 4 GSCG** (membri de familie) se depune cu primul RP în care se raportează activitatea acestora – de verificat dacă există relații de rudenie în echipă/GT.',
    '**Copii ale RP** se transmit partenerilor asociați (Anexa 7, art. 6) – CT Turda, LT „Vlădeasa” Huedin, LT Reformat Cluj-Napoca.',
])

# =====================================================================================
# PARTEA B – TEXTUL RAPORTULUI
# =====================================================================================
PAGEBREAK()
H1('Partea B – Textul Raportului de progres nr. 1, pe câmpurile MySMIS2021')
SMALL('Antet (completat automat): Raport de progres nr. 1 · Tip: Periodic · Contract 11205/16.06.2026 · Cod SMIS 352704 · Versiune proiect: 12 · '
      'Perioada de implementare 01.07.2026 – 30.06.2029 · Perioada de raportare 01.07.2026 – 30.09.2026. De verificat înainte de completare.')

# ------------------------------------------------------------------------------ 1
SECT('1. Rezumatul proiectului')
def SECTIUNE(nume):
    """Textul unei secțiuni redactate separat, din folderul sectiuni/."""
    with open(os.path.join(HERE, 'sectiuni', nume), encoding='utf-8') as fh:
        return fh.read()


def SECTIUNE_CAMPURI(nume):
    """Fișier cu mai multe câmpuri, separate prin linii '=== Eticheta'."""
    out = []
    for blk in re.split(r'^=== ', SECTIUNE(nume), flags=re.M)[1:]:
        label, _, text = blk.partition('\n')
        out.append((label.strip(), text.strip()))
    return out


FIELD('Rezumat proiect', L_LUNG, SECTIUNE('01_rezumat.txt'), note='Dacă MySMIS preia automat rezumatul din cererea de finanțare, se verifică doar corectitudinea și se lasă textul preluat. '
      'Varianta de mai sus este redactată pentru câmpul editabil (versiunea din 06.10.2026).')

# ------------------------------------------------------------------------------ 2
SECT('2. Modificări ale contractului / deciziei de finanțare')
SMALL('Rândurile (tip, dată semnare, versiune proiect) sunt aduse automat din modulul Contractare; se completează doar câmpul „Descriere” (3.500 de caractere) pentru fiecare rând.')
for _lab, _txt in SECTIUNE_CAMPURI('02_modificari_contract.txt'):
    FIELD(_lab, L_SCURT, _txt)

# ------------------------------------------------------------------------------ 3
SECT('3. Calendar de raportare')
FIELD('RP 1 – Observații', L_SCURT, '''
Perioada de raportare: iulie – septembrie 2026 (L1–L3; 01.07.2026 – 30.09.2026).
''')

# ------------------------------------------------------------------------------ 4
SECT('4. Activități implementate și rezultate obținute. Abateri')
SMALL('Ordinea din MySMIS: A1 (SA1.1), A2 (SA2.1), A3 (SA3.1) – activități suport; A4 (SA4.1, SA4.2) și A5 (SA5.1–SA5.4) – activități de bază. '
      'Pentru fiecare subactivitate se completează trei câmpuri: Rezultat obținut (3.500), Abateri/riscuri (10.500), Progres (10.500).')

H3('SA1.1 – Management de proiect, monitorizare și raportare')
for _lab, _txt in SECTIUNE_CAMPURI('04_SA1.1_management.txt'):
    FIELD(_lab, L_SCURT if 'Rezultat' in _lab else L_LUNG, _txt)
FLAG('Ședința din 25.09.2026: minuta găsită în Drive este a proiectului PIDS („întâlnire de lucru fizic centre”); pentru UNIC există doar 03.07, 16.07, 13.08 și 18.09. '
     'Dacă a existat o ședință UNIC pe 25.09, se adaugă minuta și se trece R2 = 5. Lipsesc din Drive: data aprobării procedurilor/planurilor, Codul de etică/ROI actualizat, '
     'Formularele 11 (reconciliere), data începerii activității Facilitatorului comunitar 1.')

H3('SA2.1 – Organizarea procedurilor de achiziții')
for _lab, _txt in SECTIUNE_CAMPURI('04_SA2.1_achizitii.txt'):
    FIELD(_lab, L_SCURT if 'Rezultat' in _lab else L_LUNG, _txt)
FLAG('PAAP: prima versiune aprobată de reprezentantul legal la 16.06.2026 (în dosarul achiziției auto, „1. PAAP si plan de achizitii.pdf”), actualizată la 09.09.2026 după AA1 – '
     'textul SA2.1 este aliniat la aceste date. Rămâne de confirmat: data înregistrării echipamentelor IT în evidența contabilă și inscripționarea lor cu elementele de identitate vizuală '
     '(fotografii) – placeholder galben în Progres SA2.1. Recepția serviciilor de formare se face după evaluarea din 09.10.2026 (în afara perioadei de raportare).')

H3('SA3.1 – Derularea activităților de informare și publicitate')
FIELD('SA3.1 – Rezultat obținut în perioada de raportare', L_SCURT, '''
R8: materiale publicitare realizate și distribuite – afișul A3 al proiectului, flyerul de prezentare pentru școli (față-verso) și flyerul de 12 × 17 cm.
R9: 1 anunț de începere a proiectului publicat pe subpagina proiectului de pe site-ul beneficiarului (https://napocaporolissum.ro/unic-porolissum-2/).
R10: promovarea proiectului pe site-ul beneficiarului (subpagina proiectului, creată la 02.07.2026) și pe pagina de Facebook a proiectului „UNIC: Viitor prin Educație” (https://www.facebook.com/unic.viitorprineducatie) realizată.
''')
FIELD('SA3.1 – Abateri/riscuri identificate', L_LUNG, '''
Nu au fost identificate abateri.
''')
FIELD('SA3.1 – Progres în perioada de raportare', L_LUNG, '''
În perioada de raportare iulie – septembrie 2026, SA3.1 a vizat asigurarea vizibilității proiectului și a sprijinului acordat din Fondul Social European Plus prin Programul Educație și Ocupare 2021-2027 încă de la debutul implementării, cu respectarea Manualului de identitate vizuală 2021-2027 și a Anexei 18 la Manualul beneficiarului.
La începutul lunii iulie 2026 (02.07.2026), pe site-ul beneficiarului a fost creată subpagina dedicată proiectului (https://napocaporolissum.ro/unic-porolissum-2/), în secțiunea „Programe – PEO – Programul Educație și Ocupare”. Subpagina prezintă denumirea proiectului, beneficiarul, codul MySMIS 352704, perioada de implementare, valoarea totală, sursa de finanțare, descrierea și obiectivele, grupul țintă și rezultatele așteptate, precum și trimiterea către www.mfe.gov.ro.
Pe subpagină a fost publicat anunțul de începere a proiectului, care cuprinde beneficiarul, titlul și codul MySMIS, programul (Programul Educație și Ocupare 2021-2027, Prioritatea P8) și fondul (FSE+), perioada de implementare (iulie 2026 – iunie 2029), regiunea, valoarea totală, scopul, activitățile, grupul țintă, rezultatele urmărite și datele de contact. Dovada publicării (captură de ecran cu data și adresa URL) a fost arhivată.
La 16.07.2026 au fost publicate pe aceeași subpagină Metodologia privind identificarea, recrutarea, înscrierea, verificarea, selectarea, validarea și menținerea grupului țintă și Metodologia privind acordarea sprijinului financiar pentru transport, cazare și masă, asigurând accesul egal la informație al tuturor persoanelor interesate.
Proiectul este promovat și pe pagina de Facebook „UNIC: Viitor prin Educație” (https://www.facebook.com/unic.viitorprineducatie), pe care au fost publicate, în perioada de raportare, «… postări» despre activitățile proiectului «(întâlnirile de informare din școli, debutul activităților cu elevii din septembrie …)».
În luna iulie 2026 au fost realizate materialele de informare pentru unitățile de învățământ: afișul A3 al proiectului, flyerul de prezentare față-verso destinat școlilor și flyerul de 12 × 17 cm. Materialele au fost utilizate în întâlnirile de informare și recrutare de la Colegiul Tehnic Turda (07.07 și 24.07.2026) și de la Liceul Tehnologic „Vlădeasa” Huedin (09.07.2026) și, în septembrie 2026, la Liceul Teologic Reformat Cluj-Napoca. Afișul A3 a fost expus la sediul beneficiarului din Gilău și «la unitățile de învățământ partenere în care se desfășoară activitățile», fiind realizate fotografii ca dovadă.
Toate documentele utilizate în relația cu grupul țintă (formulare, liste de prezență, fișe de lucru, teste de evaluare) au inclus elementele obligatorii de identitate vizuală și mențiunea privind cofinanțarea din Fondul Social European Plus prin Programul Educație și Ocupare 2021-2027. La înscriere, participanții au fost informați, prin nota de informare privind activitățile proiectului, cu privire la sprijinul acordat prin FSE+. Echipamentele IT recepționate la 18.09.2026 au fost «inscripționate cu autocolante care conțin elementele de identitate vizuală».
Activitatea este documentată prin materialele realizate, link-urile și capturile de ecran ale publicărilor și fotografiile afișelor expuse, centralizate în documentul „SA 3.1_07-09.2026_Informare și publicitate”.
''', note='Facebook nu a putut fi citit automat. Se completează numărul postărilor pe luni și temele lor din pagina proiectului și se atașează capturile. '
          'Afișul A3 și autocolantele IT se păstrează în text numai dacă există fotografii.')

H3('SA4.1 – Metodologia de selecție a GT; recrutarea GT; gestionarea dosarelor GT')
FIELD('SA4.1 – Rezultat obținut în perioada de raportare', L_SCURT, '''
R12: 1 metodologie de selecție a grupului țintă întocmită (versiunea 1 – 16.07.2026, actualizată în versiunea 2 – septembrie 2026) și diseminată, împreună cu cele 15 anexe-formular.
R13: «128» de elevi cu dosare de înscriere eligibile, dintre care «96» de elevi selectați și intrați în operațiune («17» pe acțiunea 8.f.1, «35» pe acțiunea 8.f.2 și «44» pe acțiunea 8.f.3); «4» cadre didactice selectate pentru participarea la formare; 0 părinți selectați în perioada de raportare.
''', note='Cifrele din R13 = registrul GT din 04.10.2026. Se înlocuiesc cu numărul real de participanți înregistrați în MySMIS și asociați la RP 1 (vezi A4 pct. 1–2). '
          'Cadrele didactice se trec numai dacă au dosar GT complet și formular de înregistrare (vezi A5).')
FIELD('SA4.1 – Abateri/riscuri identificate', L_LUNG, '''
Risc identificat: numărul elevilor eligibili care și-au exprimat acordul de participare este mai mic decât estimările inițiale ale unităților de învățământ partenere, întrucât o parte dintre elevi participă la alte proiecte cu finanțare europeană derulate în aceleași școli, iar o parte dintre familii nu au completat documentele necesare sau nu au dorit participarea.
Măsuri: extinderea bazei de recrutare prin acordul de colaborare încheiat la 09.09.2026 cu Liceul Teologic Reformat Cluj-Napoca și prin demersuri pentru implicarea Liceului Tehnologic Energetic Cluj-Napoca; verificarea evitării dublei finanțări împreună cu organizația care derulează alte programe în aceleași școli (întâlnirea din 24.08.2026); sprijin direct acordat familiilor pentru completarea dosarelor, prin deplasări repetate ale experților în școli. Recrutarea este progresivă pe întreaga durată a proiectului (3 serii, corespunzătoare anilor școlari 2026-2027, 2027-2028 și 2028-2029), iar riscul nu afectează, în acest moment, atingerea țintelor.
''')
FIELD('SA4.1 – Progres în perioada de raportare', L_LUNG, '''
În perioada de raportare iulie – septembrie 2026, SA4.1 a vizat elaborarea și diseminarea metodologiei de selecție a grupului țintă, informarea și recrutarea elevilor și părinților din unitățile de învățământ partenere și constituirea și verificarea dosarelor de înscriere.
În luna iulie 2026, experții au desfășurat următoarele activități:
• Expertul GT 1 și Expertul GT 2 au elaborat Metodologia de selecție a grupului țintă (versiunea 1, 16.07.2026), avizată de Managerul de proiect, care stabilește criteriile de eligibilitate și de departajare, procedura de înscriere, lista documentelor, modul de verificare, contestațiile și regulile de protecție a datelor, împreună cu 15 anexe-formular: opis și checklist dosar, formular de înregistrare individuală, acordul părintelui/reprezentantului legal și nota de informare GDPR, declarația de apartenență la grupul țintă și de evitare a dublei finanțări, confirmarea școlară privind riscul educațional (Anexa 5A), formularele pentru părinți și cadre didactice, grila de verificare a eligibilității și de prioritizare (Anexa 9), rapoartele de selecție, formularul de contestație, chestionarul de satisfacție și nota de informare privind activitățile;
• au fost organizate întâlniri de informare și recrutare cu elevi, părinți și cadre didactice la Colegiul Tehnic Turda (07.07 și 24.07.2026) și la Liceul Tehnologic „Vlădeasa” Huedin (09.07.2026), documentate prin minute și liste de prezență; cu conducerile școlilor au fost stabilite modalitățile de colaborare și persoanele de contact;
• au fost constituite primele 24 de dosare de înscriere (Colegiul Tehnic Turda), iar la 27.07.2026 a fost transmisă școlii solicitarea pentru documentele lipsă și pentru confirmările școlare; au fost primite 23 de confirmări școlare (Anexa 5A).
În luna august 2026:
• Expertul GT 1 a studiat modulul de înregistrare a participanților din MySMIS2021 și a completat dosarele din iulie cu documentele primite de la școală;
• la întâlnirea din 21.08.2026 de la Colegiul Tehnic Turda au fost înscriși 6 elevi noi din clasele a VII-a – a VIII-a și au fost precompletate 8 dosare;
• pe baza centralizatoarelor transmise de școli, experții au încadrat elevii identificați pe acțiunile 8.f.1, 8.f.2 și 8.f.3 (SA4.2);
• la 24.08.2026 a avut loc o întâlnire cu reprezentanții unei organizații care derulează programe în aceleași școli, pentru evitarea suprapunerii grupurilor țintă și a dublei finanțări.
În luna septembrie 2026:
• au fost precompletate 70 de dosare pentru elevii de liceu ai Colegiului Tehnic Turda (38 din clasa a IX-a, 21 din clasa a X-a și 11 din clasa a XI-a);
• au fost organizate sesiuni de informare și de colectare a documentelor la Colegiul Tehnic Turda (09.09, 11.09, 21.09 și 24.09.2026), la Liceul Tehnologic „Vlădeasa” Huedin (11.09.2026) și la Liceul Teologic Reformat Cluj-Napoca (16.09.2026 și 18.09.2026 – ședința cu părinții elevilor din clasa a IX-a D); la 28.09.2026 proiectul a fost prezentat la Liceul Tehnologic Energetic Cluj-Napoca;
• metodologia de selecție a fost actualizată (versiunea 2), pentru corelarea cu Actul adițional nr. 1 și cu Notificarea nr. 3 și pentru includerea noului partener asociat;
• au fost scanate și verificate pe grila de eligibilitate (Anexa 9) 66 de dosare, dintre care 45 complete și 21 cu documente lipsă, pentru care familiile au fost contactate în vederea completării;
• au fost semnate «24» de formulare de înregistrare individuală, iar participanții eligibili au fost înregistrați în MySMIS2021 «(n)», data intrării în operațiune fiind data primei activități la care au participat; selecția a fost validată prin «Raportul de selecție și validare nr. … din …».
Situația grupului țintă la 30.09.2026: «128» de elevi cu dosar eligibil, dintre care «96» intrați în operațiune (8.f.1 – «17»; 8.f.2 – «35»; 8.f.3 – «44»).
Activitatea experților este documentată prin rapoartele individuale de activitate, fișele de pontaj, minutele și listele de prezență ale întâlnirilor, dosarele de înscriere și grilele de verificare a eligibilității.
''')

H3('SA4.2 – Identificarea elevilor în risc de abandon școlar sau de părăsire timpurie a școlii')
FIELD('SA4.2 – Rezultat obținut în perioada de raportare', L_SCURT, '''
R14: 32 de elevi aferenți acțiunii 8.f.1 identificați (Colegiul Tehnic Turda, clasele a X-a – a XI-a).
R15: 57 de elevi aferenți acțiunii 8.f.3 identificați (clasa a IX-a: 38 la Colegiul Tehnic Turda și 19 la Liceul Teologic Reformat Cluj-Napoca).
''')
FIELD('SA4.2 – Abateri/riscuri identificate', L_LUNG, '''
Nu au fost identificate abateri.
''')
FIELD('SA4.2 – Progres în perioada de raportare', L_LUNG, '''
În perioada de raportare iulie – septembrie 2026, SA4.2 a vizat identificarea, în colaborare cu unitățile de învățământ partenere, a elevilor în risc de abandon școlar sau de părăsire timpurie a școlii și/sau a elevilor din grupuri ori medii defavorizate care necesită sprijin.
În lunile iulie și august 2026, Experții GT au solicitat școlilor partenere, prin diriginți și conducerea unităților, informații privind situația elevilor: frecvența, rezultatele școlare, situațiile de corigență și absenteism, situația socio-economică și familială. În perioada 20–25.08.2026 au fost primite centralizatoarele de la Colegiul Tehnic Turda și de la Liceul Tehnologic „Vlădeasa” Huedin, pe baza cărora au fost identificați 150 de elevi: 32 pentru acțiunea 8.f.1 (clasele a X-a – a XI-a, Colegiul Tehnic Turda), 80 pentru acțiunea 8.f.2 (clasele a VII-a – a VIII-a: 30 la Colegiul Tehnic Turda și 50 la Liceul Tehnologic „Vlădeasa” Huedin) și 38 pentru acțiunea 8.f.3 (clasa a IX-a, Colegiul Tehnic Turda). Experții au întocmit baza de date a elevilor identificați, cu încadrarea pe acțiuni și pe criteriile de vulnerabilitate: nevoia de sprijin remedial, dificultăți la competențele de bază, proveniența din medii defavorizate, familii vulnerabile, rezultate școlare slabe.
În luna septembrie 2026, după încheierea acordului de colaborare cu Liceul Teologic Reformat Cluj-Napoca (09.09.2026), au fost identificați încă 19 elevi din clasa a IX-a D (acțiunea 8.f.3), pentru care școala a transmis situația clasei și confirmările școlare (Anexa 5A, 23.09.2026).
Pentru fiecare elev identificat, nevoia de sprijin a fost confirmată de diriginte și de directorul unității de învățământ prin confirmarea școlară (Anexa 5A). La începutul programelor remediale, cadrele didactice au aplicat teste de evaluare inițială, ale căror rezultate fundamentează planificarea sprijinului pe grupe și individual. «Pentru elevii identificați ca fiind în risc au fost completate fișele de observare și de evaluare din Mecanismul de Avertizare Timpurie în Educație (MATE).»
Total elevi identificați la 30.09.2026: 169 (32 pentru acțiunea 8.f.1, 80 pentru acțiunea 8.f.2 și 57 pentru acțiunea 8.f.3).
Activitatea este documentată prin centralizatoarele transmise de școli, baza de date a elevilor identificați, confirmările școlare, rapoartele de activitate și fișele de pontaj ale experților.
''', note='Fraza despre MATE se păstrează numai dacă fișele MATE există (în baza de date coloana „MATE existent” este goală). CF prevede ca instrumente MATE, SASAT și „Raportul de evaluare a potențialului de a finaliza anul școlar”.')

H3('SA5.1 – Măsuri de facilitare a accesului și de prevenire a părăsirii timpurii a școlii (8.f.1)')
FIELD('SA5.1 – Rezultat obținut în perioada de raportare', L_SCURT, '''
R16: «17» elevi din acțiunea 8.f.1 au beneficiat de sprijin psihologic individual și de grup în perioada 16–30.09.2026. Sprijinul financiar pentru cazare, masă și transport urmează să fie acordat, în funcție de nevoia identificată, după validarea grupului țintă și evaluarea cererilor, începând cu luna «octombrie 2026».
''')
FIELD('SA5.1 – Abateri/riscuri identificate', L_LUNG, '''
Nu au fost identificate abateri.
''')
FIELD('SA5.1 – Progres în perioada de raportare', L_LUNG, '''
SA5.1 a început în luna septembrie 2026 (L3), conform graficului din cererea de finanțare. În perioada de raportare activitatea a vizat planificarea măsurilor de sprijin și debutul sprijinului psihologic pentru elevii din acțiunea 8.f.1.
Planificarea activităților. Metodologia de acordare a sprijinului financiar, a subvențiilor și a sprijinului personalizat, elaborată de Experții GT (versiunea 1, 16.07.2026), a fost actualizată în septembrie 2026 (versiunea 2), în corelare cu Notificarea nr. 3: sprijinul financiar de 500 lei/lună pentru cazare, masă și transport se acordă, pe o durată de maximum 10 luni, elevilor pentru care nevoia este identificată și justificată, fiecare elev din grupul țintă al acțiunii 8.f.1 beneficiind de cel puțin o formă de sprijin. Metodologia stabilește criteriile de acordare, echipa de evaluare, modelele de cerere, contract, fișă de monitorizare lunară și borderou, precum și condiționarea sprijinului de frecvența regulată, de rezultatele școlare și de participarea la activitățile proiectului. Metodologia a fost validată de Managerul de proiect «la data de …».
Sprijin psihologic. În perioada 16–30.09.2026, Consilierul psihologic a realizat 10 deplasări la Colegiul Tehnic Turda și la structura Școala Profesională Poiana Turda, în cadrul cărora a lucrat cu «17» elevi din clasele a X-a – a XI-a (acțiunea 8.f.1), în activități individuale și de grup: ateliere de cunoaștere și intercunoaștere, explorarea motivației școlare, autocunoaștere și planificarea traseului educațional. Au fost aplicate 13 chestionare de motivație școlară și 11 fișe de autocunoaștere („Blazonul meu”) și au fost utilizate instrumente de lucru adaptate vârstei („Rucsacul psihologului”, „Harta traseelor vieții”). Pentru fiecare elev a fost întocmit un raport individual de activitate (fișă de observație, listă de prezență, fișe de lucru), care stă la baza planului individual de sprijin.
Sprijin financiar. În perioada de raportare nu au fost acordate sume, întrucât, conform metodologiei, contractele de acordare se încheie după validarea grupului țintă și evaluarea cererilor depuse de elevi sau de reprezentanții lor legali. Procedura de contactare și de depunere a cererilor urmează să fie lansată în luna «octombrie 2026».
Activitatea este documentată prin raportul de activitate și fișa de pontaj ale Consilierului psihologic, rapoartele individuale ale elevilor, listele de prezență, fișele de lucru și fotografiile realizate cu acordul reprezentanților legali.
''', note='Cifra elevilor: raportul de activitate spune 16, registrul și dosarele copiilor 17 – se aliniază înainte de transmitere.')

H3('SA5.2 – Formarea personalului didactic din ÎPT, inclusiv dual (8.f.1)')
FIELD('SA5.2 – Rezultat obținut în perioada de raportare', L_SCURT, '''
R17: 4 cadre didactice din unitățile de învățământ partenere asociate au parcurs, în perioada 10–18.09.2026, programul de formare acreditat (30 de ore); evaluarea finală și eliberarea certificatelor sunt programate la 09.10.2026, în perioada următoare de raportare.
''')
FIELD('SA5.2 – Abateri/riscuri identificate', L_LUNG, '''
Nu au fost identificate abateri.
''')
FIELD('SA5.2 – Progres în perioada de raportare', L_LUNG, '''
SA5.2 a început în luna septembrie 2026 (L3). Conform Notificării nr. 3, formarea s-a desfășurat în paralel cu debutul programelor remediale din SA5.4.
În lunile august – septembrie 2026, Experții GT au identificat, împreună cu conducerile unităților de învățământ partenere, cadrele didactice din ÎPT care lucrează direct cu elevii din grupul țintă și au constituit grupa de formare de 4 cadre didactice. Furnizorul a fost selectat prin procedura descrisă în SA2.1.
Programul „Abilitare informațională în combaterea abandonului școlar: un ghid pentru cadre didactice”, acreditat prin OM nr. 1555/30.06.2025, a fost furnizat de Asociația Proeuro-Cons în perioada 10–18.09.2026, în format online, cu 12 ore de activități sincrone și 18 ore de activități asincrone. Tematica a vizat identificarea timpurie a riscului de abandon școlar, comunicarea eficientă cu elevii aflați în risc educațional, strategii de motivare și de menținere a elevilor în sistemul educațional și utilizarea instrumentelor digitale în procesul didactic și de evaluare. Cursanții au primit suportul de curs și materialele de lucru elaborate de furnizor.
Evaluarea finală a cursanților este programată la 09.10.2026, după care furnizorul va elibera certificatele de absolvire, iar beneficiarul va realiza recepția serviciilor. Rezultatul va fi raportat în Raportul de progres nr. 2.
Activitatea este documentată prin contractul de servicii, ordinul de începere, calendarul formării, dovada acreditării programului, suportul de curs și corespondența cu furnizorul.
''')

H3('SA5.3 – Dezvoltarea de programe de informare și conștientizare (8.f.2)')
FIELD('SA5.3 – Rezultat obținut în perioada de raportare', L_SCURT, '''
R19: «23» de elevi au participat la activitățile campaniei de informare și conștientizare (5 activități, «44» de participări).
R18: activitățile cu părinții/reprezentanții legali urmează să înceapă în luna «octombrie 2026».
''')
FIELD('SA5.3 – Abateri/riscuri identificate', L_LUNG, '''
Risc identificat: implicarea redusă a părinților în activitățile proiectului, determinată de programul de lucru, de distanțele față de școli și, în unele cazuri, de plecarea părinților la muncă în străinătate.
Măsuri: programarea atelierelor pentru părinți în intervale orare convenabile, la sediile școlilor și ale primăriilor din localitățile de domiciliu, invitarea părinților prin diriginți și prin contact direct, precum și includerea persoanelor care au în grijă elevi cu părinți plecați în străinătate, conform cererii de finanțare.
''')
FIELD('SA5.3 – Progres în perioada de raportare', L_LUNG, '''
SA5.3 a început în luna septembrie 2026 (L3). În perioada de raportare activitatea a vizat pregătirea campaniei de informare și conștientizare și primele activități cu elevii din grupul țintă al acțiunii 8.f.2.
Expertul comunicare a aplicat elevilor chestionare privind interesele și percepțiile despre meserii și despre învățământul profesional și tehnic, ca bază pentru Planul de informare și conștientizare, și a realizat afișele și pliantele campaniei. Au fost organizate 5 activități de informare și conștientizare: la Colegiul Tehnic Turda (15.09, 16.09 și 30.09.2026), la Casa de Cultură din Huedin (28.09.2026) și la Primăria Huedin (29.09.2026), la care au participat «23» de elevi, cu «44» de participări. Au fost utilizate metode interactive adaptate vârstei: jocul de intercunoaștere „Găsește pe cineva care…”, chestionarul de interese, exercițiul „Mesaj pentru mine peste 5 ani” (înregistrări audio realizate cu acordul reprezentanților legali) și discuții despre traseele educaționale și profesionale.
Facilitatorul comunitar 2 a organizat ateliere cu elevii la Colegiul Tehnic Turda (15.09.2026) și la Primăria Huedin (24.09.2026), «cu … participanți», și a început contactarea părinților elevilor din grupul țintă, în vederea organizării atelierelor pentru părinți începând cu luna octombrie 2026.
«Facilitatorul comunitar 1 nu a desfășurat activități în perioada de raportare; …»
Activitatea este documentată prin rapoartele de activitate, fișele de pontaj, listele de prezență, chestionarele aplicate, materialele campaniei și fotografiile realizate.
''', note='Facilitatorul comunitar 2 nu are încă raport de activitate și pontaj pentru septembrie, iar Facilitatorul comunitar 1 nu are niciun document. Fără ele, paragrafele respective se scot '
          'sau se explică absența (OM verifică experții notificați).')

H3('SA5.4 – Dezvoltarea și furnizarea de programe remediale (8.f.3)')
FIELD('SA5.4 – Rezultat obținut în perioada de raportare', L_SCURT, '''
R20: «44» de elevi din acțiunea 8.f.3 au participat la programele remediale în perioada 17–30.09.2026 (limba și literatura română și fizică la Colegiul Tehnic Turda; limba și literatura română la Liceul Teologic Reformat Cluj-Napoca).
R21: masa caldă urmează să fie acordată după finalizarea achiziției de servicii (L4–L5).
''')
FIELD('SA5.4 – Abateri/riscuri identificate', L_LUNG, '''
Nu au fost identificate abateri.
''')
FIELD('SA5.4 – Progres în perioada de raportare', L_LUNG, '''
SA5.4 a început în luna septembrie 2026 (L3), conform graficului din cererea de finanțare. În perioada de raportare activitatea a vizat elaborarea metodologiilor de organizare a activităților remediale, evaluarea inițială a elevilor și primele sesiuni remediale.
Cadrul didactic 1 a elaborat metodologia de organizare a activităților remediale la limba și literatura română pentru Colegiul Tehnic Turda (10.09.2026), cu structura tematică, instrumentele de evaluare și calendarul sesiunilor (2 grupe de câte 19 elevi din clasa a IX-a, câte 2 ore pe săptămână, în afara programului școlar), a aplicat testele de evaluare inițială celor două grupe și a susținut sesiunile remediale din 17.09.2026 (14 elevi) și 21.09.2026 (12 elevi), axate pe înțelegerea textului și exprimarea scrisă.
Cadrul didactic 2 a elaborat metodologia activităților remediale la fizică pentru Colegiul Tehnic Turda și testul inițial pentru clasa a IX-a, a aplicat 20 de teste de evaluare inițială și a susținut sesiunile din 22.09.2026 («20» de elevi) și 29.09.2026 (14 elevi), axate pe noțiunile de bază, calcul și rezolvarea de probleme.
Cadrul didactic 3 a elaborat metodologia activităților remediale la limba și literatura română pentru clasa a IX-a D a Liceului Teologic Reformat Cluj-Napoca (23 de elevi înscriși), testul inițial, baremul și grila de evaluare și a susținut prima sesiune remedială la 30.09.2026 («20» de elevi prezenți), stabilind planificarea pentru luna octombrie.
Metodologiile au fost validate de Managerul de proiect «la data de …». Rezultatele testelor inițiale fundamentează planificarea pe grupe și fișele individuale de progres, care vor fi actualizate după testele intermediare. În total, în perioada de raportare, «44» de elevi unici din clasa a IX-a au participat la cel puțin o sesiune remedială.
Echipa de implementare. Poziția de Cadru didactic 3 este ocupată, începând cu 17.09.2026, de persoana nominalizată prin Notificarea nr. 4, aprobată prin Informarea OIR PECU Nord-Vest nr. 17371/17.09.2026. Persoanele nominalizate prin Notificarea nr. 2 pe pozițiile de Cadru didactic 2 și Cadru didactic 3 nu au desfășurat activități în proiect, fiind înlocuite prin Notificările nr. 3 și nr. 4. Poziția de Cadru didactic 4 nu a fost ocupată în perioada de raportare, urmând să fie nominalizată prin notificare.
Masa caldă pentru elevii participanți la programele remediale va fi acordată după finalizarea achiziției de servicii (SA2.1), pe baza listelor de prezență la sesiunile remediale.
Activitatea este documentată prin rapoartele de activitate și fișele de pontaj ale cadrelor didactice, metodologiile elaborate, testele de evaluare inițială, listele de prezență și fotografiile realizate.
''', note='Cifrele pe sesiuni diferă între RA și registru (fizică 20/26 la 22.09; LTR 20/18 la 30.09). Totalul de elevi unici (44) = F3 intrați în operațiune în registru – se recalculează din listele de prezență. '
          'Cadrul didactic 3: N4 aprobată la 17.09.2026, aceeași zi cu începutul contractului de muncă.')

# ------------------------------------------------------------------------------ 5
SECT('5. Indicatori')
SMALL('Valoarea din perioadă se introduce numeric; MySMIS calculează cumulul. Pentru fiecare participant raportat se atașează un dosar PDF (vezi Partea C).')
FIELD('5.1.1 EECO06+07 „Copii și tineri” – Informații valoare raportată (valoare în perioadă: «96»)', L_PRESUPUS, '''
În perioada de raportare iulie – septembrie 2026, «96» de elevi au intrat în operațiune, după verificarea eligibilității și semnarea formularului de înregistrare individuală, astfel:
• acțiunea 8.f.1 – «17» elevi din clasele a X-a – a XI-a ai Colegiului Tehnic Turda (inclusiv structura Școala Profesională Poiana Turda), care au beneficiat de sprijin psihologic individual și de grup în cadrul SA5.1;
• acțiunea 8.f.2 – «35» de elevi, dintre care «…» din clasele a VII-a – a VIII-a, de la Colegiul Tehnic Turda și Liceul Tehnologic „Vlădeasa” Huedin, care au participat la activitățile de informare și conștientizare din cadrul SA5.3;
• acțiunea 8.f.3 – «44» de elevi din clasa a IX-a de la Colegiul Tehnic Turda și Liceul Teologic Reformat Cluj-Napoca, care au participat la programele remediale din cadrul SA5.4.
Data intrării în operațiune este data primei activități la care a participat elevul. Conform GSCS, un elev poate fi înregistrat pentru una, două sau trei acțiuni, cu câte un formular de înregistrare pentru fiecare acțiune; cele «96» de înregistrări corespund unui număr de «…» elevi unici. Pentru fiecare participant este atașat dosarul individual (formular de înregistrare generat din MySMIS2021 și semnat, acordul reprezentantului legal și nota de informare privind prelucrarea datelor, declarația privind evitarea dublei finanțări, confirmarea școlară, documentele de identitate, grila de verificare a eligibilității).
''', note='Valoarea = numărul de participanți înregistrați în MySMIS și asociați la RP 1 (A4 pct. 1). Ponderea VII–VIII în 8.f.2 trebuie să fie ≥ 50% cumulat, iar a clasei a IX-a în 8.f.3 ≥ 70%.')
FIELD('5.1.1 5SO14 „Părinți/reprezentanți legali/tutori sprijiniți” – Informații valoare raportată (valoare în perioadă: 0)', L_PRESUPUS, '''
Indicatorul nu a înregistrat progres în perioada de raportare. Atelierele pentru părinți din cadrul SA5.3 încep în luna octombrie 2026, după constituirea grupului țintă de elevi pentru acțiunea 8.f.2.
''')
FIELD('5.1.2 5SR09 „Participanți rămași în sistemul de educație sau care și-au îmbunătățit nivelul de educație” – Informații valoare raportată (valoare în perioadă: 0)', L_PRESUPUS, '''
Indicatorul de rezultat se raportează la ieșirea participanților din operațiune, pe baza secțiunilor B și C ale formularului de înregistrare. În perioada de raportare nu au existat ieșiri din operațiune.
''')

# ------------------------------------------------------------------------------ 7
SECT('7. Graficul de achiziții și stadiul derulării procedurilor')
SMALL('Liniile planului de achiziții sunt aduse automat din cererea de finanțare; pentru fiecare se completează „Stadiu” (3.500 de caractere) și se selectează „Etapa achiziție”.')
for _lab, _txt in SECTIUNE_CAMPURI('07_achizitii.txt'):
    FIELD(_lab, L_SCURT, _txt)
FLAG('Masa caldă: în Drive nu există documente de achiziție. Târgul: nu a fost demarat. Ambele sunt raportate transparent ca „Procedură în pregătire”, cu termenul de lansare în octombrie 2026 – '
     'dacă lansarea întârzie peste L4/L5, perioada din planul de achiziții trebuie actualizată prin notificare înainte de RP 2.')

# ------------------------------------------------------------------------------ 8
SECT('8. Informații privind contractele de achiziții semnate')
SMALL('8.1 – datele contractelor (număr, dată, valori, durată, ofertanți) sunt aduse din modulul Achiziții; se completează „Descriere”. 8.2 – actele adiționale la contractele de achiziție, cu „Descriere”.')
for _lab, _txt in SECTIUNE_CAMPURI('08_contracte_semnate.txt'):
    FIELD(_lab, L_PRESUPUS, _txt)
FLAG('Rândul 8.2 din MySMIS = Decizia de încetare nr. 2026090903/09.09.2026, înregistrată ca act adițional nr. 1 (cod 1224492) la contractul 2026081703. În MySMIS, „Dată semnare” apare 17-08-2026 '
     '(data contractului); dacă câmpul este editabil, se corectează la 09.09.2026, data deciziei.')

# ------------------------------------------------------------------------------ 9
SECT('9. Avize, recepții și execuția contractelor; dificultăți și întârzieri')
FIELD('9.1 Avize, acorduri, autorizații, recepții și execuție contracte de achiziție', L_LUNG, '''
În perioada de raportare au fost verificate documentele de predare-primire și recepție aferente contractelor în derulare:
1. Furnizare echipamente IT – ANILEX SOFT SRL (Contractul nr. 2026091504/15.09.2026). Echipamentele au fost livrate și recepționate cantitativ și calitativ la 18.09.2026, pe baza notei de comandă din 15.09.2026, a procesului-verbal de predare-primire-recepție și a facturii ASF 080/18.09.2026: 3 laptopuri HP Envy 17, 1 laptop Acer Nitro V15, 2 desktopuri ZMEU MAX și 2 multifuncționale Epson WorkForce Pro EM-C8100. Plata a fost efectuată la 18.09.2026. Echipamentele «au fost înregistrate în evidența contabilă a beneficiarului și repartizate …» și sunt utilizate pentru activitățile remediale, consiliere și activitatea echipei de proiect.
2. Închiriere autoturism – Vera Travel SRL (Contractul nr. 2026080603/06.08.2026). Autoturismul a fost predat la 03.09.2026, prin proces-verbal de predare-primire, la data ordinului de începere. Serviciile aferente lunii septembrie 2026 «au fost recepționate pe baza facturii nr. … și a foilor de parcurs», utilizarea autoturismului fiind corelată cu deplasările la unitățile de învățământ partenere.
3. Servicii de formare a cadrelor didactice – Asociația Proeuro-Cons (Contractul nr. 2026082804/28.08.2026). Formarea s-a desfășurat în perioada 10–18.09.2026; recepția serviciilor se va realiza după evaluarea finală din 09.10.2026 și eliberarea certificatelor, în perioada următoare de raportare.
În perioada de raportare nu au fost necesare avize, acorduri sau autorizații.
''')
FIELD('9.2 Dificultăți întâmpinate și întârzieri', L_LUNG, '''
Contractul de furnizare a echipamentelor IT nr. 2026081703/17.08.2026 a încetat prin acordul părților la 09.09.2026, deoarece furnizorul nu mai putea livra modelul de laptop ofertat. Procedura a fost reluată imediat, iar echipamentele au fost livrate și recepționate la 18.09.2026, în perioada planificată (L2–L3), fără impact asupra bugetului și asupra activităților proiectului.
''')

# ------------------------------------------------------------------------------ 10-11
SECT('10. Evidența echipamentelor · 11. Garanții și penalități')
TBL([
    ['Denumire echipament', 'Cantitate', 'Număr / dată recepție'],
    ['Laptop HP Envy 17', '3', '«PV predare-primire-recepție nr. …» / 18.09.2026'],
    ['Laptop Acer Nitro V15', '1', 'idem / 18.09.2026'],
    ['Desktop ZMEU MAX', '2', 'idem / 18.09.2026'],
    ['Multifuncțională Epson WorkForce Pro EM-C8100', '2', 'idem / 18.09.2026'],
], widths=[8.5, 2.0, 6.5], small=False)
P('**11.1 Garanții de bună execuție / 11.2 Penalități:** „-” – nu au fost constituite garanții de bună execuție și nu au fost aplicate penalități în perioada de raportare.')
FLAG('Fișierul PV IT se numește „…28.08.2026”, deși conținutul este din 18.09.2026 – se redenumește înainte de încărcare. Garanția de 12 luni din contract față de minimum 24 de luni din procedura proprie – de verificat.')

# ------------------------------------------------------------------------------ 12
SECT('12. Resurse umane implicate în activitățile raportate')
SMALL('Câte un bloc pentru fiecare persoană. Lista trebuie să fie identică cu Anexa 13 și cu fișele de pontaj. Persoanele fără pontaj/RA nu se trec până la completarea documentelor.')

FIELD('Baba Alina-Ioana – Descriere', L_SCURT, '''
Poziția: Manager de proiect – Beneficiar
Categorie: Expert management de proiect > 10 ani
Perioada de activitate: iulie – septembrie 2026
În perioada de raportare, expertul a fost implicat în SA1.1 și în coordonarea tuturor subactivităților, după cum urmează:
• coordonarea constituirii echipei de proiect și a integrării experților nominalizați prin Notificările nr. 1–4;
• organizarea și conducerea întâlnirilor de lucru din 03.07, 16.07, 13.08, 18.09 și 25.09.2026;
• coordonarea elaborării și avizarea celor 4 proceduri și 3 planuri de management, a metodologiei de selecție a grupului țintă, a metodologiei de acordare a sprijinului financiar și a metodologiilor activităților remediale;
• pregătirea Notificărilor nr. 1–4 și a solicitării de Act adițional nr. 1, inclusiv a răspunsurilor la clarificări;
• elaborarea și transmiterea planificărilor lunare ale activităților (Anexa 12) pentru iulie – octombrie 2026;
• coordonarea procedurilor de achiziție și monitorizarea contractelor de închiriere autoturism, formare și furnizare echipamente IT;
• monitorizarea lunară a activităților și a indicatorilor, verificarea pontajelor, a rapoartelor de activitate și a livrabilelor experților;
• comunicarea cu ofițerul de monitorizare din cadrul OIR PECU Nord-Vest și coordonarea elaborării Raportului de progres nr. 1.
''')
FIELD('Fătu Iulia – Descriere', L_SCURT, '''
Poziția: Asistent manager – Beneficiar
Categorie: Expert management de proiect 5–10 ani
Perioada de activitate: iulie – septembrie 2026
În perioada de raportare, expertul a fost implicat în SA1.1, SA2.1 și SA3.1, după cum urmează:
• organizarea logistică a întâlnirilor de lucru și întocmirea agendelor, minutelor și listelor de prezență;
• gestionarea registrului de intrări-ieșiri și arhivarea fizică și electronică a documentelor proiectului;
• întocmirea documentelor procedurilor de achiziție (referate de necesitate, solicitări de ofertă, contracte, ordine de începere) și încărcarea dosarelor de achiziție în MySMIS2021;
• coordonarea materialelor de informare și publicitate și actualizarea subpaginii proiectului de pe site-ul beneficiarului;
• centralizarea rapoartelor de activitate, a pontajelor și a documentelor justificative ale experților;
• îndeplinirea atribuțiilor de responsabil cu protecția datelor cu caracter personal pentru documentele grupului țintă.
''')
FIELD('Dumitrescu Marius-Gheorghe – Descriere', L_SCURT, '''
Poziția: Responsabil financiar – Beneficiar
Categorie: Expert management de proiect < 5 ani
Perioada de activitate: iulie – august 2026
În perioada de raportare, expertul a fost implicat în SA1.1 și SA2.1, după cum urmează:
• organizarea evidenței contabile analitice distincte a proiectului;
• întocmirea documentelor privind salarizarea echipei de proiect și verificarea documentelor financiare aferente deplasărilor și achizițiilor;
• urmărirea încasării prefinanțării nr. 1 (700.000,00 lei, autorizată la 10.08.2026) și a utilizării contului de prefinanțare;
• transmiterea Formularului nr. 11 – Notificare privind reconcilierea contabilă «pentru lunile iulie și august 2026».
Începând cu 04.09.2026, poziția a fost preluată de doamna Fekete Dorottya, conform Notificării nr. 3.
''', note='Pontajele pentru iulie și august lipsesc din Drive (A4 pct. 4). Fără ele, blocul se scoate.')
FIELD('Fekete Dorottya – Descriere', L_SCURT, '''
Poziția: Responsabil financiar – Beneficiar
Categorie: Expert management de proiect < 5 ani
Perioada de activitate: septembrie 2026
În perioada de raportare, expertul a fost implicat în SA1.1 și SA2.1, după cum urmează:
• preluarea evidenței financiare a proiectului și a documentelor aferente lunilor iulie – august 2026;
• verificarea documentelor financiare aferente achiziției de echipamente IT (notă de comandă, factură, plată) și contractelor de închiriere autoturism și de formare;
• centralizarea documentelor justificative pentru Cererea de rambursare nr. 1 (salarii, deplasări, închiriere autoturism, echipamente IT);
• transmiterea Formularului nr. 11 – Notificare privind reconcilierea contabilă «pentru luna septembrie 2026».
''')
FIELD('Iancu «Claudiu-Ionel-Ovidiu» – Descriere', L_SCURT, '''
Poziția: Expert grup țintă 1 – Beneficiar
Categorie: Expert implementare < 5 ani
Perioada de activitate: iulie – septembrie 2026
În perioada de raportare, expertul a fost implicat în SA4.1, SA4.2 și SA5.1, după cum urmează:
• elaborarea, împreună cu Expertul GT 2, a Metodologiei de selecție a grupului țintă și a Metodologiei de acordare a sprijinului financiar (versiunea 1 – 16.07.2026; versiunea 2 – septembrie 2026);
• participarea la întâlnirile de informare și recrutare de la Colegiul Tehnic Turda (07.07, 24.07, 21.08, 21.09 și 24.09.2026) și de la Liceul Teologic Reformat Cluj-Napoca (18.09.2026);
• constituirea a 14 dosare de înscriere în luna iulie și solicitarea documentelor lipsă și a confirmărilor școlare;
• încadrarea pe acțiuni a celor 150 de elevi identificați din centralizatoarele școlilor;
• precompletarea a 70 de dosare pentru elevii de liceu ai Colegiului Tehnic Turda;
• verificarea a 64 de dosare pe grila de eligibilitate (Anexa 9) și semnarea a 24 de formulare de înregistrare individuală;
• înregistrarea participanților în MySMIS2021 și participarea la întâlnirile de management.
''', note='Lipsește raportul de activitate pentru septembrie (A4 pct. 4). Numele se scrie exact ca în CIM și în CF.')
FIELD('Suciu Denisa – Descriere', L_SCURT, '''
Poziția: Expert grup țintă 2 – Beneficiar
Categorie: Expert implementare < 5 ani
Perioada de activitate: iulie – septembrie 2026
În perioada de raportare, expertul a fost implicat în SA4.1, SA4.2 și SA5.1, după cum urmează:
• elaborarea, împreună cu Expertul GT 1, a metodologiei de selecție a grupului țintă și a metodologiei de acordare a sprijinului financiar;
• realizarea materialelor de informare pentru școli (afiș A3, flyer față-verso, flyer 12 × 17 cm);
• organizarea întâlnirilor de informare și recrutare de la Colegiul Tehnic Turda (07.07 și 24.07.2026) și de la Liceul Tehnologic „Vlădeasa” Huedin (09.07.2026) și constituirea a 10 dosare de înscriere;
• centralizarea situațiilor transmise de școli și identificarea furnizorilor de formare pentru cadrele didactice;
• organizarea a 8 întâlniri de recrutare în septembrie la Colegiul Tehnic Turda, Liceul Tehnologic „Vlădeasa” Huedin și Liceul Teologic Reformat Cluj-Napoca;
• gestionarea a 38 de dosare ale elevilor de clasa a IX-a de la Colegiul Tehnic Turda și a 35 de dosare de la Huedin;
• actualizarea registrului grupului țintă și pregătirea planificării lunare pentru septembrie.
''')
FIELD('Moraru Georgia – Descriere', L_SCURT, '''
Poziția: Expert comunicare – Beneficiar
Categorie: Expert implementare < 5 ani
Perioada de activitate: septembrie 2026
În perioada de raportare, expertul a fost implicat în SA5.3, după cum urmează:
• aplicarea chestionarelor privind interesele și percepțiile elevilor despre meserii și despre ÎPT, ca bază pentru Planul de informare și conștientizare;
• organizarea a 5 activități de informare și conștientizare la Colegiul Tehnic Turda (15.09, 16.09 și 30.09.2026), la Casa de Cultură din Huedin (28.09.2026) și la Primăria Huedin (29.09.2026), cu «23» de elevi și «44» de participări;
• utilizarea metodelor interactive („Găsește pe cineva care…”, „Mesaj pentru mine peste 5 ani”) și realizarea înregistrărilor audio cu acordul reprezentanților legali;
• realizarea afișelor și pliantelor campaniei de informare și conștientizare;
• întocmirea listelor de prezență, a fișelor de lucru și a documentației foto.
''')
FIELD('Gujan Gabriela – Descriere', L_SCURT, '''
Poziția: Consilier psihologic – Beneficiar
Categorie: Expert implementare < 5 ani
Perioada de activitate: septembrie 2026
În perioada de raportare, expertul a fost implicat în SA5.1, după cum urmează:
• realizarea a 10 deplasări (16–30.09.2026) la Colegiul Tehnic Turda și la structura Școala Profesională Poiana Turda;
• furnizarea de sprijin psihologic individual și de grup pentru «17» elevi din clasele a X-a – a XI-a (acțiunea 8.f.1);
• aplicarea a 13 chestionare de motivație școlară și a 11 fișe de autocunoaștere și utilizarea instrumentelor „Rucsacul psihologului” și „Harta traseelor vieții”;
• întocmirea a «17» rapoarte individuale de activitate pentru elevi (fișă de observație, listă de prezență, fișe de lucru);
• participarea la întâlnirile de management din 18.09 și 25.09.2026.
''')
FIELD('Tiron Maria-Emilia – Descriere', L_SCURT, '''
Poziția: Cadru didactic 1 – Beneficiar
Categorie: Expert implementare < 5 ani
Perioada de activitate: septembrie 2026
În perioada de raportare, expertul a fost implicat în SA5.4, după cum urmează:
• elaborarea metodologiei de organizare a activităților remediale la limba și literatura română pentru Colegiul Tehnic Turda (10.09.2026);
• aplicarea testelor de evaluare inițială pentru cele 2 grupe de elevi din clasa a IX-a;
• susținerea sesiunilor remediale din 17.09.2026 (14 elevi) și 21.09.2026 (12 elevi);
• întocmirea listelor de prezență, a fișelor de lucru și a documentației foto.
''')
FIELD('Pleșoiu Viorica – Descriere', L_SCURT, '''
Poziția: Cadru didactic 2 – Beneficiar
Categorie: Expert implementare < 5 ani
Perioada de activitate: septembrie 2026
În perioada de raportare, expertul a fost implicat în SA5.4, după cum urmează:
• elaborarea metodologiei activităților remediale la fizică pentru Colegiul Tehnic Turda și a testului inițial pentru clasa a IX-a;
• aplicarea a 20 de teste de evaluare inițială;
• susținerea sesiunilor remediale din 22.09.2026 («20» de elevi) și 29.09.2026 (14 elevi);
• întocmirea listelor de prezență și a documentației foto.
''')
FIELD('Anderco Claudia-Maria – Descriere', L_SCURT, '''
Poziția: Cadru didactic 3 – Beneficiar
Categorie: Expert implementare < 5 ani
Perioada de activitate: septembrie 2026 (din 17.09.2026)
În perioada de raportare, expertul a fost implicat în SA5.4, după cum urmează:
• elaborarea metodologiei activităților remediale la limba și literatura română pentru clasa a IX-a D a Liceului Teologic Reformat Cluj-Napoca (23 de elevi înscriși);
• elaborarea testului inițial, a baremului și a grilei de evaluare;
• susținerea primei sesiuni remediale la 30.09.2026 («20» de elevi prezenți) și planificarea sesiunilor din luna octombrie;
• întocmirea listei de prezență și a documentației foto.
''')
FIELD('Golovatic Livia – Descriere', L_SCURT, '''
Poziția: Facilitator comunitar 2 – Beneficiar
Categorie: Expert implementare < 5 ani
Perioada de activitate: septembrie 2026
În perioada de raportare, expertul a fost implicat în SA5.3, după cum urmează:
• organizarea atelierelor cu elevii la Colegiul Tehnic Turda (15.09.2026) și la Primăria Huedin (24.09.2026), «cu … participanți»;
• contactarea părinților elevilor din grupul țintă și pregătirea atelierelor pentru părinți din luna octombrie 2026;
• întocmirea listelor de prezență și a fișei de planificare lunară a atelierelor.
''', note='Folderul de septembrie este gol (fără RA și fără pontaj). Blocul se păstrează numai după completarea documentelor.')

# ------------------------------------------------------------------------------ 13
SECT('13. Respectarea prevederilor privind ajutorul de stat / de minimis')
FIELD('Justificare respectare prevederi ajutor de stat / de minimis', L_LUNG, '''
Nu este cazul. Conform cererii de finanțare, proiectul nu intră sub incidența regulilor privind ajutorul de stat sau ajutorul de minimis.
''')

# ------------------------------------------------------------------------------ 14
SECT('14. Comunicare și vizibilitate')
FIELD('Descriere respectare cerințe de comunicare și vizibilitate a sprijinului din fonduri acordat', L_LUNG, '''
În perioada de raportare iulie – septembrie 2026 au fost respectate cerințele privind comunicarea și vizibilitatea sprijinului acordat din Fondul Social European Plus prin Programul Educație și Ocupare 2021-2027, conform art. 47 și 50 din Regulamentul (UE) 2021/1060, contractului de finanțare, Manualului de identitate vizuală 2021-2027 și Anexei 18 la Manualul beneficiarului, după cum urmează:
• Pe site-ul beneficiarului a fost creată, la 02.07.2026, subpagina dedicată proiectului (https://napocaporolissum.ro/unic-porolissum-2/), care prezintă denumirea, beneficiarul, codul MySMIS 352704, perioada de implementare, valoarea totală, sursa de finanțare (FSE+, Programul Educație și Ocupare 2021-2027), descrierea, obiectivele, grupul țintă și rezultatele așteptate, cu antetul proiectului și trimiterea către www.mfe.gov.ro.
• Pe subpagină a fost publicat anunțul de începere a proiectului, cu elementele obligatorii: beneficiarul, titlul și codul MySMIS, programul, prioritatea și fondul, perioada de implementare, regiunea, valoarea totală, scopul, activitățile, grupul țintă, rezultatele urmărite și datele de contact.
• La 16.07.2026 au fost publicate pe subpagină metodologia de selecție a grupului țintă și metodologia de acordare a sprijinului financiar, cu condițiile de acces la măsurile de sprijin pentru elevi și părinți (MB, Anexa 11 pct. 3).
• Pe pagina de Facebook a proiectului, „UNIC: Viitor prin Educație” (https://www.facebook.com/unic.viitorprineducatie), au fost publicate «… postări» privind activitățile proiectului.
• Afișul A3 al proiectului a fost expus la sediul beneficiarului din Gilău, la intrare, și «la unitățile de învățământ partenere în care se desfășoară activitățile (Colegiul Tehnic Turda, Liceul Tehnologic „Vlădeasa” Huedin, Liceul Teologic Reformat Cluj-Napoca)», fiind realizate fotografii ca dovadă.
• Au fost realizate și distribuite flyerul de prezentare față-verso pentru școli și flyerul de 12 × 17 cm, utilizate în întâlnirile de informare și recrutare din iulie – septembrie 2026; în septembrie au fost realizate afișele și pliantele campaniei de informare și conștientizare din SA5.3.
• Toate documentele utilizate în relația cu grupul țintă (formulare de înregistrare, liste de prezență, fișe de lucru, teste de evaluare, materiale de curs) au inclus emblema Uniunii Europene cu mențiunea „Cofinanțat de Uniunea Europeană”, sigla Guvernului României și mențiunea privind finanțarea din FSE+ prin Programul Educație și Ocupare 2021-2027.
• Participanții au fost informați, la înscriere și la fiecare activitate, cu privire la sprijinul acordat prin FSE+.
• Echipamentele IT recepționate la 18.09.2026 au fost «inscripționate cu autocolante care conțin elementele de identitate vizuală».
Dovezile (link-urile publicărilor, capturile de ecran cu data și adresa URL, fotografiile afișelor și materialele realizate) sunt centralizate în documentul „SA 3.1_07-09.2026_Informare și publicitate”, atașat raportului.
''', note='Înainte de transmitere: pe subpagină, „Cofinanțare UE: … intensitate intervenție 100%” trebuie înlocuit cu valoarea cofinanțării UE (5.879.540,52 lei FSE+), iar „acordarea de subvenții” '
          'cu masa caldă (după AA1). Numărul postărilor de pe Facebook se completează din pagina proiectului.')

# ------------------------------------------------------------------------------ 15
SECT('15. Principii orizontale și teme secundare')
NU = 'Nu este cazul pentru tipul de activități desfășurate în perioada de raportare, care au avut caracter educațional, social și de management, fără intervenții fizice asupra mediului.'
FIELD('15.1.1 Egalitate de gen', L_LUNG, '''
În perioada de raportare iulie – septembrie 2026, principiul egalității de șanse și de tratament între femei și bărbați a fost respectat prin măsurile prevăzute în cererea de finanțare, după cum urmează:
În cadrul SA1.1, recrutarea și nominalizarea membrilor echipei de proiect s-au realizat exclusiv pe baza cerințelor de studii și experiență din fișele de post, fără criterii legate de sex sau gen. Experții au asumat Codul de etică al proiectului, care include prevederi privind egalitatea de șanse și interzicerea discriminării «(asumat la …)».
În cadrul SA4.1 și SA4.2, criteriile de eligibilitate din metodologia de selecție nu fac nicio distincție în funcție de sex, iar criteriile de departajare prevăzute în cererea de finanțare includ apartenența la genul feminin. Elevii au fost identificați pe baza nevoii de sprijin confirmate de școală. Dintre elevii intrați în operațiune, «…» sunt fete și «…» sunt băieți, structura reflectând profilul specializărilor din școlile partenere.
În cadrul SA5.1, SA5.3 și SA5.4, accesul la consiliere, la activitățile de informare și la programele remediale a fost asigurat în condiții egale, iar metodele de lucru au fost adaptate grupului, nu sexului participanților. În activitățile de consiliere au fost discutate deschis opțiunile profesionale ale elevilor, inclusiv situațiile în care specializarea urmată nu corespunde intereselor lor, pentru prevenirea alegerilor bazate pe stereotipuri.
În cadrul SA3.1 și SA5.3, materialele de informare și conștientizare au prezentat meseriile și traseele educaționale din ÎPT fără mesaje, formulări sau imagini care să promoveze stereotipuri de gen.
În cadrul SA5.2, programul de formare a cadrelor didactice a inclus aspecte privind comunicarea nediscriminatorie cu elevii.
În perioada de raportare nu au fost semnalate situații de tratament diferențiat pe criterii de sex sau gen.
''')
FIELD('15.1.2 Nediscriminare', L_LUNG, '''
În perioada de raportare iulie – septembrie 2026, principiul nediscriminării a fost respectat prin măsurile prevăzute în cererea de finanțare, după cum urmează:
În cadrul SA4.1, metodologia de selecție a grupului țintă a fost elaborată și diseminată în școlile partenere, cu criterii transparente de eligibilitate și de departajare, aplicate uniform tuturor candidaților. Criteriile de departajare acordă prioritate elevilor de etnie romă și elevilor cu dizabilități. Recrutarea a vizat inclusiv elevi din mediul rural și din localități mici (structura Școala Profesională Poiana Turda, zona Huedin), iar familiile care au întâmpinat dificultăți la completarea dosarelor au fost sprijinite direct de experți, prin deplasări repetate în școli. Dintre elevii intrați în operațiune, «…» sunt de etnie romă (ținta proiectului: minimum 81 de elevi romi).
În cadrul SA4.2, identificarea elevilor s-a făcut pe criterii obiective (risc educațional, situație socio-economică, rezultate școlare), confirmate de școală, fără criterii legate de etnie, religie, limbă maternă sau alte criterii discriminatorii, altele decât cele de prioritizare prevăzute în cererea de finanțare.
În cadrul SA5.1 – SA5.4, activitățile s-au desfășurat în școlile în care învață elevii, în afara programului școlar, iar consilierea, informarea și programele remediale au fost oferite gratuit tuturor elevilor din grupul țintă. Colaborarea cu Liceul Teologic Reformat Cluj-Napoca a permis includerea în grupul țintă a elevilor dintr-o unitate de învățământ cu predare în limba maghiară «(de confirmat)».
Tema secundară „Nediscriminare” este susținută prin măsurile directe de sprijin pentru elevii din grupuri vulnerabile – sprijinul financiar pentru cazare, masă și transport și masa caldă –, care vor fi acordate începând din perioada următoare.
În perioada de raportare nu au fost semnalate situații de excludere, restricționare a accesului sau tratament diferențiat pe criterii discriminatorii.
''')
FIELD('15.1.3 Accesibilitatea pentru persoanele cu dizabilități', L_LUNG, '''
În perioada de raportare iulie – septembrie 2026, accesibilitatea a fost asigurată prin următoarele măsuri:
• activitățile cu grupul țintă (consiliere, informare, programe remediale) s-au desfășurat în clădirile unităților de învățământ în care învață elevii și în spații publice din localitățile acestora (Casa de Cultură și Primăria Huedin), reducând barierele de deplasare;
• întâlnirile de informare și recrutare au fost organizate în școli, la orele convenite cu conducerile acestora, pentru a permite participarea elevilor și a părinților;
• formarea cadrelor didactice s-a desfășurat online, iar o parte dintre întâlnirile de management au avut loc online, facilitând participarea;
• materialele de informare, formularele și fișele de lucru au fost redactate într-un limbaj simplu, adaptat vârstei elevilor, iar experții au explicat direct conținutul documentelor elevilor și părinților;
• metodologia de selecție prevede identificarea, după selecție, a nevoilor specifice ale participanților cu dizabilități sau cu cerințe educaționale speciale și adaptarea activităților la aceste nevoi.
În perioada de raportare, «au fost incluși … participanți cu dizabilități sau cu cerințe educaționale speciale / nu au fost înregistrați participanți cu dizabilități». Nu au fost semnalate situații în care accesul la activități să fi fost limitat.
''')
FIELD('15.1.4 Schimbări demografice', L_LUNG, '''
Proiectul contribuie la atenuarea efectelor schimbărilor demografice prin menținerea în sistemul educațional a elevilor din mediul rural și din localitățile mici, inclusiv a celor ai căror părinți sunt plecați la muncă în străinătate, și prin creșterea șanselor acestora de a obține o calificare profesională și de a se integra pe piața muncii locale. În perioada de raportare, au fost identificați și recrutați elevi din zone rurale și din orașe mici (Poiana Turda, zona Huedin), care vor beneficia de sprijin pentru continuarea studiilor.
''')
FIELD('15.2.1 Poluatorul plătește', L_LUNG, NU)
FIELD('15.2.2 Protecția biodiversității', L_LUNG, NU)
FIELD('15.2.3 Utilizarea eficientă a resurselor', L_LUNG, '''
În perioada de raportare iulie – septembrie 2026, utilizarea eficientă a resurselor a fost asigurată prin următoarele măsuri:
• documentele de proiect (rapoarte de activitate, fișe de pontaj, livrabile, documente de achiziție) au fost întocmite și semnate preponderent în format electronic, cu semnătură electronică calificată, și transmise, verificate și arhivate electronic, reducând consumul de hârtie și toner;
• o parte dintre întâlnirile de management (16.07 și 18.09.2026) s-au desfășurat online, iar formarea cadrelor didactice s-a desfășurat integral online, evitând deplasările;
• deplasările echipei la școlile partenere au fost grupate, astfel încât în aceeași zi să fie realizate mai multe activități (recrutare, colectare de documente, consiliere), cu utilizarea unui singur autoturism;
• documentele care au necesitat tipărire au fost imprimate față-verso;
• materialele de informare au fost distribuite și în format electronic, prin școli, reducând numărul de exemplare tipărite.
''')
FIELD('15.2.4 Reziliența la dezastre', L_LUNG, NU)
FIELD('15.2.5 Imunizarea la schimbările climatice', L_LUNG, NU)
FIELD('15.2.6 Principiul „de a nu prejudicia în mod semnificativ” (DNSH)', L_LUNG, '''
În perioada de raportare, activitățile proiectului au avut caracter educațional, social și de management (consiliere, informare, programe remediale, formare, selecția grupului țintă). Acestea nu au presupus lucrări de construcție, intervenții asupra terenurilor sau habitatelor ori procese care să genereze emisii sau deșeuri semnificative și nu au avut efecte negative semnificative asupra niciunuia dintre cele șase obiective de mediu.
Echipamentele IT achiziționate «respectă cerințele de eficiență energetică …», iar documentațiile de achiziție au inclus clauze privind respectarea principiului DNSH, conform contractului de finanțare. În cadrul SA5.3, materialele campaniei de informare și conștientizare «au inclus mesaje privind dezvoltarea durabilă și aplicarea principiului DNSH în viața de zi cu zi», conform angajamentului din cererea de finanțare.
''', note='CF promite ca DNSH să fie inclus în fiecare acțiune a campaniei și în formare. Dacă materialele din septembrie nu conțin astfel de mesaje, fraza se reformulează la viitor.')
FIELD('15.2.7 Măsuri de evitare și reducere a efectelor reziduale', L_LUNG, NU)
FIELD('15.2.8 Teme secundare', L_LUNG, '''
Proiectul contribuie la temele secundare FSE+ asumate în cererea de finanțare:
• Tema 10 – Abordarea provocărilor identificate în cadrul semestrului european: proiectul răspunde recomandării privind reducerea părăsirii timpurii a școlii, inclusiv în rândul elevilor romi și al celor din mediul rural (Programul Național de Reformă, capitolul „Educație și competențe”). În perioada de raportare au fost identificați 169 de elevi în risc sau din medii defavorizate și au început consilierea psihologică, programele remediale și campania de informare și conștientizare.
• Tema 05 – Nediscriminare: au fost aplicate criteriile de prioritizare pentru elevii romi și pentru elevii cu dizabilități, iar recrutarea a vizat elevi din grupuri vulnerabile și din mediul rural; măsurile directe de sprijin (sprijin financiar pentru cazare, masă și transport și masă caldă), în valoare de 1.464.000,00 lei, vor fi acordate începând din perioada următoare.
• Integrarea perspectivei de gen: activitățile de consiliere și informare au abordat alegerea traseului educațional fără stereotipuri de gen (detalii la 15.1.1).
''')

# ------------------------------------------------------------------------------ 16
SECT('16. Stadiul implementării recomandărilor din vizite / RP anterioare')
FIELD('Recomandări – Descriere', L_SCURT, '''
Nu este cazul – în perioada de raportare nu au fost efectuate vizite de monitorizare sau verificări la fața locului, iar prezentul raport este primul raport de progres al proiectului.
''', note='De verificat: dacă a existat o vizită ad-hoc în septembrie (pe baza Anexei 12), se completează datele ei, ca în model.')

# ------------------------------------------------------------------------------ 17
SECT('17. Stadiul îndeplinirii indicatorilor de etapă')
SMALL('Câte un set de trei câmpuri (Justificare / Abatere-întârziere / Măsuri de remediere) pentru fiecare indicator din Planul de monitorizare (Anexa 2 la contract). '
      'Unde nu există abatere: „Nu există abateri sau întârzieri.” / „Nu este cazul.”')
FIELD('IE1 – Rapoarte de progres periodice, consecutive (țintă 12) – Justificare', L_SCURT, '''
Indicatorul vizează transmiterea a 12 rapoarte de progres consecutive pe durata implementării. Prezentul Raport de progres nr. 1, aferent perioadei 01.07.2026 – 30.09.2026 (L1–L3), a fost elaborat și transmis «la data de …», în termenul de 30 de zile de la finalizarea perioadei de raportare și cu cel puțin 10 zile lucrătoare înaintea Cererii de rambursare nr. 1. Valoare realizată la data raportării: 1 raport de progres din 12.
''')
FIELD('IE2 – Cereri de rambursare conform Anexei 3 (țintă 12) – Justificare', L_SCURT, '''
Indicatorul nu are termen scadent în perioada de raportare. Conform graficului cererilor de prefinanțare/rambursare, Cererea de rambursare nr. 1 este planificată pentru 25.10.2026, în perioada următoare. În perioada de raportare a fost autorizată Cererea de prefinanțare nr. 1 (700.000,00 lei, 10.08.2026) și a început centralizarea documentelor justificative pentru Cererea de rambursare nr. 1.
''')
FIELD('IE3 – Participanți GT – elevi (țintă 500, termen 30.06.2029) – Justificare', L_SCURT, '''
Indicatorul nu are termen scadent în perioada de raportare. Selecția grupului țintă este progresivă, în 3 serii corespunzătoare anilor școlari. Până la 30.09.2026 au fost identificați 169 de elevi, au fost constituite «128» de dosare eligibile, iar «96» de elevi au intrat în operațiune (8.f.1 – «17»; 8.f.2 – «35»; 8.f.3 – «44»). Documente care probează îndeplinirea indicatorului: dosarele de grup țintă, formularele de înregistrare individuală, grilele de verificare a eligibilității și rapoartele de selecție.
''')
FIELD('IE3 – Participanți GT – părinți/reprezentanți legali/tutori sprijiniți (țintă 96, termen „30.06.2026”) – Justificare', L_SCURT, '''
Termenul de 30.06.2026 din Planul de monitorizare este anterior datei de începere a implementării (01.07.2026) și reprezintă o eroare materială; termenul corect, corelat cu indicatorul de program 5SO14, este 30.06.2029, iar corectura va fi solicitată la următoarea modificare a contractului de finanțare. În perioada de raportare nu au fost înregistrați părinți în grupul țintă; atelierele pentru părinți din SA5.3 încep în luna octombrie 2026.
''')
FIELD('IE3 – Participanți GT – părinți – Abatere/întârziere și Măsură de remediere', L_SCURT, '''
Abatere/întârziere: termenul din Planul de monitorizare (30.06.2026) este eronat și nu poate fi îndeplinit, fiind anterior începerii proiectului.
Măsură de remediere: corectarea termenului la 30.06.2029 prin notificare, la următoarea modificare a contractului; înregistrarea părinților începând cu luna octombrie 2026.
''')
FIELD('IE3 – Participanți GT – cadre didactice (țintă 4, termen 30.06.2029) – Justificare', L_SCURT, '''
Indicatorul nu are termen scadent în perioada de raportare. Cele 4 cadre didactice din unitățile de învățământ partenere asociate au parcurs programul de formare acreditat în perioada 10–18.09.2026, iar evaluarea finală are loc la 09.10.2026. Cadrele didactice au fost înregistrate ca participanți în grupul țintă, pe acțiunea 8.f.1, «la data de …».
''')
FIELD('IE4 – EECO06+07 aferent acțiunii 8.f.1 (țintă 183) – Justificare', L_SCURT, '''
Indicatorul nu are termen scadent în perioada de raportare. Au intrat în operațiune «17» elevi pe acțiunea 8.f.1, care au beneficiat de sprijin psihologic în cadrul SA5.1. Documente care probează: dosarele participanților și formularele de înregistrare atașate la secțiunea 5.
''')
FIELD('IE5 – EECO06+07 aferent acțiunii 8.f.2 (țintă 104) – Justificare', L_SCURT, '''
Indicatorul nu are termen scadent în perioada de raportare. Au intrat în operațiune «35» de elevi pe acțiunea 8.f.2, dintre care «…» din clasele a VII-a – a VIII-a, care au participat la activitățile de informare și conștientizare din cadrul SA5.3. Documente care probează: dosarele participanților și formularele de înregistrare atașate la secțiunea 5.
''')
FIELD('IE6 – EECO06+07 aferent acțiunii 8.f.3 (țintă 213) – Justificare', L_SCURT, '''
Indicatorul nu are termen scadent în perioada de raportare. Au intrat în operațiune «44» de elevi din clasa a IX-a pe acțiunea 8.f.3, care au participat la programele remediale din cadrul SA5.4. Documente care probează: dosarele participanților și formularele de înregistrare atașate la secțiunea 5.
''')
FIELD('IE7 – 5SO14 aferent acțiunii 8.f.2 (țintă 96) – Justificare', L_SCURT, '''
Indicatorul nu are termen scadent în perioada de raportare și nu a înregistrat progres; atelierele pentru părinți din cadrul SA5.3 încep în luna octombrie 2026.
''')
FIELD('IE8–IE9 – 5SR09 aferent acțiunilor 8.f.1 (țintă 165) și 8.f.3 (țintă 192) – Justificare', L_SCURT, '''
Indicatorul de rezultat nu are termen scadent în perioada de raportare. Valoarea se înregistrează la ieșirea participanților din operațiune, după finalizarea programului de sprijin din anul școlar 2026-2027; în perioada de raportare nu au existat ieșiri din operațiune.
''')

# ------------------------------------------------------------------------------ 18
SECT('18. Calitatea liderului / partenerului în alte proiecte')
P('Secțiunea se completează automat. Se verifică datele și se corelează cu „Centralizator proiecte PEO, PIDS și POCU_Beneficiar” (atașat). '
  'În documentele din Drive apar și alte proiecte ale beneficiarului: «PIDS 329335», «308485», «INOVAR 348508», «358503» – se verifică lista completă și stadiul fiecăruia.')
FLAG('Asistentul manager și Managerul de proiect lucrează și în proiectul PIDS 329335 (și AM în INOVAR 348508) – pontajele trebuie să arate orele din toate proiectele PEO/PIDS (Anexa 8).')

# ------------------------------------------------------------------------------ 19
SECT('19. Observații importante pentru succesul proiectului / propuneri pentru perioada următoare')
FIELD('Descriere informații importante pentru succesul proiectului', L_LUNG, '''
Primele trei luni de implementare au fost dedicate constituirii echipei, elaborării documentelor de management și a metodologiilor, recrutării grupului țintă și debutului, din septembrie 2026, al activităților obligatorii cu elevii. Implementarea a fost susținută de colaborarea constantă cu unitățile de învățământ partenere – Colegiul Tehnic Turda, Liceul Tehnologic „Vlădeasa” Huedin și Liceul Teologic Reformat Cluj-Napoca –, de implicarea diriginților și a conducerilor școlilor în identificarea elevilor și de adaptarea rapidă a echipei la situațiile apărute (extinderea bazei de recrutare, reluarea achiziției de echipamente IT, completarea echipei prin notificări).
Pentru perioada următoare (octombrie – decembrie 2026) sunt propuse următoarele măsuri, în vederea prevenirii eventualelor deficiențe la raportare:
• finalizarea validării grupului țintă prin rapoartele de selecție pe școli și înregistrarea în MySMIS2021 a tuturor participanților intrați în operațiune, în maximum 5 zile lucrătoare de la prima activitate;
• monitorizarea lunară, pe baza registrului grupului țintă, a ponderilor asumate: minimum 70% elevi din clasa a IX-a în acțiunea 8.f.3, minimum 50% elevi din clasele a VII-a – a VIII-a în acțiunea 8.f.2 și minimum 81 de elevi de etnie romă;
• extinderea parteneriatelor cu unitățile de învățământ (acord de colaborare cu Liceul Tehnologic Energetic Cluj-Napoca), pentru atingerea țintelor de grup țintă pe acțiunile 8.f.1 și 8.f.3;
• începerea atelierelor pentru părinți și înregistrarea primilor participanți la indicatorul 5SO14;
• acordarea sprijinului financiar pentru elevii din acțiunea 8.f.1 și a mesei calde pentru elevii participanți la programele remediale, după finalizarea procedurilor;
• nominalizarea prin notificare a Cadrului didactic 4 și lansarea achiziției pentru târgul de oportunități;
• standardizarea denumirii documentelor justificative (cod subactivitate, lună, tip document) și semnarea electronică a acestora până la data de 5 a lunii următoare.
''')

# =====================================================================================
# PARTEA C – DOCUMENTE DE ÎNCĂRCAT
# =====================================================================================
PAGEBREAK()
H1('Partea C – Documentele de încărcat la RP 1 (secțiunea „Documente”)')
SMALL('Denumirile urmează Anexa 11 din MB (GT: numele persoanei; indicatori: nume + cod indicator; experți: nume + tip document + luna.anul; livrabile: tip + versiune + expert) '
      'și convenția din model: cod subactivitate + lună + tip document. Toate PDF-urile se semnează electronic (semnătură calificată), nu cu imaginea semnăturii olografe.')
TBL([
    ['Fișier (denumire propusă)', 'Tip document în MySMIS', 'Conținut / observații'],
    ['Anexa 13_Lista experți_RP 1.pdf (+ .xlsx)', 'Alte documente', 'Un rând pe expert și lună (iul., aug., sept.); aceleași persoane ca la pct. 12.'],
    ['Anexa 14_Centralizator livrabile_RP 1.pdf', 'Alte documente', 'Metodologii (GT, sprijin financiar, remediale), proceduri și planuri – stare, experți, data aprobării; și livrabilele din alte proiecte PEO/PIDS ale beneficiarului.'],
    ['Centralizator proiecte PEO, PIDS și POCU_Beneficiar.pdf', 'Alte documente', 'Pentru secțiunea 18 și verificarea dublei finanțări.'],
    ['Raport Plan Monitorizare_RP 1.pdf', 'Secțiunea „Raport Plan Monitorizare”', 'Generat din MySMIS2021 + dovezile indicatorilor de etapă.'],
    ['SA 1.1_03.07.2026_Întâlnire de lucru_fizic.pdf · SA 1.1_16.07.2026_Întâlnire de lucru_online.pdf · SA 1.1_13.08.2026_… · SA 1.1_18.09.2026_… · SA 1.1_25.09.2026_…',
     'Alte documente', 'Agendă, minută, listă de prezență / captură de ecran.'],
    ['SA 1.1_Proceduri management_UNIC-PO-01…04_V2.pdf · SA 1.1_Planuri management_UNIC-PL-01…03_V2.pdf', 'Alte documente', 'Semnate (elaborat / avizat MP / aprobat reprezentant legal), cu data.'],
    ['SA 1.1_07-10.2026_Anexa 12_Planificare lunară.pdf', 'Alte documente', 'Iulie, august, septembrie (V5), octombrie.'],
    ['SA 1.1_FP_07.2026_Manager proiect_Baba Alina-Ioana.pdf (și pentru 08, 09; idem AM și RF)', 'Document aferent resurselor umane implicate',
     'Anexa 8 – pontaj; experții de management nu depun Anexa 10.'],
    ['SA 4.1_Doc act_07.2026_Expert GT 1_Iancu ….pdf (și 08, 09; idem Expert GT 2)', 'Document aferent resurselor umane implicate', 'Anexa 10 + Anexa 8 + livrabilele lunii (fără date personale ale elevilor dincolo de necesar).'],
    ['SA 5.1_Doc act_09.2026_Consilier psihologic_Gujan Gabriela.pdf · SA 5.3_Doc act_09.2026_Expert comunicare_Moraru Georgia.pdf · SA 5.3_Doc act_09.2026_Facilitator comunitar 2_Golovatic Livia.pdf · '
     'SA 5.4_Doc act_09.2026_Cadru didactic 1_Tiron Maria-Emilia.pdf (idem CD2, CD3)', 'Document aferent resurselor umane implicate', 'Anexa 10 + Anexa 8 + liste de prezență, fișe de lucru, fotografii.'],
    ['SA 4.1_Metodologie selecție GT_V1_16.07.2026.pdf · SA 4.1_Metodologie selecție GT_V2_….pdf', 'Document aferent grupului țintă',
     'Folosită de OM doar pentru verificarea conformității selecției (MB, Anexa 11 nota 27).'],
    ['SA 4.1_Raport selecție și validare GT_nr…_….pdf', 'Document aferent grupului țintă', 'Anexa 11 la metodologie – trebuie emis (A4 pct. 2).'],
    ['SA 5.1_Metodologie sprijin financiar_V2.pdf · SA 5.4_Metodologie remedial_română_CT Turda.pdf (idem fizică, română LTR)', 'Alte documente', 'Livrabile – format cu text selectabil.'],
    ['EECO06+07_8.f.1_[Nume Prenume].pdf (câte unul pentru fiecare participant; idem 8.f.2, 8.f.3)', 'Document aferent grupului țintă (la secțiunea 5)',
     'Formular de înregistrare generat din MySMIS și semnat, acord părinte + GDPR, declarație dublă finanțare, confirmare școlară (5A), acte, grila Anexa 9, dovada participării.'],
    ['SA 5.1_09.2026_Consiliere psihologică.pdf · SA 5.3_09.2026_Informare și conștientizare.pdf · SA 5.4_09.2026_Programe remediale_[școala]_[disciplina].pdf',
     'Document aferent grupului țintă', 'Copertă + liste de prezență + fișe/teste + fotografii (dovada participării).'],
    ['SA 2.1_1. Achiziție echipamente IT_încetat.pdf · SA 2.1_2. Achiziție servicii formare.pdf · SA 2.1_4. Achiziție închiriere autoturism.pdf · SA 2.1_5. Achiziție echipamente IT_reluată.pdf',
     'Document aferent implementării contractelor de achiziție', 'Contract, ordin de începere, PV predare-primire/recepție, factură.'],
    ['SA 3.1_07-09.2026_Informare și publicitate.pdf', 'Document informare și publicitate', 'Link-uri + capturi cu data și URL; fotografiile afișelor; flyere; autocolante.'],
    ['Acord de colaborare_Liceul Teologic Reformat Cluj-Napoca_09.09.2026.pdf', 'Alte documente', 'Partener asociat nou (Anexa 7 GSCS).'],
    ['Registrul grup țintă', '—', '**Nu se încarcă** – se generează automat din MySMIS2021 (MB, Anexa 11 pct. 1 lit. d).'],
], widths=[6.6, 3.8, 6.6])

H2('Verificări finale înainte de transmitere')
BUL([
    'Aceleași cifre în secțiunile 4, 5, 12, 15, 17 și în anexe (o singură sursă: registrul GT corectat).',
    'Experții din Anexa 13 = pct. 12 = fișele de pontaj = rapoartele de activitate; fiecare expert notificat apare sau absența lui este explicată.',
    'Participanții raportați la indicatori = formularele generate din MySMIS și asociate la RP 1 = dosarele atașate.',
    'Fiecare activitate din CF planificată în L1–L3 apare în raport (inclusiv cele nedemarate, cu explicație).',
    '„Programul Educație și Ocupare 2021-2027” scris corect peste tot.',
    'Toate PDF-urile semnate electronic; denumiri conform tabelului de mai sus; nicio dată personală a elevilor în textele libere.',
    'Toate marcajele galbene «...» înlocuite sau eliminate; casetele roșii nu se copiază.',
])

# ------------------------------------------------------------------------------ export
out_docx = os.path.join(HERE, 'RP1_UNIC_352704_Raport_de_progres.docx')
out_txt = os.path.join(HERE, 'RP1_UNIC_352704_text_MySMIS.txt')
E.doc.save(out_docx)
E.export_txt(out_txt)
E.report()
print('OK:', out_docx, out_txt)
