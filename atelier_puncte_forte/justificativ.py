# -*- coding: utf-8 -*-
"""Secțiunile care transformă scenariul în document justificativ pentru activitatea
expertului „Facilitator comunitar 2” (fișa activității + raportul de desfășurare)."""
from lib_unic import *

PROIECT = 'UNIC – Uniți pentru Nevoile Incluzive și Continuitatea Educației Elevilor'
COD = 'cod MySMIS 352704  •  Programul Educație și Ocupare (PEO) 2021–2027'
POZITIE = 'Facilitator comunitar 2'


def _kv_table(D, rows, w_label=5.0):
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


def _sec(D, text):
    para(D.d, text, 11, True, color=C['purple'], before=8, after=4, keep=True)


def signatures(D, cols):
    """cols: listă de (titlu, rol)."""
    w = CONTENT_W / len(cols)
    t = table(D.d, 1, len(cols), [w] * len(cols), borders=('single', 4, C['lav2']), inside=('single', 4, C['lav2']),
              lr=0.2, tb=0.12)
    row_setup(t.rows[0], 4.2)
    for j, (title, role) in enumerate(cols):
        c = t.cell(0, j)
        para(c, title, 10, True, color=C['purple'], align='center', after=0)
        para(c, role, 9, italic=True, color=C['grey'], align='center', after=4)
        field(c, [('Nume:', w - 0.5)], 9.5, before=8)
        field(c, [('Semnătura:', w - 0.5)], 9.5, before=14)
        field(c, [('Data:', w - 0.5)], 9.5, before=10)
    spacer(D.d, 4)


def fisa_activitate(D, sedinta, titlu, descriere, etape, livrabile):
    """Pagina 1: fișa activității (document justificativ pentru orele lucrate)."""
    t = table(D.d, 1, 1, [CONTENT_W], borders=('single', 12, C['purple']), lr=0.3, tb=0.15)
    c = t.cell(0, 0)
    para(c, 'FIȘA ACTIVITĂȚII – DOCUMENT JUSTIFICATIV', 14, True, color=C['purple'], align='center', after=0)
    para(c, 'privind activitatea desfășurată de expertul „%s” în cadrul proiectului UNIC' % POZITIE, 10,
         italic=True, align='center', after=0)
    spacer(D.d, 6)

    _sec(D, 'A. Date de identificare')
    _kv_table(D, [
        ('Proiectul', PROIECT),
        ('Cod / program', COD),
        ('Activitatea / subactivitatea din proiect', ''),
        ('Poziția în proiect', POZITIE),
        ('Numele și prenumele expertului', ''),
        ('Tipul activității', 'Atelier de dezvoltare personală „Eu, punctele mele forte și ce mă motivează” – '
                              'Ședința %d din 2: „%s”' % (sedinta, titlu)),
        ('Unitatea de învățământ / localitatea', ''),
        ('Data desfășurării', [('', 4.6), ('Interval orar:', 11.5)]),
        ('Grupul țintă', 'Elevi din clasele a VII-a – a VIII-a'),
        ('Clasa / grupa', [('', 4.6), ('Nr. participanți:', 11.5)]),
        ('Durata sesiunii cu grupul țintă', '60 de minute (1 oră)'),
    ])

    _sec(D, 'B. Descrierea pe scurt a activității')
    for x in descriere:
        para(D.d, x, 10, align='justify', after=4)

    _sec(D, 'C. Repartizarea timpului de lucru al expertului')
    rows = [[str(i + 1), e, desc, '', ''] for i, (e, desc) in enumerate(etape)]
    rows.append(['', 'TOTAL ORE', '', '', ''])
    tb_ = D.simple_table(['Nr.', 'Etapa', 'Activități realizate concret', 'Data', 'Nr. ore'], rows,
                         [0.9, 3.6, 8.8, 2.1, 1.6], size=9, zebra=False)
    last = tb_.rows[-1]
    for c in last.cells:
        shade(c, C['lyellow'])
    for c in last.cells[1:2]:
        for p in c.paragraphs:
            for r in p.runs:
                r.bold = True
    para(D.d, 'Datele și numărul de ore se completează în concordanță cu fișa de pontaj (timesheet-ul) lunar și cu atribuțiile '
              'din fișa postului.', 8.5, italic=True, color=C['grey'], after=4)

    _sec(D, 'D. Rezultate și livrabile')
    for x in livrabile:
        bullet(D.d, x, 10)

    _sec(D, 'E. Documente doveditoare anexate')
    checkbox_grid(D.d, ['Lista de prezență semnată de participanți',
                        'Fotografii din timpul activității (cu acordul părinților / GDPR)',
                        'Scenariul activității și materialele-suport (prezentul document)',
                        'Produse ale activității (fișe completate de elevi)',
                        'Raportul privind desfășurarea activității (secțiunea 12)',
                        'Alte documente: ______________________'], 2, CONTENT_W, 9.5)
    spacer(D.d, 8)
    signatures(D, [('Întocmit', 'Facilitator comunitar 2'),
                   ('Confirmat', 'Unitatea de învățământ (director / diriginte), ștampila'),
                   ('Avizat', 'Coordonator / manager de proiect')])
    page_break(D.d)


