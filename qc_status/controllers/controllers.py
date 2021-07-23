# -*- coding: utf-8 -*-
# from odoo import http


# class QcStatus(http.Controller):
#     @http.route('/qc_status/qc_status/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/qc_status/qc_status/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('qc_status.listing', {
#             'root': '/qc_status/qc_status',
#             'objects': http.request.env['qc_status.qc_status'].search([]),
#         })

#     @http.route('/qc_status/qc_status/objects/<model("qc_status.qc_status"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('qc_status.object', {
#             'object': obj
#         })
