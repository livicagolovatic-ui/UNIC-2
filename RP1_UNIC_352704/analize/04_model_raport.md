# 04. Analiza modelului de Raport de progres (RP nr. 8, alt proiect) – structură, stil, anexe, șablon pentru RP nr. 1

> **Scop:** extragem din modelul primit (RP nr. 8 al unui alt proiect, program PIDS, MySMIS2021) **forma**: structura secțiunilor din MySMIS, formulările, modul de construire a textului, denumirea documentelor și anexelor, aspectele pe care se pune accent. **Nu** se preiau datele factuale ale proiectului-model.
>
> **Sursa analizată:** folderul Google Drive „model” (ID `1k3DlojQZC5E9TagxVgr4b0cv8BqdnNdh`), listat recursiv integral (toate paginile de rezultate parcurse). Exportul MySMIS `RaportProgres_8_..._2026-08-14_18-52-00.pdf` (223 pagini) a fost descărcat și extras **integral** cu `pdftotext` (citirea directă prin Drive se oprea la pagina 80/223). Au fost citite integral: Anexa 13 (xlsx + docx), Centralizator livrabile (docx), Centralizator proiecte (docx), centralizatorul de copii unici (docx), rapoarte de monitorizare, o minută de întâlnire, o fișă de pontaj, un raport de activitate expert („Doc act”), un dosar de indicator EECO06, o compilație de fișe de direcționare, o compilație de excursie, dosarul de achiziție exportat din MySMIS, fundamentarea procentului pentru închirierea auto. Restul fișierelor (în majoritate scanări mari, 10–45 MB) au fost analizate după denumire, dosar și tipul de document.
>
> **Protecția datelor:** în acest document numele persoanelor (copii, părinți, experți, membri ai comisiilor) au fost înlocuite cu `[Nume]`. Nu se reproduc CNP-uri, adrese sau date de contact.
>
> **Observație de context:** în „Centralizator proiecte_Beneficiar si Partener 1” al modelului apare, la același solicitant, un proiect PEO aflat în implementare din 01.07.2026 (cod SMIS 352704, „UNIC – Uniți pentru Nevoile Incluzive și Continuitatea Educației Elevilor”). Este posibil să fie proiectul nostru. **Aceasta este o deducție și trebuie confirmată.** Dacă se confirmă, RP nr. 1 acoperă primele luni de implementare, începând cu iulie 2026.

---

## 1. Inventarul folderului-model și convențiile de denumire

### 1.1. Inventar complet (structura de foldere)

Legendă tip: PDF / DOCX / XLSX / FOLDER. Numele de persoane din titluri sunt anonimizate.

```
/ (folder model)
├── RaportProgres_8_329335_2026-08-14_18-52-00.pdf ........ PDF – exportul MySMIS al RP (223 pag.), semnat digital
├── Anexa 13_Lista experți_RP 8.xlsx ...................... XLSX – lista experților (sursă editabilă)
├── Anexa 13_Lista experți_RP 8.docx ...................... DOCX – aceeași listă, format Word cu note de subsol
├── Anexa 13_Lista experți_RP 8.pdf ....................... PDF – versiunea semnată, încărcată în MySMIS
├── Centralizator livrabile_RP 8.docx / .pdf .............. DOCX + PDF – centralizatorul livrabilelor (studii, ghiduri etc.)
├── Centralizator proiecte_Beneficiar si Partener 1.docx / .pdf  DOCX + PDF – proiectele PEO/PIDS/POCU ale beneficiarului și partenerului
├── Registru Grup Țintă_RP 8.pdf .......................... PDF – exportul MySMIS al registrului GT, semnat digital
├── centralizator copii unici_ Maguri_iun-iul 2026.docx ... DOCX – centralizatorul copiilor unici (partener)
│
├── SA 2.1/ ............................................... FOLDER – documente justificative SA 2.1 + participarea la activități
│   ├── SA 2.1_06-07.2026_Servicii de kinetoterapie.pdf
│   ├── SA 2.1_07.2026_Servicii organizare excursii.pdf
│   └── PARTICIPARE ACTIVITĂȚI/
│       ├── MODEL DOC abandon scolar IUNIE (.docx/.pdf) ........ coperți-separator pe tip de activitate și lună
│       ├── MODEL DOC consiliere psihologica P / NP IUNIE|IULIE (.docx/.pdf)
│       ├── MODEL DOC consiliere vocationala IUNIE|IULIE (.docx/.pdf)
│       ├── MODEL DOC fise directionare copii IUNIE|IULIE (.docx/.pdf)
│       ├── MODEL DOC masuri acompaniere IUNIE|IULIE (.docx/.pdf)
│       ├── iunie 2026/
│       │   ├── SA1.2_06.2026_Fișe direcționare copii.pdf
│       │   ├── SA 2.1_06.2026_Consiliere vocaționala și activități suport.pdf
│       │   ├── SA 2.1_06.2026_consiliere psihologică și suport.pdf
│       │   ├── SA 3.1_06.2026_ consiliere psihologică și suport.pdf
│       │   ├── SA 3.1_06.2026_Activități de prevenire a abandonului școlar; sensibilizare și conștientizare.pdf
│       │   └── SA 4.1_06.2026_ Măsuri de acompaniere a familiei.pdf
│       └── iulie 2026/
│           ├── SA1.2_07.2026_Fișe direcționare copii.pdf
│           ├── SA 2.1_07.2026_Consiliere vocaționala și activități suport.pdf  (+ „... suport 1.pdf”, a doua parte)
│           ├── SA 2.1_07.2026_consiliere psihologică și suport.pdf
│           ├── SA 3.1_07.2026_ consiliere psihologică și suport.pdf
│           └── SA 4.1_07.2026_ Măsuri de acompaniere a familiei.pdf
│
├── SA 5.1/ ............................................... FOLDER – management
│   ├── SA5.1_06.2026_raport monitorizare coordonator.pdf ..... raport lunar al coordonatorului partenerului
│   ├── SA5.1_06.2026_raport monitorizare manager.pdf ......... raport lunar al managerului de proiect
│   ├── SA5.1_07.2026_raport monitorizare coordonator.pdf
│   ├── SA5.1_07.2026_raport monitorizare manager.pdf
│   ├── Întâlniri de lucru/
│   │   ├── SA 5.1_05.06.2026_Întâlnire de lucru centre.pdf
│   │   ├── SA 5.1_18.06.2026_Întâlnire de lucru financiar.pdf
│   │   ├── SA 5.1_22.06.2026_Întâlnire de lucru online.pdf
│   │   ├── SA 5.1_03.07.2026_Întâlnire de lucru centre.pdf
│   │   ├── SA 5.1_13.07.2026_Întâlnire de lucru financiar.pdf
│   │   └── SA 5.1_21.07.2026_ Întâlnire de lucru online.pdf
│   └── Rapoarte de activitate&livrabile/
│       ├── Fișe pontaj/
│       │   ├── 06.2026/  (20 fișiere)  SA 5.1_FP_06.2026_<Funcție>_<Nume>.pdf
│       │   └── 07.2026/  (17 fișiere)  SA 5.1_FP_07.2026_<Funcție>_<Nume>.pdf
│       └── RA&Livrabile/
│           ├── iunie 2026/ (15 fișiere) SA x.y_Doc act_06.2026_<Funcție>_<Nume>.pdf
│           └── iulie 2026/ (12 fișiere) SA x.y_Doc act_07.2026_<Funcție>_<Nume>.pdf
│
├── SA 6.1/ ............................................... FOLDER – informare și publicitate
│   ├── SA 6.1_06.2026_Informare și Publicitate.pdf ........... linkuri + capturi de ecran ale postărilor
│   └── SA 6.1_07.2026_Informare și Publicitate.pdf
│
├── Indicatori de realizare_EECO06/ ....................... FOLDER – dosarele persoanelor raportate la indicator în perioadă
│   ├── EECO06_[Nume copil 1].pdf  (≈12 MB)
│   └── EECO06_[Nume copil 2].pdf  (≈21 MB)
│
└── achiziții/ ............................................ FOLDER – achiziții
    ├── 1. Achiziție servicii organizare excursii.pdf
    ├── 2. Achiziție servicii închiriere auto.pdf
    ├── 3. Servicii de kinetoterapie.pdf
    ├── 4. Achiziție pachete de rechizite.pdf
    ├── 5.  Achiziție servicii hrană.pdf  / 5.1 / 5.2 / 5.3 Achiziție servicii hrană.pdf
    ├── 6. Achiziție servicii de organizare tabere și excursii.pdf
    ├── achizitie tabere/ (31 fișiere = dosarul procedurii, numerotat 0–30)
    │   ├── 0. Decizie numire comisie de evaluare.pdf
    │   ├── 1. Anunt publicitar.pdf
    │   ├── 2. Nota estimativa privind determ val_tabere si excursii.pdf
    │   ├── 3. Caiet de sarcini_tabere_excursii.pdf
    │   ├── 4. Referat_de_necesitate_tabere_excursii.pdf
    │   ├── 5. Strategia_de_contractare_tabere_excursii.pdf
    │   ├── 6. Instructiuni_catre_ofertanti_tabere_excursii.pdf
    │   ├── 7. Formulare.pdf
    │   ├── 8. Dovada publicare anunt de participare.pdf
    │   ├── 9.–11. Decl. de impartialitate_[Nume].pdf (câte una pentru fiecare membru al comisiei)
    │   ├── 12.–14. Oferta Lot 1_s / Lot 2_s / Lot 3_s.pdf
    │   ├── 15. Dovada primire oferte lot1,2,3.pdf
    │   ├── 16. PV deschidere oferte.pdf
    │   ├── 17. PV evaluare garantie de participare.pdf
    │   ├── 18. PV evaluare doc de calificare.pdf
    │   ├── 19. Anexa1 la PV evaluare tehnica.pdf
    │   ├── 20. Solicitare de clarificari_propunere tehnica.pdf
    │   ├── 21. Dovada transmitere solicitare clarificari.pdf
    │   ├── 22. PV evaluare tehnica.pdf
    │   ├── 23. PV evaluare financiara.pdf
    │   ├── 24. Raportul procedurii.pdf
    │   ├── 25.–27. Comunicare Lot1_s / Lot2_s / Comunicare - respingere oferta_Lot3.pdf
    │   ├── 28. Dovada transmitere_confirmare _comunicari.pdf
    │   ├── 29.–30. Contract_Lot 1_Tabere in strainatate / Contract_Lot 2_Tabere in tara.pdf
    │   └── DosarAchizitieOriginal_<cod>_<data>.pdf ......... exportul MySMIS al dosarului de achiziție
    └── CR 12 (iunie - iulie 2026)/ ....................... documentele pentru cererea de rambursare aferentă perioadei
        ├── Excursie [Locație]/ Deviz excursie, Diagrama de cazare, Lista de prezenta_excursie, PV excursie,
        │                        RAPORT DE ACTIVITATE excursie, Tabel centralizator, poze excursie, 1. Achiziție ... .pdf
        ├── Kinetoterapie/  Centralizator servicii kinetoterapie, Deviz, Factura, PV kinetoterapie,
        │                   Servicii kinetoterapie mai/iunie/iulie.pdf
        ├── Rechizite/  Borderou rechizite_CR11, Decizie repre. legal, Deviz, Extras de cont, Factura, Nota fundamentare
        │               rechizite, OP_plata rechizite, Proces verbal, Procedura_acordare_subventii_rechizite, [Nume copil].pdf
        ├── Închiriere auto/  2. Achiziție ... .pdf, Deviz factura, Factura, Fundamentarea procentului propus_iun-iul,
        │                     PV inchiriere auto, Procedură internă privind închirierea auto [nr. auto],
        │                     Iunie 2026/ (Deplasari ..._autoturism inchiriat, Tabel centralizare masina)
        │                     Iulie 2026/ (Deplasari autoturism inchiriat_iulie, Tabel centralizare masina)
        ├── Deplasări/  Iunie 2026/ și Iulie 2026/: BF <nr>_<data>_<Nume>.pdf (bonuri fiscale de combustibil),
        │               OD <nr>_<lună>_<Nume>.pdf (ordine de deplasare), Centralizatorul_deplasarilor - <Lună>.pdf
        └── Masa/ (gol)
```

