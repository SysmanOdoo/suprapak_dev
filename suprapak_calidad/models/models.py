# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class suprapak_calidad(models.Model):
#     _name = 'suprapak_calidad.suprapak_calidad'
#     _description = 'suprapak_calidad.suprapak_calidad'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
