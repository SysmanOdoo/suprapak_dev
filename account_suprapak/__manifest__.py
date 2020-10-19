# -*- coding: utf-8 -*-
{
    'name': "Invoice LYS",

    'summary': "",

    'description': "This is a module for Suprapak",

    'author': "Todoo",
    'website': "http://www.todoo.co",
    'contributors': "Livingston Arias la@todoo,co",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Account',
    'version': '13.1',

    # any module necessary for this one to work correctly
    'depends': ['account','hr_expense','sale_management','account_accountant','account_asset', 'delivery', 'l10n_co_e_invoicing_comfiar'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/dispatch_route_data.xml',
        'views/res_partner.xml',
        'views/account_move_template.xml',
        'wizard/wizard_budget_view.xml',
        'views/view_expenses.xml',
        'views/account_asset_view.xml',
        'views/account_move_views.xml',
        'views/account_journal_views.xml',
        # 'views/autonomous_heritage_views.xml',
        "report/account_move_reports.xml",
    ],
    # only loaded in demonstration mode
    'images': [],
    'application': True,
}