**Ce s-a încărcat efectiv în MySMIS (secțiunea „Documente atașate la Raportul de Progres”, 110 fișiere), pe tip de document:**

| „Document tip” ales în MySMIS | Ce fișiere s-au încărcat cu acest tip |
|---|---|
| Alte documente | Centralizator proiecte, Centralizator livrabile, Anexa 13 Lista experți, minutele întâlnirilor de lucru (SA 5.1_<data>_Întâlnire de lucru ...) |
| Document aferent grupului țintă | `SA x.y_<lună>_<tip activitate>.pdf` (participare la activități), fișele de direcționare, compilațiile de kinetoterapie și excursie |
| Document aferent implementării contractelor de achiziție | `1.–6. Achiziție ... .pdf` (câte un PDF pentru fiecare contract sau procedură) |
| Document aferent resurselor umane implicate | rapoartele de monitorizare SA5.1, `SA x.y_Doc act_<lună>_<Funcție>_<Nume>`, `SA 5.1_FP_<lună>_<Funcție>_<Nume>` |
| Registru Grup Țintă | `Registru Grup Țintă_RP 8.pdf` |
| Document informare și publicitate | `SA 6.1_<lună>_Informare și Publicitate.pdf` |
| Document aferent indicatorilor de realizare (încărcat în secțiunea 5) | `EECO06_<Nume participant>.pdf` (câte un fișier pentru fiecare persoană nouă raportată la indicator) |

### 1.2. Convenția de denumire (pattern-uri de reutilizat)

| Tip document | Pattern | Exemplu de pattern (anonimizat) |
|---|---|---|
| Anexă numerotată conform Manualului beneficiarului | `Anexa <nr>_<Denumire>_RP <nr>` | `Anexa 13_Lista experți_RP 1` |
| Centralizatoare cerute de AM/OI | `Centralizator <obiect>_RP <nr>` | `Centralizator livrabile_RP 1`, `Centralizator proiecte_Beneficiar si Partener 1` |
| Registru GT | `Registru Grup Țintă_RP <nr>` | `Registru Grup Țintă_RP 1` |
| Folder pentru fiecare subactivitate | `SA x.y` | `SA 2.1`, `SA 5.1`, `SA 6.1` |
| Document de activitate pentru o lună | `SA x.y_<LL.AAAA>_<Tip activitate>` | `SA 6.1_07.2026_Informare și Publicitate` |
| Document pentru mai multe luni | `SA x.y_<LL-LL.AAAA>_<Serviciu>` | `SA 2.1_06-07.2026_Servicii de kinetoterapie` |
| Întâlnire de management | `SA 5.1_<ZZ.LL.AAAA>_Întâlnire de lucru <tip>` (tipuri folosite: centre / financiar / online) | `SA 5.1_05.06.2026_Întâlnire de lucru centre` |
| Raport lunar de monitorizare | `SA5.1_<LL.AAAA>_raport monitorizare <manager/coordonator>` | `SA5.1_07.2026_raport monitorizare manager` |
| Fișă de pontaj | `SA 5.1_FP_<LL.AAAA>_<Funcție>_<Nume>` | `SA 5.1_FP_06.2026_Expert GT 1_[Nume]` |
| Raport de activitate + livrabile expert | `SA x.y_Doc act_<LL.AAAA>_<Funcție>_<Nume>` | `SA 1.2_Doc act_07.2026_Asistent social 1 B_[Nume]` |
| Dosar indicator | `<Cod indicator>_<Nume participant>` | `EECO06_[Nume]` (în folderul `Indicatori de realizare_EECO06`) |
| Dosar de achiziție (pentru RP) | `<nr>. Achiziție <obiect>` (sub-numerotare pentru tranșe: 5, 5.1, 5.2, 5.3) | `3. Servicii de kinetoterapie` |
| Piesele procedurii de achiziție | `<nr. ordine>. <Denumire piesă>` în ordinea cronologică a procedurii (0 = decizia comisiei ... 30 = contract) | `16. PV deschidere oferte` |
| Folder pentru cererea de rambursare | `CR <nr> (<luni an>)` | `CR 12 (iunie - iulie 2026)` |
| Deplasări | `OD <nr>_<lună an>_<Nume>`, `BF <nr>_<data>_<Nume>`, `Centralizatorul_deplasarilor - <Lună an>` | — |
| Coperți-separator | `MODEL DOC <tip activitate> <LUNĂ>` | `MODEL DOC consiliere vocationala IUNIE` |

**Reguli de denumire observate:**
1. Fiecare fișier începe cu **codul subactivității** („SA x.y”), ca să fie clar de ce activitate ține.
2. Urmează **perioada** (`LL.AAAA`) sau data exactă (`ZZ.LL.AAAA`) și apoi **tipul de document sau activitate**.
3. Documentele de resurse umane se termină cu **funcția și numele expertului**. Funcția este scrisă exact ca în Tabelul resurselor umane, cu sufixul B (beneficiar) sau P (partener) și codul centrului.
4. Documentele de achiziție sunt **numerotate**, iar piesele unei proceduri urmează ordinea cronologică.
5. Separarea pe luni se face prin sub-foldere (`iunie 2026/`, `iulie 2026/`, `06.2026/`, `07.2026/`).
6. Sufixul `_s` din titlu marchează documentele semnate sau scanate.
7. Anexele standard folosesc numărul din Manualul beneficiarului (Anexa 8 = fișă de pontaj, Anexa 10 = raport de activitate, Anexa 13 = listă experți RP). Aceste numere se văd pe documentele din interior.

---

## 2. Structura exactă a Raportului de progres exportat din MySMIS

Exportul are format A4 landscape, este generat de MySMIS („openhtmltopdf”) și are paginare „n/223”. Ordinea secțiunilor și etichetele câmpurilor sunt redate mai jos exact cum apar.

### 2.0. Antet (completat automat de sistem)
- `RAPORT DE PROGRES NR. <n>`
- Tip raport: `Periodic - Altă perioadă`. Alte valori întâlnite în calendar: `Periodic - Lunar`, `Periodic - Trimestrial`.
- `Cod <id raport>`
- `Numele beneficiarului:`
- `Nr. înregistrare beneficiar:` · `Dată înregistrare beneficiar:` · `Versiune:`
- `Număr contract / Dată semnare contract:`
- `Titlul proiectului:`
- `Cod SMIS:` · `Versiune proiect:`
- `Prioritate:`
- `Obiective specifice:`
- `Perioada de implementare a proiectului: de la ... până la ...`
- `Perioada de raportare: de la ... până la ...`
- Titlu intermediar: `PERIOADA DE IMPLEMENTARE`

### 2.1. Tabel-sinteză: secțiuni, tip de conținut, volum folosit în model

Caracterele au fost numărate cu spații, după extragerea textului din PDF și eliminarea etichetelor și a numerelor de pagină. Valorile sunt aproximative (±3%).

