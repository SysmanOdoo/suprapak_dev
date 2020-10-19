# -*- coding: utf-8 -*-
from odoo import api, fields, models

class AutonomousHeritage(models.Model):
    _name = 'autonomous.heritage'
    _description = 'Autonomous heritage'

    name = fields.Char(string='Name')
    code = fields.Char(string='Code')
    description = fields.Text(string='Description')

    def name_get(self):
        res = []
        for record in self:
            name = u'[%s] %s' % (record.code or '', record.name or '')
            res.append((record.id, name))
    
        return res
    
    