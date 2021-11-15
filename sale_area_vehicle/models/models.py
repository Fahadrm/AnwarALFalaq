# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleArea(models.Model):
    _name = 'sale.area'
    _description = 'Area'

    name = fields.Char(string="Area")


class SaleVehicleModel(models.Model):
    _name = 'sale.vehicle'
    _description = 'Vehicle'

    name = fields.Char(string="Vehicle")


class SaleOrder(models.Model):
    _inherit = "sale.order"

    vehicle_id = fields.Many2one('sale.vehicle',string="Vehicle")
    area_id = fields.Many2one('sale.area',string="Area")

    # def _prepare_invoice(self):
    #     res = super(SaleOrder, self)._prepare_invoice()
    #     res.update(
    #         {
    #             'vehicle_id': self.vehicle_id,
    #             'area_id': self.area_id,
    #         }
    #     )
    #     return res
