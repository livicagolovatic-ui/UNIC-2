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
