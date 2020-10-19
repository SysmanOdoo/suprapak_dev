# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ProductTemplateInherit(models.Model):
    _inherit = 'product.template'

    subgroups_ids = fields.Many2one('product.template.subgroup', string='Sub-Group', domain="[('categ_id', '=?', categ_id)]")
    default_code = fields.Char('Internal Reference', compute='_compute_code', store=True)

    # @api.depends('categ_id','subgroups_ids')
    # def _compute_code(self):
    #     for record in self:
    #         if record.categ_id.name == 'PAPELERIA':
    #             record.default_code = 1
    #         elif record.categ_id.name == 'CAFETERIA Y ASEO':
    #             record.default_code = 2
    #         elif record.categ_id.name == 'MANTENIMIENTO':
    #             record.default_code = 3
    #         elif record.categ_id.name == 'EQUIPOS DE OFICINA':
    #             record.default_code = 4
    #         elif record.categ_id.name == 'DOTACION':
    #             record.default_code = 5
    #         elif record.categ_id.name == 'SERVICIOS Y HONORARIOS':
    #             record.default_code = 6
    #         elif record.categ_id.name == 'PENDIENTE':
    #             record.default_code = 7

    #         if record.subgroups_ids and record.default_code == '1':
    #             if record.subgroups_ids.name =='PAPELERIA GENERAL':
    #                 record.default_code = record.default_code + '.' + '1'
    #             if record.subgroups_ids.name =='PAPELERIA IMPRESA':
    #                 record.default_code = record.default_code + '.' + '2'
    #             if record.subgroups_ids.name =='PENDIENTE':
    #                 record.default_code = record.default_code + '.' + '3'
    #         elif record.subgroups_ids and record.default_code == '2':
    #             if record.subgroups_ids.name =='CAFETERIA Y ASEO':
    #                 record.default_code = record.default_code + '.' + '1'
    #             if record.subgroups_ids.name =='PENDIENTE 1':
    #                 record.default_code = record.default_code + '.' + '2'
    #             if record.subgroups_ids.name =='PENDIENTE 2':
    #                 record.default_code = record.default_code + '.' + '3'
    #         elif record.subgroups_ids and record.default_code == '3':
    #             if record.subgroups_ids.name =='MANTENIMIENTO':
    #                 record.default_code = record.default_code + '.' + '1'
    #             if record.subgroups_ids.name =='INFRAESTRUCTURA':
    #                 record.default_code = record.default_code + '.' + '2'
    #             if record.subgroups_ids.name =='SERVICIO DE MANTENIMIENTO':
    #                 record.default_code = record.default_code + '.' + '3'
    #         elif record.subgroups_ids and record.default_code == '4':
    #             if record.subgroups_ids.name =='PENDIENTE 1':
    #                 record.default_code = record.default_code + '.' + '1'
    #             if record.subgroups_ids.name =='PENDIENTE 2':
    #                 record.default_code = record.default_code + '.' + '2'
    #             if record.subgroups_ids.name =='PENDIENTE 3':
    #                 record.default_code = record.default_code + '.' + '3'
    #         elif record.subgroups_ids and record.default_code == '5':
    #             if record.subgroups_ids.name =='DOTACION PERSONAL':
    #                 record.default_code = record.default_code + '.' + '1'
    #             if record.subgroups_ids.name =='DOTACION UNIFORMES':
    #                 record.default_code = record.default_code + '.' + '2'
    #             if record.subgroups_ids.name =='PENDIENTE':
    #                 record.default_code = record.default_code + '.' + '3' 
    #         elif record.subgroups_ids and record.default_code == '6':
    #             if record.subgroups_ids.name =='PENDIENTE 1':
    #                 record.default_code = record.default_code + '.' + '1'
    #             if record.subgroups_ids.name =='PENDIENTE 2':
    #                 record.default_code = record.default_code + '.' + '2'
    #             if record.subgroups_ids.name =='PENDIENTE 3':
    #                 record.default_code = record.default_code + '.' + '3'
    #         elif record.subgroups_ids and record.default_code == '7':
    #             if record.subgroups_ids.name =='PENDIENTE 1':
    #                 record.default_code = record.default_code + '.' + '1'
    #             if record.subgroups_ids.name =='PENDIENTE 2':
    #                 record.default_code = record.default_code + '.' + '2'
    #             if record.subgroups_ids.name =='PENDIENTE 3':
    #                 record.default_code = record.default_code + '.' + '3'
    #         else:
    #             record.default_code = False
                
    @api.model
    def create(self,values):

        sub_categ_id = self.env['product.template.subgroup'].browse(values.get('subgroups_ids'))
        values['default_code'] = sub_categ_id.sequence_products_id._next()
        res=super(ProductTemplateInherit,self).create(values)
        return res
            
    # def write(self,values):

    #     sub_categ_id = self.env['product.template.subgroup'].browse(values.get('subgroups_ids'))
    #     values['default_code'] = sub_categ_id.sequence_products_id._next()
    #     res=super(ProductTemplateInherit,self).write(values)
    #     return res
            
