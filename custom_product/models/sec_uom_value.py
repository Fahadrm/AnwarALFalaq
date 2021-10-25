from odoo import api, fields, models


class SecUomValue(models.Model):

    _name = 'sec.uom.value'
    _rec_name = 'product_id'

    product_id = fields.Many2one('product.template', string="Product Name")
    sec_uom_view_ids = fields.Many2many('uom.uom', 'sec_uom_value_id', string="Secondary UOM")

    def name_get(self):
        result = []
        for obj in self:
            name = obj.product_id.uom_id.name
            if obj.product_id.uom_id.name and obj.product_id.uom_id.product_uom:
                name = str(obj.product_id.uom_id.product_uom) + ' ' + obj.product_id.uom_id.name
            result.append((obj.id, name))
        return result

# class UomquantityUpdateInherit(models.Model):
#
#     _inherit = "uom.uom"
#
#     def name_get(self):
#         result = []
#         for obj in self:
#             name = obj.name
#             if obj.name and obj.product_uom:
#                 name = str(obj.product_uom) + ' ' + obj.name
#             result.append((obj.id, name))
#         return result


