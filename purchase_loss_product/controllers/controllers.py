# -*- coding: utf-8 -*-
# from odoo import http


# class PurchaseLossProduct(http.Controller):
#     @http.route('/purchase_loss_product/purchase_loss_product/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/purchase_loss_product/purchase_loss_product/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('purchase_loss_product.listing', {
#             'root': '/purchase_loss_product/purchase_loss_product',
#             'objects': http.request.env['purchase_loss_product.purchase_loss_product'].search([]),
#         })

#     @http.route('/purchase_loss_product/purchase_loss_product/objects/<model("purchase_loss_product.purchase_loss_product"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('purchase_loss_product.object', {
#             'object': obj
#         })
