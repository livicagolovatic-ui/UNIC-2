# -*- coding: utf-8 -*-
"""Ședința 2 – „Ce mă motivează și ce vreau să dezvolt?” – scenariu complet + anexe de tipărit."""
import os
from lib_unic import *
from justificativ import fisa_activitate, metode, raport, etape_fisa_post

OUT = os.path.join(HERE, 'Sedinta_2_Ce_ma_motiveaza_Scenariu_si_Anexe.docx')
D = UnicDoc('Proiect UNIC – cod MySMIS 352704   |   Atelier „Eu, punctele mele forte și ce mă motivează”   |   Ședința 2')
d = D.d

# =====================================================================  SCENARIU
D.banner('ATELIER DE DEZVOLTARE PERSONALĂ  •  ȘEDINȚA 2 DIN 2',
         'CE MĂ MOTIVEAZĂ ȘI CE VREAU SĂ DEZVOLT?',
         'Atelier „Eu, punctele mele forte și ce mă motivează”  •  60 de minute  •  Clasele a VII-a – a VIII-a  •  10–15 elevi',
         'Tema creativă: LEVEL UP – agenții trec la nivelul următor')

fisa_activitate(D, 2, 'Ce mă motivează și ce vreau să dezvolt?', [
    'Ședința este a doua (și ultima) din atelierul de dezvoltare personală „Eu, punctele mele forte și ce mă motivează”, destinat elevilor din '
    'clasele a VII-a – a VIII-a. Scopul ședinței este explorarea surselor personale de motivație și conectarea punctelor forte, identificate '
    'în Ședința 1, cu un obiectiv personal mic, realist și realizabil.',
    'În conformitate cu atribuțiile din fișa postului (pct. 3), facilitatorul comunitar a planificat activitatea împreună cu '
    'managerul de proiect și echipa de implementare, a informat și a mobilizat elevii, a pregătit documentele și materialele de lucru '
    '(agenda și scenariul, Anexele 1–10, lista de prezență, instrumentele de feedback), a asigurat suportul logistic și a verificat '
    'condițiile de participare și siguranță pentru minori, a facilitat participarea elevilor la ședință, a monitorizat participarea '
    'și a documentat și raportat activitatea. '
    'Ședința cuprinde 8 secvențe de învățare, descrise la secțiunea 9.',
], etape_fisa_post('Anexele 1–10', 'fișa de feedback a atelierului'), [
    'Scenariul complet al Ședinței 2 (prezentul document), cu 10 materiale-suport (Anexele 1–10).',
    'Ședință de 60 de minute desfășurată cu elevi din clasele a VII-a – a VIII-a (numărul de participanți – conform listei de prezență).',
    'Produse ale elevilor: Fișele 3–7, provocările personale de 30 de zile, Cardurile de agent finalizate, scrisorile sigilate.',
    'Fișele de feedback ale atelierului și diplomele „Agent LEVEL UP” acordate participanților.',
    'Raportul privind desfășurarea activității (secțiunea 12).',
])

D.h('SCENARIUL ACTIVITĂȚII', 1)
D.h('1. Fundamentare și legătura cu Ședința 1')
D.p('În Ședința 1, elevii și-au identificat punctele forte și au completat **Cardul de agent – Nivelul 1**. Ședința 2 continuă procesul: '
    'trecem de la „ce am bun” la „ce mă pune în mișcare” și „ce pas fac mai departe”. Folosind în continuare elemente de gamificare '
    '(tema „Level Up”, inspirată din jocurile video), activitatea arată că progresul personal se bazează pe:', align='justify', after=2)
D.b('un **motiv** de a continua → //combustibilul// (motivația);')
D.b('folosirea **abilităților** proprii → //superputerea// (un punct forte pe care elevul îl are deja);')
D.b('**obiective mici**, duse la capăt → //quest-ul de 30 de zile// (un obiectiv mic, clar și posibil).')
D.p('Activitatea contribuie la scopul proiectului UNIC – incluziunea și continuitatea educației elevilor – prin dezvoltarea motivației pentru '
    'învățare, a capacității de a-și stabili obiective realiste și a perseverenței, factori care susțin participarea și menținerea elevilor în educație.',
    align='justify')

D.h('2. Scopul ședinței')
D.p('Explorarea surselor personale de motivație și conectarea punctelor forte cu un obiectiv mic, realist și realizabil.')

D.h('3. Obiective')
D.p('La finalul ședinței, elevii vor putea:', after=2)
D.b('**O1** – să identifice cel puțin două lucruri care îi motivează;')
D.b('**O2** – să explice că oamenii (și chiar aceeași persoană, în situații diferite) pot fi motivați de lucruri diferite;')
D.b('**O3** – să facă legătura dintre un punct forte propriu și o situație în care îl pot folosi;')
D.b('**O4** – să formuleze o provocare personală pentru 30 de zile și un prim pas concret.')

D.h('4. Elemente de proiectare')
metode(D, [
    ['Domeniul', 'Consiliere și dezvoltare personală – motivație, stabilirea obiectivelor, planificarea dezvoltării personale.'],
    ['Competențe vizate', ['- identificarea surselor personale de motivație și a factorilor care o frânează;',
                           '- utilizarea resurselor personale (punctelor forte) în situații concrete;',
                           '- formularea unor obiective personale realiste și a primilor pași.']],
    ['Metode și procedee', 'Jocul „colțurilor” (alegere prin mișcare), studiul de caz pe grupe, vizualizarea („superputerea”), metoda pașilor mici '
                           '(transformarea dorințelor în obiective), licitația valorilor, scrisoarea către sine, reflecția ghidată, gamificarea.'],
    ['Forme de organizare', 'Frontal, pe grupe, în perechi, individual.'],
    ['Resurse', 'Materiale: Anexele 1–10, Cardurile de agent din Ședința 1, plicuri și consumabile (secțiunea 5). Temporale: 60 de minute. '
                'Umane: 10–15 elevi, facilitatorul comunitar. Spațiale: sală de clasă cu scaune în cerc.'],
    ['Evaluare', 'Observarea sistematică; analiza produselor (Fișele 3–6, provocarea de 30 de zile); fișa de feedback a atelierului; '
                 'autoevaluare (runda „Un cuvânt”).'],
])

