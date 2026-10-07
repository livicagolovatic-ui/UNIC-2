# -*- coding: utf-8 -*-
"""Regenerează tot pachetul de comunicare: logo, fișa de identitate, flyere, afișe, postări, texte și documentul Word."""
import runpy, pathlib
HERE = pathlib.Path(__file__).resolve().parent
for m in ['logo', 'fisa_identitate', 'flyere', 'afise', 'social', 'postari_texte', 'postari_retele', 'build_pachet_docx', 'placa', 'build_placa_docx']:
    print('->', m)
    runpy.run_path(str(HERE / f'{m}.py'), run_name='__main__')
