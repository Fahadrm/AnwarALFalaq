import itertools
from collections import defaultdict


from odoo import api, fields, models, tools, _, SUPERUSER_ID
from odoo.tools import float_is_zero, float_compare



class ProductTemplate(models.Model):

    _inherit = "product.template"

    STATUS_LIST = [('updated', 'Sec UOM Updated'), ('cancelled', 'Cancelled')]

    sec_uom_select = fields.Boolean(string="If Secondary UOM Product")
    sec_uom_ids = fields.Many2many('uom.uom', string="Secondary UOM")
    total_qty = fields.Float(string="Total Quantity", compute="_amount_all")
    uom_qty_name = fields.Char(string="Secondary Qty")
    state = fields.Selection(STATUS_LIST, readonly=True)

    @api.onchange('sec_uom_ids')
    def _amount_all(self):
        total_list = []
        for order in self:
            print(order, 'order')
            qty_dict = {}
            for sec in order.sec_uom_ids:
                if order.total_qty >= 0.0 and sec.factor_inv > 0.0:
                    sec.product_uom = order.qty_available/sec.factor_inv
                    print("order.uom_id", sec.factor_inv)
                    print("order.qty_available", order.qty_available)
                    print('order.total_qty', order.total_qty)
                qty_dict = sec.product_uom
                print(qty_dict, 'qty')
                total_list.append(qty_dict)
                print('total_list', total_list)
                print(type(total_list), 'type')
                res = list(map(float, total_list))
                print("list after conversion :", str(res))

    def view_product_qty(self):
        self.ensure_one()
        return {
            'name': ('Secondary Product Uom'),
            'domain': [('product_id', '=', self.id)],
            'view_type': 'form',
            'res_model': 'sec.uom.value',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',

        }

    def view_received_qty(self):
        self.ensure_one()
        return {
            'name': ('Secondary Product Uom'),
            # 'domain': [('product_id', '=', self.id)],
            'view_type': 'form',
            'res_model': 'stock.received',
            'view_id': False,
            'view_mode': 'form',
            'type': 'ir.actions.act_window',

        }

    def update_uom_values(self):
        sec_uom_obj = self.env['sec.uom.value']
        print(sec_uom_obj, 'sec')
        mapped_sec_uom=self.sec_uom_ids.mapped('id')
        print(mapped_sec_uom,"map out")

        data = {
                'product_id': self.id,
                'sec_uom_view_ids': mapped_sec_uom,
            }
        print(data, 'data')
        new_sec_uom_obj = sec_uom_obj.create(data)
        print('new sec uom', new_sec_uom_obj)
        return self.write({'state': 'updated'})

    def action_cancelled(self):
        return self.write({'state': 'cancelled'})

class ProductProduct(models.Model):

    _inherit = 'product.product'

    def view_received_qty(self):
        self.ensure_one()
        return {
            'name': ('Secondary Product Uom'),
            # 'domain': [('product_id', '=', self.id)],
            'view_type': 'form',
            'res_model': 'stock.received',
            'view_id': False,
            'view_mode': 'form',
            'type': 'ir.actions.act_window',

        }

class UomquantityUpdate(models.Model):

    _inherit = "uom.uom"

    def name_get(self):
        if not self.env.context.get('show_uom'):
            result = []
            for uom in self:
                name = str(uom.name)
                result.append((uom.id, name))
        return result




