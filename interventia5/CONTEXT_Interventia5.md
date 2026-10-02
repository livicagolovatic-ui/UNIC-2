# Intervenția 5 – „Educație pentru mediu în teritoriul GAL Napoca Porolissum – micro-granturi pentru mediu”

Dosar de context pentru lucrul la documentele proiectului. Rezumă documentele
primite pe 02.10.2026 și semnalează neconcordanțele dintre ele. Textele integrale
extrase sunt în `surse/`. Din cererea de finanțare NU s-au preluat CNP-ul, datele
din CI și adresa personală a reprezentantului legal.

## 1. Documente primite

| Document | Data | Stare |
|---|---|---|
| Anexa 1 – Descriere proiect (20 p.) | 27.05.2026 | depusă cu CF; calendarul din text este cel inițial |
| Fundamentarea bugetului, nr. 2026060302 | 03.06.2026 | versiune „actualizată” |
| Cererea de finanțare DR-36 Servicii (XFA) – versiunea după clarificări | – | stă la baza contractului |
| Anexa 2 – Graficul de implementare, vers. 1 | 27.05.2026 | aprobat prin contract |
| Nota explicativă nr. 2026092401 – modificarea nr. 1 | 24.09.2026 | **în așteptarea aprobării AFIR** |
| Anexa 2 – Graficul de implementare, vers. 2 | 24.09.2026 | anexă la modificarea nr. 1 |
| Ghidul solicitantului GAL – Intervenția 5 „LEADER în verde”, sesiunea 2/2026 (29 p.) | 19.01.2026 | ghidul apelului GAL în care a fost selectat proiectul |
| Metodologia de selecție a sub-proiectelor, sesiunea 2/2026 (11 p.) | – | anexă la CF; calendarul din cap. IX este cel inițial |
| Ghid de identitate vizuală GAL Napoca Porolissum pentru beneficiari (23 p.) | 2025 | contrazice AFIR în câteva puncte (vezi documentul de comunicare) |

Documente AFIR descărcate de pe afir.ro (02.10.2026), cu textul în `surse/`:
Anexa II C1.1 la contract „Materiale și activități de informare de tip
publicitar” (Ed. I Rev. 1); Ghidul de identitate vizuală PS 2027 V3 (ianuarie
2026); modelele V3 pentru placă, afiș și autocolant LEADER (`surse/afir_modele/`);
Ghidul de implementare DR-36 Ed. I Rev. 3; Anexa 2 „Detalii privind proiectele
umbrelă”.

Documente încă neprimite: contractul de finanțare semnat, cu anexele lui
(versiunea exactă a Anexei II, instrucțiunile de plată și de achiziții, graficul
de eșalonare a plăților), memoriul justificativ al modificării nr. 1, CV-ul lui
Iancu Dănuț, modelul AFIR de contract de grant (anexă la Manualul de procedură
DR-36).

## 1b. Livrabile produse

| Fișier | Conținut |
|---|---|
| `Int5_Comunicare_si_vizibilitate_analiza.docx` | Partea 1 a analizei Ghidului: obligațiile de comunicare și vizibilitate, datele pentru placă, bara de sigle, evenimente, beneficiari finali, calendar, întrebări, alte constatări (v1, 02.10.2026). Se generează cu `build_comunicare_vizibilitate_docx.py` (motor: `gal_docx.py`). |

## 2. Date de identificare

- Beneficiar: Asociația Grupul de Acțiune Locală Napoca Porolissum, CUI 28885000,
  reg. asociații 9/2011, înființată 19.07.2011, sediu Gilău, str. Eroilor nr. 6,
  bl. I1, parter, ap. 1, jud. Cluj; contact@napocaporolissum.ro
- Reprezentant legal: Dumitrescu Marius-Gheorghe, președinte
- Contract de finanțare AFIR: **C 36010804713061304413 / 08.09.2026**
- Program: PS PAC 2023-2027, DR-36 LEADER, cod intervenție L804 „LEADER în verde”,
  anunț 804/000, apel 2 (apel SDL 10), 2026; GAL autorizat nr. 130/01.08.2024
- Tip: proiect umbrelă de servicii, GAL ca administrator de schemă de granturi;
  instrumentare la nivel OJFIR
- Durată: 21 de luni. Proiectul este depus fără parteneri. Indicator monitorizat:
  6 sub-proiecte finanțate (NR_SUBPROIECTE_FINANTATE_IN_PROIECTE_UMBRELA = 6).
  CF declară contribuția la indicatorul R.27.
