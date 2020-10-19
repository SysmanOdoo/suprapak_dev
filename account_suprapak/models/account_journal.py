# -*- coding: utf-8 -*-
from odoo import models, api, fields
from odoo.exceptions import AccessDenied


class AccountJournal(models.Model):
    _inherit = 'account.journal'

    description_pa = fields.Text(string='Description Autonomous Heritage', help='Text to be displayed in the electronic invoice format in the additional observations')