# -*- coding: utf-8 -*-
# from odoo import http


# class LossProduct(http.Controller):
#     @http.route('/loss_product/loss_product/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/loss_product/loss_product/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('loss_product.listing', {
#             'root': '/loss_product/loss_product',
#             'objects': http.request.env['loss_product.loss_product'].search([]),
#         })

#     @http.route('/loss_product/loss_product/objects/<model("loss_product.loss_product"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('loss_product.object', {
#             'object': obj
#         })