- Punctaj de selecție autoevaluat: 65 p. (C1 = 25, C2 = 25, C3 = 15, C4 = 0)

## 3. Bugetul contractat (din CF, euro)

| Capitol | Eligibil | TVA neeligibil | Total |
|---|---:|---:|---:|
| Cap. 1 Cheltuieli cu personalul (3 experți) | 10.903 | – | 10.903 |
| Cap. 2 Schimb de bune practici | 8.740 | 1.259 | 9.999 |
| Cap. 3 Micro-granturi (6 sub-proiecte) | 119.000 | – | 119.000 |
| **Total** | **138.643** | **1.259** | **139.902** |

- Sprijin public 100% din eligibil (138.643 €). TVA-ul de 1.259 € este
  **contribuție proprie a GAL**.
- Ponderea sprijinului pentru GAL (Cap. 1 + Cap. 2) = 19.643 / 138.643 = 14,17%
  din eligibil (limita: max. 15%). Raportat doar la granturi ar fi 16,5%, deci
  trebuie verificată baza de calcul din ghid.
- Curs fundamentare: 1 € = 5,0979 lei (09.03.2026).

### Cap. 1 – personal (498 ore)

| Post | Persoană | Ore | Ore/lună × luni | Net/oră | Brut/oră | Brut total (lei) | € |
|---|---|---:|---|---:|---:|---:|---:|
| Manager proiect | Golovatic Livia | 189 | 9 × 21 | 70 | 108 | 20.412 | 4.004,00 |
| Expert coordonare, implementare și monitorizare | Burdujan Liliana | 189 | 9 × 21 | 70 | 108 | 20.412 | 4.004,00 |
| Expert animare locală | Bălaș Aurora-Livia → **Iancu Dănuț** (mod. 1) | 120 | 6 × 20 | 80 | 123 | 14.760 | 2.895,31 |

Plafon BD LEADER: 70 lei net/oră pentru experiență sub 5 ani și 80 lei net/oră
pentru 5–10 ani. Postul de animare locală este bugetat la 80 lei, deci presupune
**5–10 ani de experiență**.

### Cap. 2 – schimb de bune practici (ofertă SADC Expert Consulting SRL, CAEN 8230)

~8 participanți, 5 zile: cazare cu mic dejun (5 nopți) 3.964 + 11% TVA; prânz
900,80 + 11%; cină 900,80 + 11%; transport 2.892,56 + 21%; consumabile 82,64 + 21%.
Total 8.740,80 € fără TVA, 1.259,01 € TVA, 9.999,81 € cu TVA.

### Cap. 3 – micro-granturi

6 × max. 19.833,3 € = 119.000 €; intensitate 100%; plata în două tranșe: 80% la
semnarea contractului de grant și 20% după finalizare și dovada îndeplinirii a
minimum 90% din obiectivele asumate.

## 4. Calendarul

Luna L1 este socotită de la semnarea contractului (08.09.2026). Datele sunt
estimative și trebuie confirmate cu clauza din contract.

| Activitate | Vers. 1 (aprobată) | Vers. 2 (mod. 1, în aprobare) | Perioada reală după vers. 2 |
|---|---|---|---|
| A1 Recrutarea personalului | L1 | L1–L2 | 08.09 – 07.11.2026 |
| A2 Campania de informare și promovare | L1–L2 | L1–L5 | 08.09.2026 – 07.02.2027 |
| A3 Fluxul operațional al schemei | L2–L21 | L2–L21 | 08.10.2026 – 07.06.2028 |
| A4 Lansarea apelului (ghid, publicare, sesiuni de informare) | L2 | L5–L7 | 08.01 – 07.04.2027 |
| A5 Schimbul de bune practici | L2–L4 | L5–L8 | 08.01 – 07.05.2027 |
| A6 Depunerea și înregistrarea proiectelor | L2–L3 | L6–L8 | 08.02 – 07.05.2027 |
| A7 Evaluarea (30 de zile calendaristice) | L3–L4 | L7–L8 | 08.03 – 07.05.2027 |
| A8 Soluționarea contestațiilor | L4 | L8 | 08.04 – 07.05.2027 |
| A9 Raportul final de selecție | L4 | L8 | 08.04 – 07.05.2027 |
| A10 Raportul de activitate intermediar | L4 | L8 | 08.04 – 07.05.2027 |
| A11 Contractarea, implementarea și monitorizarea | L4–L20 | L9–L20 | 08.05.2027 – 07.05.2028 |
| A12 Verificările pe teren (2 pe proiect) | L5–L20 | L9–L20 | 08.05.2027 – 07.05.2028 |
| A13 Raportul final de activitate | L21 (în Gantt v1: L20–L21) | L21 | 08.05 – 07.06.2028 |

