# Raport de progres nr. 1 – UNIC (SMIS 352704)

Perioada de raportare: 01.07.2026 – 30.09.2026 (L1–L3).

| Fișier | Ce este |
|---|---|
| `RP1_UNIC_352704_Raport_de_progres.docx` | Documentul de lucru: A – nota managerului de proiect (termene, limite de caractere, probleme de rezolvat înainte de transmitere); B – textul raportului, câmp cu câmp, în ordinea din MySMIS2021, cu contorul de caractere; C – documentele de încărcat și denumirile fișierelor. |
| `RP1_UNIC_352704_text_MySMIS.txt` | Doar textele de copiat în MySMIS, cu numărul de caractere pe câmp. |
| `build_rp1_docx.py`, `rp1_engine.py` | Sursa: textele se modifică în `build_rp1_docx.py`, apoi `python3 build_rp1_docx.py` regenerează ambele fișiere și afișează contorul. |
| `analize/` | Notele de analiză folosite: cererea de finanțare v12 (N4), Manualul beneficiarului v5, ghidurile (GSCS 8.F, GSCG), modelul RP 8, documentele de implementare din Drive. |

Marcajul «...» (galben în docx) = informație de confirmat sau completat înainte de copiere.
Limitele de caractere: Manualul de utilizare MySMIS2021 FO – Raport de progres (v2, sept. 2024).

## Antet oficial (de la 07.10.2026)
Toate documentele proiectului se generează pe șabloanele primite de la Managerul de proiect:
`livrabile/Antet_subsol_UNIC_Porolissum_PEO_A4_portret.docx` (implicit) și
`livrabile/Antet_subsol_UNIC_Porolissum_PEO_A4_peisaj.docx` (pentru tabele late).
Antetul: titlul proiectului + „Proiect cofinanțat din Fondul Social European Plus prin Programul
Educație și Ocupare 2021-2027 | Cod MySMIS 352704”, cu siglele UE, Guvern, GAL și UNIC; subsolul cu bandă grafică.
`rp1_engine.py` și `build_sa31_doc.py` pornesc din șablonul portret (marginile și antetul rămân cele din șablon).

## Documentul justificativ SA5.2 (formarea cadrelor didactice)

`build_sa52_doc.py` generează `livrabile/SA 5.2_09.2026_Formarea cadrelor didactice.docx` pe șablonul portret: fișa activității, recrutarea cadrelor didactice și identificarea furnizorului, contractul + ordinul de începere + transmiterea lor, acreditarea și calendarul, e-mailul de debut și suportul de curs, o selecție de 24 de capturi din sesiunile Google Meet (10, 15, 16.09.2026), raportul de participare din 10.09, corespondența și etapele următoare. Imaginile comprimate sunt în `livrabile/sa52_img/` (capturile originale, 48 de fișiere, și înregistrarea video rămân în Drive, folderul „Desfățurare curs”).

`build_texte_doc.py` generează `livrabile/RP1_texte_SA1.1_A4_A5.docx` – textele de progres SA1.1 + A4/A5 pe antetul oficial, cu numărul de caractere pe câmp, pentru revizuire înainte de MySMIS.

## Anexele 13 și 14 (Manualul beneficiarului)
- `livrabile/Anexa 13_Lista experti_RP 1_UNIC_352704.docx` – lista experților, 21 de rânduri (un rând pe expert și lună), completată după modelul Anexei 13 din RP 8 al proiectului PIDS 329335: categorie cu nivel de experiență (>10 ani / 5–10 ani / <5 ani, conform echipei din CF v12), „Lider – Asociația Grupul de Acțiune Locală Napoca Porolissum”, coduri S.A., luni cu majusculă. Pontajele Responsabilului financiar pentru iulie–august (Dumitrescu) există în Drive (încărcate 07–13.10.2026).
- `livrabile/Anexa 14_Lista livrabile_RP 1_UNIC_352704.docx` – centralizatorul livrabilelor, cu antetul din modelul RP 8 (denumire proiect, cod SMIS, nr. RP, beneficiar, partener – nu este cazul) și un singur rând pentru 352704, cu mențiunea „Nu este cazul” (fără livrabile de tip studii/analize/strategii/curricula/ghiduri/platforme/manuale în RP 1).
- Generate din șabloanele oficiale cu scriptul din scratchpad `anexe_src/fill.py` (python-docx; rânduri clonate din șablon, formatare Trebuchet MS 12 pt păstrată).
- `sectiuni/05_indicatori.txt` / `livrabile/RP1_texte_sectiunea_5_indicatori.docx` – textele pentru secțiunea 5 Indicatori (EECO06+07 „Copii și tineri” – 98 de elevi intrați în operațiune: 17 / 35 / 46; 5SO14 și 5SR09 – 0). Valoarea 98 este cea raportată în MySMIS; registrul GT din 14.10 are 97 de intrări până la 30.09 (vezi FLAG în raport).

## Documentele lunare SA 3.1 (informare și publicitate)
- `livrabile/SA_3.1_Informare_si_publicitate_UNIC_352704_IULIE_2026_3.docx` – versiunea curentă pentru iulie (pornind de la varianta echipei cu fotografiile de la Turda): fotografiile afișului din avizierul Liceului Tehnologic „Vlădeasa” Huedin (Figurile 7–8), figurile următoare renumerotate 9–14; `..._IULIE_2026_2.docx` rămâne ca istoric. `..._AUGUST_2026_2.docx` – documentul echipei completat cu link-urile postărilor verificate online.
- `livrabile/SA_3.1_Informare_si_publicitate_UNIC_352704_SEPTEMBRIE_2026_3.docx` – versiunea curentă pentru septembrie: postarea din 17.09, cele 3 postări LinkedIn din 29.09, link-uri corectate și (v3) secțiunea 5.6 cu captura de pe site a secțiunii „Metodologii” (versiunea 2 a Metodologiei GT publicată la 15.09.2026), prima pagină a PDF-ului și rândul 1 în tabelul recapitulativ. Versiunea _2 rămâne ca istoric.
- Scripturi de patch (scratchpad): `sa31v2/patch_docs.py`, `sa31v3/patch_sept3.py`, `sa31v4_src/patch_iulie3.py`; capturi: `sa31v3/site_view_3.jpg`, `sa31v3/met_v2_p1.jpg`.