| Nr. | Secțiune (etichetă MySMIS) | Tip conținut | Cine completează | Volum folosit în model |
|---|---|---|---|---|
| 1 | `1. Rezumatul proiectului` | text liber | preluat din cererea de finanțare | ≈ 7.040 car. |
| 2 | `2. Modificări ale contractului / deciziei de finanțare aprobate pe parcursul perioadei de raportare` | tabel: **Tip** (Notificare / Act adițional / Contract inițial) · **Dată semnare** · **Versiune proiect** · **Observații** (text) | sistem + beneficiar (Observații) | 186 – 1.999 car. pe rând. Modelul listează **toate** modificările de la semnarea contractului, nu doar pe cele din perioadă. |
| 3 | `3. Calendar de raportare` | tabel: **Tip Raport** · **Dată limită transmitere** · **Observații** | sistem + beneficiar | Observații: de regulă doar „Perioada de raportare: <luni>”; un rând are o frază despre respectarea termenului de 30 de zile |
| 4 | `4. Activități implementate și rezultate obținute pe parcursul perioadei de raportare. Abateri survenite față de graficul de implementare/calendarul proiectului` | bloc repetat pentru fiecare activitate și subactivitate (vezi 2.2) | sistem + beneficiar | „Progres” între 3.599 și 8.677 car. pe subactivitate |
| 5 | `5. Indicatori` → `5.1. Indicatori de realizare și indicatori de rezultat (program)` → `5.1.1. De realizare:` / `5.1.2. De rezultat:`; `5.2. Indicatori suplimentari` (5.2.1 / 5.2.2) + `Documente atașate` | tabel: Indicator · Tip de regiune · Tip · Unitate de măsură · Țintă · **Valoare realizată în perioada raportată** · Detalii indicatori tip întreprinderi/procent/dezagregare · **Informații valoare raportată** (text) + „Sumar indicatori ...” (automat) | beneficiar: valoarea din perioadă + text | text ≈ 775 car. pentru EECO06; „-” unde valoarea este 0 |
| 6 | `6. Grup țintă în perioada de raportare` → `A. Registru grup țintă - participant`, `B. Registru grup țintă - entitate` | tabel generat automat din MySMIS (vezi 4.3) | sistem | ~134 pagini. Registrul este **cumulat** (toți participanții, cu datele de intrare și ieșire). |
| 7 | `7. Graficul de achiziții și stadiul derulării procedurilor de achiziții pe contracte` | tabel: Aplicant · Titlu · Descriere · Tip · Perioada (L..–L..) · Valoare TVA · Valoare estimată fără TVA · Valoare totală estimată · **Stadiu** (text) · **Etapă achiziție** (listă: *Procedură în pregătire* / *Contract în implementare* / *Contract finalizat*) | sistem (din Planul de achiziții) + beneficiar (Stadiu, Etapă) | Stadiu: ≈ 100 – 650 car. pe rând |
| 8 | `8. Informații privind contractele de achiziții semnate ...` → `8.1. Contracte achiziții semnate`, `8.2. Acte adiționale achiziții` | tabel: Nume contract · Cod contract · Număr/Dată semnare · Valoare fără TVA · TVA · Total · Durată luni · Durată zile · Autoritate contractantă · Ofertanți · **Descriere** (text). La 8.2 se adaugă: Nume act adițional · Cod act · Număr act. | sistem (din dosarele de achiziție) + text | Descriere ≈ 500 – 700 car. |
| 9 | `9. Situație avize, acorduri, autorizații, recepții și execuție contracte de achiziții, inclusiv dificultăți întâmpinate și întârzieri` → `9.1. Avize, acorduri, autorizații, recepții și execuție contracte de achiziție` / `9.2. Dificultăți întâmpinate și întârzieri` | text liber | beneficiar | 9.1 ≈ 5.004 car.; 9.2 = „-” |
| 10 | `10. Evidența echipamentelor (...)` | tabel: Nume · Număr recepție · Dată recepție | sistem / beneficiar | listă cumulată de echipamente |
| 11 | `11. Stadiul garanțiilor de bună execuție și penalităților ...` → `11.1. Garanții de bună execuție`, `11.2. Penalități` | tabel: Număr · Dată · Valoare · Dată expirare · Aplicant · Contract achiziție · Număr/Dată contract · Act adițional · Număr/Dată act adițional (11.2: Valoare · Dată instituire · ... · Justificare) | beneficiar | „-” unde nu este cazul |
| 12 | `12. Resurse umane implicate în activitățile raportate (echipa de management+echipa de implementare), implicarea efectivă a partenerilor ...` | tabel: Nume · CNP/CIF · **Descriere** (text) · Tip (PERSOANA) · Categorii (Echipă de proiect) · Adăugată din proiect (Nu) | beneficiar | Descriere 680 – 1.663 car. pe persoană (20 persoane) |
| 13 | `13. Respectarea prevederilor privind ajutorul de stat / de Minimis` | text | beneficiar | „-” |
| 14 | `14. Respectarea cerințelor cu privire la comunicarea și vizibilitatea sprijinul din fonduri acordat în cadrul proiectului` | text liber | beneficiar | ≈ 5.517 car. (practic textul de la SA6.1) |
| 15 | `15. Principii orizontale și teme secundare` | text liber pe subsecțiuni (vezi 2.3) | beneficiar | 2.228 – 5.156 car. pe subsecțiune |
| 16 | `16. Stadiul implementării recomandărilor formulate în cadrul vizitei/vizitelor de verificare la fața locului .../recomandărilor formulate la aprobarea rapoartelor de progres anterioare` | bloc pentru fiecare vizită: Cod raport vizită la fața locului · Autoritate · Tip vizită · Scopul vizitei · Număr înregistrare · Recomandări / plan de măsuri · Stadiul implementării · **Observații** (text) | sistem + beneficiar | Observații ≈ 1.184 car. |
| 17 | `17. Stadiul îndeplinirii INDICATORILOR DE ETAPĂ. Abateri/întârzieri față de planul de monitorizare` | bloc pentru fiecare indicator de etapă: Nume indicator · Categorie (*Indicator de etapă de reper* / *de realizare*) · Criteriu validare · Valoare intermediară · Țintă · Unitate de măsură · Termen · Stadiu · **Justificare/Motive** · **Abatere întârziere** · **Măsură remediere** | sistem + beneficiar | Justificare 106 – 718 car. |
| 18 | `18. Calitatea liderului/partenerului în alte proiecte` | tabel: Nume aplicant · Lider · Cod SMIS · Nume proiect · Entitate finanțatoare · Dată semnare · Eligibil beneficiar · Nerambursabil beneficiar · Dată început · Dată sfârșit | sistem (din profil sau cererea de finanțare) | — |
| 19 | `19. OBSERVAȚII IMPORTANTE PENTRU SUCCESUL PROIECTULUI / PROPUNERI PENTRU PERIOADA URMĂTOARE ÎN VEDEREA PREÎNTÂMPINĂRII EVENTUALELOR DEFICIENȚE LA MOMENTUL RAPORTĂRII` | text liber | beneficiar | ≈ 1.067 car. |
| — | `Documente atașate la Raportul de Progres:` | tabel: Nume · Document tip · Încărcat din bibliotecă · Entitate juridică · Dată încărcare · Încărcat de | beneficiar (upload) | 110 fișiere |
| — | Declarația reprezentantului legal (punctele a–g) + Data, Nume și prenume, Semnătura | text standard al sistemului + semnătură electronică | sistem + semnătură | — |

### 2.2. Blocul repetat din secțiunea 4 (pentru fiecare activitate și subactivitate)

```
Activitate: <cod și titlu activitate din cererea de finanțare>
Obiectiv specific: <OS program>
Fond UE: Fondul Social European+
Tip: Precontractuală | Postcontractuală
Activitate de bază: Da | Nu
Dată început: · Dată finalizare: · Durată: <n> luni
Subactivități
  Subactivitate  SAx.y <titlu>
  Dată început · Dată finalizare · Durată
  Rezultate previzionate ........ (automat, preluat din CF: „RAx.y.z: <țintă> ... IMBUNATATIRI/ BENEFICII REALE: ...”)
  Parteneri implicați ............ (automat)
  Rezultat obținut în perioada de raportare ...... TEXT SCURT (beneficiar)
  Abateri/riscuri identificate .................. TEXT SCURT (beneficiar)
  Progres în perioada de raportare .............. TEXT LUNG (beneficiar)
```

**Ordinea activităților în export:** întâi activitățile care nu sunt „de bază” (A0 precontractuală, apoi A5 Management, A6 Informare și publicitate), apoi activitățile de bază (A1, A2, A3, A4). Activitatea precontractuală finalizată are doar: Rezultat „-”, Abateri „-”, Progres „Activitate finalizată în data de <dată>.”

**Volumul folosit în model în câmpurile completate de beneficiar:**

| Subactivitate | Rezultat obținut | Abateri/riscuri | Progres în perioada de raportare |
|---|---|---|---|
| SA0.1 (precontractuală, finalizată) | „-” | „-” | ≈ 45 car. |
| SA5.1 Management | ≈ 95 car. | 32 car. („Nu au fost identificate abateri.”) | ≈ 6.779 car. |
| SA6.1 Informare și publicitate | ≈ 115 car. | 32 car. | ≈ 5.395 car. |
| SA1.1 Selecție GT | ≈ 190 car. | 32 car. | ≈ 5.062 car. |
| SA1.2 Evaluare / management de caz | ≈ 55 car. | 32 car. | ≈ 3.599 car. |
| SA2.1 Centru de zi 1 | ≈ 480 car. (4 RA) | 32 car. | **≈ 8.677 car.** (maximul din raport) |
| SA3.1 Centru de zi 2 | ≈ 360 car. (3 RA) | 32 car. | ≈ 3.787 car. |
| SA4.1 Acompanierea familiei | ≈ 260 car. (2 RA) | 32 car. | ≈ 3.652 car. |

### 2.3. Subsecțiunile secțiunii 15 (cu volumul folosit)

| Subsecțiune | Completare în model |
|---|---|
| `15.1. Egalitate de șanse` → `15.1.1. Egalitate de gen` | ≈ 4.025 car. |
| `15.1.2. Nediscriminare` | ≈ 5.156 car. |
| `15.1.3. Accesibilitatea pentru persoanele cu dizabilități` | ≈ 4.592 car. |
| `15.1.4. Schimbări demografice` | lăsat gol |
| `15.2. Dezvoltare durabilă` → `15.2.1. Poluatorul plătește` | „-” |
| `15.2.2. Protecția biodiversității` | gol |
| `15.2.3. Utilizarea eficientă a resurselor` | ≈ 2.656 car. |
| `15.2.4. Reziliența la dezastre` | gol |
| `15.3. Aspecte de mediu (inclusiv aplicarea Directivei 2011/92/UE ...)` → `15.3.1 Imunizarea la schimbările climatice` | „-” |
| `15.3.2 Principiul ”do no significant harm” – DNSH` | ≈ 2.228 car. |
| `15.3.3 Măsuri de evitare și reducere a efectelor reziduale (Directiva SEA ...)` | gol |
| `15.4. Teme secundare` | ≈ 3.774 car. |

### 2.4. Limitele de caractere din MySMIS (estimare)

Exportul PDF **nu afișează limitele de caractere**. Din volumele folosite în model se pot face doar estimări:
- **Câmpurile lungi** (Progres pe subactivitate, secțiunile 14, 15.x, 9.1, Rezumat) au primit până la ~8.700 de caractere fără trunchiere vizibilă. Limita este probabil de **10.000 de caractere** (valoare des întâlnită în formularele MySMIS) sau mai mare.
- **Celulele de tabel** (Observații la secțiunea 2, Stadiu la secțiunea 7, Descriere la secțiunea 8 și 12, Justificare la secțiunea 17) au primit până la ~2.000 de caractere. Limita este probabil de **2.000 de caractere** (sau 4.000).
- **Câmpurile scurte** (Rezultat obținut, Abateri/riscuri) au fost folosite telegrafic, sub 500 de caractere.
- **Recomandare:** câmpurile lungi să rămână sub ~8.000 de caractere și celulele de tabel sub ~1.500. Limitele exacte trebuie verificate în formularul MySMIS (contorul apare la editare). **Atenție:** cifrele de mai sus sunt deduse, nu confirmate.

---

## 3. Modelul de redactare, pe câmpuri (cu fragmente anonimizate)

