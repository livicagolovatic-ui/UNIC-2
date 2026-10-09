# -*- coding: utf-8 -*-
"""Blocuri reutilizabile pentru documentele justificative ale Facilitatorului comunitar 2 (proiectul UNIC):
fișa activității, raportul de desfășurare, lista de prezență, elementele de proiectare.

Toate funcțiile primesc un `UnicDoc` (din lib_unic) și scriu în el. Datele proiectului sunt
centralizate mai jos; actualizează-le aici dacă se schimbă (ex.: alt manager de proiect).
"""
from lib_unic import *

PROIECT = 'UNIC – Uniți pentru Nevoile Incluzive și Continuitatea Educației Elevilor'
COD = 'cod MySMIS 352704  •  Programul Educație și Ocupare (PEO) 2021–2027'
BENEFICIAR = 'Asociația Grupul de Acțiune Locală Napoca Porolissum'
POZITIE = 'Facilitator comunitar 2'
NUME = 'GOLOVATIC LIVIA'
COR = '341204 – Facilitator de dezvoltare comunitară'
SUBACT = 'SA5.3 – Dezvoltarea de programe de informare și conștientizare'


def etape_fisa_post(activitate='activitate', durata='60 de minute', materiale='materialele de lucru',
                    feedback='fișa de feedback', public='elevilor'):
    """Etapele de lucru standard, formulate după atribuțiile din fișa postului (pct. 3).
    Returnează (etapa, ce s-a făcut concret, atribuția din fișa postului). Adaptează textele la activitate."""
    return [
        ('Planificare',
         'Planificarea %s și a calendarului intervenției împreună cu managerul de proiect și echipa de implementare; '
         'stabilirea cu unitatea de învățământ / partenerii a datei, a spațiului și a participanților.' % activitate,
         'Planifică activitățile comunitare și calendarul intervențiilor.'),
        ('Informare și mobilizare',
         'Informarea %s (și, după caz, a părinților și a dirigintelui) într-un limbaj accesibil; mobilizarea pentru participare; '
         'verificarea acordurilor necesare pentru minori, inclusiv pentru fotografii.' % public,
         'Informează și mobilizează elevii și părinții.'),
        ('Documente și materiale de lucru',
         'Elaborarea agendei, a %s, a listei de prezență și a instrumentelor de feedback (%s).' % (materiale, feedback),
         'Pregătește agende, liste de prezență, materiale de lucru, fișe de feedback.'),
        ('Suport logistic',
         'Multiplicarea materialelor, pregătirea consumabilelor, amenajarea spațiului; verificarea condițiilor de '
         'participare și siguranță aplicabile minorilor.',
         'Asigură suportul logistic; verifică condițiile de siguranță pentru minori.'),
        ('Desfășurarea activității',
         'Facilitarea participării %s la %s (%s); gestionarea listei de prezență; monitorizarea participării și a implicării.'
         % (public, activitate, durata),
         'Facilitează participarea; monitorizează implicarea beneficiarilor.'),
        ('Monitorizare și raportare',
         'Centralizarea prezenței, a absențelor, a dificultăților și a feedbackului; informarea echipei; raportul de desfășurare; '
         'transmiterea fotografiilor și a sintezei către Expertul comunicare (după verificarea acordurilor); arhivarea documentelor.',
         'Centralizează; transmite foto și sinteze Expertului comunicare; raportează; arhivează.'),
    ]


def _kv_table(D, rows, w_label=5.0):
    """rows: (etichetă, valoare). Valoarea '' = rând gol de completat; listă = câmpuri pe același rând."""
    t = table(D.d, len(rows), 2, [w_label, CONTENT_W - w_label], borders=('single', 4, C['lav2']),
              inside=('single', 4, C['lav2']), lr=0.2, tb=0.07)
    for i, (k, v) in enumerate(rows):
        row_setup(t.rows[i], 0.75)
        kc, vc = t.cell(i, 0), t.cell(i, 1)
        shade(kc, C['lav'])
        kc.vertical_alignment = vc.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
        para(kc, k, 9.5, True, color=C['purple'], after=0)
        if isinstance(v, list):
            field(vc, v, 9.5, before=3, bold_labels=False)
        elif v:
            para(vc, v, 9.5, after=0)
        else:
            lines(vc, 1, CONTENT_W - w_label - 0.5, 9.5, before=3)
    spacer(D.d, 6)
    return t


