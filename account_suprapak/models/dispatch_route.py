# -*- coding: utf-8 -*-
from odoo import api, fields, models

class DispatchRoute(models.Model):
    _name = 'dispatch.route'
    _description = 'Dispatch routes'

    name = fields.Char(string='Name')
    code = fields.Char(string='code')
