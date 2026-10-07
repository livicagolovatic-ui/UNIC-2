# -*- coding: utf-8 -*-
"""Fișa plăcii informative pentru sediul GAL: datele completate, specificațiile de producție și montaj, întrebările de confirmat."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent))
import gal_docx as E
from gal_docx import TITLE, H1, H2, H3, P, SMALL, QUOTE, BUL, NUM, TBL, CALLOUT, IMG, FOOTER
from placa import DATE

C = HERE.parent
PPTX = 'Placa_informativa_sediu_GAL_70x50cm_Calibri.pptx'
FOOTER('Intervenția 5 – Placa informativă de la sediul GAL  ·  v2, 07.10.2026')

TITLE('Placa informativă de la sediul GAL')
SMALL('Proiectul „Educație pentru mediu în teritoriul GAL Napoca Porolissum – micro-granturi pentru mediu”, contract C 36010804713061304413 / 08.09.2026. '
      'Realizată pe modelul oficial AFIR „A.2 – Placă FEADR LEADER” V3, după Anexa la contract „Materiale și activități de informare de tip publicitar” '
      'V3 (AFIR nr. 1790/28.01.2026, republicată pe afir.ro la 05.10.2026), pct. A-(2). Versiunea 2, 07.10.2026.')

IMG(str(C / 'placa' / 'Placa_informativa_sediu_GAL_previzualizare.png'), 16.5,
    f'Placa completată, 70 × 50 cm. Fișierul de lucru: placa/{PPTX} (textele în Calibri). '
    'Imaginea e o previzualizare cu Carlito, echivalentul metric al lui Calibri.')

CALLOUT('Ce s-a schimbat în versiunea 2', [
    f'**Codul proiectului:** {DATE["cod"]}, codul atribuit de AFIR, comunicat de GAL.',
    '**Data de finalizare:** ' + '/'.join(DATE['finalizare']) + '. Contractul prevede doar durata, 21 de luni, de la 08.09.2026. '
    'Termenul pe luni se încheie în ziua cu același număr din ultima lună: 08.09.2026 + 21 de luni = 08.06.2028.',
    '**Fontul:** textele introduse sunt acum în **Calibri**, cum cere anexa, într-un fișier PowerPoint de 70 × 50 cm. '
    'PDF-ul pentru tipografie se exportă din PowerPoint (pașii sunt la capitolul 3).',
], fill='EAF4EA', line='9CC79C')

CALLOUT('De confirmat înainte de tipar', [
    '**1. Proiectant / Executant.** La un proiect de servicii am trecut „Nu este cazul” la proiectant și GAL-ul ca executant. De confirmat cu OJFIR Cluj.',
    '**2. Localitatea și dimensiunea.** Am trecut toate cele 14 localități din cererea de finanțare, cu Gilău primul (ponderea cea mai mare, 9%). '
    'La 70 × 50 cm lista e scrisă mărunt; dacă vreți textul mai mare, placa se poate face 100 × 70 cm (aceleași proporții, anexa permite până la 100 × 140 cm).',
    '**3. Altă placă la sediu.** Dacă la sediu există deja o placă pentru alt proiect FEADR al GAL, vedeți capitolul 4 (modelul multifond).',
], fill='FBEAEA', line='E0A0A0')

H1('1. Datele trecute pe placă')
TBL([
    ['Câmpul din model', 'Ce am scris', 'Sursa'],
    ['Proiect finanțat cu fonduri nerambursabile prin PS 2023 - 2027', DATE['titlu'], 'Contractul de finanțare și CF (titlul exact)'],
    ['Cod proiect', DATE['cod'], 'Codul atribuit de AFIR (confirmat de GAL, 07.10.2026)'],
    ['Județ', DATE['judet'], 'CF – amplasarea proiectului'],
    ['Localitate', DATE['localitate'], 'CF – amplasarea proiectului: Gilău 9%, celelalte 13 UAT-uri câte 7%'],
    ['Beneficiar', DATE['beneficiar'], 'Contractul de finanțare'],
    ['Valoarea totală eligibilă a proiectului', DATE['valoare'] + ' Euro', 'Bugetul contractat (eligibil)'],
    ['din care, finanțare nerambursabilă PS 2023-2027', DATE['nerambursabil'] + ' Euro', 'Bugetul contractat (100% din eligibil)'],
    ['Proiectant', DATE['proiectant'], 'Proiect de servicii, fără proiectare (de confirmat)'],
    ['Executant', DATE['executant'], 'GAL implementează direct proiectul (de confirmat)'],
    ['Demarare', '/'.join(DATE['demarare']), 'Data semnării contractului'],
    ['Finalizare', '/'.join(DATE['finalizare']), 'Contractul: 21 de luni de implementare de la 08.09.2026'],
], widths=[4.4, 7.4, 5.2])
P('Valoarea de pe placă este cea **eligibilă** din contract (138.643 euro). TVA-ul de 1.259 euro, suportat de GAL, nu apare: placa cere valoarea '
  'totală eligibilă și finanțarea nerambursabilă.')
P('Dacă AFIR aprobă o prelungire a duratei de implementare, se schimbă doar data de finalizare: se corectează în PowerPoint și se retipărește '
  'placa (sau se aplică un autocolant cu noua dată, dacă tipografia îl poate potrivi exact).')

H1('2. Ce am respectat din modelul AFIR')
BUL([
    'Am folosit **modelul oficial V3** de pe afir.ro (Identitate vizuală – Materiale publicitare PS 2027 V3), varianta LEADER, fără nicio modificare de '
    'grafică: stema Guvernului, drapelul UE cu „Cofinanțat de Uniunea Europeană”, textele fixe, AFIR, LEADER, fundalul și chenarele rămân neatinse.',
    'Am scos **doar liniile punctate** ale câmpurilor de completat (878 de puncte) și am scris datele în locul lor. Barele oblice din câmpurile de dată au rămas.',
    '**Textul introdus de beneficiar** e negru pe fondul alb și alb în casetele albastre, cum cere anexa.',
    '**Fontul este Calibri**, cum cere anexa: Bold pentru toate câmpurile, Regular pentru lista de localități. În PowerPoint, modelul AFIR este '
    'imaginea de fundal (vectorială), iar fiecare text este o casetă separată, în Calibri, așezată pe locul liniei punctate.',
    'Rândurile și centrările au fost calculate cu **Carlito**, fontul liber cu aceleași lățimi de litere ca Calibri, deci textul încape exact la fel. '
    'Previzualizarea din această fișă e randată cu Carlito; pe calculatorul cu Office se vede în Calibri.',
    'Marginea de siguranță de 3 cm e deja în model; niciun text nou nu iese din chenarele prevăzute.',
])

H1('3. Producție')
H2('Exportul PDF-ului de tipar din PowerPoint')
NUM([
    f'Deschideți **{PPTX}** pe un calculator cu Microsoft Office (Calibri vine cu Office). Nu mutați și nu redimensionați nimic: '
    'fundalul este modelul AFIR, iar casetele de text sunt deja la locul lor.',
    'Verificați încă o dată codul, sumele și datele.',
    '**Windows:** Fișier → Export → Creare document PDF/XPS (File → Export → Create PDF/XPS Document) → Opțiuni: bifați '
    '„Compatibil ISO 19005-1 (PDF/A)” → Publicare. **Mac:** Fișier → Export → PDF, calitate „Cea mai bună pentru imprimare” (Best for printing).',
    'PowerPoint încorporează automat fontul Calibri în PDF. Verificați în Adobe Reader: Fișier → Proprietăți → Fonturi trebuie să apară Calibri '
    '(„Încorporat subset”). PDF-ul are 70 × 50 cm, la scara 1:1.',
    'Trimiteți PDF-ul tipografiei. Ca variantă, tipografia poate retasta textele în Calibri direct în modelul EPS de la AFIR, după tabelul de la capitolul 1.',
])
TBL([
    ['Element', 'Specificație', 'Sursa'],
    ['Dimensiune', '70 × 50 cm (lățime × înălțime), la scara 1:1. Variantă opțională: 100 × 70 cm, aceleași proporții (o pregătim la cerere).', 'Anexa V3: 50–100 × 70–140 cm'],
    ['Culori', 'Policromie, fond alb cu elementele grafice în transparență, exact ca în model.', 'Anexa V3, A-(2)(b)'],
    ['Font', 'Calibri: negru pe alb, alb în casetele albastre.', 'Anexa V3, A-(2)'],
    ['Material', 'Recomandat: plăci compozite din aluminiu de 3 mm sau PVC expandat de 5 mm, print UV, cu laminare anti-UV pentru exterior.', 'Anexa V3: materiale rezistente la intemperii (tablă, PVC)'],
    ['Fișier', f'PDF exportat din {PPTX}, cu Calibri încorporat. Fundalul e vectorial (SVG); PowerPoint-urile mai vechi, fără SVG, '
               'folosesc o copie la 200 dpi. Modelul nu are margine de tăiere; tipografia poate adăuga 3 mm de fond alb dacă printează până la margine.', '–'],
    ['Probă', 'Cereți o probă de culoare și verificați încă o dată codul, sumele și datele pe probă.', '–'],
], widths=[2.8, 9.4, 4.8])

H1('4. Montaj și păstrare')
BUL([
    '**Unde:** pe clădirea sediului GAL din Gilău, str. Eroilor nr. 6, bl. I1, lângă intrare, acolo unde se vede cel mai bine din căile de acces publice, '
    'fără să fie acoperită de alte elemente. Fiind un bloc de locuințe, cereți acordul asociației de proprietari pentru montarea pe fațadă.',
    '**La ce înălțime:** marginea de jos a plăcii la 130–200 cm de sol.',
    '**Când:** cât mai repede. Anexa cere montarea de la începerea implementării, iar contractul curge din 08.09.2026.',
    '**Cât timp:** expusă corect și continuu cel puțin până la finalul perioadei de monitorizare a proiectului. Dacă se degradează, se înlocuiește.',
    '**Dovada:** fotografii datate la montare (de aproape și din stradă), apoi periodic. Se păstrează la dosarul proiectului, pentru raportul de activitate și pentru vizitele OJFIR.',
    '**Dacă la sediu există deja o placă pentru alt proiect FEADR al GAL** (de exemplu funcționarea): anexa permite o singură placă, pe modelul multifond, '
    'când mai multe operațiuni se desfășoară în același loc. De întrebat la OJFIR dacă preferă placă separată sau multifond.',
])

E.doc.save(str(C / 'placa' / 'Placa_sediu_GAL_fisa_tehnica.docx'))
print('saved')