def sec(D, text):
    para(D.d, text, 11, True, color=C['purple'], before=8, after=4, keep=True)


def signatures(D, cols):
    """cols: listă de (titlu, rol). Prima coloană este a facilitatorului (numele e precompletat)."""
    w = CONTENT_W / len(cols)
    t = table(D.d, 1, len(cols), [w] * len(cols), borders=('single', 4, C['lav2']), inside=('single', 4, C['lav2']),
              lr=0.2, tb=0.12)
    row_setup(t.rows[0], 3.3)
    for j, (title, role) in enumerate(cols):
        c = t.cell(0, j)
        para(c, title, 10, True, color=C['purple'], align='center', after=0)
        para(c, role, 9, italic=True, color=C['grey'], align='center', after=2)
        if role.startswith(POZITIE):
            para(c, 'Nume: ' + NUME, 9.5, before=6, after=0)
        else:
            field(c, [('Nume:', w - 0.5)], 9.5, before=6)
        field(c, [('Semnătura:', w - 0.5)], 9.5, before=10)
        field(c, [('Data:', w - 0.5)], 9.5, before=8)
    spacer(D.d, 4)


def fisa_activitate(D, tip_activitate, descriere, etape, livrabile, *, subactivitate=SUBACT,
                    grup_tinta='Elevi', durata='60 de minute (1 oră)', loc='', data='',
                    dovezi=None, sectiune_raport=None, confirmare='Unitatea de învățământ (ștampila)'):
    """Fișa activității – document justificativ pentru orele lucrate (de regulă pagina 1–2).
    loc/data goale = câmpuri de completat de mână (nu inventa date care nu au fost furnizate)."""
    t = table(D.d, 1, 1, [CONTENT_W], borders=('single', 12, C['purple']), lr=0.3, tb=0.15)
    c = t.cell(0, 0)
    para(c, 'FIȘA ACTIVITĂȚII – DOCUMENT JUSTIFICATIV', 14, True, color=C['purple'], align='center', after=0)
    para(c, 'privind activitatea desfășurată de expertul „%s” în cadrul proiectului UNIC' % POZITIE, 10,
         italic=True, align='center', after=0)
    spacer(D.d, 6)

    sec(D, 'A. Date de identificare')
    _kv_table(D, [
        ('Proiectul', PROIECT),
        ('Cod / program', COD),
        ('Subactivitatea din proiect', subactivitate),
        ('Poziția în proiect', POZITIE),
        ('Numele și prenumele expertului', NUME),
        ('Codul ocupației (COR)', COR),
        ('Tipul activității', tip_activitate),
        ('Locația / localitatea', loc),
        ('Data desfășurării', [(data + ' ' if data else '', 4.6), ('Interval orar:', 11.5)]),
        ('Grupul țintă', grup_tinta),
        ('Clasa / grupa', [('', 4.6), ('Nr. participanți:', 11.5)]),
        ('Durata sesiunii cu grupul țintă', durata),
    ])

    sec(D, 'B. Descrierea pe scurt a activității')
    for x in descriere:
        para(D.d, x, 10, align='justify', after=4)

    sec(D, 'C. Repartizarea timpului de lucru al expertului, corelată cu atribuțiile din fișa postului')
    rows = [[str(i + 1), e, desc, '//' + atr + '//', '', ''] for i, (e, desc, atr) in enumerate(etape)]
    rows.append(['', 'TOTAL ORE', '', '', '', ''])
    tb_ = D.simple_table(['Nr.', 'Etapa', 'Activități realizate concret', 'Atribuția din fișa postului (pct. 3)', 'Data', 'Nr. ore'],
                         rows, [0.8, 2.5, 7.9, 3.4, 1.3, 1.1], size=8.5, zebra=False)
    for c in tb_.rows[-1].cells:
        shade(c, C['lyellow'])
    para(D.d, 'Datele și numărul de ore se completează în concordanță cu fișa de pontaj (timesheet-ul) lunar și cu atribuțiile '
              'din fișa postului.', 8.5, italic=True, color=C['grey'], after=4)

    sec(D, 'D. Rezultate și livrabile')
    for x in livrabile:
        bullet(D.d, x, 10)

    sec(D, 'E. Documente doveditoare anexate')
    rap = 'Raportul privind desfășurarea activității' + (' (secțiunea %d)' % sectiune_raport if sectiune_raport else '')
    checkbox_grid(D.d, dovezi or ['Agenda activității', 'Lista de prezență semnată de participanți',
                                  'Materialele de lucru și fișele de feedback', 'Produse ale activității (fișe completate)',
                                  'Fotografii (cu acordurile verificate, conform GDPR)',
                                  'Dovada transmiterii foto / sintezei către Expertul comunicare', rap,
                                  'Alte documente: ______________________'], 2, CONTENT_W, 9.5)
    spacer(D.d, 4)
    signatures(D, [('Întocmit', POZITIE), ('Confirmat', confirmare), ('Avizat', 'Manager de proiect')])
    page_break(D.d)


