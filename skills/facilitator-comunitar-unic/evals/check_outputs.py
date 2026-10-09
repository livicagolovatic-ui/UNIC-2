# -*- coding: utf-8 -*-
"""Verificări automate pentru rulările de test ale skill-ului facilitator-comunitar-unic.
Utilizare: python3 check_outputs.py <director outputs> <eval_name>  → JSON cu rezultate pe aserțiuni."""
import sys, os, re, json, glob, zipfile

out_dir, ev = sys.argv[1], sys.argv[2]


def docx_text(path):
    z = zipfile.ZipFile(path)
    txt = []
    for n in z.namelist():
        if re.match(r'word/(document|header\d*|footer\d*)\.xml$', n):
            x = z.read(n).decode('utf8')
            x = re.sub(r'</w:p>', '\n', x)
            txt.append(re.sub(r'<[^>]+>', '', x))
    return '\n'.join(txt)


def has_header_logo(path):
    z = zipfile.ZipFile(path)
    hdrs = [n for n in z.namelist() if re.match(r'word/header\d*\.xml$', n)]
    imgs = [n for n in z.namelist() if n.startswith('word/media/')]
    big = [n for n in imgs if z.getinfo(n).file_size > 50000]
    return any('<w:drawing' in z.read(h).decode('utf8') or '<v:imagedata' in z.read(h).decode('utf8') for h in hdrs) and bool(big)


def is_a4(path):
    x = zipfile.ZipFile(path).read('word/document.xml').decode('utf8')
    sizes = re.findall(r'<w:pgSz[^>]*w:w="(\d+)"', x)
    return bool(sizes) and all(abs(int(w) - 11906) < 60 for w in sizes)

docs = [p for p in glob.glob(os.path.join(out_dir, '*.docx'))]
xlsx = [p for p in glob.glob(os.path.join(out_dir, '*.xlsx'))]
reply = open(os.path.join(out_dir, 'REPLY.md')).read() if os.path.exists(os.path.join(out_dir, 'REPLY.md')) else ''
alltext = '\n'.join(docx_text(p) for p in docs)
if xlsx:
    import openpyxl
    for p in xlsx:
        wb = openpyxl.load_workbook(p)
        for ws in wb:
            for row in ws.iter_rows(values_only=True):
                alltext += '\n' + ' | '.join(str(v) for v in row if v is not None)
low = alltext.lower()
res = []


def a(text, passed, evidence):
    res.append({'text': text, 'passed': bool(passed), 'evidence': evidence})


a('Există cel puțin un livrabil .docx', len(docs) >= 1, '%d docx: %s' % (len(docs), [os.path.basename(d) for d in docs]))
logo = [os.path.basename(d) for d in docs if has_header_logo(d)]
a('Antetul UNIC (imagine în header) apare în toate documentele Word', docs and len(logo) == len(docs),
  'cu antet: %s din %d' % (logo, len(docs)))
ced = [c for c in 'şţŞŢ' if c in alltext + reply]
a('Diacritice corecte (fără ş/ţ cu sedilă)', not ced, 'caractere cu sedilă găsite: %s' % ced if ced else 'niciun caracter cu sedilă')
a4 = [os.path.basename(d) for d in docs if is_a4(d)]
a('Format de pagină A4 (standard în România) pentru toate documentele', docs and len(a4) == len(docs), 'A4: %d din %d' % (len(a4), len(docs)))
a('Numele expertului (Golovatic Livia) este completat', 'golovatic' in low, 'apare: %s' % ('golovatic' in low))
a('Răspunsul către utilizator (REPLY.md) există', bool(reply.strip()), '%d caractere' % len(reply))

if ev == 'sesiune-turda-orientare':
    a('Documentul menționează SA5.3 și Facilitator comunitar 2', 'sa5.3' in low and 'facilitator comunitar 2' in low,
      'SA5.3: %s; FC2: %s' % ('sa5.3' in low, 'facilitator comunitar 2' in low))
    a('Orele sunt corelate cu fișa postului', 'fișa postului' in low or 'fisa postului' in low, 'apare „fișa postului”: %s' % ('fișa postului' in low))
    a('Include listă de prezență', 'listă de prezență' in low or 'lista de prezență' in low, '')
    n_fise = len(set(re.findall(r'fișa\s+(\d+)', low)))
    a('Include cel puțin 2 fișe de lucru numerotate pentru elevi', n_fise >= 2, '%d fișe numerotate distincte' % n_fise)
    a('Data și locația sesiunii apar corect (12.10.2026, Poiana)', ('12.10.2026' in alltext or '12 octombrie 2026' in low) and 'poiana' in low, '')
elif ev == 'raport-lunar-octombrie':
    dates = ['02.10', '09.10', '12.10', '29.10']
    found = {d: alltext.count(d) for d in dates}
    a('Raportul include toate zilele cu sesiuni FC2 (02.10, 09.10, 12.10, 29.10)', all(found[d] for d in dates), str(found))
    hued = alltext.count('10:15') + alltext.count('11:55')
    a('Ambele sesiuni din 09.10 (10:15 și 11:55) apar', '10:15' in alltext and '11:55' in alltext, '10:15: %s, 11:55: %s' % ('10:15' in alltext, '11:55' in alltext))
    others = [d for d in ['14.10', '16.10', '19.10', '13.10'] if d in alltext]
    a('Nu atribuie FC2 sesiunile altor experți (14.10, 16.10, 19.10, 13.10 ca activități proprii)', not others or
      ('expert comunicare' in low), 'date ale altor experți găsite: %s' % others)
    flags = [k for k in ['40 de minute', '40 min', 'suprapun', 'dubl', 'expertul comunicare', 'expert comunicare', 'gt declarat', 'versiune nouă', 'versiunea 3']
             if k in (low + reply.lower())]
    a('Semnalează cel puțin o neconcordanță din Anexa 12', bool(flags), 'indicii: %s' % flags)
    a('Corelare cu pontajul / atribuțiile', 'pontaj' in low and ('atribu' in low), '')
elif ev == 'atelier-parinti-huedin':
    a('Include invitație pentru părinți', 'invita' in low, '')
    m = re.search(r'(whatsapp[\s\S]{0,40}?)\n', low)
    a('Include varianta pentru WhatsApp', 'whatsapp' in (low + reply.lower()), '')
    a('Include agenda', 'agend' in low, '')
    a('Include listă de prezență cu coloană pentru părinte / elev', ('prezență' in low) and ('părinte' in low or 'tutore' in low), '')
    a('Include fișă de feedback', 'feedback' in low, '')
    a('Data și ora corecte (05.11.2026 / 5 noiembrie, 17:00–18:30)', ('05.11.2026' in alltext or '5 noiembrie' in low) and '17:00' in alltext and '18:30' in alltext, '')

print(json.dumps({'expectations': res, 'summary': {'passed': sum(r['passed'] for r in res), 'failed': sum(not r['passed'] for r in res),
                  'total': len(res), 'pass_rate': round(sum(r['passed'] for r in res) / len(res), 2)}}, ensure_ascii=False, indent=1))