D.h('5. Materiale necesare (listă de verificare)')
D.simple_table(['Material', 'Cantitate', 'Unde îl găsești', '✓'], [
    ['Cardurile de agent din Ședința 1 (în plic) + câteva carduri goale pentru elevii noi', '1 / elev', 'Ședința 1, Anexa 7', '☐'],
    ['Fotografia sau afișul cu Harta echipei din Ședința 1', '1', '–', '☐'],
    ['Cartonașe mari „Ce mă motivează?” (8, pentru pereți)', '1 set', 'Anexa 1', '☐'],
    ['Cartonașe „Motivația se schimbă” (6 situații)', '1 set', 'Anexa 2', '☐'],
    ['Fișa 3 – Combustibil și frâne', '1 / elev', 'Anexa 3', '☐'],
    ['Fișa 4 – Superputerea mea', '1 / elev', 'Anexa 4', '☐'],
    ['Fișa 5 – Provocarea LEVEL UP 30', '1 / elev', 'Anexa 5', '☐'],
    ['Semn de carte – trackerul de 30 de zile', '1 / elev', 'Anexa 6', '☐'],
    ['Fișa 6 – Licitația super-echipei + cartonașele calităților (pentru tablă)', '1 / elev + 1 set', 'Anexa 7', '☐'],
    ['Fișa 7 – Scrisoare către mine, peste un an', '1 / elev', 'Anexa 8', '☐'],
    ['Plicuri (pentru scrisori)', '1 / elev', '–', '☐'],
    ['Fișa de feedback a atelierului', '1 / elev', 'Anexa 9', '☐'],
    ['Diplome „Agent LEVEL UP”', '1 / elev', 'Anexa 10', '☐'],
    ['Tablă / flipchart, markere, carioci, pixuri, bandă adezivă', '–', '–', '☐'],
    ['Un „ciocănel” de licitație (un marker sau o riglă e suficient)', '1', '–', '☐'],
], [9.0, 3.0, 3.8, 1.2])

D.h('6. Pregătirea sălii (cu 10 minute înainte)')
D.b('Scaunele în cerc, ca în Ședința 1. Lipește pe pereți, la distanță unele de altele, cele **8 cartonașe „Ce mă motivează?”** (Anexa 1).')
D.b('Scrie pe tablă: **LEVEL UP!  Nivelul 2: COMBUSTIBIL – SUPERPUTERE – QUEST.**')
D.b('Desenează pe tablă un tabel cu cele 8 calități pentru licitație (sau lipește cartonașele din Anexa 7) și lasă loc pentru totaluri.')
D.b('Pune harta echipei (sau fotografia ei proiectată/printată) la vedere.')
D.b('Pregătește cardurile de agent în ordine alfabetică, ca să le împarți repede.')

D.h('7. Principii pentru facilitator')
D.callout('REGULI DE AUR', [
    '- **Nicio motivație nu este „greșită”.** Inclusiv „să câștig bani” sau „să demonstrez că pot” sunt motive legitime. Nu moraliza.',
    '- **Nu cerem alegerea unei profesii.** Accentul cade pe dezvoltare și pe pași mici, nu pe „ce vrei să te faci”.',
    '- **Mic, clar, posibil.** Ajută-i să transforme dorințele mari și vagi în pași concreți, pe care îi pot face chiar săptămâna aceasta.',
    '- **Greșeala face parte din joc.** În jocuri, nimeni nu trece un nivel din prima încercare. Normalizează reîncercarea.',
    '- **Confidențialitate:** scrisorile către „eu, peste un an” nu se citesc. Le păstrezi sigilate.',
    '- **Codul agenției** rămâne valabil: ce se spune aici rămâne aici; râdem împreună, nu unii de alții; oricine poate spune „pas”.',
], C['lyellow'], C['yellow'], C['ink'])

D.h('8. Agenda pe scurt')
D.simple_table(['Timp', 'Activitate', 'Ce urmărim', 'Materiale'], [
    ['0–4\'', '0. Reconectare – bateria mea', 'Revenirea în grup, legătura cu Ședința 1', 'Carduri de agent'],
    ['4–11\'', '1. Colțurile motivației', 'Alegere personală, activare prin mișcare', 'Anexa 1'],
    ['11–18\'', '2. Motivația se schimbă', 'Motivația depinde de persoană și de situație', 'Anexele 2, 3'],
    ['18–27\'', '3. Superputerea mea', 'Legăm punctul forte de acțiune', 'Anexa 4'],
    ['27–40\'', '4. Provocarea LEVEL UP 30', 'Obiectiv mic, realist + primul pas', 'Anexele 5, 6'],
    ['40–48\'', '5. Licitația super-echipei', 'Reflecție asupra calităților importante', 'Anexa 7'],
    ['48–55\'', '6. Scrisoare către mine, peste un an', 'Integrare, proiecție în viitor', 'Anexa 8, plicuri'],
    ['55–60\'', '7. Încheiere – un cuvânt + diplome', 'Închiderea atelierului, feedback', 'Anexele 9, 10'],
], [1.6, 5.6, 6.0, 3.8], bold_first=True)

D.h('9. Desfășurarea pas cu pas')

D.activity('0', 'Reconectare – bateria mea', '4 min', 'minutele 0–4', [
    ('SCOP', 'Elevii revin în atmosfera atelierului și își reamintesc ce au descoperit data trecută.'),
    ('FĂ', ['- Împarte cardurile de agent. Elevii noi primesc un card gol și îl completează rapid cu un punct forte.',
            '- **Check-in „Bateria”:** la semnalul tău, fiecare arată cu degetele cât de „încărcat” este azi, de la 1 la 5. Nu se comentează.',
            '- Arată harta echipei din Ședința 1 și citește 3–4 post-it-uri.']),
    ('SPUNE', ['„Bine ați revenit, agenți! Data trecută am descoperit ce avem bun. Astăzi trecem la nivelul următor: LEVEL UP.”',
               '„În orice joc, un personaj crește în nivel dacă are un motiv să continue, dacă își folosește abilitățile și dacă duce la capăt misiuni mici. '
               'Exact asta facem azi: găsim combustibilul, superputerea și quest-ul fiecăruia.”']),
])

