# -*- coding: utf-8 -*-
# from odoo import http


# class UniqueProduct(http.Controller):
#     @http.route('/unique_product/unique_product/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/unique_product/unique_product/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('unique_product.listing', {
#             'root': '/unique_product/unique_product',
#             'objects': http.request.env['unique_product.unique_product'].search([]),
#         })

#     @http.route('/unique_product/unique_product/objects/<model("unique_product.unique_product"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('unique_product.object', {
#             'object': obj
#         })