### 3.0. Reguli generale de stil, valabile în tot raportul
- **Persoana a III-a, diateza pasivă reflexivă sau pasivă, timpul perfect compus:** „au fost organizate”, „a fost transmisă”, „s-au desfășurat”, „au fost întocmite”, „expertul a realizat”. Persoana I nu apare în RP (apare doar în rapoartele de activitate ale experților: „Am întocmit...”).
- **Formula de deschidere aproape fixă:** „În perioada de raportare <luna1>–<luna2> <an>, ...” sau „În perioada <luna1>–<luna2> <an>, ...”.
- **Structură cronologică pe luni:** „În luna iunie <an>, experții au desfășurat următoarele activități:” → apoi **fiecare expert pe funcție** (fără nume în secțiunea 4; numele apar doar la secțiunea 12 și la modificările de echipă).
- **Activitățile se cuantifică mereu:** număr de activități, deplasări, participări, copii (distinct de „participări”), documente întocmite pe tipuri (de ex. „13 cereri de admitere; 9 fișe de evaluare; 2 anchete sociale”), localitățile și datele.
- **Paragraful de închidere** descrie documentarea: „Activitatea experților este documentată prin rapoarte individuale de activitate, livrabile, fișe de pontaj, minutele ședințelor și listele de prezență aferente.”
- Se folosesc liste cu puncte (MySMIS le păstrează) și liniuțe „–” pentru intervale de date (09–12.07.2026).
- Codurile se scriu consecvent: „SA1.2”, „SA 2.1”, „RA 2.1.4”, codul centrului (de ex. „Centru [cod serviciu social]”), „Partenerul UAT Comuna [X]”, „liderul de parteneriat”.
- Absența unui expert se explică explicit: „În luna iulie <an>, <Funcția> nu și-a mai desfășurat activitatea în cadrul SA x.y, întrucât nu a mai făcut parte din echipa de implementare ... În consecință, nu au fost raportate activități sau documente întocmite de acest expert pentru luna iulie.”

### 3.1. Secțiunea 2 – Observații la modificările contractului
**Tipar:** „În data de <ZZ.LL.AAAA> a fost transmisă Notificarea nr. <n>, prin care <s-a solicitat / a fost actualizată> <obiectul modificării>. <Justificarea>. Modificarea nu afectează valoarea totală a proiectului, obiectivele, activitățile, indicatorii, rezultatele asumate sau durata de implementare. Notificarea a fost aprobată prin <Informarea / Nota de informare> <OI> nr. <nr>/<dată>.”
- Formula de **neimpact** se repetă aproape identic la fiecare modificare.
- Pentru actul adițional: data depunerii solicitării, data semnării, secțiunile CF modificate și **temeiul** (de ex. modificarea cotei TVA printr-o lege nouă).

Fragmente anonimizate:
> „În data de [..] a fost transmisă Notificarea nr. [..], prin care a fost actualizată echipa de implementare a Partenerului [..], prin nominalizarea [..] pentru funcțiile de [..] și completarea corespunzătoare a secțiunii „Resurse umane” din cererea de finanțare. Modificarea nu afectează valoarea totală a proiectului, obiectivele, activitățile, indicatorii, rezultatele asumate sau durata de implementare. Notificarea a fost aprobată prin Informarea [OI] nr. [..]/[..].”

> „Modificarea a fost justificată prin necesitatea prevenirii unui posibil conflict de interese, având în vedere faptul că [..]. În notificare se precizează că, pentru respectarea principiilor de transparență, imparțialitate și bună gestiune financiară, atribuțiile ... urmau să fie preluate integral de noul expert propus, care îndeplinește cerințele prevăzute în fișa postului din cererea de finanțare.”

> „În data de [..] a fost semnat Contractul de finanțare cu nr. [..]. Data de începere a activităților proiectului este [..].” *(rândul „Contract inițial” este singurul rând de acest fel la RP 1)*

### 3.2. Secțiunea 3 – Calendar de raportare
Observații telegrafice: „Perioada de raportare: <luni an>”. Pentru raportul deja transmis: „Raportul de progres a fost transmis în data de [..], respectând termenul de maxim 30 de zile de la finalizarea perioadei de raportare pentru transmitere și cuprinde lunile de implementare L1-L3 ([..]).”

### 3.3. Secțiunea 4 – „Rezultat obținut în perioada de raportare”
**Tipar:** codul rezultatului din CF + **valoarea din perioadă** + formularea rezultatului, reluată aproape identic din CF (fără partea „IMBUNATATIRI/BENEFICII”). Câte un rând pentru fiecare RA atins în perioadă. RA-urile fără progres nu se trec.
> „RA 5.1.1: [n] întâlniri de lucru realizate; [n] rapoarte lunare de monitorizare/progres întocmite.”

> „R.A.1.1.2: [n] persoane selectate cu dosare complete de selecție și înregistrare GT (consimțământul pentru prelucrarea datelor cu caracter personal, documente personale, formulare înregistrare, declarații pe propria răspundere).”

> „RA 2.1.4: [n] de copii în risc de separare de familie ce beneficiază de servicii de [..] și sunt menținuți în familie”

> „RA 6.1.1: [n] anunțuri pentru ocuparea posturilor vacante în echipa Partenerului [..] publicate.”

Valoarea este cea **din perioadă**. Pentru serviciile acordate copiilor, numărul este de **copii unici** în perioadă, nu de participări.

### 3.4. Secțiunea 4 – „Abateri/riscuri identificate”
În toate subactivitățile: **„Nu au fost identificate abateri.”** Situațiile care ar putea părea abateri (expert plecat, post vacant, copii retrași și înlocuiți, factură care include și o lună anterioară) **nu sunt trecute aici**, ci sunt explicate neutru în câmpul „Progres”, cu soluția aplicată:
> „Doi copii menționați în perioada anterioară de raportare au renunțat la serviciu și au fost înlocuiți cu alți doi copii eligibili, fără modificarea numărului total de beneficiari.”

> „În luna [..], postul de [..] a devenit vacant și a făcut obiectul unei proceduri de recrutare, motiv pentru care nu sunt raportate activități distincte ale acestui expert pentru această lună.”

**Recomandare pentru RP 1:** dacă există o întârziere reală față de graficul din CF (de ex. o achiziție care încă nu a început), ea trebuie numită aici, cu o frază scurtă: abaterea, cauza, măsura și impactul asupra indicatorilor („fără impact asupra ...”).

### 3.5. Secțiunea 4 – „Progres în perioada de raportare” (câmpul principal)
**Structura-tip în 4 pași:**
1. **Fraza-umbrelă:** „În perioada de raportare <luni>, SA x.y a vizat <obiectul>. Activitățile au inclus <enumerare>.”
2. **Pe luni, apoi pe experți (funcții):** „În luna <..>, experții au desfășurat următoarele activități:” → „<Funcția> a <verb> ...” cu cifre, localități și date.
3. **Evenimente transversale** (excursie, tabără, serviciu externalizat), cu numărul de participanți și **documentul care atestă** („Participarea este documentată prin lista de prezență aferentă excursiei.”).
4. **Paragraful de documentare și coordonare:** participarea la ședințe și lista documentelor justificative.

Fragmente anonimizate:

*SA management (5.1)*
> „În perioada [..]–[..], activitatea de management a inclus coordonarea implementării subactivităților proiectului, monitorizarea activităților desfășurate de beneficiar și de Partenerul [..], ..., verificarea documentelor justificative și realizarea demersurilor de raportare tehnică și financiară.
> În ceea ce privește raportarea tehnică și financiară, au fost realizate următoarele demersuri:
> • în data de [..] a fost transmisă Cererea de prefinanțare nr. [..] pentru liderul de parteneriat – [..];
> • în data de [..] a fost transmis Raportul de progres nr. [..], aferent perioadei [..], acesta fiind autorizat în data de [..];”

> „În perioada de raportare au fost organizate [n] întâlniri de lucru ale echipei de proiect, dintre care [n] întâlniri fizice la sediul [..] și [n] întâlniri online, prin platforma [..]. ... În cadrul întâlnirii financiare din [..] au fost analizate pregătirea Cererii de rambursare nr. [..], centralizarea documentelor justificative și situația financiară a Partenerului ... Cele [n] întâlniri au fost documentate prin minute și liste de prezență, iar pentru întâlnirile online au fost realizate capturi de ecran.”

> „La nivel administrativ și financiar, au fost verificate pontajele, rapoartele de activitate, documentele privind grupul țintă, documentele aferente achizițiilor și contractelor, precum și documentele justificative pentru cheltuielile solicitate la rambursare.”

> „Comunicarea cu Partenerul [..] a fost asigurată prin participarea reprezentanților partenerului la întâlnirile de management fizice și online ... Aspectele financiare au fost gestionate prin comunicarea directă dintre departamentele financiare ale liderului de parteneriat și partenerului, iar aspectele operaționale au fost coordonate cu Coordonatorul de proiect P ...”

*SA selecție GT (1.1)*
> „Expertul GT 1: a verificat documentele aferente dosarelor de înscriere pentru copii din UAT [..]; a întocmit dosarele de înscriere pentru [n] copii ...; a completat listele de verificare a eligibilității și fișele criteriilor de selecție ...; a actualizat în platforma MySMIS formularele de înscriere pentru [n] copii din grupul țintă; ...”

> „Ambii experți au participat la ședințele echipei de implementare ..., contribuind la analiza situației grupului țintă, corelarea evidențelor, monitorizarea progresului indicatorilor și stabilirea măsurilor necesare pentru desfășurarea corespunzătoare a SA1.1.”

*SA servicii directe (2.1 / 3.1)*
> „Psihologul Centrului [..] a realizat [n] deplasări în [..], în cadrul cărora a lucrat cu [n] copii. A furnizat servicii de consiliere psihologică individuală și de grup ... Au fost utilizate chestionare, fișe de lucru, tehnici cognitiv-comportamentale ... Expertul a completat registrul de evaluare și consiliere pentru cei [n] copii și a întocmit [n] anexe aferente Planurilor de intervenție personalizată.”

> „În perioada [..], au fost organizate [n] ședințe de [serviciu externalizat], cu [n] participări și [n] copii din GT. Beneficiarii se află în etape diferite, fiecare urmând să efectueze un total de [n] ședințe.”

*SA acompaniere (4.1)* – listă datată pentru fiecare activitate:
> „[ZZ.LL.AAAA], [Unitate de învățământ / locație] – atelier de [..], cu [n] copii, pentru [scop];”

> „În perioada de raportare [n] copii unici au beneficiat de serviciul de masă. Această măsură a urmărit reducerea barierelor materiale și susținerea participării copiilor la activitățile proiectului.”

> „Activitățile au fost documentate prin minute, liste de prezență, fotografii, materiale de lucru, formulare de feedback, borderouri și liste privind serviciul de masă, documentele fiind centralizate și arhivate pentru justificarea progresului înregistrat în cadrul SA 4.1.”