D.activity('1', 'Colțurile motivației', '7 min', 'minutele 4–11', [
    ('SCOP', 'Elevii își aleg sursa principală de motivație și văd că alții pot alege diferit.'),
    ('FĂ', ['- Pe pereți sunt cele 8 cartonașe (Anexa 1): SĂ FIU BUN/BUNĂ • SĂ FAC CE ÎMI PLACE • SĂ-MI FAC FAMILIA MÂNDRĂ • SĂ CÂȘTIG BANI • '
            'SĂ AJUT OAMENII • SĂ AJUNG UNDE ÎMI DORESC • SĂ DEMONSTREZ CĂ POT • SĂ ÎNVĂȚ LUCRURI NOI.',
            '- **Runda 1:** fiecare merge la cartonașul care i se potrivește cel mai bine. Întreabă 2–3 voluntari, din grupuri diferite: „De ce ai ales asta?”',
            '- **Runda 2:** „Acum mergeți la al doilea motiv, cel de rezervă.” Observă ce grupuri se formează și cine își schimbă locul.']),
    ('SPUNE', '„Imaginați-vă că trebuie să faceți ceva greu: să vă antrenați pentru un concurs, să învățați pentru un test dificil sau să terminați '
              'un proiect lung. Ce v-ar face să continuați, atunci când ați vrea să renunțați? Mergeți la cartonașul care vi se potrivește cel mai bine.”'),
    ('ÎNTREABĂ', ['- „Ce observați? Suntem toți la același cartonaș?”',
                  '- „Cine a ales alt cartonaș la runda a doua? De ce?”']),
    ('MESAJ-CHEIE', '**Nu există o singură motivație corectă. Oamenii pot fi puși în mișcare de lucruri diferite și, de obicei, au mai multe motive în același timp.**'),
    ('ATENȚIE', 'Dacă un elev rămâne singur la un cartonaș, apreciază-i curajul: „Ai ales după tine, nu după grup. Asta e o calitate.”'),
])

D.activity('2', 'Motivația se schimbă', '7 min', 'minutele 11–18', [
    ('SCOP', 'Elevii înțeleg că motivația depinde de situație și că există atât „combustibil”, cât și „frâne”.'),
    ('FĂ', ['- Împarte grupul în 3 echipe. Fiecare echipă extrage **2 cartonașe-situație** (Anexa 2) și are **3 minute** să răspundă la '
            'întrebările de pe cartonaș.',
            '- Fiecare echipă spune, în 30 de secunde, cea mai bună idee găsită (2 minute în total).',
            '- Introdu ideea de **combustibil** (ce ne pune în mișcare) și **frâne** (ce ne oprește: frica de greșeală, comparația cu alții, '
            'oboseala, telefonul, rezultatele care nu vin repede).',
            '- Elevii completează individual **Fișa 3 – Combustibil și frâne** (Anexa 3). Timp: 2 minute. Dacă nu ajung, o termină acasă.']),
    ('ÎNTREABĂ', ['- „Ce te-ar face să continui în situația aceasta?”',
                  '- „Ar funcționa același lucru pentru toți? Dar pentru tine, în altă zi?”']),
    ('MESAJ-CHEIE', '**Motivația poate fi diferită de la o persoană la alta și chiar de la o situație la alta. Dacă îmi cunosc frânele, '
                    'pot să-mi pregătesc un plan pentru ele.**'),
])

D.activity('3', 'Superputerea mea', '9 min', 'minutele 18–27', [
    ('SCOP', 'Elevii transformă un punct forte într-o „superputere” pe care o pot folosi concret.'),
    ('FĂ', ['- Elevii se uită la abilitățile de pe Cardul de agent și pe harta echipei și aleg **o singură superputere**.',
            '- Completează **Fișa 4** (Anexa 4): numele superputerii, simbolul, când îi ajută, unde ar putea s-o folosească, un exemplu real și '
            '**kryptonita** (ce le slăbește puterea). Timp: 5 minute.',
            '- **Trailerul eroului** (3 minute): 3–4 voluntari își prezintă superputerea ca pe un trailer de film, cu vocea unui crainic: '
            '„Într-o lume în care toți renunță la primul eșec... un singur elev are puterea de a încerca din nou...”',
            '- Elevii trec superputerea pe Cardul de agent, la Nivelul 2.']),
    ('SPUNE', '„Imaginați-vă că aveți o superputere reală, nu una din filme. Este o calitate sau o abilitate pe care o aveți deja. '
              'De exemplu: umorul, care poate liniști o ceartă; răbdarea, cu care explici altcuiva; creativitatea; perseverența; '
              'faptul că știi să asculți. Și orice supererou are o kryptonită: ce vă slăbește superputerea?”'),
    ('ATENȚIE', 'Elevii care spun „n-am nicio superputere” pot primi ajutor de la un coleg („Ce superputere crezi că are el/ea?”) sau se pot uita '
                'la complimentele primite în Ședința 1, notate pe card.'),
])

D.activity('4', 'Provocarea LEVEL UP 30', '13 min', 'minutele 27–40', [
    ('SCOP', 'Fiecare elev își alege un singur lucru mic de dezvoltat în următoarele 30 de zile și primul pas concret.'),
    ('SPUNE', '„Nu vă cer să decideți acum ce veți face toată viața. Alegem un singur lucru mic pe care vrem să-l îmbunătățim în următoarele 30 de zile '
              '– ca un quest dintr-un joc. Nu trebuie să schimbați totul. Un singur lucru, mic.”'),
    ('FĂ', ['# Pasul 1 – Transformatorul (3 min)',
            '- Scrie pe tablă o dorință vagă și transform-o, împreună cu grupul, într-un quest concret, după formula: '
            '**CE fac + CÂND / CÂT DE DES + CUM îmi dau seama că am reușit.**',
            '- „Vreau să fiu mai bun la sport” → „Fac 20 de genuflexiuni luni, miercuri și vineri, după școală.”',
            '- „Vreau să învăț mai bine” → „Îmi fac tema la matematică înainte de ora 18, cu telefonul în altă cameră, 4 zile pe săptămână.”',
            '- „Vreau să stau mai puțin pe telefon” → „Nu iau telefonul în mână în prima jumătate de oră după ce vin de la școală.”',
            '- „Vreau să am mai mult curaj” → „Ridic mâna o dată pe săptămână la o oră la care de obicei tac.”',
            '# Pasul 2 – Fișa 5 (6 min)',
            '- Elevii completează **Fișa 5 – Provocarea LEVEL UP 30** (Anexa 5). Tu circuli printre ei și îi ajuți să facă obiectivul mai mic și mai clar.',
            '- Verificarea rapidă: **Mic? Clar? Posibil? Îl pot bifa?** Dacă răspunsul e „nu” la una dintre întrebări, mai „micșorăm” quest-ul.',
            '# Pasul 3 – Semnul de carte (3 min)',
            '- Fiecare primește semnul de carte (Anexa 6), scrie pe el quest-ul și îl va folosi ca tracker: bifează o căsuță în fiecare zi în care face pasul.',
            '# Pasul 4 – Partenerul de quest (1 min, opțional)',
            '- Elevii care vor își aleg un coleg cu care să-și verifice progresul o dată pe săptămână („Cum merge quest-ul?”).']),
    ('MESAJ-CHEIE', '**Obiectivul trebuie să fie mic, clar și posibil. Dacă ratezi o zi, nu ai pierdut jocul: continui a doua zi.**'),
    ('ATENȚIE', 'Quest-urile rămân personale. Nimeni nu este obligat să și-l citească cu voce tare. Evită obiectivele legate de greutate sau de aspectul '
                'fizic; redirecționează-le spre energie, mișcare, somn sau sănătate („mă plimb 20 de minute”).'),
])

