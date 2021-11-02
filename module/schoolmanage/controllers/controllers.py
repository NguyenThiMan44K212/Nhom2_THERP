# -*- coding: utf-8 -*-
# from odoo import http


#   class Schoolmanage(http.Controller):
#     @http.route('/schoolmanage/schoolmanage/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/schoolmanage/schoolmanage/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('schoolmanage.listing', {
#             'root': '/schoolmanage/schoolmanage',
#             'objects': http.request.env['schoolmanage.schoolmanage'].search([]),
#         })

#     @http.route('/schoolmanage/schoolmanage/objects/<model("schoolmanage.schoolmanage"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('schoolmanage.object', {
#             'object': obj
#         })
