---
name: minuta-unic
description: Redactează minuta unei întâlniri de management / de lucru / financiare pentru proiectul UNIC (finanțat prin PIDS, UNIC – Porolissum, MySMIS 329335) sau UNIC2 (finanțat prin PEO, „Uniți pentru Nevoile Incluzive…”, SMIS 352704), direct pe șablonul și în stilul minutelor din Drive (antet UE/Guvern/UNIC, subsol GAL, semnături, poze). Folosește-l când utilizatorul dă poze și notițe dintr-o ședință și cere „minuta”, „minuta întâlnirii”, „fă minuta pentru UNIC/UNIC2/PIDS/PEO”, „ședința de management de azi”, „întâlnirea financiară”, chiar dacă nu spune „skill”. Generates meeting minutes (.docx + PDF) for the UNIC / UNIC2 projects.
---

# Minute de management – UNIC (PIDS) și UNIC2 (PEO)

Căile sunt relative la rădăcina repo-ului. Generatorul: `.claude/skills/minuta-unic/build_minuta.py`
(JSON → `.docx` pe șablon, opțional PDF + PNG pe pagini pentru verificare).

| Spune utilizatorul | `proiect` | Ce produce |
|---|---|---|
| UNIC, PIDS, UNIC Porolissum | `"UNIC"` | „Minuta întâlnirii de lucru”, text negru, „Activitatea 5 / S.A.5.1” (nu la `tip: financiar`), participanți cu „- ”, „Concluzii și măsuri stabilite:”, tabel semnături cu chenar negru |
| UNIC2, UNIC 2, PEO | `"UNIC2"` | bloc Beneficiar/Proiect/Cod SMIS/Activitatea A.1/S.A. 1.1, „Minuta întâlnirii de management” mov cu linie albastră, participanți cu „•”, titluri mov, concluziile ca ultim punct numerotat, tabel „Numele, prenumele și poziția / Semnătura” |

Ambele: antet cu logo UE + Guvern + UNIC și textul proiectului (Arial 8,5), subsol logo GAL, A4,
Times New Roman 12, poze la final. Geometria e măsurată din minutele din 25.09 și 06.10.2026.

## Flux de lucru (pentru fiecare minută)

1. **Ce proiect?** Dacă nu e clar din mesaj, întreabă: UNIC (PIDS) sau UNIC2 (PEO). Nu ghici: au
   antete, coduri SMIS și echipe diferite.
2. **Strânge datele**: data, ora început–sfârșit, fizic/online, participanții. Pentru nume și funcții
   folosește `reference/echipe.md`. Din captura Zoom poți citi lista de participanți, dar confirmă
   numele pe care nu le găsești acolo. Dacă lipsește ora, întreabă (durata se calculează din ore).
3. **Redactează conținutul** din notițe după `reference/stil_redactare.md`: scop, (introducere),
   4–7 puncte numerotate, concluzii/măsuri. Nu inventa decizii, cifre sau termene.
4. **Pozele**: salvează-le într-un folder de lucru (ex. `minute/poze_DD.MM/`). Orice format
   (JPG/PNG/WEBP, rotite de telefon) e normalizat automat.
5. **Scrie JSON-ul** (pornește de la `examples/`) și rulează generatorul cu `--preview`:

   ```bash
   python3 .claude/skills/minuta-unic/build_minuta.py .claude/skills/minuta-unic/examples/unic2_peo_25.09.2026_fizic.json --preview
   python3 .claude/skills/minuta-unic/build_minuta.py .claude/skills/minuta-unic/examples/unic_pids_06.10.2026_financiar.json --preview
   ```
   Ieșire implicită: `./minute/<denumirea uzuală>.docx` + `.pdf` + `_pagina-N.png`.
   Pentru alt nume: `-o minute/Minuta_UNIC2_12.10.2026_online.docx`.
6. **Uită-te la PNG-uri** (Read): antet, numerotare, tabel de semnături întreg, poze vizibile.
7. **Livrează** `.docx` (și `.pdf`) cu `SendUserFile`. Celula „Semnătura” rămâne goală: echipa
   semnează digital PDF-ul.
8. **Drive**: nu modifica nimic din Drive. Încarci ca fișier nou numai dacă ți se cere, în folderul
   lunii (vezi `reference/drive.md`).

