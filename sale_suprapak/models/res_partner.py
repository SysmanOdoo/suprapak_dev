from odoo import fields,models,api

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    average_days = fields.Char('Average Days',related='country_id.average_days')