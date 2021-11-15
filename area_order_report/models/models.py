# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date


class AreaOrderReport(models.TransientModel):
    _name = "area.order.report"
    _description = "Area Order Report"

    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company,required=True)
    date_from = fields.Date(string='Start Date',required=True,default=date.today())
    date_to = fields.Date(string='End Date',required=True,default=date.today())
    area_id = fields.Many2one('sale.area',string="Area",required=True)


    def check_report(self):

        self.ensure_one()
        context = self._context
        datas = {'ids': context.get('active_ids', [])}
        # datas['model'] = self.env.context.get('active_model', 'ir.ui.menu')
        datas['model'] = 'sale.order'
        datas['form'] = self.read()[0]
        for field in datas['form'].keys():
            if isinstance(datas['form'][field], tuple):
                datas['form'][field] = datas['form'][field][0]

        return self.env.ref('area_order_report.pdf_report_menu_area_order_report').report_action(self, data=datas)


    def export_xls(self):
        context = self._context
        datas = {'ids': context.get('active_ids', [])}
        datas['model'] = 'sale.order'
        datas['form'] = self.read()[0]
        for field in datas['form'].keys():
            if isinstance(datas['form'][field], tuple):
                datas['form'][field] = datas['form'][field][0]

        return self.env.ref('area_order_report.report_menu_area_order_report').report_action(self, data=datas)
