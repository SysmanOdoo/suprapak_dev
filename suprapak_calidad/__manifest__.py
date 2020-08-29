# -*- coding: utf-8 -*-
{
    'name': "suprapak_calidad",

    'summary': """
        Control de Calidad del producto en su fabricacion
        subtitle on modules listing or apps.openerp.com
    """,

    'description': """
        Permite crear Formatos (patrones de calidad) por cada proceso, cada uno con sus caracteristicas
        a evaluar.
        Al final puede generar el certificado de calidad en formato pdf.
    """,

    'author': "Odoo Community Association (OCA)",
    'website': "http://www.yourcompany.com",
    'contributors': "Guido Orejuela",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Calidad',
    'version': '13.1',

    # any module necessary for this one to work correctly
    'depends': ['kronos'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'views/views.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    #    'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,

}
