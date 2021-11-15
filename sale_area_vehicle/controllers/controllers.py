# -*- coding: utf-8 -*-
# from odoo import http


# class SaleAreaVehicle(http.Controller):
#     @http.route('/sale_area_vehicle/sale_area_vehicle/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_area_vehicle/sale_area_vehicle/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_area_vehicle.listing', {
#             'root': '/sale_area_vehicle/sale_area_vehicle',
#             'objects': http.request.env['sale_area_vehicle.sale_area_vehicle'].search([]),
#         })

#     @http.route('/sale_area_vehicle/sale_area_vehicle/objects/<model("sale_area_vehicle.sale_area_vehicle"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_area_vehicle.object', {
#             'object': obj
#         })
