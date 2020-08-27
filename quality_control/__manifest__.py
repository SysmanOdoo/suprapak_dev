# -*- coding: utf-8 -*-
{
    'name': "quality_control",

    'summary': """
        Modulo control de calidad Version 1
        """,

    'description': """
        control de calidad permite definir formatos de evaluacion por proceso de produccion
        definiendo variables para cada formato.
        Por cada pedido se podra hacer analisis de calidad el cual esta conformado por
        inspecciones de calidad conteniendo diferentes formatos de evaluacion
    """,

    'author': "Odoo Community Association (OCA)",
    'website': "http://www.yourcompany.com",
    'contributors': "Guido Orejuela guido.orejuela94@gmail.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Quality control',
    'version': '13.1',

    # any module necessary for this one to work correctly
    'depends': ['mrp'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #],
}