def metode(D, rows):
    """Tabel „Elemente de proiectare”: rows = [[element, descriere sau listă de '- bullet'], ...]."""
    D.simple_table(['Element', 'Descriere'], rows, [4.2, 12.8], size=9.5, bold_first=True)


def raport(D, titlu, obiective, produse_hint=None, participanti='elevi', page_before=True):
    """Raportul privind desfășurarea activității – se completează de mână după activitate (o pagină)."""
    if page_before:
        page_break(D.d)
    D.h(titlu)
    para(D.d, 'Se completează de facilitator imediat după desfășurarea activității și se anexează la documentele justificative.',
         9.5, italic=True, color=C['grey'], after=4)
    _kv_table(D, [
        ('Data și intervalul orar efectiv', [('', 4.6), ('ora:', 11.5)]),
        ('Locația / clasa / grupul', ''),
        ('Număr %s participanți' % participanti, [('total:', 3.5), ('din care fete / femei:', 8.0), ('băieți / bărbați:', 11.5)]),
    ])
    sec(D, 'Gradul de realizare a obiectivelor')
    rows = [[o, '☐', '☐', '☐', ''] for o in obiective]
    t = D.simple_table(['Obiectiv', 'Realizat', 'Parțial', 'Nerealizat', 'Observații'], rows,
                       [7.4, 1.6, 1.6, 1.9, 4.5], size=9, zebra=False)
    for r in t.rows[1:]:
        row_setup(r, 0.7)
        for c in r.cells[1:4]:
            c.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    sec(D, 'Desfășurarea activității')
    checkbox_grid(D.d, ['conform agendei / scenariului', 'cu adaptări (descrise mai jos)'], 2, CONTENT_W, 10)
    lines(D.d, 1, CONTENT_W, 10, before=8)
    sec(D, 'Verificări și transmiteri (conform fișei postului)')
    checkbox_grid(D.d, ['acordurile pentru minori (inclusiv foto) au fost verificate',
                        'condițiile de participare și siguranță au fost verificate',
                        'foto și sinteza au fost transmise Expertului comunicare',
                        'documentele au fost arhivate fizic și electronic'], 2, CONTENT_W, 9.5)
    for q, n, hint in [('Participare; absențe și dificultăți semnalate echipei', 2, None),
                       ('Rezultate obținute / produse ale activității', 1, produse_hint),
                       ('Dificultăți întâmpinate și modul de rezolvare', 1, None),
                       ('Concluzii și recomandări', 1, None)]:
        para(D.d, q, 10, True, before=5, after=0, keep=True)
        if hint:
            para(D.d, hint, 8.5, italic=True, color=C['grey'], after=0, keep=True)
        lines(D.d, n, CONTENT_W, 10, before=8)
    spacer(D.d, 6)
    t = table(D.d, 1, 2, [8.5, 8.5], lr=0.2, tb=0.1)
    row_setup(t.rows[0])
    field(t.cell(0, 0), [('Data:', 7.5)], 10, before=6)
    para(t.cell(0, 1), POZITIE, 10, True, align='center', after=0)
    para(t.cell(0, 1), 'Nume: ' + NUME, 10, before=8, after=0)
    field(t.cell(0, 1), [('Semnătura:', 8.0)], 10, before=12)


