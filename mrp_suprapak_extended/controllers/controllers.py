# -*- coding: utf-8 -*-
# from odoo import http


# class MaxAndMi(http.Controller):
#     @http.route('/max_and_mi/max_and_mi/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/max_and_mi/max_and_mi/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('max_and_mi.listing', {
#             'root': '/max_and_mi/max_and_mi',
#             'objects': http.request.env['max_and_mi.max_and_mi'].search([]),
#         })

#     @http.route('/max_and_mi/max_and_mi/objects/<model("max_and_mi.max_and_mi"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('max_and_mi.object', {
#             'object': obj
#         })