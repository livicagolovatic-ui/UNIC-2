# Cum se redactează textul minutei (stilul din minutele existente)

Utilizatorul dă **notițe brute** („ce s-a discutat”) și **poze**. Tu transformi notițele în text de
minută; generatorul se ocupă de formatare. Nu adăuga fapte care nu sunt în notițe: minuta e document
justificativ pentru finanțator (verificări, vizite ad-hoc, OIR/AM).

## Ton și formulări
- Limbă română administrativă, cu diacritice (ș, ț cu virgulă), persoana a III-a, diateza pasivă/impersonală,
  timp trecut: „A fost analizată…”, „S-a discutat despre…”, „S-a stabilit ca…”, „Au fost semnalate…”,
  „S-a menționat că…”, „S-a subliniat necesitatea…”, „Totodată,…”, „De asemenea,…”, „În cadrul întâlnirii…”.
- Lucrurile de făcut se scriu la viitor/indicativ: „…urmează să fie analizată”, „Aurora se va ocupa de…”,
  „va fi pregătită o situație privind…”. Persoanele pot fi numite cu prenumele când notițele o fac.
- Cifrele și datele se păstrează exact (date DD.MM.YYYY, ore HH:MM, „Cererea de rambursare nr. 12”,
  „Anexa 12”). Nu cumula/recalcula cifre; dacă notițele sunt ambigue, consemnează-le ca atare
  („…a fost consemnat ca aspect discutat în ședință”) sau întreabă.
- Fără nume de copii din grupul țintă dacă nu sunt strict necesare (preferă „trei copii din grupul țintă”).
- Ideile din notițe se grupează în **4–7 puncte numerotate**, fiecare cu un titlu scurt (substantival:
  „Stadiul înscrierii în grupul țintă”, „Aspecte logistice privind…”) și 1–2 paragrafe de 2–4 fraze.

## Structura conținutului (câmpurile JSON)
| Câmp | Ce conține | Exemplu de formulare |
|---|---|---|
| `scop` | 1 frază: „Analizarea/Coordonarea … , cu accent pe … , precum și …” | „Analizarea dificultăților întâmpinate în activitatea în teren și în recrutarea grupului țintă…” |
| `introducere` | (PIDS – aproape mereu; PEO – opțional) 1 paragraf-sinteză | „Întâlnirea online din data de 21.09.2026 a vizat coordonarea activităților planificate pentru perioada următoare și clarificarea…” |
| `puncte[]` | `titlu` + `paragrafe[]` (+ opțional `liste[]`) | vezi exemplele din `examples/` |
| `concluzii` | PIDS: `masuri[]` → „Concluzii și măsuri stabilite:” cu „- …;”. PEO: devine ultimul punct numerotat („Concluzii”, „Calendarul întâlnirilor și concluzii” sau „Concluzii și măsuri stabilite”) cu `paragrafe` și/sau `masuri` | „- actualizarea anexei 12 privind programul activităților, în special pentru ziua de vineri;” |
| `nota_participanti` | doar dacă e cazul (ex. experți care încă nu și-au început activitatea) | — |

Măsurile se scriu cu literă mică, substantival („transmiterea…”, „centralizarea…”, „pregătirea…”);
la PIDS generatorul pune automat „;” după fiecare și „.” la ultima.

## Pozele
- Capturile Zoom și fotografiile din sală se pun la final, în ordinea primită (`poze`).
- Captura Zoom arată de obicei lista participanților: folosește-o ca să verifici/completezi
  `participanti`, dar confirmă cu utilizatorul numele pe care nu le poți potrivi cu `echipe.md`.
- O poză cu o listă de prezență / agendă scrisă de mână se **citește** (pentru participanți, oră, puncte),
  nu se inserează, decât dacă utilizatorul cere.
