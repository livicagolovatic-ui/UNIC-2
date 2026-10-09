# Proiectul UNIC – date de referință

Datele **stabile** ale proiectului (identificare, subactivități, roluri) sunt mai jos. Informațiile provin din documentele proiectului furnizate de utilizator (Anexa 12 – Planificare octombrie 2026 V2,
fișa postului, antetul). Proiectul nu are o prezență publică online care să poată fi verificată; când un document nou
contrazice datele de aici, documentul nou are prioritate – semnalează diferența utilizatorului.

## Identificare

| Câmp | Valoare |
|---|---|
| Titlu | UNIC – „Uniți pentru Nevoile Incluzive și Continuitatea Educației Elevilor” |
| Cod SMIS | 352704 |
| Contract de finanțare | nr. 11205 / 16.06.2026 |
| Program | Programul Educație și Ocupare (PEO) 2021–2027, cofinanțat de Uniunea Europeană |
| Beneficiar (Lider) | Asociația Grupul de Acțiune Locală (GAL) Napoca Porolissum |
| Organism intermediar | OIR PECU NV (destinatarul Anexei 12) |
| Manager de proiect | Baba Alina-Ioana |
| Reprezentant legal | Dumitrescu Marius-Gheorghe |

Antetul (logo UE „Cofinanțat de Uniunea Europeană”, stema Guvernului României, GAL Napoca Porolissum, UNIC Porolissum,
titlul proiectului, „Proiect cofinanțat de Uniunea Europeană prin Programul Educație și Ocupare (PEO 2021-2027)”,
„cod MySmis 352704”) trebuie să apară pe **toate** materialele – este o cerință de vizibilitate a finanțării UE.
Fișierul este în `assets/antet_UNIC.docx`; `scripts/lib_unic.py` îl aplică automat pe fiecare pagină.

## Subactivitățile din Anexa 12 (octombrie 2026)

| Cod | Denumire | Cine (exemple) |
|---|---|---|
| SA5.1 | Măsuri de facilitare a accesului la programele de formare profesională și de prevenire și combatere a părăsirii timpurii a școlii la nivelul ÎPT | Consilier psihologic |
| SA5.2 | Formarea personalului didactic din învățământul profesional și tehnic, inclusiv dual | Formator |
| **SA5.3** | **Dezvoltarea de programe de informare și conștientizare** | **Facilitator comunitar 2**, Expert comunicare |
| SA5.4 | Dezvoltarea și furnizarea de programe remediale | Cadre didactice |

Activitățile FC2 se încadrează în **SA5.3**. Atelierele pentru părinți, târgurile de oportunități și vizitele la operatori
economici (atribuțiile 8–10) pot ține de alte subactivități – dacă utilizatorul nu precizează codul, lasă câmpul de
completat și menționează-l, în loc să ghicești.

## Unități de învățământ / locații (cunoscute până în octombrie 2026 – lista se poate extinde)

| Unitate | Adresă | Grup țintă tipic |
|---|---|---|
| Colegiul Tehnic Turda | str. Câmpiei nr. 51, Turda (și str. Basarabiei nr. 48) | elevi ÎPT |
| Colegiul Tehnic Turda – Structura Poiana | str. Câmpiei nr. 51, Turda | elevi |
| Liceul Tehnologic „Vlădeasa” Huedin | Piața Republicii nr. 39–42, Huedin | elevi de gimnaziu (clasele VII–VIII) |
| Liceul Teologic Reformat Cluj-Napoca | str. Câmpeni nr. 4, Cluj-Napoca | elevi, cadre didactice |

## Echipa (roluri relevante pentru FC2; persoanele se pot schimba – verifică în Anexa 12 curentă)

- **Manager de proiect** – superior direct; avizează documentele FC2.
- **Expert comunicare** (Moraru Georgia) – primește de la FC2 materiale foto-video și sinteze (doar cu acorduri verificate).
- **Consilier psihologic** (SA5.1) – intervenții de consiliere; FC2 **nu** face consiliere psihologică, ci trimite către specialist.
- **Cadre didactice** (SA5.4) – programe remediale.

## Planificarea lunară (Anexa 12)

Beneficiarul transmite OIR lunar „Anexa 12 – Planificare lunară activități” cu: activitatea (subactivitatea), locația,
modalitatea (fizic/online), data, intervalul orar, entitatea responsabilă, persoana de contact, grupul țintă implicat.
Declarația din anexă cere comunicarea **oricărei modificări** (expert, locație, GT, program) **cu cel puțin o zi înainte**,
printr-o versiune nouă; nerespectarea poate atrage invalidarea activității și neeligibilitatea cheltuielilor.

Consecințe pentru documentele FC2:
- data, ora, locația și durata dintr-un document justificativ trebuie să corespundă Anexei 12 (sau versiunii ei actualizate);
- dacă numărul real de participanți diferă de GT declarat, semnalează nevoia unei versiuni noi a Anexei 12;
- dacă același interval apare la doi experți, semnalează riscul de dublă raportare (atribuția 19).

Programarea concretă a FC2 **se schimbă lunar** și nu se păstrează aici ca adevăr: o citești de fiecare dată din Anexa 12
a lunii curente (cu `scripts/extrage_anexa12.py`) sau din ce îți spune utilizatorul. Lunile anterioare sunt doar istoric,
în `istoric-activitati.md`.

## Materiale deja realizate (pot fi refolosite / adaptate)

- Atelierul „Eu, punctele mele forte și ce mă motivează” (clasele VII–VIII, 2 × 60 min): Ședința 1 „Cine sunt eu și ce am bun?”
  (temă: Agenția Secretă a Punctelor Forte; 9 anexe) și Ședința 2 „Ce mă motivează și ce vreau să dezvolt?” (temă: LEVEL UP;
  10 anexe), fiecare cu fișa activității și raport de desfășurare. Sursele sunt în depozitul utilizatorului, `atelier_puncte_forte/`.
- Excel de planificare pentru Huedin (grupe, tematici, prezențe) – generatorul este în `planificare_huedin/`.