*SA informare și publicitate (6.1)*
> „În luna [..] au fost realizate [n] publicări online, astfel: [n] postări pe pagina de Facebook a proiectului ([link]); [n] postări pe contul de Instagram al proiectului ([link]) ...”

> „Materialele publicate au respectat cerințele de informare și vizibilitate aplicabile proiectului, prin includerea elementelor obligatorii de identitate vizuală și a mențiunii privind cofinanțarea din Fondul Social European Plus, prin Programul [..]. Pentru fiecare material au fost centralizate linkurile și capturile de ecran care confirmă publicarea, acestea fiind păstrate ca documente justificative pentru activitățile raportate în cadrul SA 6.1.”

**Cum se face trimiterea la anexe și livrabile:** modelul **nu citează numele fișierelor** în text. Folosește formule generice („documentată prin rapoarte individuale de activitate, livrabile, fișe de pontaj ...”). Legătura cu dovezile se face prin **denumirea standardizată a fișierelor încărcate** (cod SA + lună). Excepțiile sunt documentele administrative, citate cu număr și dată („prin Decizia nr. [..]/[..] a încetat contractul individual de muncă ...”, „Notificarea nr. [..]”, „Informarea OI nr. [..]/[..]”).

### 3.6. Secțiunea 5 – „Informații valoare raportată” (indicatori)
**Tipar:** cifra din perioadă → cine a fost inclus → în ce activități a participat → ce a primit concret. Valoarea este **pe perioadă (necumulată)**. Cumulul apare doar la secțiunea 17. Unde valoarea este 0, câmpul rămâne „-”.
> „În perioada de raportare [..], [n] copii au fost incluși în grupul țintă al proiectului și au beneficiat de măsuri de sprijin în vederea [..], prin participarea la activitățile desfășurate în cadrul SA[..] și SA[..]. În cadrul SA[..], copiii au participat la activități de [..], care au urmărit [..]. În cadrul SA[..], au fost realizate activități de [..] ...”

La „Documente atașate” se încarcă **un PDF pentru fiecare persoană raportată în perioadă** (`<COD INDICATOR>_<Nume>`), cu tipul „Document aferent indicatorilor de realizare”.

### 3.7. Secțiunea 7 – „Stadiu” (graficul de achiziții)
Tiparul diferă după etapă:
- **Contract semnat:** „Procedura de achiziție a fost finalizată, iar cu operatorul economic [..] a fost încheiat Contractul de servicii nr. [..]/[..], având ca obiect [..] pentru [n] copii și [n] însoțitori. Valoarea contractului este de [..] lei fără TVA, la care se adaugă TVA în valoare de [..] lei, rezultând o valoare totală de [..] lei. Prestarea efectivă a serviciilor se va realiza în baza ordinului de începere emis de achizitor.”
- **Procedură în pregătire sau prelungită:** „Perioada de realizare a achiziției a fost prelungită de la L[..]–L[..] la L[..]–L[..]. În perioada de raportare au fost revizuite necesarul de [..], în vederea stabilirii cerințelor și pregătirii documentelor aferente achiziției.”
- **Lot anulat:** „... a fost depusă o singură ofertă la data de [..]. Oferta a fost respinsă ca neconformă, deoarece ofertantul nu a răspuns în termen la solicitarea de clarificări ... În lipsa unei oferte admisibile, procedura aferentă Lotului [n] a fost anulată și urmează să fie reluată.”
- **Contract finalizat:** formulă scurtă cu nr./dată contract, valoare + TVA, „Achiziție directă” / „Norme proprii pentru servicii Anexa 2B”.

### 3.8. Secțiunea 8 – „Descriere” (contracte semnate)
> „Autoritatea contractantă: Beneficiar. A fost încheiat Contractul de [servicii/furnizare] nr. [..]/[..] cu [..], pentru [..], în cadrul proiectului „[titlu]”, cod MySMIS [..]. Serviciile sunt destinate [..] în cadrul SA [..]. Valoarea estimată a contractului este de [..] lei fără TVA, la care se adaugă TVA de [..] lei, valoarea totală fiind de [..] lei. Contractul este valabil [n] luni, dar nu mai târziu de [..] ...”

La 8.2 (acte adiționale): „Prin actul adițional nr. [..]/[..] la contractul [..] nr. [..], a fost [actualizată valoarea / prelungit termenul], ca urmare a [cauza + temei legal].”

### 3.9. Secțiunea 9.1 – Recepții și execuția contractelor
**Tipar:** fraza introductivă, apoi o listă numerotată pe contracte („1. <Serviciu> – <Furnizor>”). Pentru fiecare contract: temeiul (nr./dată), **cantitățile din perioadă** (porții, ședințe, copii unici, participanți), **documentele verificate** (deviz, factură seria/nr./dată, PV de recepție/predare-primire, raportul prestatorului, centralizatoare, liste de prezență), **corelarea** cu activitățile și **excluderea explicită a cantităților din alte perioade**.
> „În perioada de raportare au fost verificate documentele de recepție aferente serviciilor prestate în lunile [..] și a fost urmărit stadiul contractelor și al achizițiilor aflate în curs.”

> „Deși factura cuprinde și servicii aferente lunii [..], în cadrul prezentului raport au fost luate în considerare exclusiv cele [n] porții furnizate în lunile [..]. Cantitățile menționate în deviz au fost verificate și corelate cu listele de prezență la activități, centralizatoarele lunare ale beneficiarilor și evidențele privind acordarea mesei calde.”

> „Numărul ședințelor din documentele prestatorului a fost corelat cu prezența copiilor și cu perioada efectivă de prestare.”

> „Furnizarea și recepția întregii cantități au fost documentate anterior perioadei raportate prin: factura [..]; Nota de recepție și constatare de diferențe – NIR nr. [..]; bonul de consum nr. [..]. În perioada de raportare ..., din stocul recepționat a fost acordat [n] pachet ... justificat prin borderoul de distribuire semnat de părintele/reprezentantul legal.”

9.2 Dificultăți: „-” dacă nu există.

### 3.10. Secțiunea 12 – „Descriere” (resurse umane)
**Tipar fix pentru fiecare persoană:**
```
Poziția: <funcția exact ca în CF, cu sufix B/P/Beneficiar/Partener>
Categorie: <Expert implementare <5 ani | >5 ani | Expert management de proiect >10 ani ...>
Perioada de activitate: <luni an>
În perioada de raportare, expertul a fost implicat în SAx.y, după cum urmează:
• realizarea a [n] activități ... / participarea la întâlnirile din [date] ...
• desfășurarea activităților în [localități];
• utilizarea [metode/instrumente];
• completarea minutelor, listelor de prezență, fișelor de lucru, registrelor ...;
• colaborarea cu [..];
• participarea la ședințele de lucru aferente lunilor [..].
```
- Lista folosește **substantive verbale** („realizarea”, „desfășurarea”, „organizarea”, „completarea”, „monitorizarea”, „participarea”).
- **Orele lucrate nu apar în RP.** Ele se găsesc în fișele de pontaj (Anexa 8) și în rapoartele de activitate (Anexa 10). Atenție: cifrele de activități din descriere trebuie să coincidă cu cele de la secțiunea 4 și 15 (în model: 47 de activități la psiholog = 27 + 20; 14 = 8 + 6 la consilierul vocațional).

Fragment anonimizat:
> „Poziția: Manager proiect – Beneficiar / Categorie: Expert management de proiect >10 ani / Perioada de activitate: [..] / În perioada de raportare, expertul a fost implicat în realizarea SA5.1 – Managementul proiectului, după cum urmează: coordonarea generală și monitorizarea activităților implementate de beneficiar și partener; organizarea și coordonarea întâlnirilor de lucru din [date]; ... verificarea documentelor justificative, a rapoartelor experților și a informațiilor necesare raportului de progres; menținerea comunicării cu partenerul, experții și instituțiile implicate în implementare.”

### 3.11. Secțiunea 14 – Comunicare și vizibilitate
Reia în esență textul de la SA6.1: numărul de postări pe canal și pe lună, link-urile canalelor, conținutul pe scurt, anunțurile de recrutare și paragraful de conformitate cu identitatea vizuală („includerea elementelor obligatorii de identitate vizuală și a mențiunii privind cofinanțarea ...”). Se precizează că dovezile sunt linkurile și capturile de ecran.

### 3.12. Secțiunea 15 – Principii orizontale
**Tipar pentru fiecare principiu:** fraza-umbrelă („În perioada de raportare [..], principiul [..] a fost respectat prin ...”), apoi **câte un paragraf pentru fiecare subactivitate** („În cadrul SA1.1, ...”, „În cadrul SA1.2, ...”, ..., „În cadrul SA5.1, ...”, „În cadrul SA6.1, ...”). Paragrafele reiau cifrele concrete din perioadă (activități, participări, fișe), apoi urmează o frază de concluzie sau constatare negativă.
> „Participarea beneficiarilor a fost stabilită în funcție de eligibilitate și de nevoile individuale identificate, fără aplicarea unor criterii diferite în funcție de sex sau gen.”

> „În cadrul SA6.1, materialele și postările publicate ... au prezentat activitățile proiectului fără mesaje, formulări sau reprezentări care să promoveze stereotipuri de gen.”

> „În perioada raportată nu au fost semnalate situații de excludere, restricționare a accesului sau tratament diferențiat pe criterii discriminatorii.”

> (DNSH) „... activitățile proiectului au avut caracter social, educațional ... Acestea nu au presupus lucrări de construcție, intervenții asupra terenurilor sau habitatelor, procese industriale ... și nu au generat efecte semnificative asupra mediului.”

> (Utilizarea eficientă a resurselor) „... ședințele online ... Documentele ... au fost transmise, verificate și centralizate preponderent în format electronic, reducând consumul de hârtie, toner ... Utilizarea canalelor online a redus necesitatea multiplicării ... materialelor tipărite.”

Subsecțiunile fără relevanță se lasă goale sau cu „-” (în model: Schimbări demografice, Poluatorul plătește, Biodiversitate, Reziliență, Imunizare climatică, SEA). **Recomandare pentru RP 1:** în loc de câmp gol, o frază scurtă de tipul „Nu este cazul pentru tipul de activități desfășurate în perioada de raportare.”

### 3.13. Secțiunea 16 – Recomandări din vizite
Observațiile reiau faptic: decizia sau numărul vizitei, data, intervalul orar, locațiile, subactivitatea verificată, numărul de participanți prezenți, numărul de persoane intervievate, concluzia („Nu au fost formulate recomandări sau măsuri suplimentare ...”). Câmpul „Stadiul implementării” are valoarea „Implementat”. **La RP 1**, dacă nu a avut loc nicio vizită: „Nu este cazul – în perioada de raportare nu au fost efectuate vizite la fața locului și nu au existat rapoarte de progres anterioare.”

