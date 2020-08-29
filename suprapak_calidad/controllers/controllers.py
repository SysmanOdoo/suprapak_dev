# -*- coding: utf-8 -*-
# from odoo import http


# class SuprapakCalidad(http.Controller):
#     @http.route('/suprapak_calidad/suprapak_calidad/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/suprapak_calidad/suprapak_calidad/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('suprapak_calidad.listing', {
#             'root': '/suprapak_calidad/suprapak_calidad',
#             'objects': http.request.env['suprapak_calidad.suprapak_calidad'].search([]),
#         })

#     @http.route('/suprapak_calidad/suprapak_calidad/objects/<model("suprapak_calidad.suprapak_calidad"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('suprapak_calidad.object', {
#             'object': obj
#         })