def lista_prezenta(D, titlu_activitate, coloane=None, randuri=20, subactivitate=SUBACT, page_before=True):
    """Listă de prezență goală (numele NU se precompletează din surse nesigure; se semnează pe loc).
    coloane: [(antet, lățime_cm), ...] – implicit pentru elevi. Pentru părinți folosește ex.:
    [('Nr.',1),('Numele și prenumele',5.5),('Părinte / tutore al elevului',4.5),('Telefon (opțional)',2.5),('Semnătura',3.5)]."""
    if page_before:
        page_break(D.d)
    coloane = coloane or [('Nr.', 1.0), ('Numele și prenumele', 6.0), ('Clasa', 2.0), ('Semnătura', 4.5), ('Observații', 3.5)]
    para(D.d, 'LISTĂ DE PREZENȚĂ', 15, True, color=C['purple'], align='center', after=2)
    para(D.d, titlu_activitate, 11, True, align='center', after=2)
    para(D.d, '%s  •  %s' % (PROIECT, subactivitate), 9, italic=True, color=C['grey'], align='center', after=6)
    _kv_table(D, [('Locația', ''), ('Data / interval orar', [('', 4.6), ('ora:', 11.5)]),
                  ('Expert responsabil', '%s – %s' % (POZITIE, NUME))])
    t = D.simple_table([h for h, _ in coloane], [[str(i + 1)] + [''] * (len(coloane) - 1) for i in range(randuri)],
                       [w for _, w in coloane], size=9.5, zebra=False)
    for r in t.rows[1:]:
        row_setup(r, 0.75)
    para(D.d, 'Prin semnare, participanții (sau părinții / tutorii, pentru minori, conform acordurilor existente) confirmă prezența. '
              'Datele cu caracter personal sunt prelucrate exclusiv în scopul proiectului, conform GDPR.',
         8, italic=True, color=C['grey'], before=4, after=6)
    t = table(D.d, 1, 2, [8.5, 8.5], lr=0.2, tb=0.1)
    para(t.cell(0, 0), 'Întocmit, ' + POZITIE, 10, True, after=0)
    para(t.cell(0, 0), NUME, 10, after=0)
    field(t.cell(0, 0), [('Semnătura:', 7.5)], 10, before=10)
    para(t.cell(0, 1), 'Confirmat, reprezentant unitate / partener', 10, True, after=0)
    field(t.cell(0, 1), [('Nume:', 8.0)], 10, before=6)
    field(t.cell(0, 1), [('Semnătura / ștampila:', 8.0)], 10, before=10)


# ---------------------------------------------------------------- Anexa 10 – raport lunar oficial
PROGRAM_PEO = ('FSE+ / Programul Educație și Ocupare (PEO) 2021-2027, P8, ESO4.6 – apel PEO/648/PEO_P8/OP4/ESO4.6/PEO_A68_C '
               '„O șansă în plus prin învățământul profesional și tehnic – regiuni mai puțin dezvoltate” (acțiuni 8.f.1, 8.f.2, 8.f.3)')
BENEFICIAR_MAJ = 'ASOCIAȚIA GRUPUL DE ACȚIUNE LOCALĂ NAPOCA POROLISSUM'
CONTRACT = 'contract individual de muncă nr. 380/31.08.2026, valabil până la 01.06.2029'
CATEGORIE = 'Experiență < 5 ani'


