from odoo import models, fields, api, _
from num2words import num2words
from odoo.exceptions import UserError
import logging
from odoo.exceptions import ValidationError
logger = logging.getLogger(__name__)
class StockMove(models.Model):
    _inherit  = 'stock.move'

    cant_cajas = fields.Integer('Cant cajas')
    peso_neto = fields.Float('Peso neto (Kg)')
    peso_bruto = fields.Float('Peso bruto (kg)')
    diference = fields.Float('hello baby', compute='_check_weight')
    
    @api.constrains('peso_neto', 'peso_bruto')
    def _check_weight_validity(self):
        if  self.peso_neto > self.peso_bruto:
            raise ValidationError(_(
                'Error ! El peso neto no puede ser mayor al peso bruto.'))
        return True
    
    #_sql_constraints = [('check_weight_validity_s', 'CHECK(peso_neto < peso_bruto)', 'Quotation Validity is #required and must be greater than 0.')]
    