D.activity('5', 'Licitația super-echipei', '8 min', 'minutele 40–48', [
    ('SCOP', 'Elevii reflectează asupra calităților pe care le prețuiesc și asupra celor de care au nevoie pentru quest-ul lor.'),
    ('SPUNE', '„Fiecare dintre voi are 10 monede de aur. Construiți super-echipa ideală pentru o misiune grea. Puteți investi monedele în 8 calități: '
              'curaj, creativitate, umor, răbdare, comunicare, perseverență, organizare și lucru în echipă. Puteți pune toate cele 10 monede într-o singură '
              'calitate sau le puteți împărți. Total: exact 10.”'),
    ('FĂ', ['- Elevii completează coloana „Monedele mele” din **Fișa 6** (Anexa 7). Timp: 2 minute.',
            '- **Licitația live** (3 minute): ești licitatorul, cu „ciocănelul” în mână. Strigi fiecare calitate: „CURAJ! Cine a investit cel puțin 3 monede? '
            'Cine are 5? 7? Cine bate oferta? ... Adjudecat!” Ridică mâinile, aplaudă oferta câștigătoare și notează pe tablă totalul grupului '
            'pentru fiecare calitate (suma monedelor tuturor).',
            '- Priviți împreună tabla: care sunt calitățile pe care grupul le prețuiește cel mai mult?']),
    ('ÎNTREABĂ', ['- „De ce ai pus cele mai multe monede acolo?”',
                  '- „Ce calitate te-ar ajuta cel mai mult la provocarea ta de 30 de zile?”',
                  '- „Ai deja măcar puțin din această calitate? Unde se vede?”']),
    ('VARIANTĂ', 'Dacă grupul este liniștit sau timpul e scurt, sari peste licitația live: faceți doar totalurile pe tablă și discutați 2 întrebări.'),
])

D.activity('6', 'Scrisoare către mine, peste un an', '7 min', 'minutele 48–55', [
    ('SCOP', 'Integrare: elevii se gândesc la direcția în care vor să crească, fără presiunea de a alege o profesie.'),
    ('FĂ', ['- Împarte **Fișa 7 – Scrisoare către mine, peste un an** (Anexa 8) și câte un plic.',
            '- Elevii scriu scrisoarea (5 minute), o pliază, o pun în plic, îl lipesc și scriu pe el numele lor și „A SE DESCHIDE LA: ___”.',
            '- Strânge plicurile. Le vei înmâna elevilor la finalul proiectului sau al anului școlar (stabilește cu dirigintele). '
            'Elevii care vor să-și păstreze scrisoarea o pot lua acasă.']),
    ('SPUNE', ['„Imaginați-vă că peste un an primiți o scrisoare de la voi, cei de azi. Ce v-ați spune? Ce ați vrea să fi încercat până atunci? '
               'Cum ați vrea să puteți spune despre voi: «Eu sunt o persoană care...»?”',
               '„Nimeni nu va citi scrisorile, nici măcar eu. Sunt doar ale voastre.”']),
    ('ATENȚIE', 'Respectă promisiunea: nu deschide plicurile. Dacă un elev vrea să-ți spună ce a scris, ascultă-l, dar nu cere asta nimănui.'),
])

D.activity('7', 'Încheiere – un cuvânt + diplome', '5 min', 'minutele 55–60', [
    ('SCOP', 'Închiderea atelierului într-o notă pozitivă și colectarea feedbackului.'),
    ('FĂ', ['- Elevii completează **Fișa de feedback** (Anexa 9). Timp: 1–2 minute.',
            '- **Runda „Un cuvânt”:** pe rând, fiecare spune un singur cuvânt despre cum pleacă de la atelier (sau „pas”).',
            '- Înmânează **diplomele „Agent LEVEL UP”** (Anexa 10), cu aplauze pentru fiecare. Elevii iau acasă Cardul de agent și semnul de carte.']),
    ('SPUNE', ['„Nu trebuie să știți astăzi exact cine veți fi peste câțiva ani. Important este să vă cunoașteți, să știți ce aveți bun '
               'și să puteți face pași mici în direcția dorită.”',
               '„Puneți-vă cardul și semnul de carte undeva unde le vedeți zilnic. Peste 30 de zile, verificați câte căsuțe ați bifat. '
               'Misiune îndeplinită, agenți: LEVEL UP!”']),
])

D.h('10. Situații dificile – ce faci dacă...')
D.simple_table(['Situația', 'Ce poți face'], [
    ['Un elev spune „pe mine nu mă motivează nimic”.',
     'Acceptă răspunsul fără să-l contrazici. Întreabă: „Pentru ce ai fi dispus să te trezești mai devreme sâmbătă?” sau „Ce faci fără să-ți spună nimeni?”. '
     'Acolo se ascunde, de obicei, combustibilul.'],
    ['Quest-ul este prea mare („vreau să iau 10 la toate materiile”).',
     'Nu respinge visul. Întreabă: „Care ar fi cel mai mic pas spre asta, pe care îl poți face săptămâna aceasta?” și scrieți pasul ca quest.'],
    ['Elevii fac glume pe seama motivației „bani” sau „familia”.',
     'Amintește că toate motivațiile sunt valabile și că tocmai diferențele ne fac interesanți. Reamintește regula „râdem împreună, nu unii de alții”.'],
    ['Licitația devine prea gălăgioasă.',
     'Folosește semnalul „Agenți, pe poziții!”. Treci la varianta fără licitație live (doar totalurile pe tablă).'],
    ['Un elev a lipsit la Ședința 1.',
     'Dă-i un card gol. Roagă un coleg să-i spună, în 1 minut, ce puncte forte a observat la el sau ea. Elevul își completează cardul pe loc.'],
    ['Rămâi fără timp.',
     'Fișa 3 se poate termina acasă. Licitația se poate face fără runda live. Nu sări peste scrisoare și peste încheiere.'],
    ['Un elev spune ceva îngrijorător.',
     'Nu aprofunda subiectul în grup. Discută cu elevul individual după ședință și urmează procedura școlii și a proiectului '
     '(consilierul școlar, dirigintele, coordonatorul proiectului).'],
], [5.2, 11.8], bold_first=True)

