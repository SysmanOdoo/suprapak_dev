# -*- coding: utf-8 -*-
from datetime import datetime

from odoo import models, api, fields
from odoo.exceptions import AccessDenied


class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.model
    def _get_zzz(self):
        zz_id = self.env['account.payment.mean.code'].search([('code','=','ZZZ')])
        if zz_id:
            return zz_id.id
        return False

    # state = fields.Selection(selection_add=[('blocked', 'Blocked')])
    dispatch_route = fields.Many2one('dispatch.route', string='Dispatch route')
    observation = fields.Text(string='Observations')
    observation_pa = fields.Text(string='Observations PA')
    # pa_id = fields.Many2one('autonomous.heritage', string='Autonomous heritage')
    insurances = fields.Float('Insurances', digits='Product Price')
    freight = fields.Float('Freight', digits='Product Price')
    other_expenses = fields.Float('Others', digits='Product Price')
    carrier_id = fields.Many2one('delivery.carrier', string='Carrier')
    carrier_tracking_ref = fields.Char(string='Tracking Reference', copy=False)
    net_weight = fields.Float('Net weight', digits='Stock Weight')
    gross_weight = fields.Float('Gross weight', digits='Stock Weight')
    total_boxes = fields.Float('Total boxes',digits='Stock Weight')
    payment_mean_code_id = fields.Many2one(default=_get_zzz)
    invoice_date = fields.Date(default=datetime.now().date())
    
    
    @api.onchange('journal_id')
    def _onchange_pa_id(self):
        if self.journal_id:
            if self.journal_id.description_pa:
                self.observation_pa = self.journal_id.description_pa
            else:
                self.observation_pa = ''
            
    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        res = super(AccountMove, self)._onchange_partner_id()
        if self.partner_id.sale_journal_id:
            self.journal_id = self.partner_id.sale_journal_id.id
        self._onchange_pa_id()
        return res
    
    @api.onchange('invoice_type_code')
    def _selection_dispatch_route(self):
        if self.invoice_type_code == '01':
            domain = [('code', 'in', ('TL','TT'))]
        elif self.invoice_type_code == '02':
            domain = [('code', 'in', ('A','M'))]
        else:
            domain = []
        return {'domain': {'dispatch_route': domain}}

    # def validation_budget(self):
    #     flag = True
    #     for record in self:
    #         if record.type == 'in_invoice' and record.state != 'blocked':
    #             accounts = record.invoice_line_ids.account_id.ids
    #             for account in accounts:
    #                 dic = {}
    #                 dic['date'] = record.date
    #                 dic['account'] = account
    #                 domain = [('account_id.id', '=', account), ('move_id.id', '=', record.id)]
    #                 total = 0
    #                 for line in record.invoice_line_ids.search(domain):
    #                     total += line.price_subtotal
    #                 dic['total'] = total
    #                 flag = self.validate_budget_lines(dic)
    #     return flag

    # def action_post(self):
    #     if not self.validation_budget():
    #         # res = self.action_create_activity()
    #         res = self.action_wizard_budget()
    #     else:
    #         res = super(AccountMove, self).action_post()
    #     return res

    # def validate_budget_lines(self, dic):
    #     # dic = {'date', 'account', 'total'}
    #     flag = True
    #     domain = [('crossovered_budget_id.state', '=', 'done'), ('date_from', '<=', dic['date']),
    #               ('date_to', '>=', dic['date']),
    #               ('general_budget_id.account_ids', 'in', dic['account'])]
    #     lines = self.env['crossovered.budget.lines'].search(domain)
    #     for line in lines:
    #         # if dic['account'] in line.general_budget_id.account_ids.ids:
    #         if dic['total'] > line.planned_amount + line.practical_amount:
    #             flag = False
    #     return flag

    # def action_wizard_budget(self):
    #     imd = self.env['ir.model.data']
    #     for record in self:
    #         partners = record.message_follower_ids.partner_id.ids
    #         users = self.env['res.users'].search([('partner_id.id', 'in', partners)])
    #         ids = []
    #         for user in users:
    #             ids.append((4, user.id))
    #         vals_wiz = {
    #             'message': 'Superó el presupuesto estimado, por favor notifique con el area encargada',
    #             'users_ids': ids,
    #         }
    #         wiz_id = self.env['budget.wizard'].create(vals_wiz)
    #         action = imd.xmlid_to_object('account_suprapak.action_budget_wizard')
    #         form_view_id = imd.xmlid_to_res_id('account_suprapak.view_budget_wizard_form')
    #         return {
    #             'name': action.name,
    #             'help': action.help,
    #             'type': action.type,
    #             'views': [(form_view_id, 'form')],
    #             'view_id': form_view_id,
    #             'target': action.target,
    #             'context': action.context,
    #             'res_model': action.res_model,
    #             'res_id': wiz_id.id,
    #         }
