# -*- coding: utf-8 -*-

import time
from odoo import api, models, _
from odoo.exceptions import UserError
import datetime
from datetime import datetime


class AreaReportPDF(models.AbstractModel):
    _name = 'report.area_order_report.pdf_area_order_report'

    def get_sale(self, data):

        lines = []

        date_from = data['form']['date_from']
        date_to = data['form']['date_to']
        company_id = data['form']['company_id']
        area_id = data['form']['area_id']

        sl = 0

        query = '''



              SELECT sum(sl.product_uom_qty) AS order_qty,pt.name as product_name,
         to_char(date_trunc('day',so.date_order),'DD-MM-YYYY') AS order_date,
            			   sl.product_id FROM sale_order_line AS sl
                           JOIN sale_order AS so ON sl.order_id = so.id
            			   left join product_product as p on (sl.product_id=p.id)
            			  left join product_template as pt on (pt.id=p.product_tmpl_id)
                           WHERE so.state IN ('sale','done')
            			   and  to_char(date_trunc('day',so.date_order),'YYYY-MM-DD')::date between %s and %s
                           AND so.area_id =%s and so.company_id = %s 

        				   group by sl.product_id,to_char(date_trunc('day',so.date_order),'DD-MM-YYYY'),pt.id

                                       '''

        self.env.cr.execute(query, (
            date_from, date_to, area_id, company_id
        ))
        for row in self.env.cr.dictfetchall():
            sl += 1

            product_name = row['product_name'] if row['product_name'] else " "
            order_qty = row['order_qty'] if row['order_qty'] else 0.0
            order_date = row['order_date'] if row['order_date'] else " "

            res = {
                'sl_no': sl,
                'product_name': product_name,
                'order_qty': order_qty if order_qty else 0.0,
                'order_date': order_date if order_date else " ",

            }

            lines.append(res)
        if lines:
            return lines
        else:
            return []




    def _get_report_values(self, docids, data=None):
        if not data.get('form') or not self.env.context.get('active_model'):
            raise UserError(_("Form content is missing, this report cannot be printed."))

        model = self.env.context.get('active_model')
        docs = self.env[model].browse(self.env.context.get('active_ids', []))

        date_from = data['form']['date_from']
        date_to = data['form']['date_to']
        company_id = data['form']['company_id']
        area_id = data['form']['area_id']
        area = self.env['sale.area'].browse(data['form']['area_id'])
        area_name = area.name


        get_sale = self.get_sale(data)

        date_object_startdate = datetime.strptime(date_from, '%Y-%m-%d').date()
        date_object_enddate = datetime.strptime(date_to, '%Y-%m-%d').date()

        docargs = {
            'doc_ids': docids,
            'doc_model': model,
            'data': data['form'],
            'date_start': date_object_startdate.strftime('%d-%m-%Y'),
            'date_end': date_object_enddate.strftime('%d-%m-%Y'),
            'docs': docs,
            'time': time,
            'get_sale': get_sale,
            'area_name':area_name if area_name else " "

        }
        return docargs
