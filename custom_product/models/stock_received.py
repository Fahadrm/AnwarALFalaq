from odoo import api, fields, models


class StockReceived(models.Model):

    _name = 'stock.received'
    _rec_name = 'qty_received'

    qty_received = fields.Float(string="Received Quantity")

    # @api.model
    def default_get(self, values):
        company_id = self.env.company.id
        picking_obj = self.env['stock.picking.type'].search([('company_id', '=', company_id)])
        print('picking_obj', picking_obj)
        product_context = self.env.context
        print('product context', product_context)
        current_product_tmpl = product_context.get('active_id')
        current_product_obj = self.env['product.product'].search([('product_tmpl_id', '=', current_product_tmpl)])
        current_product = current_product_obj.id
        print('current_product', current_product)
        for pick in picking_obj:
            if pick.code == 'incoming':
                print('picking code', pick.code)
                product_pick_domain = [('company_id', '=', company_id), ('state', '=', 'done'), ('product_id', '=', current_product),  ('picking_code', '=', 'incoming')]
                print('product pick domain', product_pick_domain)
                move_lines = self.env['stock.move.line'].search(product_pick_domain)
                print('move lines', move_lines)
                # total_quantity = move_lines.mapped('quantity_done')
                # print('total qty', total_quantity)
                # self_obj = self.search([])
                # self_obj[0].qty_received = total_quantity
        return super(StockReceived, self).default_get(values)


