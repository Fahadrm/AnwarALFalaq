# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    def action_open_last_sale_product_value_view(self):
        if self.product_id:
            so_line = self.env['sale.order.line'].search([('product_id', '=', self.product_id.id),
                                                              ('id', "!=", self.id), ('state', 'in', ['sale', 'done'])], order="id desc", limit=3)
            domain = [
                ("id", "in", so_line.ids)
            ]
            return {
                "name": _("Product Sale Value"),
                "type": "ir.actions.act_window",
                "res_model": "sale.order.line",
                "view_type": "form",
                "view_id": self.env.ref('last_3_product_sale_value.view_last_3_sale_value_tree').id,
                "view_mode": "tree",
                "target": "new",
                "domain": domain,
            }
