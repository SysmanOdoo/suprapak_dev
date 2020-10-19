from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _prepare_invoice(self):
        journal_id = self.partner_id.sale_journal_id or False
        if journal_id:
            self = self.with_context(default_journal_id=journal_id.id)
        res = super(SaleOrder, self)._prepare_invoice()
        return res
    
    def _create_invoices(self, grouped=False, final=False):
        res = super(SaleOrder, self)._create_invoices(grouped=grouped, final=final)
        for move in res:
            move._onchange_invoice_dates()
            move._onchange_pa_id()
        return res