## Formatul JSON

```json
{
  "proiect": "UNIC2",                      // "UNIC" (PIDS) | "UNIC2" (PEO)
  "tip": "management",                     // opțional; "financiar" la UNIC ascunde Activitatea 5 și dă numele _financiar_UNIC
  "data": "25.09.2026",
  "ora_inceput": "12:30", "ora_sfarsit": "14:00",   // sau "durata": "text liber"
  "modalitate": "Fizic, la sediul social str. Eroilor nr.6, bl.I1, ap.1, parter, Gilău, jud.Cluj",
  "scop": "Analizarea …",
  "participanti": ["Baba Alina-Ioana – Manager proiect", "…"],
  "nota_participanti": "opțional",
  "introducere": "opțional (la UNIC aproape mereu)",
  "puncte": [{"titlu": "…", "paragrafe": ["…", "…"], "liste": ["opțional"]}],
  "concluzii": {"titlu": "opțional", "paragrafe": ["…"], "masuri": ["…"]},
  "semnaturi": true,                       // false = fără tabel; "semnatari": [...] dacă diferă de participanți
  "poze": ["poze/zoom1.png", "poze/sala.jpg"],      // relative la fișierul JSON
  "titlu": "opțional – suprascrie titlul",  "afiseaza_activitatea": true
}
```
(fără comentarii `//` în fișierul real). Textul acceptă `**bold**`.

Durata se scrie automat în stilul fiecărui proiect: UNIC → „40 minute (12:00-12:40)”;
UNIC2 → „12:30–14:00, 1 oră și 30 de minute” / „10:00–10:30 (30 de minute)”.

## Gotchas
- **Două generații de antet în Drive.** Până pe 21.09.2026, minutele UNIC aveau o bandă de logo-uri
  POIDS (cu stema Măguri-Răcătău). Începând cu 06.10, ambele proiecte au antetul „Titlul proiectului: …
  | Cod MySMIS …” și GAL în subsol. Generatorul folosește antetul nou. Dacă utilizatorul vrea antetul
  vechi, spune-i că nu e implementat.
- **Proiectul PEO apare în Drive ca „UNIC”**, iar utilizatorul îl numește „UNIC2”. Codul SMIS 352704 = PEO;
  329335 = PIDS. Verifică după cod, nu după nume.
- **Word e mai strict decât LibreOffice** cu ordinea elementelor XML (`pBdr`, `tblBorders`, `tblLayout`).
  Generatorul le inserează în ordinea din schemă. Dacă modifici XML-ul, folosește
  `insert_element_before`, nu `append`, altfel Word afișează „conținut ilizibil”, deși preview-ul arată bine.
- **python-docx refuză unele JPEG-uri** extrase din PDF / cu profil CMYK (`UnrecognizedImageError`),
  precum și WEBP. De aceea toate pozele trec prin PIL (RGB, rotație EXIF, max. 2000 px). Minuta originală
  din 13.08 avea 6 MB din cauza a două PNG-uri. HEIC (iPhone) nu se deschide fără `pillow-heif`:
  cere JPG sau convertește.
- **Tabelul de semnături nu se rupe între pagini** (keep-with-next pe rânduri): dacă nu încape, trece
  întreg pe pagina următoare, ca în originale. Dacă are peste ~10 semnatari (o pagină), se va rupe oricum.
- Preview-ul folosește fonturile Liberation, metric-compatibile cu Times New Roman/Arial. Paginarea din
  Word iese practic identică.

## Troubleshooting
| Simptom | Cauză / soluție |
|---|---|
| `Proiect necunoscut: …` | `proiect` trebuie să fie UNIC/PIDS sau UNIC2/PEO (spațiile și cratimele sunt ignorate) |
| `UnrecognizedImageError` | ai ocolit `add_photos`; trece imaginea prin PIL (vezi funcția) |
| `IndexError` la `doc.paragraphs[0]` | `Document()` nou nu are paragrafe în corp, nu încerca să-l ștergi |
| PDF/PNG lipsesc | `soffice` și `pdftoppm` trebuie să fie instalate (`apt-get install libreoffice-writer poppler-utils`) |
