# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    def action_open_last_purchase_product_value_view(self):
        if self.product_id:
            po_line = self.env['purchase.order.line'].search([('product_id', '=', self.product_id.id),
                                                              ('id', "!=", self.id), ('state', 'in', ['purchase', 'done'])], order="id desc", limit=4)
            domain = [
                ("id", "in", po_line.ids)
            ]
            return {
                "name": _("Product Purchase Value"),
                "type": "ir.actions.act_window",
                "res_model": "purchase.order.line",
                "view_type": "form",
                "view_id": self.env.ref('last_4_product_purchase_value.view_last_4_purchase_value_tree').id,
                "view_mode": "tree",
                "target": "new",
                "domain": domain,
            }