def metode(D, rows):
    D.simple_table(['Element', 'Descriere'], rows, [4.2, 12.8], size=9.5, bold_first=True)


def raport(D, nr, obiective, produse_hint):
    """Raportul privind desfășurarea activității – se completează după ședință."""
    page_break(D.d)
    D.h('%d. Raport privind desfășurarea activității' % nr)
    para(D.d, 'Se completează de facilitator imediat după desfășurarea ședinței și se anexează la documentele justificative.',
         9.5, italic=True, color=C['grey'], after=4)
    _kv_table(D, [
        ('Data și intervalul orar efectiv', [('', 4.6), ('ora:', 11.5)]),
        ('Unitatea de învățământ / clasa', ''),
        ('Număr elevi participanți', [('total:', 3.5), ('din care fete:', 7.5), ('băieți:', 11.5)]),
    ])
    _sec(D, 'Gradul de realizare a obiectivelor')
    rows = [[o, '☐', '☐', '☐', ''] for o in obiective]
    t = D.simple_table(['Obiectiv', 'Realizat', 'Parțial', 'Nerealizat', 'Observații'], rows,
                       [7.4, 1.6, 1.6, 1.9, 4.5], size=9, zebra=False)
    for r in t.rows[1:]:
        row_setup(r, 0.7)
        for c in r.cells[1:4]:
            c.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    _sec(D, 'Desfășurarea activității')
    checkbox_grid(D.d, ['conform scenariului', 'cu adaptări (descrise mai jos)'], 2, CONTENT_W, 10)
    lines(D.d, 1, CONTENT_W, 10, before=8)
    for q, n, hint in [('Implicarea și participarea elevilor', 2, None),
                       ('Rezultate obținute / produse ale activității', 2, produse_hint),
                       ('Dificultăți întâmpinate și modul de rezolvare', 2, None),
                       ('Concluzii și recomandări', 2, None)]:
        para(D.d, q, 10, True, before=5, after=0, keep=True)
        if hint:
            para(D.d, hint, 8.5, italic=True, color=C['grey'], after=0, keep=True)
        lines(D.d, n, CONTENT_W, 10, before=8)
    spacer(D.d, 6)
    t = table(D.d, 1, 2, [8.5, 8.5], lr=0.2, tb=0.1)
    row_setup(t.rows[0])
    field(t.cell(0, 0), [('Data:', 7.5)], 10, before=6)
    para(t.cell(0, 1), 'Facilitator comunitar 2', 10, True, align='center', after=0)
    field(t.cell(0, 1), [('Nume:', 8.0)], 10, before=8)
    field(t.cell(0, 1), [('Semnătura:', 8.0)], 10, before=12)
