# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 DevIntelle Consulting Service Pvt.Ltd (<http://www.devintellecs.com>).
#
#    For Module Support : devintelle@gmail.com  or Skype : devintelle
#
##############################################################################

from odoo import models, fields

class res_partner(models.Model):
    _inherit= 'res.partner'
    
    check_credit = fields.Boolean('Check Portfolio')
    credit_limit_on_hold  = fields.Boolean('Portfolio limit on hold')
    credit_limit = fields.Float('Portfolio Limit')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: