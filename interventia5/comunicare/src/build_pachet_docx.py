# -*- coding: utf-8 -*-
"""Documentul Word care însoțește pachetul de comunicare: ce conține, cum respectă cerințele, calendarul și textele postărilor."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent))          # interventia5/ (gal_docx)
import gal_docx as E
from gal_docx import TITLE, H1, H2, H3, P, SMALL, QUOTE, BUL, NUM, TBL, CALLOUT, IMG, PAGEBREAK, FOOTER
from postari_texte import POSTARI, MENTIUNE, HASHTAGS

C = HERE.parent  # interventia5/comunicare
FOOTER('Intervenția 5 – Pachetul de comunicare  ·  v1, 06.10.2026')

TITLE('Pachetul de comunicare: logo, flyere, afișe, postări')
SMALL('Proiectul „Educație pentru mediu în teritoriul GAL Napoca Porolissum – micro-granturi pentru mediu”, contract C 36010804713061304413 / 08.09.2026. '
      'Materiale pentru campania de informare și promovare (activitatea A2) și pentru lansarea apelului (A4). Versiunea 1, 06.10.2026.')

CALLOUT('Înainte de tipar și de publicare', [
    '**1. Lista materialelor la OJFIR.** Anexa II la contract (prevederea 9) cere aprobarea scrisă a AFIR pentru folosirea siglelor pe alte materiale '
    'decât cele din anexă. Propun o adresă cu lista: flyere, afișe, postări. Machetele din acest pachet se atașează la adresă.',
    '**2. Data lansării apelului.** Materialele spun „începutul anului 2027”, după calendarul din modificarea nr. 1, care e încă în aprobare. '
    'Dacă AFIR nu o aprobă, textul se schimbă în toate materialele.',
    '**3. Afișul sesiunii de informare** este un șablon: câmpurile evidențiate cu galben (data, ora, locul) se completează pentru fiecare sesiune.',
    '**4. Proba de culoare.** PDF-urile sunt în RGB, cu 3 mm de margine de tăiere. Tipografia face conversia CMYK; cereți o probă înainte de tiraj.',
], fill='FBEAEA', line='E0A0A0')

# ------------------------------------------------------------------ 1
H1('1. Ce conține pachetul')
TBL([
    ['Material', 'Format', 'Fișiere (în interventia5/comunicare/)', 'La ce folosește'],
    ['Logo-ul proiectului', 'orizontal, vertical, simbol; color, alb, mono', 'logo/ – SVG, PDF, PNG transparent',
     'Pe toate materialele proiectului, în corpul materialului, sub bara de sigle'],
    ['Fișa de identitate vizuală', 'A4 orizontal, 2 pagini', 'logo/Fisa_identitate_vizuala_proiect.pdf',
     'Regulile pentru orice material nou: culori, fonturi, bara de sigle'],
    ['Flyer 1 „Ai o idee verde?”', 'A5, față-verso', 'flyere/Flyer1_A5_fata-verso_tipar_bleed3mm.pdf + PNG',
     'Distribuire largă: școli, primării, evenimente'],
    ['Flyer 2 „Ghid rapid”', 'A4 pliat în trei', 'flyere/Flyer2_A4_pliat_in_trei_tipar_bleed3mm.pdf + PNG',
     'Pentru directori, profesori, ONG-uri: toate detaliile pe scurt'],
    ['Afiș 1 „Natura are nevoie de ideile tale.”', 'A3', 'afise/Afis1_A3_campanie_tipar_bleed3mm.pdf + PNG',
     'Avizierele școlilor, primăriilor, căminelor culturale'],
    ['Afiș 2 „Sesiune de informare”', 'A3, șablon', 'afise/Afis2_A3_sesiune_informare_SABLON_tipar_bleed3mm.pdf + PNG',
     'Anunțul fiecărei sesiuni de informare (A4)'],
    ['Model A și Model B de postare', '1080 × 1350 px', 'social/ModelA_…SABLON.png, social/ModelB_…SABLON.png',
     'Șabloane pentru postările viitoare'],
    ['5 postări săptămânale', '1080 × 1350 px + texte', 'social/Postarea1…5.png, social/Postari_saptamanale_texte.md',
     'Campania online, 15.10 – 12.11.2026'],
], widths=[3.6, 3.2, 5.4, 4.8])
SMALL('Sursele (HTML/SVG + scripturi Python) sunt în comunicare/src/. Orice text se poate schimba și materialele se regenerează identic. '
      'PDF-urile se pot importa și în Canva, ca design editabil.')

# ------------------------------------------------------------------ 2
H1('2. Cum arată')
H3('Logo-ul')
IMG(str(C / 'logo' / 'logo_proiect_orizontal_color.png'), 10.5)
P('Concept: o **carte deschisă** (educația) din care crește un **mugur** (mediul și comunitatea), cu **soarele** în fundal. '
  'Micro-grantul e sămânța care pornește creșterea. Culorile sunt cele din manualul GAL, verde #4FAB50 și maro #3D2E31, '
  'ca proiectul să fie recunoscut ca parte din familia GAL. Sloganul campaniei: //„Plantăm idei. Creștem comunități.”//')
H3('Flyer 1 – A5 față-verso')
IMG(str(C / 'flyere' / 'Flyer1_A5_fata-verso_pagina1.png'), 7.6)
IMG(str(C / 'flyere' / 'Flyer1_A5_fata-verso_pagina2.png'), 7.6)
H3('Flyer 2 – A4 pliat în trei')
IMG(str(C / 'flyere' / 'Flyer2_A4_pliat_in_trei_pagina1.png'), 16)
IMG(str(C / 'flyere' / 'Flyer2_A4_pliat_in_trei_pagina2.png'), 16, 'Exterior (sus): clapetă, spate, copertă. Interior (jos): cine, ce, cum.')
H3('Afișele A3')
IMG(str(C / 'afise' / 'Afis1_A3_campanie.png'), 8.4)
IMG(str(C / 'afise' / 'Afis2_A3_sesiune_informare_SABLON.png'), 8.4)
H3('Modelele de postare')
IMG(str(C / 'social' / 'ModelA_anunt_SABLON.png'), 6.4)
IMG(str(C / 'social' / 'ModelB_card_informativ_SABLON.png'), 6.4,
    'Model A – anunț (fundal verde, mesaj mare). Model B – card informativ (iconițe, carduri, bare de punctaj).')

# ------------------------------------------------------------------ 3
H1('3. Cum respectă cerințele')
TBL([
    ['Cerința', 'Sursa', 'Cum am aplicat-o'],
    ['Emblema UE cu „Cofinanțat de Uniunea Europeană” (proiecte LEADER)', 'Anexa II; GIV AFIR V3, cap. 2.C și 2.G',
     'Pe toate materialele, cu fișierul oficial AFIR („Sigle 2024”), nemodificat.'],
    ['Ordinea siglelor: UE · MADR · PS 2023-2027 · beneficiar · AFIR', 'GIV AFIR V3, cap. 3', 'Aceeași ordine peste tot, toate siglele la aceeași înălțime.'],
    ['LEADER pe un rând separat de emblema UE', 'GIV AFIR V3, cap. 2.G', 'Rândul al doilea, sub bară.'],
    ['Cele trei mențiuni obligatorii și datele proiectului', 'Anexa II, C1.1-6', 'În subsolul flyerelor și afișelor; în textul fiecărei postări.'],
    ['Material gratuit, de interes public, necomercial', 'Anexa II, prevederea 9', '„Material distribuit gratuit” pe toate tipăriturile.'],
    ['Social media: cel puțin emblema UE și declarația pe fiecare postare', 'GIV AFIR V3, B-(2)', 'Bara completă de sigle în header, la fiecare imagine.'],
    ['Manualul GAL: culori, Montserrat, sigla GAL nedeformată', 'Manualul de identitate GAL', 'Paleta și fontul GAL; sigla GAL din manual, la proporțiile originale.'],
    ['Conținut fidel proiectului aprobat', 'CF, Anexa 1, Metodologia', 'Solicitanți, sumă (19.833,3 €), 6 granturi, tipuri de inițiative, criterii și praguri preluate exact.'],
    ['Placa, afișul A2 și autocolantul AFIR', 'Anexa II, C1.1-(2)–(4)', 'Nu fac parte din pachet: se completează pe modelele AFIR, fără soluții creative. '
     'Afișele din pachet sunt promoționale și nu le înlocuiesc.'],
], widths=[5.6, 3.6, 7.8])
P('**Un punct de confirmat cu OJFIR:** ghidul AFIR cere o înălțime minimă de 13 mm pentru sigla AFIR. Pe afișele A3 bara are 14 mm. '
  'Pe A5 și pe panoul de 99 mm al trifoldului, cele cinci sigle nu încap la 13 mm nici pe un rând, nici pe două: am folosit cea mai mare '
  'dimensiune posibilă (8,6 mm pe A5 și 7,8 mm pe trifold, pe două rânduri). Merită întrebat odată cu lista materialelor.')

# ------------------------------------------------------------------ 4
H1('4. Calendarul postărilor')
TBL([['Nr.', 'Când', 'Tema', 'Model', 'Imagine']] +
    [[str(p['nr']), p['data'], p['tema'], p['model'], p['fisier']] for p in POSTARI], widths=[1, 4, 4.2, 3.6, 4.2])
P('Joia la 10:00 prinde profesorii și directorii în pauza de dimineață. Publicați pe Facebook și Instagram; pe LinkedIn, TikTok, X și YouTube '
  'poate merge aceeași imagine, cu textul scurtat. Prima postare poate fi fixată sus pe pagină, ca informare despre finanțare (GIV V3, B-(2)).')
P('Postarea 5 strânge adresele școlilor și ONG-urilor interesate. Răspunsurile intră direct în **registrul potențialilor beneficiari informați** '
  '(ținta: minimum 20), care e dovadă pentru campania A2.')

# ------------------------------------------------------------------ 5
H1('5. Textele postărilor')
P('La finalul fiecărei postări se lipește mențiunea obligatorie și hashtag-urile de mai jos. Versiunea pentru copy-paste, cu totul inclus, '
  'este în social/Postari_saptamanale_texte.md.')
QUOTE(MENTIUNE)
QUOTE(HASHTAGS)
for p in POSTARI:
    H2(f"Postarea {p['nr']} – {p['tema']}")
    SMALL(f"{p['data']} · {p['model']} · imagine: social/{p['fisier']}")
    IMG(str(C / 'social' / p['fisier']), 6.2)
    for par in p['text'].split('\n\n'):
        q = E.doc.add_paragraph(); E.runs(q, par)   # aliniat la stânga: textul are rânduri scurte și emoji
    SMALL('Text alternativ: ' + p['alt'])

# ------------------------------------------------------------------ 6
H1('6. Indicații pentru tipografie')
TBL([
    ['Material', 'Format final', 'Hârtie recomandată', 'Observații'],
    ['Flyer 1', 'A5, 148 × 210 mm, față-verso', '150–170 g/m², lucioasă sau mată', 'PDF cu 3 mm de margine de tăiere pe fiecare latură.'],
    ['Flyer 2', 'A4, 297 × 210 mm, pliat în trei (2 big-uri)', '170 g/m², mată', 'Panouri egale de 99 mm; tipografia poate îngusta clapeta interioară la 97 mm.'],
    ['Afiș 1 și Afiș 2', 'A3, 297 × 420 mm', '170–200 g/m², lucioasă', 'Pentru exterior, hârtie rezistentă la apă.'],
], widths=[2.6, 4.6, 4.2, 5.6])

E.doc.save(str(C / 'Pachet_comunicare_Educatie_pentru_mediu.docx'))
print('saved')