### 3.14. Secțiunea 17 – Indicatori de etapă
Pentru fiecare indicator de etapă din planul de monitorizare: „Stadiu: Nu are termen scadent” → „Justificare/Motive” → „Abatere întârziere: Nu există abateri sau întârzieri.” → „Măsură remediere: Nu este cazul.”
> „Indicatorul nu are termen scadent în perioada de raportare. Activitatea de selecție și înregistrare a grupului țintă este în curs de realizare. În perioada aferentă raportării au fost înregistrați [n] [participanți] în GT ... Documente care probează îndeplinirea indicatorului: Dosare de grup țintă și documente care atestă participarea la activitățile din cadrul [..].”

> „... În registrul Grupului Țintă au fost înregistrați [n] participanți. În perioadele anterioare de raportare, în registru au fost incluși [n] participanți.” ← **aici apare cumulul**

> „Indicatorul ... nu a înregistrat progres în perioada de raportare, nefiind incluși [categorie] în lunile [..].”

Indicatorii de etapă de tip „Cereri de rambursare” și „Rapoarte de progres” se justifică prin documentele transmise în perioadă („au fost transmise cererea de rambursare nr. [..] ...”; „Raportul de progres aferent lunilor [..] a fost redactat și este în curs de transmitere.”).

### 3.15. Secțiunea 19 – Observații importante
Un singur paragraf (≈1.000 de caractere), pozitiv și sintetic. Cuprinde factorii de succes (echipa, partenerul, adaptarea la nevoi și la perioadă) și contribuția la obiective. Modelul **nu face propuneri** pentru perioada următoare, deși titlul o cere. **Recomandare pentru RP 1:** adăugați 2–3 propuneri sau măsuri preventive concrete.
> „Succesul proiectului în perioada de raportare [..] a fost susținut prin implicarea constantă a echipei de implementare, a partenerului și a experților specializați, precum și prin adaptarea activităților la nevoile [..]. Activitățile desfășurate au contribuit la [..] ...”

---

## 4. Analiza anexelor și a documentelor justificative

### 4.1. Anexa 13 – Listă experți RP (xlsx, docx, pdf semnat)
- **Antet:** „ANEXA 13 – Listă Experți RP” / „Listă experți care au derulat activități în perioada de raportare aferentă Raport de progres nr. [n]” / Denumire proiect / Cod SMIS / Perioada de raportare.
- **Coloane:** `Nr. crt.` · `Categorie expert` (de ex. „Expert management proiect >10 ani”, „Expert implementare proiect <5 ani”) · `Rol / Funcție` · `Nume și prenume expert` · `Nume Lider/Partener (L/P1/P2…/Pn)` (de ex. „Lider – Asociația [..]”, „Partener – Comuna [..]”) · `Activitate / Subactivitate` (formatul „S.A.5.1”) · `Luna, an` (de ex. „Iunie 2026”) · `Observații` (doar în xlsx, cu valoarea „-”).
- **Subsol:** „Data întocmirii” + „Semnătură”.
- **Reguli din notele de subsol:**
  1. Se raportează doar experții decontați pe bază de costuri reale.
  2. Experții trebuie să fie **aceiași** cu cei de la secțiunea 12 a RP.
  3. **Câte un rând pentru fiecare lună de activitate.** Un expert care a lucrat 2 luni are 2 rânduri.
- Un expert cu două funcții apare pe rânduri separate pentru fiecare funcție. Expertul plecat apare doar pentru luna în care a lucrat.

### 4.2. Centralizator livrabile_RP n (docx și pdf)
- **Antet:** Denumire proiect · Cod SMIS · „Nr. RP final” · Denumire Beneficiar · Denumire Partener 1 · titlu „Centralizator Livrabile RP nr. [n]”.
- **Coloane:** `Nr. crt.` · `Program (PEO/PIDS)` · `Obiectiv specific` · `Cod SMIS proiect` (proiecte finalizate și în implementare, finanțate prin PEO/PIDS, ale beneficiarului și partenerilor) · `Livrabile Studii/ Analize/ Strategii/Curricula/Ghiduri/ Platforme/ Manuale, realizate conform ultimului RT validat` · `Denumire Beneficiar/ Partener` · `Rol în cadrul proiectului (Beneficiar/ Partener)` · `Nume Expert implicat/ Experți implicați` · `Stare la RP curent (în realizare/ finalizat)` · `Data finalizării/ aprobării livrabilului` · `Nr. RP la care a fost transmisă versiunea finală/ aprobată`.
- **Utilizare în model:** câte un rând pentru beneficiar și pentru partener, cu „-” în coloanele de livrabile. Asta înseamnă că nu există livrabile de tip studiu, ghid sau metodologie în perioadă. Totuși, documentul se depune.
- **Pentru proiectul nostru (PEO):** dacă în RP 1 se realizează metodologii, ghiduri sau curricula prevăzute ca rezultate (în model, de ex. „RA 1.1.1 O Metodologie ...”), ele trebuie trecute aici, cu starea „în realizare” sau „finalizat”, experții implicați și data aprobării.

### 4.3. Registru Grup Țintă_RP n (export MySMIS, PDF semnat) – doar structura coloanelor
- **Coloane de identificare a participantului:** Nume · Prenume · CNP · Dată naștere · Gen · Email · Telefon · Naționalitate · Adresă și localitate de domiciliu · Județ, țară de domiciliu · Adresă și localitate de reședință · Județ, țară de reședință · Mediul de rezidență (Urban/Rural).
- **Coloane de situație:** Statutul pe piața muncii (de ex. INACTIV) · Nivelul studiilor (ISCED) · Participant cu dizabilități · Resortisant al unei țări terțe · Participant de origine străină · Aparține minorităților naționale (inclusiv etnie romă) · Locuiește într-o comunitate marginalizată · Persoană fără adăpost / excluziune locativă · Angajat al organizației beneficiarului sau partenerilor · Alte categorii defavorizate.
- **Coloane despre participarea în operațiune:** Data completării formularului · Data intrării în operațiune · Vârsta la intrare (ani) · Indicatori de realizare · Tip regiune · Data raportării indicatorului · **Activități conform CF** (activitatea sau subactivitatea și datele participării, de ex. „Grup suport parental: [dată], 3.1.3 consiliere psihologică: [dată]”) · Tip / Descriere activități · Categorie Grup Țintă · Data ieșirii din operațiune · Motivul ieșirii · Indicatori de rezultat (căutarea unui loc de muncă, studii, calificare, loc de muncă, activitate independentă la ieșire și la 6 luni) · Tip regiune și dată raportare indicator de rezultat · **Partener care a realizat recrutarea**.
- În RP (secțiunea 6.A) apare o versiune redusă: Nume și prenume · CNP · Adresă reședință · Categorie formular GT · Dată completare formular · Dată intrare operațiune · Dată ieșire operațiune · Indicatori de realizare · Indicatori de rezultat. Secțiunea 6.B (entități) are „-”.
- **Registrul este cumulat**, cu toți participanții de la începutul proiectului. ⚠ Conține date personale. Se încarcă doar în MySMIS, nu se distribuie.

### 4.4. Centralizator proiecte_Beneficiar si Partener 1 (docx și pdf)
- Titlu: „CENTRALIZATOR PROIECTE PEO, PIDS ȘI POCU”, apoi un tabel pentru SOLICITANT și un tabel pentru fiecare PARTENER.
- **Coloane:** `Nr. Crt.` · `Denumire proiect` · `Cod smis` · `Număr și data contractului de finanțare` · `Program de finanțare (PEO, PIDS, POCU)` · `Calitatea în proiect (Solicitant/ partener)` · `Perioada de implementare` · `Stadiu (finalizat, în implementare)`.
- Semnat de reprezentantul legal. Are legătură cu secțiunea 18 a RP și cu verificarea dublei finanțări și a încărcării experților în mai multe proiecte (coloanele „proiect 2/3” din fișa de pontaj).

### 4.5. Centralizator copii unici (docx, întocmit la partener)
- **Scop:** dovada numărării **unice** (nu a participărilor) pentru rezultatele RA și pentru măsura de masă caldă. Se folosește pentru „[n] copii unici” din RP.
- **Tabele:**
  1. „Centralizator copii unici care au beneficiat de masa calda”: Nr.crt. · Luna · Nr. unic copii. Rânduri pe lună și un rând „Luna1+Luna2”. **Totalul pe perioadă nu este suma lunilor**, ci numărul de copii unici din perioadă.
  2. „Centralizator copii unici care au participat la subactivitati”: Nr. Crt. · Luna · Subactivitate (codul rezultatului RA, de ex. 3.1.3) · Nr. copii unic, pe lună și pe perioadă.
  3. „Copii noi intrati”: Nr. crt. · Nume copii · Data intrare activitate (aceștia sunt cei raportați la indicator în perioadă).
- Antet și subsol cu datele de contact ale beneficiarului și partenerului.

### 4.6. Conținutul folderelor pe subactivități și al folderului de indicator

