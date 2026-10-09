# Unde sunt minutele în Google Drive (doar citire!)

**Nu modifica, nu redenumi, nu muta și nu șterge nimic din Drive.** Documentele existente servesc
doar ca model. O minută nouă se încarcă în Drive numai dacă utilizatorul cere explicit, ca **fișier nou**
(`create_file`), în folderul lunii corespunzătoare.

| Proiect | Cale | ID folder |
|---|---|---|
| UNIC (PIDS) | PIDS- UNIC › 4. Implementare › Minute_intalniri de lucru › `<Luna AAAA>` (ex. „Octombrie 2026”) | `11QDd9sAtJBTisHxDHiwY4XGZHrRHUozK` |
| UNIC2 (PEO) | PEO-UNIC 2 › 3. IMPLEMENTARE › 6. Întâlniri de lucru › `<n. Luna AAAA>` (ex. „3. Septembrie 2026”) | `1IO6M9_IZ8osLT7ZwDvS14sp2vAtvI2X4` |

Subfolderele lunare: `search_files` cu `parentId = '<ID>'` (rezultatele sunt paginate – urmează
`nextPageToken`, altfel „lipsesc” luni).

Denumiri uzuale (generatorul le folosește implicit):
- UNIC: `Minuta_intalnirii_DD.MM.YYYY_online.docx` / `_fizic` / `Minuta_intalnirii_DD.MM.YYYY_financiar_UNIC.docx`
- UNIC2: `Minuta_UNIC2_DD.MM.YYYY_fizic.docx` / `_online` (în Drive există și „Minuta_UNIC_25.09.2026_fizic”,
  „Minuta_UNIC 2_18.09.2026_Zoom” – denumirea finală o alege utilizatorul; `-o` o suprascrie)

Modele folosite la construirea șablonului (pentru reverificare dacă se schimbă antetul):
- UNIC: `Minuta_intalnirii_06.10.2026_financiar_UNIC.pdf` (antet nou), `Minuta_intalnirii_UNIC_Porolissum_21.09.2026_online` (antet vechi, cu bandă de logo POIDS)
- UNIC2: `Minuta_UNIC_25.09.2026_fizic.pdf`, `Minuta_UNIC 2_18.09.2026_Zoom.pdf`

Dacă antetul se schimbă: descarcă noul PDF (`download_file_content`), `pdfimages -png` pentru
logo-uri (imaginea + `smask` = transparența) și `pdfplumber` pentru poziții/fonturi/culori, apoi
actualizează `assets/` și constantele din `build_minuta.py`.
