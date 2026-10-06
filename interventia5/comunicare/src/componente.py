# -*- coding: utf-8 -*-
"""Componente comune ale machetelor: QR, insigne, subsol cu mențiunile obligatorii, CSS de bază."""
import io, re
import qrcode, qrcode.image.svg
from common import *
from logo import lockup_orizontal, lockup_vertical, simbol_svg
from ilustratii import peisaj, icon, ICON_LABEL

TAGLINE = 'Plantăm idei. Creștem comunități.'
LANSARE = 'Apelul se lansează la începutul anului 2027'


def qr(url='https://www.napocaporolissum.ro', color=MARO):
    img = qrcode.make(url, image_factory=qrcode.image.svg.SvgPathImage, box_size=10, border=1)
    buf = io.BytesIO(); img.save(buf)
    svg = buf.getvalue().decode()
    svg = re.sub(r'<\?xml[^>]*\?>', '', svg)
    svg = svg.replace('#000000', color).replace('<path d=', f'<path fill="{color}" d=', 1)
    svg = re.sub(r'width="[^"]+" height="[^"]+"', 'width="100%" height="100%"', svg, count=1)
    return svg


BASE_CSS = f"""
.svgfill svg {{ display:block; width:100%; height:100%; }}
.logo-h svg, .logo-v svg {{ display:block; width:100%; height:auto; }}
.ico svg {{ display:block; width:100%; height:100%; }}
.hand {{ font-family:'Caveat', cursive; font-weight:700; }}
.verde {{ color:{VERDE_TEXT}; }}
.maro {{ color:{MARO}; }}
b, strong {{ font-weight:700; }}
"""


def subsol_obligatoriu(font='6.2pt', culoare='#FFFFFF', fundal=VERDE_INCHIS, pad='2.6mm 9mm 3mm', gratuit=True):
    g = ' Material distribuit gratuit.' if gratuit else ''
    return (f'<div style="background:{fundal};color:{culoare};font-size:{font};line-height:1.35;padding:{pad}">'
            f'{MENTIUNI}<br><span style="opacity:.92">{DATE_PROIECT}{g}</span></div>')