Termene din metodologie: depunere 30 de zile calendaristice; evaluare max. 30 de
zile; contestații 5 zile lucrătoare pentru depunere și 5 pentru soluționare;
raportul final de selecție la 3 zile după contestații; contractare în max. 15 zile
lucrătoare de la notificare; implementarea sub-proiectelor max. 12 luni;
monitorizarea sustenabilității 36 de luni după finalizare; raportul final în max.
10 zile lucrătoare; cererea de plată finală în max. 10 zile lucrătoare de la
avizarea raportului final.

## 5. Parametrii concursului de micro-granturi

- Solicitanți eligibili: unități de învățământ (grădinițe, școli, licee) din
  teritoriul GAL și ONG-uri active în educația pentru mediu, cu
  sediu/sucursală/activitate dovedită în teritoriu, cu personalitate juridică.
- Inițiative eligibile: conștientizare (aer, apă, păduri, reciclare, resurse
  regenerabile, biodiversitate, schimbări climatice, transport cu emisii scăzute);
  activități practice (reciclare, colectare selectivă, plantări, ecologizare);
  activități culturale în școli (teatru, scenete, after-school, pictură); sport
  legat de mediu; concursuri cu drone; achiziții de active și echipamente pentru
  protecția mediului.
- Juriu mixt: min. 3 angajați GAL și 2 experți externi, aceștia din urmă voluntari
  și neremunerați; instruire prealabilă; declarații de imparțialitate,
  confidențialitate și evitare a conflictului de interese; scorul este media
  aritmetică a evaluatorilor.
- Criterii: ore de voluntariat (asociate sub-proiectului și celor
  organizate/sprijinite de GAL), proiecte comunitare, calitatea planului de
  intervenție, capacitatea de implementare demonstrată la interviu. Maximum 100 p.,
  prag minim 50 p. Finanțarea se acordă în ordinea descrescătoare a punctajului.
- Dosarul: cerere de finanțare (formular-tip), plan de intervenție, buget
  detaliat, acte privind forma juridică, declarația de numire a coordonatorului,
  CI-ul reprezentantului legal, dovezi ale capacității financiare, alte documente
  specifice.
- Depunerea exclusiv online (link Google Drive în Anexa 1); o singură rundă de
  clarificări, cu răspuns în 5 zile lucrătoare; fără modificări de fond.
- Comisia de contestații este diferită de cea de evaluare; decizia este finală la
  nivelul GAL.
- Consiliere pentru solicitanți (fizic/online), fără consultanță la scrierea
  proiectelor.
- Ținte: minimum 20 de potențiali beneficiari informați; 2 campanii (online și
  offline); 2 sesiuni de informare; 1 ghid; 1 apel; 6 contracte; min. 2 vizite pe
  proiect; 1 schimb de bune practici; rata contestațiilor sub 10%; 1 raport
  intermediar; 1 raport final.

## 6. Neconcordanțe și riscuri identificate