def raport_anexa10(D, luna_an, randuri, detaliere, probleme=None, ore_total=None):
    """Raportul lunar de activitate în formatul oficial Anexa 10 (Manualul Beneficiarului PEO/PIDS).
    luna_an: ex. 'octombrie 2026'.
    randuri: listă de dict cu cheile activitate, responsabilitati (listă de '- …'), prestata (listă), rezultate (listă),
             comun ('Da'/'Nu'), ore (text; '' = de completat conform pontajului).
    detaliere: listă de paragrafe (persoana I, cronologic). probleme: text sau None (→ „nu au fost întâmpinate…”).
    Nu inventa ore sau participanți: lasă '' acolo unde datele nu sunt cunoscute."""
    para(D.d, 'ANEXA 10 – Raport de activitate', 9, italic=True, color=C['grey'], align='right', after=2)
    para(D.d, 'Raport de Activitate', 16, True, color=C['purple'], align='center', after=0)
    para(D.d, luna_an, 12, True, align='center', after=6)
    _kv_table(D, [('Program', PROGRAM_PEO), ('Codul proiectului', '352704'),
                  ('Titlul proiectului', 'UNIC – „Uniți pentru Nevoile Incluzive și Continuitatea Educației Elevilor”'),
                  ('Beneficiar', BENEFICIAR_MAJ), ('Numele expertului', NUME), ('Poziția în cadrul proiectului', POZITIE),
                  ('Nr. și tipul contractului', CONTRACT), ('Categorie expert', CATEGORIE)], w_label=4.6)
    sec(D, '1. Prezentare succintă a activității prestate în perioada de raportare')
    rows = []
    for i, r in enumerate(randuri, start=1):
        rows.append([str(i) + '.', r['activitate'], r['responsabilitati'], r['prestata'], r['rezultate'],
                     r.get('comun', 'Nu'), r.get('ore', '')])
    if ore_total is not None:
        rows.append(['', 'TOTAL', '', '', '', '', ore_total])
    t = D.simple_table(['Nr. crt.', 'Nr. / titlul activității conform cererii de finanțare',
                        'Responsabilități și sarcini conform contractului / fișei postului', 'Activitate prestată',
                        'Rezultate obținute / documente justificative / livrabile',
                        'Livrabil comun cu alți experți (Da/Nu)', 'Nr. ore lucrate'],
                       rows, [1.0, 2.4, 4.0, 3.6, 3.6, 1.3, 1.1], size=8, zebra=False)
    for r in t.rows[1:]:
        for c in r.cells[5:]:
            c.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    sec(D, '2. Detalierea activităților realizate și a rezultatelor obținute')
    for x in detaliere:
        para(D.d, x, 10, align='justify', after=5)
    sec(D, '3. Întârzieri / probleme întâmpinate în realizarea sarcinilor specifice')
    para(D.d, probleme or 'Nu au fost întâmpinate întârzieri sau probleme de natură să afecteze realizarea sarcinilor '
                          'planificate pentru luna de raportare.', 10, align='justify', after=10)
    t = table(D.d, 1, 2, [8.5, 8.5], lr=0.2, tb=0.1)
    row_setup(t.rows[0])
    para(t.cell(0, 0), 'Numele expertului: ' + NUME, 10, True, after=0)
    field(t.cell(0, 0), [('Data:', 7.5)], 10, before=10)
    field(t.cell(0, 1), [('Semnătură:', 8.0)], 10, before=6)


def minuta_activitate(D, titlu, data='', interval='', loc='', participanti='', subactivitate=SUBACT,
                      desfasurare=None, rezultate=None, observatii=None):
    """Minută de activitate pentru o activitate de teren (document justificativ folosit lunar de FC2).
    Câmpurile goale devin linii de completat. desfasurare/rezultate/observatii: liste de paragrafe sau '- bullet'."""
    para(D.d, 'MINUTĂ DE ACTIVITATE', 15, True, color=C['purple'], align='center', after=0)
    para(D.d, titlu, 11, True, align='center', after=6)
    _kv_table(D, [('Proiect / subactivitate', '%s – cod SMIS 352704 • %s' % (PROIECT, subactivitate)),
                  ('Data', data), ('Interval orar', interval), ('Locația', loc),
                  ('Participanți', participanti), ('Expert responsabil', '%s – %s' % (POZITIE, NUME))])
    for title, items, n in (('Desfășurarea activității', desfasurare, 6), ('Rezultate', rezultate, 3),
                            ('Observații și direcții pentru activitățile următoare', observatii, 3)):
        sec(D, title)
        if items:
            for x in items:
                (bullet(D.d, x[2:], 10) if x.startswith('- ') else para(D.d, x, 10, align='justify', after=4))
        else:
            lines(D.d, n, CONTENT_W, 10, before=10)
    sec(D, 'Documente anexate')
    checkbox_grid(D.d, ['listă de prezență', 'documentare foto (cu acorduri verificate)', 'instrumente completate de participanți',
                        'materiale de lucru', 'alte documente: ____________'], 3, CONTENT_W, 9.5)
    spacer(D.d, 8)
    t = table(D.d, 1, 2, [8.5, 8.5], lr=0.2, tb=0.1)
    para(t.cell(0, 0), 'Întocmit, ' + POZITIE, 10, True, after=0)
    para(t.cell(0, 0), NUME, 10, after=0)
    field(t.cell(0, 0), [('Semnătura:', 7.5)], 10, before=10)
    field(t.cell(0, 1), [('Data:', 8.0)], 10, before=6)
