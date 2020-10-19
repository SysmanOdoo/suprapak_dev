# -*- coding: utf-8 -*-
{
    'name': "Product Suprapak",

    'summary': "",

    'description': "This is a module for Suprapak",

    'author': "Todoo",
    'website': "http://www.todoo.co",
    'contributors': "Fernando Fernández ng@todoo,co",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Product',
    'version': '13.1',

    # any module necessary for this one to work correctly
    'depends': ['stock','product'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/product_categ_data.xml',
        'views/categ.xml',
        'views/product_template_view.xml',
        'views/subproduct_menu.xml'
    ],
    # only loaded in demonstration mode
    'images': [],
    'application': True,
}