| # | Problemă | Unde | Ce propun |
|---|---|---|---|
| 1 | Bugetul din Anexa 1 §9 (schimb 10.000 €, total 139.903,3131 €) nu corespunde cu CF-ul (8.740 € eligibil + 1.259 € TVA neeligibil; 138.643 € eligibil) și nici cu fundamentarea, care trece 9.999,81 € ca „valoare eligibilă”. | Anexa 1, Fundamentare, CF | Referința este bugetul din contract. TVA-ul de 1.259 € se acoperă din fonduri proprii. |
| 2 | 6 × 19.833,3 = 118.999,80 €, nu 119.000 €. | Anexa 1, Fundamentare | Ghidul GAL fixează plafonul la maximum 19.833,3 €, deci în ghidul sub-proiectelor plafonul este 19.833,30 €, iar 0,20 € din Cap. 3 rămân neutilizați. Ghidul trebuie să precizeze și moneda bugetelor și cursul folosit. |
| 3 | Schimbul de bune practici este „pentru beneficiarii selectați”, dar e programat înainte de selecție: L2–L4 în v1, L5–L8 în v2. Selecția se încheie abia în L8. | Gantt v1/v2, Nota nr. 1 | Dacă nota mai poate fi completată înainte de aprobare: A5 în L8–L10 sau L9–L11. Altfel, evenimentul se ține la finalul L8, după publicarea raportului final de selecție. |
| 4 | Fereastra A11 (L9–L20) are 12 luni, cât durata maximă a unui sub-proiect, deci nu mai rămâne timp pentru vizita din perioada de monitorizare, tranșa a II-a și raportul final (L21). | Anexa 1 §7f, Gantt v2 | Ghidul să limiteze sub-proiectele la circa 9–10 luni, cu finalizare cel târziu în L18–L19. |
| 5 | Postul de animare locală e bugetat la plafonul de 5–10 ani (80 lei net/oră). Nota afirmă că bugetul postului se menține. | Fundamentare, Nota nr. 1 | Trebuie verificat că Iancu Dănuț are 5–10 ani de experiență relevantă. Altfel plafonul scade la 70 lei/oră. |
| 6 | Toți cei 3 experți ai proiectului sunt în comisia de evaluare, iar comisia de contestații trebuie să fie diferită. | Anexa 1 §7, §11 | Comisia de contestații se formează din alți angajați ai GAL sau din alte persoane, prin decizie separată. |
| 7 | CF-ul declară că metodologia acoperă „situațiile de incompatibilitate privind înscrierea în concurs” și contribuția la R.27, dar Anexa 1 nu le descrie. | CF (criterii eligibilitate), Anexa 1 | Ghidul să conțină explicit incompatibilitățile solicitanților și modul de raportare R.27. |
| 8 | Anexa 1 §11 crit. 3 promite „concursul pentru cele mai de impact 2 sub-proiecte”, care nu apare nicăieri altundeva. | Anexa 1 | De clarificat dacă rămâne; dacă nu, nu îl preluăm în ghid. |
| 9 | Anexa 1 §1 dă perioada „iunie 2026 – februarie 2028”. Cu contractul din 08.09.2026, perioada devine circa sept. 2026 – iun. 2028. | Anexa 1 | Documentele noi folosesc lunile L1–L21 și datele reale. |
| 10 | Fundamentare: „Planul de afaceri” în loc de „Planul de intervenție”; la consumabile prețul unitar este 369, deși totalul e 82,64; „~8 participanți”, deși 6 beneficiari + 3 experți = 9. | Fundamentare | Le corectăm în documentele noi (contract de grant, caietul de sarcini pentru schimb). |
| 11 | La A9, rezultatul din CF dublează A10 („1 raport final și 1 raport de activitate intermediar”). | CF | Doar de reținut la raportare. |
| 12 | Depunerea printr-un folder Google Drive partajat ridică riscuri de confidențialitate și GDPR (solicitanții se pot vedea între ei) și nu oferă dovada orei de depunere. Linkul pare și trunchiat. | Anexa 1 §7i | Formular cu încărcare de fișiere într-un folder restricționat sau e-mail dedicat cu confirmare și număr de înregistrare. |
| 13 | Campaniile de promovare și sesiunile de informare nu au linie de buget. | Anexa 1, CF | Se acoperă din timpul experților sau din bugetul de funcționare al GAL, cu atenție la dubla finanțare. |
| 14 | Nota menționează minimum 10/20 de participanți pe grupă la acțiunile de informare/formare. Schimbul de bune practici are ~8–9 participanți. | Nota nr. 1, Fundamentare | De verificat în manualul DR-36 dacă limita se aplică schimbului și sesiunilor de informare. |
| 15 | Raportul net/brut 70/108 pare să nu includă impozitul pe venit și CAM-ul de 2,25%. La contractele part-time, contribuțiile pot fi datorate la nivelul salariului minim. | Fundamentare | De verificat cu contabilul. Diferențele se suportă din fonduri proprii. |
| 16 | Tranșa I înseamnă 80% × 119.000 = 95.200 € de plătit în L9. Avansul AFIR la proiectele umbrelă este de cel mult 50% din activitățile GAL de sprijin pentru solicitanți: circa 4.370 € dacă se socotește doar schimbul de bune practici, circa 9.821 € dacă intră și personalul. Ghidul de implementare DR-36 Rev. 3 nu acoperă deci granturile. | Fundamentare; Ghid implementare DR-36 | Plan de flux de numerar și graficul de eșalonare a cererilor de plată înainte de L9: fonduri proprii sau credit, apoi rambursare. |
| 17 | Monitorizarea sustenabilității durează 36 de luni după finalizarea sub-proiectelor, mult după finalul proiectului GAL (L21). | Anexa 1 §12 | Un plan de monitorizare ex-post cu resurse proprii. |