D.h('11. Lista anexelor și numărul de exemplare de tipărit')
D.p('Recomandare: fișele de lucru se pot tipări alb-negru. Cartonașele pentru pereți (Anexa 1), semnele de carte (Anexa 6) '
    'și diplomele (Anexa 10) arată mai bine color, eventual pe carton.', italic=True, color=C['grey'])
D.simple_table(['Anexa', 'Conținut', 'De tipărit (pentru 15 elevi)'], [
    ['Anexa 1', 'Cartonașe mari „Ce mă motivează?” (8, câte 2 pe pagină)', '1 set (4 pagini)'],
    ['Anexa 2', 'Cartonașe „Motivația se schimbă” (6 situații)', '1 pagină'],
    ['Anexa 3', 'Fișa 3 – Combustibil și frâne', '15 exemplare'],
    ['Anexa 4', 'Fișa 4 – Superputerea mea', '15 exemplare'],
    ['Anexa 5', 'Fișa 5 – Provocarea LEVEL UP 30', '15 exemplare'],
    ['Anexa 6', 'Semn de carte – trackerul de 30 de zile (3 pe pagină)', '5 pagini, de preferință pe carton'],
    ['Anexa 7', 'Fișa 6 – Licitația super-echipei + cartonașele calităților pentru tablă', '15 exemplare + 1 pagină de cartonașe'],
    ['Anexa 8', 'Fișa 7 – Scrisoare către mine, peste un an', '15 exemplare + 15 plicuri'],
    ['Anexa 9', 'Fișa de feedback a atelierului (2 pe pagină)', '8 pagini'],
    ['Anexa 10', 'Diploma „Agent LEVEL UP” (2 pe pagină)', '8 pagini, de preferință color'],
], [2.2, 9.6, 5.2], bold_first=True)

raport(D, 12, ['O1 – identifică cel puțin două surse personale de motivație', 'O2 – explică faptul că motivația diferă între persoane și situații',
              'O3 – leagă un punct forte de o situație concretă', 'O4 – formulează o provocare de 30 de zile și un prim pas'],
       'De ex.: nr. de provocări de 30 de zile formulate, fișe completate, scrisori sigilate (păstrate de facilitator), media scorurilor din fișele de feedback.')

# =====================================================================  ANEXE
MOT = [
    ('SĂ FIU BUN / BUNĂ LA CEEA CE FAC', 'Îmi place să simt că mă descurc din ce în ce mai bine.', C['purple'], C['lav']),
    ('SĂ FAC CE ÎMI PLACE', 'Continui pentru că activitatea în sine mă bucură.', C['green'], C['lgreen']),
    ('SĂ-MI FAC FAMILIA MÂNDRĂ', 'Contează pentru mine ce simt cei dragi.', C['orange'], C['lorange']),
    ('SĂ CÂȘTIG BANI', 'Vreau să-mi permit lucrurile pe care mi le doresc.', 'B07A00', C['lyellow']),
    ('SĂ AJUT OAMENII', 'Mă pune în mișcare gândul că fac bine cuiva.', '2C6E6A', 'E0F0EE'),
    ('SĂ AJUNG UNDE ÎMI DORESC', 'Am un vis sau un scop și merg spre el.', C['blue'], C['lblue']),
    ('SĂ DEMONSTREZ CĂ POT', 'Mă motivează o provocare sau cineva care nu crede în mine.', 'A0263C', 'F8E1E5'),
    ('SĂ ÎNVĂȚ LUCRURI NOI', 'Sunt curios / curioasă și îmi place să descopăr.', '5B6B00', 'EEF2D6'),
]
for k in range(4):
    D.annex_title('ANEXA 1', 'Cartonașe „Ce mă motivează?”  (%d / 4)' % (k + 1))
    for j in range(2):
        idx = k * 2 + j
        name, sub, col, light = MOT[idx]
        t = table(d, 1, 1, [CONTENT_W], borders=('single', 24, col), lr=0.5, tb=0.3)
        row_setup(t.rows[0], 10.4, exact=True)
        cell = t.cell(0, 0)
        shade(cell, light)
        cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
        para(cell, 'MOTIVUL %d' % (idx + 1), 12, True, color=col, align='center', after=4)
        para(cell, name, 38 if len(name) < 22 else 30, True, color=col, align='center', after=10, line=1.0)
        para(cell, '„' + sub + '”', 17, italic=True, color=C['ink'], align='center', after=0)
        if j == 0:
            spacer(d, 10)

# ---- Anexa 2 – Situații
D.annex_title('ANEXA 2', 'Cartonașe „Motivația se schimbă”')
scissors_note(d, '✂  Decupează. Fiecare echipă extrage 2 cartonașe și are 3 minute pentru discuție.')
SIT = [
    'Mâine ai test la matematică. Prietenii tăi tocmai te-au chemat la un joc online.',
    'Echipa ta a pierdut un meci important cu 5–0. Antrenamentul următor este mâine dimineață.',
    'Vrei să înveți să cânți la chitară (sau să desenezi). După o săptămână, încă nu-ți iese nimic.',
    'Ai o idee de proiect pentru clasă, dar nu știi dacă o să reușească și dacă le va plăcea colegilor.',
    'Ai lucrat două zile la un video sau la un desen. L-ai postat și a primit doar 3 aprecieri.',
    'Mai sunt multe luni până la Evaluarea Națională și simți că ai timp „de-ajuns”.',
]


