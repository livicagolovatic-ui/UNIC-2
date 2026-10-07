# -*- coding: utf-8 -*-
"""Fișa plăcii informative pentru sediul GAL: datele completate, specificațiile de producție și montaj, întrebările de confirmat."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent))
import gal_docx as E
from gal_docx import TITLE, H1, H2, H3, P, SMALL, QUOTE, BUL, NUM, TBL, CALLOUT, IMG, FOOTER
from placa import DATE

C = HERE.parent
FOOTER('Intervenția 5 – Placa informativă de la sediul GAL  ·  v1, 07.10.2026')

TITLE('Placa informativă de la sediul GAL')
SMALL('Proiectul „Educație pentru mediu în teritoriul GAL Napoca Porolissum – micro-granturi pentru mediu”, contract C 36010804713061304413 / 08.09.2026. '
      'Realizată pe modelul oficial AFIR „A.2 – Placă FEADR LEADER” V3, după Anexa la contract „Materiale și activități de informare de tip publicitar” '
      'V3 (AFIR nr. 1790/28.01.2026, republicată pe afir.ro la 05.10.2026), pct. A-(2). Versiunea 1, 07.10.2026.')

IMG(str(C / 'placa' / 'Placa_informativa_sediu_GAL_previzualizare.png'), 16.5,
    'Placa completată, 70 × 50 cm. Fișierul de tipar: placa/Placa_informativa_sediu_GAL_70x50cm.pdf (vectorial, fonturi încorporate).')

CALLOUT('De confirmat înainte de tipar', [
    '**1. Codul proiectului.** Am trecut C36010804713061304413, adică numărul contractului. Anexa cere „codul cererii de finanțare atribuit de AFIR”: '
    'verificați în platforma AFIR că este același cod.',
    '**2. Data de finalizare.** Am calculat 07.06.2028 (21 de luni de la 08.09.2026). Se ia din contract, din articolul despre durata de implementare.',
    '**3. Proiectant / Executant.** La un proiect de servicii am trecut „Nu este cazul” și, ca executant, GAL-ul. De confirmat cu OJFIR Cluj.',
    '**4. Localitatea.** Am trecut toate cele 14 localități din cererea de finanțare, cu Gilău primul (ponderea cea mai mare, 9%). La 70 × 50 cm lista e '
    'scrisă mărunt; dacă vreți textul mai mare, placa se poate face 100 × 70 cm (aceleași proporții, anexa permite până la 100 × 140 cm).',
], fill='FBEAEA', line='E0A0A0')

H1('1. Datele trecute pe placă')
TBL([
    ['Câmpul din model', 'Ce am scris', 'Sursa'],
    ['Proiect finanțat cu fonduri nerambursabile prin PS 2023 - 2027', DATE['titlu'], 'Contractul de finanțare și CF (titlul exact)'],
    ['Cod proiect', DATE['cod'], 'Contractul de finanțare (de confirmat, vezi mai sus)'],
    ['Județ', DATE['judet'], 'CF – amplasarea proiectului'],
    ['Localitate', DATE['localitate'], 'CF – amplasarea proiectului: Gilău 9%, celelalte 13 UAT-uri câte 7%'],
    ['Beneficiar', DATE['beneficiar'], 'Contractul de finanțare'],
    ['Valoarea totală eligibilă a proiectului', DATE['valoare'] + ' Euro', 'Bugetul contractat (eligibil)'],
    ['din care, finanțare nerambursabilă PS 2023-2027', DATE['nerambursabil'] + ' Euro', 'Bugetul contractat (100% din eligibil)'],
    ['Proiectant', DATE['proiectant'], 'Proiect de servicii, fără proiectare'],
    ['Executant', DATE['executant'], 'GAL implementează direct proiectul'],
    ['Demarare', '/'.join(DATE['demarare']), 'Data semnării contractului'],
    ['Finalizare', '/'.join(DATE['finalizare']), 'Finalul celor 21 de luni de implementare (de confirmat)'],
], widths=[4.4, 7.4, 5.2])
P('Valoarea de pe placă este cea **eligibilă** din contract (138.643 euro). TVA-ul de 1.259 euro, suportat de GAL, nu apare: placa cere valoarea '
  'totală eligibilă și finanțarea nerambursabilă.')

H1('2. Ce am respectat din modelul AFIR')
BUL([
    'Am folosit **modelul oficial V3** de pe afir.ro (Identitate vizuală – Materiale publicitare PS 2027 V3), varianta LEADER, fără nicio modificare de '
    'grafică: stema Guvernului, drapelul UE cu „Cofinanțat de Uniunea Europeană”, textele fixe, AFIR, LEADER, fundalul și chenarele rămân neatinse.',
    'Am scos **doar liniile punctate** ale câmpurilor de completat (878 de puncte) și am scris datele în locul lor. Barele oblice din câmpurile de dată au rămas.',
    '**Textul introdus de beneficiar** e negru pe fondul alb și alb în casetele albastre, cum cere anexa.',
    '**Fontul.** Anexa cere Calibri. Calibri e un font Microsoft, licențiat, pe care nu l-am putut folosi aici. Am folosit **Carlito**, fontul liber '
    'creat ca echivalent metric al lui Calibri: aceleași lățimi de litere, aceeași așezare a textului, forme aproape identice. Dacă tipografia lucrează pe Windows, '
    'poate retasta aceleași texte în Calibri direct în modelul EPS de la AFIR, după tabelul de mai sus. Pozițiile nu se schimbă.',
    'Marginea de siguranță de 3 cm e deja în model; niciun text nou nu iese din chenarele prevăzute.',
])

H1('3. Producție')
TBL([
    ['Element', 'Specificație', 'Sursa'],
    ['Dimensiune', '70 × 50 cm (lățime × înălțime), la scara 1:1 în PDF. Variantă opțională: 100 × 70 cm, aceleași proporții.', 'Anexa V3: 50–100 × 70–140 cm'],
    ['Culori', 'Policromie, fond alb cu elementele grafice în transparență, exact ca în model.', 'Anexa V3, A-(2)(b)'],
    ['Material', 'Recomandat: plăci compozite din aluminiu de 3 mm sau PVC expandat de 5 mm, print UV, cu laminare anti-UV pentru exterior.', 'Anexa V3: materiale rezistente la intemperii (tablă, PVC)'],
    ['Fișier', 'PDF vectorial cu fonturile încorporate. Modelul nu are margine de tăiere; tipografia poate adăuga 3 mm de fond alb dacă printează până la margine.', '–'],
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
