import datetime
from odoo.exceptions import UserError
from datetime import datetime, date
import time
from odoo import api, models, _
from odoo.exceptions import UserError
from xlsxwriter.utility import xl_range, xl_rowcol_to_cell


class AreaReportXls(models.AbstractModel):
    _name = 'report.area_order_report.action_area_order_report_xls'
    _inherit = 'report.report_xlsx.abstract'

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






    def generate_xlsx_report(self, workbook, data, lines):

        if not data.get('form') or not self.env.context.get('active_model'):
            raise UserError(_("Form content is missing, this report cannot be printed."))

        sheet = workbook.add_worksheet(_('Area Order Report'))
        sheet.set_landscape()
        sheet.set_default_row(25)
        sheet.fit_to_pages(1, 0)
        sheet.set_zoom(80)


        company = self.env['res.company'].browse(data['form']['company_id'])

        date_from = data['form']['date_from']
        date_to = data['form']['date_to']
        company_id = data['form']['company_id']
        area_id = data['form']['area_id']
        area = self.env['sale.area'].browse(data['form']['area_id'])

        if company.street:
            res = company.street
        else:
            res=""
        if company.street2:
            res2 = company.street2
        else:
            res2 = ""


        date_start = data['form']['date_from']
        date_end = data['form']['date_to']
        if date_start:

            date_object_date_start = datetime.strptime(date_start, '%Y-%m-%d').date()
        if date_end:
            date_object_date_end = datetime.strptime(date_end, '%Y-%m-%d').date()


        font_size_8 = workbook.add_format({'bottom': True, 'top': True, 'right': True, 'left': True, 'font_size': 14})
        font_size_8_center = workbook.add_format(
            {'bottom': True, 'top': True, 'left': True, 'font_size': 14, 'align': 'center'})
        font_size_8_right = workbook.add_format(
            {'bottom': True, 'top': True, 'left': True, 'font_size': 14, 'align': 'right'})
        font_size_8_left = workbook.add_format(
            {'bottom': True, 'top': True, 'left': True, 'font_size': 14, 'align': 'left'})

        formattotal = workbook.add_format(
            {'bg_color': 'e2e8e8', 'font_size': 14, 'bottom': True, 'right': True, 'left': True, 'top': True,
             'align': 'right', 'bold': True})


        blue_mark2 = workbook.add_format(
            {'bottom': True, 'top': True, 'right': True, 'left': True, 'font_size': 14, 'bold': True,
             'color': 'ffffff', 'bg_color': '7b0b5b', 'align': 'center'})
        font_size_8blod = workbook.add_format(
            {'bottom': True, 'top': True, 'right': True, 'left': True, 'font_size': 14, 'bold': True, })

        blue_mark3 = workbook.add_format(
            {'bottom': True, 'top': True, 'right': True, 'left': True, 'font_size': 18, 'bold': True,
             'color': 'ffffff', 'bg_color': '7b0b5b', 'align': 'center'})

        title_style = workbook.add_format({'font_size': 14, 'bold': True,
                                           'bg_color': '000000', 'color': 'ffffff',
                                           'bottom': 1, 'align': 'center'})
        account_style = workbook.add_format({'font_size': 14, 'bold': True,
                                           'bg_color': '929393', 'color': 'ffffff',
                                           'bottom': 1, 'align': 'left'})

        sheet.set_column(1, 1, 20)
        sheet.set_column(2, 2, 25)
        sheet.set_column(3, 3, 25)
        sheet.set_column(4, 4, 20)
        sheet.set_column(5, 5, 25)
        sheet.set_column(6, 6, 20)
        sheet.set_column(7, 7, 20)
        sheet.set_column(8, 8, 20)
        sheet.set_column(9, 9, 20)
        sheet.set_column(10, 10, 20)
        sheet.set_column(11, 11, 20)
        sheet.set_column(12, 12, 20)
        sheet.set_column(13, 13, 20)
        sheet.set_column(14, 14, 20)
        sheet.set_column(15, 15, 20)
        sheet.set_column(16, 16, 20)
        sheet.set_column(17, 17, 20)
        sheet.set_column(18, 18, 20)
        sheet.set_column(19, 19, 20)
        sheet.set_column(20, 20, 20)
        sheet.set_column(21, 21, 30)
        sheet.set_column(22, 22, 20)
        sheet.set_column(23, 23, 20)
        sheet.set_column(24, 24, 20)

        sheet.merge_range('A1:D1', company.name, blue_mark3)
        sheet.merge_range('A2:D2', res + " ," + res2, blue_mark2)
        sheet.merge_range('A3:D3', "Area Order Report", blue_mark2)

        model = self.env.context.get('active_model')
        docs = self.env[model].browse(self.env.context.get('active_ids', []))

        sheet.merge_range('A4:D4',
                          "Area : " + area.name, font_size_8blod)

        if date_start and date_end:

            sheet.merge_range('A5:D5',
                              "Date : " + date_object_date_start.strftime('%d-%m-%Y') + " to " + date_object_date_end.strftime(
                                  '%d-%m-%Y'), font_size_8blod)
        elif date_start:
            sheet.merge_range('A5:D5', "Date : " + date_object_date_start.strftime('%d-%m-%Y'),
                              font_size_8blod)

        sheet.write('A6', "Sl No.", title_style)
        sheet.write('B6', "Date", title_style)
        sheet.write('C6', "Product", title_style)
        sheet.write('D6', "Total Order Qty", title_style)

        linw_row = 6
        line_column = 0

        for line in self.get_sale(data):
            sheet.write(linw_row, line_column, line['sl_no'], font_size_8_center)
            sheet.write(linw_row, line_column + 1, line['order_date'], font_size_8_left)
            sheet.write(linw_row, line_column + 2, line['product_name'], font_size_8_left)
            sheet.write(linw_row, line_column + 3, '{0:,.2f}'.format(float(line['order_qty'])), font_size_8_center)

            linw_row = linw_row + 1
            line_column = 0

        line_column = 0

        sheet.merge_range(linw_row, 0, linw_row, 2, "TOTAL", font_size_8_left)

        # total_cell_range2 = xl_range(8, 2, linw_row - 1, 2)
        total_cell_range3 = xl_range(6, 3, linw_row - 1, 3)


        # sheet.write_formula(linw_row, 2, '=SUM(' + total_cell_range2 + ')', font_size_8_center)
        sheet.write_formula(linw_row, 3, '=SUM(' + total_cell_range3 + ')', font_size_8_center)


