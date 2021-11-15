# -*- coding: utf-8 -*-
# from odoo import http


# class Last4ProductPurchaseValue(http.Controller):
#     @http.route('/last_4_product_purchase_value/last_4_product_purchase_value/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/last_4_product_purchase_value/last_4_product_purchase_value/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('last_4_product_purchase_value.listing', {
#             'root': '/last_4_product_purchase_value/last_4_product_purchase_value',
#             'objects': http.request.env['last_4_product_purchase_value.last_4_product_purchase_value'].search([]),
#         })

#     @http.route('/last_4_product_purchase_value/last_4_product_purchase_value/objects/<model("last_4_product_purchase_value.last_4_product_purchase_value"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('last_4_product_purchase_value.object', {
#             'object': obj
#         })
