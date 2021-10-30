# -*- coding: utf-8 -*-
# from odoo import http


# class ProductMultiUom(http.Controller):
#     @http.route('/product_multi_uom/product_multi_uom/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_multi_uom/product_multi_uom/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_multi_uom.listing', {
#             'root': '/product_multi_uom/product_multi_uom',
#             'objects': http.request.env['product_multi_uom.product_multi_uom'].search([]),
#         })

#     @http.route('/product_multi_uom/product_multi_uom/objects/<model("product_multi_uom.product_multi_uom"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_multi_uom.object', {
#             'object': obj
#         })
