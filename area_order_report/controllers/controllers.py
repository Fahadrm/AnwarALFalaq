# -*- coding: utf-8 -*-
# from odoo import http


# class AreaOrderReport(http.Controller):
#     @http.route('/area_order_report/area_order_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/area_order_report/area_order_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('area_order_report.listing', {
#             'root': '/area_order_report/area_order_report',
#             'objects': http.request.env['area_order_report.area_order_report'].search([]),
#         })

#     @http.route('/area_order_report/area_order_report/objects/<model("area_order_report.area_order_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('area_order_report.object', {
#             'object': obj
#         })