def sit(cell, i):
    shade(cell, [C['lav'], C['lyellow'], C['lgreen']][i % 3])
    para(cell, 'SITUAȚIA %d' % (i + 1), 14, True, color=C['purple'], after=4)
    para(cell, SIT[i], 11.5, after=8)
    for q in ('Ce te-ar face să continui?', 'Ce te-ar putea face să renunți?', 'Ce ai putea face concret?'):
        bullet(cell, q, 10, mark='▸', after=1)


cut_grid(d, 6, 2, 8.5, 7.1, sit)

# ---- Anexa 3 – Fișa 3
D.annex_title('ANEXA 3', 'FIȘA 3 – Combustibil și frâne: ce mă pune în mișcare?')
field(d, [('Numele meu:', 10)], 10.5, before=0, after=4)
para(d, 'COMBUSTIBILUL MEU – Alege 2 lucruri care te motivează cel mai mult:', 11, True, color=C['green'], before=6, after=3)
checkbox_grid(d, ['Să fiu bun/bună la ceea ce fac', 'Să fac ceea ce îmi place', 'Să-mi fac familia mândră', 'Să câștig bani',
                  'Să ajut alți oameni', 'Să ajung unde îmi doresc', 'Să demonstrez că pot', 'Să învăț lucruri noi'], 2, CONTENT_W, 10.5)
para(d, 'Un lucru care mă face să continui chiar și când este greu:', 10.5, True, before=8, after=0)
lines(d, 2, CONTENT_W, 10.5, before=10)
para(d, 'FRÂNELE MELE – Ce mă poate face să renunț prea repede? (bifează)', 11, True, color=C['orange'], before=12, after=3)
checkbox_grid(d, ['frica de a greși', 'mă compar cu alții', 'oboseala', 'telefonul / jocurile',
                  'nu văd rezultate repede', 'cineva râde de mine', 'nu știu de unde să încep', 'altceva: ____________'], 2, CONTENT_W, 10.5)
para(d, 'Planul meu anti-frână – ce m-ar putea ajuta atunci?', 10.5, True, before=8, after=0)
lines(d, 2, CONTENT_W, 10.5, before=10)
spacer(d, 8)
t = table(d, 1, 1, [CONTENT_W], borders=('single', 12, C['yellow']), lr=0.3, tb=0.15)
cell = t.cell(0, 0)
shade(cell, C['lyellow'])
para(cell, 'Știai că...?', 10.5, True, color=C['purple'], after=2)
para(cell, 'Motivația nu e ca un buton care ori e pornit, ori e oprit. Vine și pleacă, ca valurile. De aceea, oamenii care reușesc nu sunt '
           'cei care au mereu chef, ci cei care au **un plan pentru zilele fără chef**: un pas foarte mic, un prieten care îi încurajează, o recompensă.',
     10, after=2)

# ---- Anexa 4 – Fișa 4 Superputerea
D.annex_title('ANEXA 4', 'FIȘA 4 – Superputerea mea')
field(d, [('Numele meu de agent:', 10)], 10.5, before=0, after=4)
para(d, 'Imaginează-ți că ai o superputere pe care o folosești deja în viața reală: o calitate sau o abilitate pe care o ai.',
     10, italic=True, color=C['grey'], before=2, after=6)
t = table(d, 1, 2, [5.6, 11.4], borders=('single', 12, C['purple']), inside=('single', 6, C['lav2']), lr=0.3, tb=0.15)
row_setup(t.rows[0], 5.6)
a, b_ = t.cell(0, 0), t.cell(0, 1)
para(a, 'SIMBOLUL SUPERPUTERII MELE', 8.5, True, color=C['grey'], align='center', after=0)
para(a, '(desenează un logo, ca la supereroi)', 8, italic=True, color=C['grey'], align='center', after=0)
shade(b_, C['lav'])
para(b_, 'SUPERPUTEREA MEA ESTE:', 12, True, color=C['purple'], after=0)
lines(b_, 1, 10.8, 13, before=14)
para(b_, 'Exemple: umorul, răbdarea, creativitatea, perseverența, curajul, să ascult, să explic, să organizez, să-i încurajez pe alții...',
     8.5, italic=True, color=C['grey'], before=8, after=0)
for q in ['Mă ajută atunci când:', 'Aș putea să o folosesc pentru:', 'Un exemplu real, când am folosit această superputere:']:
    para(d, q, 10.5, True, before=10, after=0, keep=True)
    lines(d, 2, CONTENT_W, 10.5, before=10)
t = table(d, 1, 2, [8.4, 8.6], borders=('single', 6, C['lav2']), inside=('single', 6, C['lav2']), lr=0.3, tb=0.15)
a, b_ = t.cell(0, 0), t.cell(0, 1)
shade(a, C['lorange'])
shade(b_, C['lgreen'])
para(a, 'KRYPTONITA MEA', 10.5, True, color=C['orange'], after=0)
para(a, 'Ce îmi slăbește superputerea?', 9, italic=True, after=0)
lines(a, 2, 7.8, 10.5, before=10)
para(b_, 'CUM ÎMI REÎNCARC PUTEREA', 10.5, True, color=C['green'], after=0)
para(b_, 'Ce mă ajută să-mi revin?', 9, italic=True, after=0)
lines(b_, 2, 8.0, 10.5, before=10)
spacer(d, 8)
para(d, 'TRAILERUL EROULUI (citește-l cu voce de crainic de film):', 10.5, True, color=C['purple'], before=6, after=0)
field(d, [('„Într-o lume în care', CONTENT_W)], 10.5, before=10, bold_labels=False)
field(d, [('un singur elev are puterea de a', CONTENT_W)], 10.5, before=10, bold_labels=False)
para(d, '.” În curând, la o școală lângă tine!', 10.5, italic=True, align='right', before=6)

# ---- Anexa 5 – Fișa 5 LEVEL UP 30
D.annex_title('ANEXA 5', 'FIȘA 5 – Provocarea LEVEL UP 30')
t = table(d, 1, 1, [CONTENT_W], borders=('single', 8, C['blue']), lr=0.3, tb=0.12)
cell = t.cell(0, 0)
shade(cell, C['lblue'])
para(cell, 'TRANSFORMATORUL: din dorință vagă → în quest concret   (CE fac + CÂND / CÂT DE DES + CUM știu că am reușit)', 9.5, True, color=C['blue'], after=2)
for ex in ['„Vreau să fiu mai bun la sport” → „Fac 20 de genuflexiuni luni, miercuri și vineri, după școală.”',
           '„Vreau să citesc mai mult” → „Citesc 10 pagini în fiecare seară, înainte de culcare.”',
           '„Vreau să fiu mai sociabil” → „În fiecare săptămână vorbesc cu un coleg cu care n-am mai vorbit.”']:
    bullet(cell, ex, 9, mark='▸', mark_color=C['blue'], after=0)
