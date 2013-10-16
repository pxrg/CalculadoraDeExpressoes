#!usr/bin/env python
#-*-coding:utf-8-*-

from distutils.core import setup
import py2exe
import glob
import sys
 
sys.path.append('src') # o código fonte ta aqui 
 
includes = ['encodings', 'encodings.utf-8',]
opts = {
    'py2exe': {
        'includes': 'pango,atk,gobject,cairo,pangocairo,gtk.keysyms,encodings,encodings.*',
        'dll_excludes': [
            'iconv.dll','intl.dll','libatk-1.0-0.dll',
            'libgdk_pixbuf-2.0-0.dll','libgdk-win32-2.0-0.dll',
            'libglib-2.0-0.dll','libgmodule-2.0-0.dll',
            'libgobject-2.0-0.dll','libgthread-2.0-0.dll',
            'libgtk-win32-2.0-0.dll','libpango-1.0-0.dll',
            'libpangowin32-1.0-0.dll','libcairo-2.dll',
            'libpangocairo-1.0-0.dll','libpangoft2-1.0-0.dll',
        ],
    }
}
 
setup(
    name = 'Calculadora',
    version = '1.0',
    description = 'Calculadora de Expressoes que faz a analise lexica e sintatica',
    #author = 'Vc',
    #url = '',
    #download_url = '',
    #license = 'GPL',
 
    windows = [{'script': 'src/calculadora_form.py', #aqui fica o script principal
                'icon_resources': [(1, 'src/forms/calc.ico')]}], #aqui fica o icone do programa
    options=opts,
 
    data_files=[('data', glob.glob('src/*.*')),
                ('data/forms', glob.glob('src/forms/*.*')), # pastas e arquivos que acompanham o programa
                
    ],
)
##
##setup(
##    name = "CalculadoraExpressoes"
##    description = "Calculadora de Expressoes que faz a analise lexica e sintatica",
##    version = "1.0",
##    windows = [
##        {"script":"calculadora_form.py",
##         "icon_resources":[(1,"form/calc.ico")],
##    options = opts,
##    data_files = [('form', glob.glob('form/*.*')),
##                  ('', glob.glob('*.*')),
##    ],
##)
