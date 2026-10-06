# Pachetul de comunicare – „Educație pentru mediu” (micro-granturi)

Materiale pentru campania de informare și promovare (A2) și pentru lansarea apelului (A4) din proiectul
„Educație pentru mediu în teritoriul GAL Napoca Porolissum – micro-granturi pentru mediu”
(contract C 36010804713061304413 / 08.09.2026). Versiunea 1, 06.10.2026.

## Ce găsești aici

| Folder / fișier | Conținut |
|---|---|
| `Pachet_comunicare_Educatie_pentru_mediu.docx` | Documentul însoțitor: ce conține pachetul, cum respectă cerințele, calendarul și textele postărilor, indicații pentru tipografie |
| `logo/` | Logo-ul proiectului (orizontal, vertical, simbol; color, alb, monocrom) în SVG, PDF și PNG transparent + `Fisa_identitate_vizuala_proiect.pdf` |
| `flyere/` | Flyer 1 – A5 față-verso; Flyer 2 – A4 pliat în trei. PDF de tipar cu 3 mm margine de tăiere + PNG de previzualizare |
| `afise/` | Afiș 1 – A3 campanie; Afiș 2 – A3 sesiune de informare (șablon: câmpurile galbene se completează) |
| `social/` | Model A și Model B (șabloane), cele 5 postări săptămânale (1080 × 1350 px), `Postari_saptamanale_texte.md` cu textele gata de copiat |
| `assets/sigle_oficiale/` | Siglele oficiale decupate din pachetul AFIR „Sigle 2024” (UE „Cofinanțat de Uniunea Europeană”, MADR, PS 2023-2027, AFIR, LEADER) și sigla GAL din manualul GAL |
| `assets/fonts/` | Montserrat (fontul GAL) și Caveat, licență OFL; `static/` conține instanțele folosite la randare |
| `src/` | Sursele: machetele în HTML/SVG și scripturile Python care le randează |

## Regenerare

```bash
cd interventia5/comunicare/src
python3 build_all.py
```

Cerințe: Python 3 cu `pymupdf`, `qrcode`, `pillow`, `python-docx`, `fonttools` și Chromium
(implicit `/opt/pw-browsers/chromium-1194/chrome-linux/chrome`, se poate schimba prin variabila `CHROME`).
Textele comune (date proiect, mențiuni obligatorii, contact) sunt în `src/common.py`; textele postărilor în `src/postari_texte.py`.

## Reguli de reținut

- Bara de sigle, în ordinea din ghidul AFIR de identitate vizuală V3: UE „Cofinanțat de Uniunea Europeană” · MADR · PS 2023-2027 · GAL · AFIR. LEADER stă pe un rând separat.
- Pe fiecare material: cele trei mențiuni obligatorii (Anexa II, C1.1-6), datele proiectului și „Material distribuit gratuit”.
- Placa, afișul informativ A2 și autocolantul AFIR **nu** se fac din acest pachet: se completează modelele AFIR din `../surse/afir_modele/`, fără modificări.
- Înainte de tipar: lista materialelor se trimite la OJFIR (Anexa II, prevederea 9).
- „Începutul anului 2027” depinde de aprobarea modificării nr. 1 a contractului.