| Folder / fișier | Ce conține (tipuri de documente) |
|---|---|
| `SA x.y_<lună>_<tip activitate>.pdf` (PARTICIPARE ACTIVITĂȚI) | Copertă-separator („MODEL DOC ...”: titlul SA, tipul de activitate, luna). Urmează listele de prezență pe activitate (antet cu identitatea vizuală, „Proiect cofinanțat de UE din FSE+ prin Programul [..] – cod MySMIS [..]”, subactivitatea, data, locația, coloanele Nr. crt. / Nume și prenume / Semnătură, uneori „Cum te simți azi?”, mențiunea GDPR „Declar pe propria răspundere că îmi dau acordul cu privire la prelucrarea datelor cu caracter personal”), minutele activităților, fișele de lucru și lucrările copiilor, fotografiile. |
| `SA1.2_<lună>_Fișe direcționare copii.pdf` | Copertă + câte o „FIȘĂ DE DIRECȚIONARE COPIL” pentru fiecare copil: Nume copil · Localitate · Perioada direcționării · Servicii accesate · Observații · Nevoi identificate · Motivul direcționării · Recomandări · Alte observații (monitorizare/reevaluare) · semnătura facilitatorului. |
| `SA 2.1_<lună>_Servicii organizare excursii.pdf` | Copertă (SA, serviciu, perioadă, locație) + raportul de activitate al prestatorului + lista de prezență pe zile (semnături pe fiecare zi) + fotografii. |
| `SA 2.1_<luni>_Servicii de kinetoterapie.pdf` | Centralizatorul ședințelor + listele de prezență + rapoartele prestatorului. |
| SA 5.1 – `raport monitorizare manager/coordonator` | Raport lunar: I. Activități desfășurate (pe SA, cu cifre: activități, participări, porții, **copii unici în lună**) · II. Monitorizarea resurselor umane (plecări, pontaje depuse) · III. Informare și publicitate · IV. Concluzii. Semnat digital. |
| SA 5.1 – `Întâlniri de lucru/` | **Minuta**: Data · Durata (interval orar) · Modalitate (fizic / online, platforma) · Scop · Participanți (nume – funcție) · „Activitatea conform CF” · Aspecte discutate pe SA · Semnăturile participanților + lista de prezență sau captura de ecran. |
| SA 5.1 – `Fișe pontaj/<LL.AAAA>/` | **ANEXA 8 – Fișă individuală de pontaj**: expert, poziție, categorie, entitate angajatoare, Program/Cod SMIS/titlu (proiect 1, 2, 3), pentru fiecare zi: Nr. activității (SA), titlul activității, ore în proiectul 1, ore în alte proiecte PEO/PIDS, ore la același angajator în afara proiectelor, total. Semnături expert și reprezentant legal. Notă: **maximum 12 ore/zi și 60 ore/săptămână cumulat PEO+PIDS**. |
| SA 5.1 – `RA&Livrabile/<lună>/SA x.y_Doc act_...` | **ANEXA 10 – Raport de activitate** (lunar, pentru fiecare expert): Program, cod, titlu, Beneficiar/Partener, nume expert, poziție, nr. și tipul contractului, categorie; **1. Prezentare succintă** (tabel: Nr. crt. / Titlul activității / Responsabilități conform CF / Activitate prestată / Rezultate obținute / Livrabile / Realizat în comun cu alți experți Da/Nu / **Nr. ore lucrate**); **2. Detalierea activităților și a rezultatelor** (text, persoana I); **3. Întârzieri/probleme întâmpinate**. Urmează pagina „LIVRABILE <lună>” (lista livrabilelor) și **livrabilele propriu-zise** (de ex. fișe lunare de monitorizare către DGASPC, centralizatorul serviciului de hrană, centralizatoare de tabără, centralizatorul copiilor unici, licențe sau decizii, minute de activitate, liste de prezență). |
| SA 6.1 – `<lună>_Informare și Publicitate.pdf` | Pe canale (pagina proiectului, pagina partenerului, Instagram): lista **linkurilor** fiecărei postări + capturile de ecran. Semnat digital. |
| `Indicatori de realizare_EECO06/EECO06_<Nume>.pdf` | **Dosarul complet al participantului raportat**: formularul de înregistrare individuală MySMIS (secțiunile A/B/C, situația pe piața muncii, ISCED, categorii dezavantajate, ieșirea din operațiune, situația la 6 luni) semnat; Nota de informare GDPR + consimțământul + declarația de asumare; declarația de informare privind activitățile proiectului; **declarația de evitare a dublei finanțări**; declarația privind alergiile; certificatul de naștere sau actele de identitate „conform cu originalul”; fișa de verificare a eligibilității semnată de expertul GT; **ancheta socială**; dovezile participării la activități în perioadă (minută + listă de prezență + lucrări). ⚠ Date foarte sensibile (copii). |
| `achiziții/<nr>. Achiziție <obiect>.pdf` | Dosarul fiecărui contract pentru perioadă: contract / act adițional, devize, facturi, PV de recepție, rapoarte ale prestatorului, centralizatoare. |
| `achiziții/achizitie tabere/` | Dosarul complet al procedurii (0–30, vezi inventarul) + `DosarAchizitieOriginal_<cod>_<data>.pdf` (exportul MySMIS: publicare, loturi, comisie, ofertanți, oferte pe lot cu rezultatul evaluării, contracte, beneficiari reali, declarația reprezentantului legal). |
| `achiziții/CR <nr> (<luni>)/` | Suportul pentru cererea de rambursare: devize, facturi, PV, extrase și OP, borderouri, proceduri interne (de ex. acordarea subvențiilor pentru rechizite, închirierea auto), **fundamentarea procentului de decontare** (zile de utilizare pe SA, regula de trei simplă, pragul de eligibilitate de 50% din zilele lunii), foi de parcurs, ordine de deplasare, bonuri fiscale, centralizatoare de deplasări, diagrame de cazare, fotografii. |

---

## 5. Aspecte la care se atrage atenția (ce subliniază modelul, explicit sau implicit)

1. **Corelarea cifrelor în tot raportul.** Același număr (activități, participări, copii unici, fișe) apare în secțiunile 4, 12, 15 și 9.1 și în anexe. Modelul are câteva **neconcordanțe, de evitat la noi**: excursia apare ca 09–12.07 și ca 10–12.07; un an este scris „20226”; numărul de copii unici la masă din RP diferă de centralizatorul partenerului, fără explicație că primul este cumulat beneficiar + partener.
2. **„Copii unici” vs „participări”.** Modelul le separă peste tot („6 activități, cu 35 de participări”; „13 ședințe, cu 102 participări și 40 de copii”). Rezultatele RA și indicatorii se raportează în **persoane unice**, cu centralizator dedicat.
3. **Indicatori: perioadă vs cumulat.** La secțiunea 5 se trece **doar valoarea din perioadă**. Cumulul și „perioadele anterioare” se explică la secțiunea 17. Fiecare persoană raportată la indicator are un **dosar PDF** atașat la secțiunea 5.
4. **Fiecare afirmație are o dovadă:** „documentat prin minute, liste de prezență, fotografii, capturi de ecran, rapoarte individuale de activitate, livrabile, fișe de pontaj”. Dovezile au **nume standardizate** (SA + lună), ca să poată fi găsite ușor de ofițerul de monitorizare.
5. **Echipa de proiect:** modificările (încetări de contract, nominalizări prin notificare, posturi vacante, recrutare) se raportează cu **nr./dată decizie/notificare/informare OI**. Lunile fără activitate ale unui expert se explică explicit. Experții din Anexa 13 = cei din secțiunea 12 = cei cu fișe de pontaj (Anexa 8) și rapoarte de activitate (Anexa 10).
6. **Limita de ore și dubla finanțare:** fișa de pontaj cere orele din alte proiecte PEO/PIDS și de la același angajator (maximum 12 ore/zi și 60 ore/săptămână). Centralizatorul de proiecte și declarația de evitare a dublei finanțări (pentru GT) susțin această verificare.
7. **GDPR:** consimțământ și notă de informare în fiecare dosar GT. Mențiune GDPR pe listele de prezență. Datele copiilor apar **doar** în registrul GT și în dosarele de indicator, nu în textul RP. În textul RP, experții apar pe **funcții**, fără nume, cu excepția secțiunii 12 și a modificărilor de echipă.
8. **Achiziții:** stadiul fiecărei linii din Planul de achiziții (inclusiv cele „în pregătire”, cu prelungirea perioadei L..–L.. aprobată prin notificare). Lotul anulat se raportează transparent, cu motivul. Recepțiile se raportează cu cantitățile din perioadă și cu **excluderea cantităților din alte perioade**. Se fac trimiteri la NIR, bon de consum și borderou pentru stocuri.
9. **Formula de neimpact** la orice modificare: „nu afectează valoarea totală, obiectivele, activitățile, indicatorii, rezultatele asumate sau durata de implementare”.
10. **Abateri:** modelul scrie mereu „Nu au fost identificate abateri.” și tratează problemele în „Progres”, cu soluția aplicată (înlocuirea copiilor retrași „fără modificarea numărului total de beneficiari”, recrutare pentru postul vacant). Riscul este ca o abatere reală nedeclarată să fie considerată lipsă de transparență.
11. **Principii orizontale tratate pe fiecare subactivitate** (egalitate de gen, nediscriminare, accesibilitate, utilizarea eficientă a resurselor, DNSH) și tema secundară, **cu cifre concrete**, nu generic. Accesibilitatea este interpretată larg: acces fizic și geografic, comunicare adaptată, metode adaptate vârstei.
12. **Comunicare și vizibilitate:** numărul de postări pe canal și pe lună, link-uri, capturi de ecran, elemente obligatorii de identitate vizuală și mențiunea de cofinanțare. **La noi: mențiunea corectă a programului (PEO 2021-2027).** Modelul folosește variante inconsecvente: „Programul Incluziune și Demnitate Socială”, „POIDS”, „PoIDS”.
13. **Raportarea tehnică și financiară în SA5.1:** cererile de prefinanțare, rambursare și plată și rapoartele de progres transmise în perioadă, cu date. Se precizează și autorizarea RP anterior.
14. **Coerența cu indicatorii de etapă** (secțiunea 17): pentru fiecare indicator din planul de monitorizare, stadiul, justificarea, abaterea și măsura.
15. **Vizite de monitorizare:** se raportează chiar și fără recomandări, cu detaliile vizitei.
16. **Decontarea proporțională** (de ex. auto închiriat): fundamentare documentată pe zile de utilizare și pe SA, conform Manualului beneficiarului.
17. **Semnătura digitală** pe toate documentele încărcate (reprezentant legal + întocmitor). Rapoartele lunare și minutele sunt semnate de toți participanții.

---

## 6. ȘABLON – Raport de progres nr. 1 (pentru proiectul nostru PEO)

> Instrucțiuni: textul din `[...]` se înlocuiește. Formulările sunt adaptate stilului modelului. Cifrele trebuie corelate în toate secțiunile. RP 1 acoperă de la data începerii proiectului (`[ZZ.LL.AAAA]`) până la `[ZZ.LL.AAAA]`.

### Antet (completat automat de MySMIS) – de verificat
Nr. raport = 1 · Tip: Periodic – `[Lunar/Trimestrial/Altă perioadă]` · Contract `[nr./dată]` · Cod SMIS `[..]` · Versiune proiect · Perioada de implementare · **Perioada de raportare: de la `[..]` până la `[..]`**.

### 1. Rezumatul proiectului
Se verifică preluarea din CF. Nu se rescrie.

### 2. Modificări ale contractului / deciziei de finanțare
- Rândul „Contract inițial”: *„În data de [..] a fost semnat Contractul de finanțare cu nr. [..]. Data de începere a activităților proiectului este [..].”*
- Pentru fiecare notificare sau act adițional din perioadă: *„În data de [..] a fost transmisă Notificarea nr. [..], prin care [obiect]. [Justificare]. Modificarea nu afectează valoarea totală a proiectului, obiectivele, activitățile, indicatorii, rezultatele asumate sau durata de implementare. Notificarea a fost aprobată prin [Informarea/Nota de informare OI] nr. [..]/[..].”* (sub ~1.500 car. pe rând)

