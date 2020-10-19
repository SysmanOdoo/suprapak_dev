from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    bool_parent = fields.Boolean('Parent', default=False)
    sale_journal_id = fields.Many2one('account.journal', string="Sales invoice journal")
