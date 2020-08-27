# -*- coding: utf-8 -*-
# from odoo import http


# class QualityControl(http.Controller):
#     @http.route('/quality_control/quality_control/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/quality_control/quality_control/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('quality_control.listing', {
#             'root': '/quality_control/quality_control',
#             'objects': http.request.env['quality_control.quality_control'].search([]),
#         })

#     @http.route('/quality_control/quality_control/objects/<model("quality_control.quality_control"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('quality_control.object', {
#             'object': obj
#         })