### 3. Calendar de raportare
Observații: *„Perioada de raportare: [luni an] (L1–L[n]).”*

### 4. Activități implementate și rezultate obținute. Abateri
Pentru **fiecare subactivitate** (în ordinea din export):

**Rezultat obținut în perioada de raportare** (scurt)
`RA x.y.z: [valoare în perioadă] [formularea rezultatului din CF]` – câte un rând pentru fiecare RA cu progres. Se folosesc **persoane unice**. Dacă nu există progres: „-” sau *„Subactivitatea nu a început în perioada de raportare, conform graficului (începe în L[n]).”*

**Abateri/riscuri identificate** (scurt)
*„Nu au fost identificate abateri.”* SAU *„[Abaterea] față de graficul din CF, cauzată de [..]. Măsura: [..]. Abaterea nu afectează [indicatorii/rezultatele/durata].”*

**Progres în perioada de raportare** (≤ ~8.000 car.)
1. *„În perioada de raportare [luni an], SA x.y a vizat [obiect]. Activitățile au inclus [enumerare].”*
2. *„În luna [..] [an], experții au desfășurat următoarele activități:”* → pe funcții: *„[Funcția] a [verb] [n] [activități] în [localități/unități], cu [n] participări și [n] [elevi/persoane] unice. [Metode/instrumente]. A întocmit [n] [documente].”*
3. Evenimente sau servicii externalizate: *„În perioada [..] a fost organizat/ă [..], la care au participat [n] [..]. Participarea este documentată prin lista de prezență aferentă.”*
4. *„În perioada de raportare, experții implicați în cadrul SA x.y au participat la ședințele echipei de implementare ... Activitatea experților este documentată prin rapoarte individuale de activitate, livrabile, fișe de pontaj, minutele ședințelor și listele de prezență aferente.”*

*Particularități pentru RP 1:*
- **SA Management:** constituirea echipei, ROF și proceduri interne (dacă sunt rezultate în CF), **ședința de lansare și ședințele lunare** (date, format, teme), rapoartele lunare de monitorizare, demersurile de raportare (cererea de prefinanțare nr. 1, RP 1), notificările privind echipa, pornirea achizițiilor (referate, strategii), comunicarea cu partenerii (dacă există).
- **SA Informare și publicitate:** planul de comunicare, comunicatul sau anunțul de lansare, crearea paginilor (Facebook/Instagram/site), afișul obligatoriu la sediu, numărul de postări pe canal și pe lună, cu link-uri, conformarea cu Manualul de identitate vizuală și mențiunea de cofinanțare **PEO 2021-2027**.
- **SA Grup țintă:** metodologia de selecție (dacă este rezultat), campania de informare, dosare verificate și eligibile, înregistrarea în MySMIS (formulare, consimțăminte), câte persoane noi, din ce localități sau unități de învățământ.
- **SA cu servicii directe:** doar dacă au început conform graficului.

### 5. Indicatori
- 5.1.1 / 5.1.2: **valoarea din perioadă** pentru fiecare indicator. „Informații valoare raportată” (≤ ~1.000 car.): *„În perioada de raportare [..], [n] [persoane] au fost incluse în grupul țintă ... și au beneficiat de [..] în cadrul SA[..] ... ”*. Unde valoarea este 0: „-” sau *„Indicatorul nu a înregistrat progres în perioada de raportare, conform graficului (selecția GT începe în L[n]).”*
- Documente atașate: `[COD INDICATOR]_[Nume Prenume].pdf`, câte unul pentru fiecare persoană nouă, cu tipul „Document aferent indicatorilor de realizare”.

### 6. Grup țintă
Se generează din MySMIS. Înainte de export se verifică formularele (data completării, data intrării, categoria GT, indicatorii, activitățile).

### 7. Graficul de achiziții (pentru fiecare linie)
- În pregătire: *„În perioada de raportare au fost [elaborate referatul de necesitate / nota estimativă / caietul de sarcini / strategia de contractare] pentru [..], în vederea [lansării procedurii în L[n]].”* → Etapa: Procedură în pregătire.
- Contract semnat: *„Procedura de achiziție a fost finalizată, iar cu operatorul economic [..] a fost încheiat Contractul de [..] nr. [..]/[..], având ca obiect [..]. Valoarea contractului este de [..] lei fără TVA, la care se adaugă TVA în valoare de [..] lei, rezultând o valoare totală de [..] lei.”* → Contract în implementare.
- Neînceput conform graficului: *„Achiziția este planificată în perioada L[..]–L[..]; nu au fost demarate demersuri în perioada de raportare.”*

### 8. Contracte semnate / acte adiționale
Descriere: *„Autoritatea contractantă: Beneficiar. A fost încheiat Contractul de [..] nr. [..]/[..] cu [..], pentru [..], în cadrul proiectului „[..]”, cod MySMIS [..]. [Bunurile/Serviciile] sunt destinate [..] în cadrul SA [..]. Valoarea ... Contractul este valabil [..].”* Dacă nu există contracte: „-”.

### 9. Avize, recepții, execuție contracte
9.1: *„În perioada de raportare au fost verificate documentele de recepție aferente [..] ...”*, apoi pe contracte: temei · cantități din perioadă · documente verificate (factură, PV de recepție, NIR, raportul prestatorului) · corelare. Dacă nu există: *„Nu este cazul – în perioada de raportare nu au fost efectuate recepții.”*
9.2: dificultăți sau întârzieri, ori „-”.

### 10. Evidența echipamentelor · 11. Garanții / penalități
Nume echipament · nr./dată recepție. Pentru 11: „-” dacă nu există.

### 12. Resurse umane (câte un bloc pentru fiecare expert activ în perioadă)
```
Poziția: [funcția exact ca în CF] – [Beneficiar/Partener]
Categorie: [Expert management/implementare <5 / 5-10 / >10 ani]
Perioada de activitate: [luni an]
În perioada de raportare, expertul a fost implicat în SA[x.y], după cum urmează:
• [realizarea/organizarea/elaborarea] ... ([n], [date], [localități]);
• ...;
• participarea la întâlnirile echipei de proiect din [date];
• întocmirea [rapoartelor/minutelor/listelor de prezență/livrabilelor].
```
(≤ ~1.500 car.) Lista trebuie să fie identică cu Anexa 13 și cu fișele de pontaj.

### 13. Ajutor de stat / de minimis
„-” sau *„Nu este cazul – proiectul nu intră sub incidența ajutorului de stat/de minimis.”* (de verificat în CF)

### 14. Comunicare și vizibilitate
Postările pe canal și pe lună (cu link-uri), afișul sau placa, comunicatul de lansare, conformarea cu MIV, mențiunea de cofinanțare din FSE+ prin **Programul Educație și Ocupare 2021-2027**, dovezile (linkuri și capturi) din `SA [x.y]_[LL.AAAA]_Informare și Publicitate.pdf`.

### 15. Principii orizontale și teme secundare
Pentru fiecare dintre: Egalitate de gen · Nediscriminare · Accesibilitate · Schimbări demografice (dacă este relevant) · Utilizarea eficientă a resurselor · DNSH · Teme secundare: fraza-umbrelă + *„În cadrul SA[..], ...”* pentru fiecare subactivitate activă, cu cifre + concluzie (*„În perioada raportată nu au fost semnalate situații de ...”*). La cele irelevante: *„Nu este cazul pentru tipul de activități desfășurate în perioada de raportare.”*

### 16. Recomandări din vizite / RP anterioare
*„Nu este cazul – în perioada de raportare nu au fost efectuate vizite la fața locului, iar prezentul raport este primul raport de progres.”* (sau detaliile vizitei, ca în model)

### 17. Indicatori de etapă
Pentru fiecare indicator de etapă din planul de monitorizare: Justificare *„Indicatorul are termenul [..] / nu are termen scadent în perioada de raportare. În perioada aferentă raportării [..]. Documente care probează: [..].”* · Abatere: *„Nu există abateri sau întârzieri.”* · Măsură: *„Nu este cazul.”* Dacă un termen a fost ratat: cauza, măsura și noul termen.

### 18. Calitatea liderului/partenerului în alte proiecte
Se verifică datele preluate și se corelează cu „Centralizator proiecte_Beneficiar si Partener [n]”.

### 19. Observații importante / propuneri
Un paragraf cu factorii de succes din perioada de debut + **2–3 propuneri concrete** pentru perioada următoare (de ex. calendarul selecției GT, pregătirea procedurilor de achiziție, standardizarea documentelor justificative).

### Documente atașate la RP 1 (listă de verificare, cu denumiri)
| Fișier | Tip document în MySMIS |
|---|---|
| `Anexa 13_Lista experți_RP 1.pdf` (+ xlsx intern) | Alte documente |
| `Centralizator livrabile_RP 1.pdf` | Alte documente |
| `Centralizator proiecte_Beneficiar si Partener [n].pdf` | Alte documente |
| `SA 5.1_[ZZ.LL.AAAA]_Întâlnire de lucru [tip].pdf` (fiecare ședință) | Alte documente |
| `SA5.1_[LL.AAAA]_raport monitorizare manager.pdf` (+ coordonator partener, dacă există) | Document aferent resurselor umane implicate |
| `SA 5.1_FP_[LL.AAAA]_[Funcție]_[Nume].pdf` (Anexa 8, fiecare expert și lună) | Document aferent resurselor umane implicate |
| `SA x.y_Doc act_[LL.AAAA]_[Funcție]_[Nume].pdf` (Anexa 10 + livrabile) | Document aferent resurselor umane implicate |
| `SA x.y_[LL.AAAA]_[Tip activitate].pdf` (participare: copertă + liste + minute + foto) | Document aferent grupului țintă |
| `Registru Grup Țintă_RP 1.pdf` | Registru Grup Țintă |
| `SA [6.1]_[LL.AAAA]_Informare și Publicitate.pdf` | Document informare și publicitate |
| `[nr]. Achiziție [obiect].pdf` / `DosarAchizitieOriginal_...pdf` | Document aferent implementării contractelor de achiziție |
| `[COD INDICATOR]_[Nume].pdf` (la secțiunea 5) | Document aferent indicatorilor de realizare |
| centralizator de persoane unice pe RA sau lună (intern, sau atașat ca „Alte documente”) | Alte documente |

**Verificări finale înainte de transmitere:** (1) aceleași cifre în secțiunile 4, 5, 12, 15, 17 și în anexe; (2) experții din Anexa 13 = secțiunea 12 = fișele de pontaj; (3) persoanele raportate la indicator = dosarele atașate = registrul GT; (4) numele programului PEO scris corect peste tot; (5) toate PDF-urile sunt semnate digital; (6) date calendaristice consecvente; (7) nu există date personale în textul liber.
