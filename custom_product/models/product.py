import itertools
from collections import defaultdict


from odoo import api, fields, models, tools, _, SUPERUSER_ID


class ProductTemplate(models.Model):

    _inherit = "product.template"

    @api.model
    def _get_default_uom_id(self):
        return self.env.ref('uom.product_uom_unit')

    sec_uom_select = fields.Boolean(string="If Secondary UOM Product")
    sec_uom_id = fields.Many2one('uom.uom', string="Secondary UOM", default=_get_default_uom_id, domain="[('category_id', '=', product_uom_category_id)]")
    total_qty = fields.Float(string="Total Quantity", compute="_amount_all")
    product_uom_category_id = fields.Many2one('uom.category', related='sec_uom_id.category_id', string="Secondary Product Category")


    @api.depends('sec_uom_id.factor_inv')
    def _amount_all(self):
        for order in self:
            total_qty = 0.0
            if order.total_qty == 0.0 and order.sec_uom_id.factor_inv > 0.0:
                total_qty = order.qty_available/order.sec_uom_id.factor_inv
        print("order.uom_id", order.sec_uom_id.factor_inv)
        print("order.qty_available", order.qty_available)
        order.update({
            'total_qty': total_qty,
        })

    # @api.model
    def view_product_qty(self):
        self.ensure_one()
        return True