spacer(d, 4)
blocks = [('QUEST-UL MEU – În următoarele 30 de zile vreau să:', 2),
          ('De ce este important pentru mine?', 1),
          ('Superputerea (punctul forte) care mă ajută:', 1),
          ('Primul pas – ce fac exact și când (chiar săptămâna aceasta):', 2),
          ('Cine m-ar putea ajuta dacă am nevoie?', 1),
          ('Cum îmi dau seama, după 30 de zile, că am reușit?', 1)]
for q, n in blocks:
    para(d, q, 10.5, True, color=C['purple'] if q.startswith('QUEST') else None, before=7, after=0, keep=True)
    lines(d, n, CONTENT_W, 10.5, before=9)
para(d, 'Verificarea quest-ului – quest-ul meu este:', 10.5, True, before=10, after=2)
checkbox_grid(d, ['MIC', 'CLAR', 'POSIBIL', 'POT SĂ-L BIFEZ'], 4, CONTENT_W, 10.5)
para(d, 'Dacă nu-mi iese din prima, eu:', 10.5, True, before=6, after=2)
checkbox_grid(d, ['mai încerc', 'cer ajutor', 'schimb metoda', 'încerc din nou mai târziu'], 4, CONTENT_W, 10.5)
field(d, [('Recompensa mea după 30 de zile:', CONTENT_W)], 10.5, before=10)
field(d, [('Motto-ul meu: „', 16.6)], 10.5, before=10)

# ---- Anexa 6 – Semn de carte
D.annex_title('ANEXA 6', 'Semn de carte – trackerul LEVEL UP 30')
scissors_note(d, '✂  Decupează pe linia punctată. Recomandare: tipărește pe carton, color.')


