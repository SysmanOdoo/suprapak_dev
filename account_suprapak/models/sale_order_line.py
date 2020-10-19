from odoo import api, fields, models

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    def _prepare_invoice_line(self):
        res = super(SaleOrderLine, self)._prepare_invoice_line()
        if self.order_id:
            res['order'] = self.order_id.name
        if self.order_id and self.order_id.client_order_ref:
            res['ref_comfiar'] = self.order_id.client_order_ref
        return res