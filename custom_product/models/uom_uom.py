from odoo import api, fields, models, tools, _, SUPERUSER_ID


class UomquantityUpdate(models.Model):

    _inherit = "uom.uom"

    product_uom = fields.Float("Secondary total qty")