def bookmark(cell, i):
    shade(cell, [C['lav'], C['lgreen'], C['lyellow']][i])
    para(cell, 'LEVEL UP', 22, True, color=C['purple'], align='center', after=0, line=1.0)
    para(cell, '30 DE ZILE', 11, True, color=C['green'], align='center', after=6)
    para(cell, 'Quest-ul meu:', 9.5, True, after=0)
    lines(cell, 3, 4.9, 10, before=12)
    field(cell, [('Superputerea mea:', 4.9)], 9, before=10)
    para(cell, 'Bifează o căsuță în fiecare zi în care faci pasul:', 8, italic=True, color=C['grey'], before=8, after=3)
    g = table(cell, 6, 5, [0.95] * 5, borders=('single', 6, C['purple']), inside=('single', 6, C['purple']), lr=0.02, tb=0.02)
    for r in g.rows:
        row_setup(r, 1.25, exact=True)
    for k in range(30):
        gc = g.cell(k // 5, k % 5)
        shade(gc, 'FFFFFF')
        para(gc, str(k + 1), 7.5, color=C['grey'], align='left', after=0)
    para(cell, 'Ai ratat o zi? Nu-i nimic. Continui a doua zi!', 8.5, True, italic=True, color=C['orange'], align='center', before=8, after=4)
    para(cell, 'Progresul meu (colorează):', 8.5, True, before=4, after=2)
    para(cell, 'Săpt. 1 ☐  2 ☐  3 ☐  4 ☐', 10, True, color=C['purple'], align='center', after=2)
    field(cell, [('Ziua 30 – recompensa mea:', 4.9)], 8.5, before=8)
    field(cell, [('Partener de quest:', 4.9)], 8.5, before=8)
    para(cell, 'Pas cu pas, nivel cu nivel.', 10, True, color=C['purple'], align='center', before=10, after=0)


cut_grid(d, 3, 3, 5.66, 21.6, bookmark)

# ---- Anexa 7 – Licitația
D.annex_title('ANEXA 7', 'FIȘA 6 – Licitația super-echipei')
field(d, [('Numele meu:', 10)], 10.5, before=0, after=4)
para(d, 'Ai 10 monede de aur. Investește-le în calitățile de care ar avea nevoie super-echipa ta pentru o misiune grea. '
     'Poți pune toate monedele într-o singură calitate sau le poți împărți. Total: exact 10.', 10, italic=True, color=C['grey'], before=4, after=6)
QUAL = [('CURAJ', 'să încerci, chiar dacă îți e frică'), ('CREATIVITATE', 'idei noi, soluții neobișnuite'),
        ('UMOR', 'destinde atmosfera, ridică moralul'), ('RĂBDARE', 'aștepți, explici, nu te enervezi ușor'),
        ('COMUNICARE', 'asculți și te faci înțeles'), ('PERSEVERENȚĂ', 'nu renunți la prima piedică'),
        ('ORGANIZARE', 'plan, ordine, timp bine folosit'), ('LUCRU ÎN ECHIPĂ', 'colaborezi, împarți sarcinile')]
t = D.simple_table(['Calitatea', 'Ce înseamnă', 'Monedele mele', 'Totalul grupului'],
                   [[q, m, '', ''] for q, m in QUAL] + [['TOTAL', '', '10', '']],
                   [4.0, 7.0, 3.0, 3.0], size=10.5, bold_first=True)
for r in t.rows[1:]:
    row_setup(r, 0.9)
    for c_ in r.cells:
        c_.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
for c_ in t.rows[-1].cells:
    shade(c_, C['lyellow'])
for q in ['Am investit cele mai multe monede în ______________________ pentru că:',
          'Calitatea care m-ar ajuta cel mai mult la quest-ul meu de 30 de zile:',
          'O calitate din listă pe care o am deja (măcar puțin) și unde se vede:']:
    para(d, q, 10.5, True, before=8, after=0, keep=True)
    lines(d, 2, CONTENT_W, 10.5, before=10)

D.annex_title('ANEXA 7', 'Cartonașele calităților – pentru tablă')
scissors_note(d, '✂  Decupează și lipește cartonașele pe tablă. Sub fiecare, notează totalul monedelor grupului.')


def qual(cell, i):
    cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
    shade(cell, [C['lav'], C['lyellow']][(i // 2 + i) % 2])
    para(cell, QUAL[i][0], 26 if len(QUAL[i][0]) < 13 else 21, True, color=C['purple'], align='center', after=4, line=1.0)
    para(cell, QUAL[i][1], 11, italic=True, color=C['grey'], align='center', after=0)


cut_grid(d, 8, 2, 8.5, 5.3, qual)

# ---- Anexa 8 – Scrisoare
D.annex_title('ANEXA 8', 'FIȘA 7 – Scrisoare către mine, peste un an')
t = table(d, 1, 1, [CONTENT_W], borders=('double', 6, C['purple']), lr=0.6, tb=0.3)
cell = t.cell(0, 0)
p = para(cell, '', after=0)
p.paragraph_format.tab_stops.add_tab_stop(Cm(15.6), WD_TAB_ALIGNMENT.RIGHT)
runs(p, 'Data de azi: ____________\tA SE DESCHIDE LA: ____________', 10, True, color=C['purple'])
para(cell, 'Dragă eu (cel / cea de peste un an),', 14, True, italic=True, color=C['purple'], before=12, after=2)
para(cell, 'Nu trebuie să știi exact ce vei face în viitor. Gândește-te doar la direcția în care vrei să crești.', 9.5, italic=True,
     color=C['grey'], after=4)
for q, n in [('Până atunci, aș vrea să fiu mai bun / bună la:', 2), ('Aș vrea să fi încercat:', 2),
             ('Aș vrea să pot spune despre mine: „Eu sunt o persoană care...', 2),
             ('Un lucru pe care îl pot începe chiar de acum:', 2), ('Un sfat pentru tine, de la mine:', 3)]:
    para(cell, q, 10.5, True, before=8, after=0, keep=True)
    lines(cell, n, 15.6, 11, before=13)
para(cell, 'Cu drag,', 11, italic=True, before=12, after=0)
field(cell, [('eu, la vârsta de ____ ani,', 15.6)], 11, before=8, bold_labels=False, after=4)
para(d, 'Pliază scrisoarea, pune-o în plic, lipește plicul și scrie pe el numele tău. Nimeni nu o va citi.', 9, italic=True,
     color=C['grey'], align='center', before=6)

# ---- Anexa 9 – Feedback
D.annex_title('ANEXA 9', 'Fișa de feedback a atelierului')
scissors_note(d, '✂  Fișa este anonimă. Decupează pe linia punctată.')


def feedback(cell, i):
    para(cell, 'CUM A FOST ATELIERUL? – fișă anonimă', 11, True, color=C['purple'], after=0)
    para(cell, 'Încercuiește: 1 = deloc   •   5 = foarte mult', 8.5, italic=True, color=C['grey'], after=3)
    g = table(cell, 5, 2, [11.7, 4.4], borders=None, inside=('single', 4, C['lav2']), lr=0.1, tb=0.03)
    items = ['Am descoperit lucruri noi despre mine.', 'M-am simțit în siguranță în grup.', 'Activitățile au fost interesante.',
             'Știu care este următorul meu pas (quest-ul).', 'Aș recomanda atelierul unui prieten.']
    for k, it in enumerate(items):
        para(g.cell(k, 0), it, 9.5, after=0)
        para(g.cell(k, 1), '1   2   3   4   5', 10, True, color=C['purple'], align='center', after=0)
    para(cell, 'Activitatea mea preferată (bifează una):', 9.5, True, before=5, after=1)
    checkbox_grid(cell, ['Colțurile motivației', 'Superputerea mea', 'LEVEL UP 30', 'Licitația', 'Scrisoarea', 'Detectivii (Ședința 1)'],
                  3, 16.1, 9)
    field(cell, [('Ce aș schimba:', 16.1)], 9.5, before=9)
    field(cell, [('Un lucru pe care îl iau cu mine:', 16.1)], 9.5, before=9)
    field(cell, [('Atelierul într-un cuvânt:', 16.1)], 9.5, before=9)
    field(cell, [('Un mesaj pentru facilitator:', 16.1)], 9.5, before=9)
    lines(cell, 1, 16.1, 9.5, before=11)


cut_grid(d, 2, 1, CONTENT_W, 10.9, feedback)

# ---- Anexa 10 – Diplomă
D.annex_title('ANEXA 10', 'Diploma „Agent LEVEL UP”')
scissors_note(d, '✂  Decupează pe linia punctată. Recomandare: tipărire color, pe carton.')


def diploma(cell, i):
    cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
    inner = table(cell, 1, 1, [15.9], borders=('double', 12, C['purple']), lr=0.5, tb=0.2)
    row_setup(inner.rows[0], 10.0, exact=True)
    ic = inner.cell(0, 0)
    ic.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
    shade(ic, C['lav'])
    para(ic, '★  ★  ★', 14, True, color='B58A00', align='center', after=0)
    para(ic, 'DIPLOMĂ DE AGENT LEVEL UP', 22, True, color=C['purple'], align='center', after=4)
    para(ic, 'Se acordă agentului / agentei', 11, italic=True, align='center', after=0)
    p = para(ic, '', align='center', before=6, after=4)
    p.paragraph_format.tab_stops.add_tab_stop(Cm(12.5), WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.LINES)
    p.paragraph_format.left_indent = Cm(2.4)
    runs(p, '\t', 14)
    para(ic, 'pentru că și-a descoperit punctele forte, și-a găsit superputerea și a acceptat provocarea LEVEL UP 30 '
             'în cadrul atelierului „Eu, punctele mele forte și ce mă motivează”.', 10.5, align='center', before=4, after=6)
    p = para(ic, '', before=8, after=0)
    p.paragraph_format.tab_stops.add_tab_stop(Cm(7.0), WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.LINES)
    p.paragraph_format.tab_stops.add_tab_stop(Cm(8.2), WD_TAB_ALIGNMENT.LEFT)
    p.paragraph_format.tab_stops.add_tab_stop(Cm(14.8), WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.LINES)
    runs(p, '**Superputere:** \t\t**Data:** \t', 10)
    p = para(ic, '', before=10, after=0)
    p.paragraph_format.tab_stops.add_tab_stop(Cm(14.8), WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.LINES)
    runs(p, '**Facilitator:** \t', 10)


cut_grid(d, 2, 1, CONTENT_W, 10.9, diploma)

D.save(OUT)
print('OK', OUT)
