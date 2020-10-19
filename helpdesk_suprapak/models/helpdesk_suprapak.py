from odoo import models, fields, api


class FaultTree(models.Model):
    _name = 'complaint.claim'
    _description = 'complaint claim'
    
    code = fields.Char('Code')
    name = fields.Char('Complain or Claim')
    
    
class TypeComplaint(models.Model):
    _name = 'type.complaint'
    _description = 'Type Complaint'
    
    complain_type_id = fields.Many2one('complaint.claim','Complain or Claim')
    name = fields.Char('Types')
    
    
class SubtypeComplaint(models.Model):
    _name = 'subtype.complaint'
    _description = 'Subtype Complaint'
    
    type_id = fields.Many2one('type.complaint','Types')
    name = fields.Char('Subtypes')
    
    
class Helpdesk(models.Model):
    _inherit = 'helpdesk.ticket'
    
    complain_type_id = fields.Many2one('complaint.claim','Complain or Claim')
    type_id = fields.Many2one('type.complaint','Type')
    subtype_id = fields.Many2one('subtype.complaint','Subtype')
    action_plan = fields.Boolean('Action Plan')
    replacement_material = fields.Boolean('Replacement Material')
    return_material = fields.Boolean('Return Material')
    credit_note = fields.Boolean('Credit Note')
    queja = fields.Boolean(compute="_compute_funtion_bool")
    reclamo = fields.Boolean(compute="_compute_funtion_bool1")
    quantity_report = fields.Integer('Quantity Report')
    unit_product_id = fields.Many2one('uom.uom','Unit of measure Product')
    bool_tecnology = fields.Boolean(compute='_compute_bool_tecnology')

    @api.depends('team_id')
    def _compute_bool_tecnology(self):
        if self.team_id.name == 'SOPORTE TECNOLOGICO':
            self.bool_tecnology = True
        else:
            self.bool_tecnology = False
    
    @api.depends('ticket_type_id')
    def _compute_funtion_bool(self):
        if self.ticket_type_id.name =='QUEJA': 
            self.queja = True
        else:
            self.queja = False
    
    @api.depends('ticket_type_id')
    def _compute_funtion_bool1(self):
        if self.ticket_type_id.name == 'RECLAMO':
            self.reclamo = True
        else:
            self.reclamo = False
            
                
class HelpdeskTicketType(models.Model):
    _inherit = 'helpdesk.ticket.type'

    team_id = fields.Many2one('helpdesk.team', 'Helpdesk Team')