## 7. Istoric de finanțări ale GAL (din CF – pentru documente de capacitate)

PNDR 2014-2020: centru de incluziune socială; Leader Enjoy Wine; Experiența celor
4 sezoane; Enport Beta; Say cheese! Balkan cheese!; lanțuri scurte pomicole
(2 proiecte); lanțuri scurte lavandă; formare fermieri NV; MIRELA C; BEE SMART,
BEE HEALTHY; Children and youth camp (climă, 2025). FSE/POCU: stagii de practică
NV; Incluziune socială GAL Napoca Porolissum; Parteneriat pentru formare și
ocupare (6255/20.06.2024); UNIC-Porolissum (1848/20.02.2025, 1.990.225). Erasmus+:
Go Aut and Live; Let's green, digital and animate rural inclusive territories;
Rural community ADAPTs to natural forest fires!; Rural Youth Parliament; Circular
Organic Management; SMART+CULTURE; Green education; YouProclima; ALL4JOBS; BEYOND a
Hiking for a Greener Future. AFM: Alege Verde!; Pune verdele în mișcare!. CERV:
Voices of change.

## 8. Constatări din Ghidul solicitantului, metodologie și documentele AFIR (02.10.2026)

Detaliate în `Int5_Comunicare_si_vizibilitate_analiza.docx`, secțiunile 2–7 și 11. Pe scurt:

- **Vizibilitate:** placa informativă este obligatorie la sediul GAL (model AFIR
  V3 „Placă FEADR LEADER”, 50 × 70 cm). Mai sunt obligatorii caseta pe prima
  pagină a site-ului, cu link către pagina Comisiei despre FEADR, informarea pe
  fiecare canal social media și cele trei mențiuni obligatorii pe materialele
  tipărite și multimedia. Siglele folosite pe alte materiale decât cele din
  Anexa II cer aprobarea scrisă a AFIR.
- **Ordinea siglelor (AFIR GIV V3):** UE „Cofinanțat de Uniunea Europeană” ·
  MADR · PS 2023-2027 · GAL · AFIR, iar LEADER pe un rând separat. Manualul GAL
  are altă ordine; aplicăm AFIR.
- **Evenimente:** graficul calendaristic actualizat, cu locații și agendă, se
  încarcă în platformă cu ≥ 10 zile lucrătoare înainte. Listele de prezență se
  fac pe zile, cu adresă, telefon, e-mail și semnătură. Fiecare participant
  declară că n-a mai participat la evenimente cu aceeași temă. Dacă peste 50%
  din chestionare au note sub 3, activitatea nu se avizează. La vizita OJFIR
  participă un reprezentant al GAL.
- **Juriul** are obligatoriu număr impar de membri și reprezentanți ai
  domeniului din județ sau regiune.
- **Criteriile de selecție nu pot fi afectate prin modificări:** rămân minimum
  3 angajați GAL în juriu și minimum 4 sub-proiecte contractate (ținta e 6).
- **Incompatibilitate:** echipa, asociații și angajații GAL nu pot fi angajați
  sau asociați ai entităților finanțate. GAL nu poate cumpăra servicii sau
  bunuri de la beneficiarii granturilor.
- **Tranșele granturilor:** cea inițială ≤ 90%, cea finală ≥ 10%, după
  realizarea a ≥ 90% din acțiuni. Fundamentarea greșește trimiterea la „planul de
  afaceri”.
- **Raportul de activitate intermediar** se trimite la AFIR în ≤ 10 zile
  lucrătoare de la selecție. Avizarea lui deblochează contractele de grant.
  Răspunsul vine în 6 zile lucrătoare, cu o singură retransmitere permisă.
- **Metodologia** are calendarul vechi. Criteriul „proiecte comunitare” e ambiguu
  (experiență anterioară sau angajament?), iar criteriul „calitatea planului” nu
  are punctaje pe subcriterii.
- **Neeligibile la sub-proiecte:** echipamente second-hand, mijloace de transport
  (atenție la biciclete), cheltuieli de dinainte de contractul de grant, TVA
  recuperabil.
- **Costurile de vizibilitate** ale sub-proiectelor pot fi eligibile prin
  derogarea LEADER (Reg. 2022/129, Anexa III pct. 2 lit. a, b, e).
- **Indicatorul R.27** are valoarea 2 în ghid; CF-ul nu dă un număr.
- **Cursul AFIR pentru 2026** este 5,0968 lei/euro (ghidul DR-36). Fundamentarea a
  folosit 5,0979 (09.03.2026).
