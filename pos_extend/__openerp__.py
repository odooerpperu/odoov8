# -*- encoding: utf-8 -*-
 
{
    'name' : 'Mount to Text',
    'version': '1.0',
    'summary': 'Monto a texto',
    'category': 'Tools',
    'description':
        """
Odoo Modulo Web - Monto a texto
====================================
 
Convierte el monto a texto en el POS
        """,
    'data': [ ],
    'depends' : ['base','base_translate_tools','point_of_sale',],
    'js': [
        'static/src/js/main.js',
        'static/src/js/amount_text.js',
    ],
    'qweb': ['static/src/xml/*.xml'],
    'application': True,
}