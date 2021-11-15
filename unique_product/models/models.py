# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.constrains('name')
    def _check_unique_constraint(self):
        for rec in self:
            record = rec.search([('name', '=ilike', rec.name), ('id', '!=', rec.id)])
            if record:
                raise ValidationError(_('Another product with the same name exists!'))

    @api.model
    def create(self, vals):
        res = super(ProductTemplate, self).create(vals)
        res.name = res.name.rstrip().lstrip()
        return res

    def write(self, vals):
        if 'name' in vals:
            vals['name'] = vals['name'].rstrip().lstrip()
        return super(ProductTemplate, self).write(vals)

    # @api.model
    # def create(self, values):
    #     record = super(YourClass, self).create(values)
    #     matching_products = self.env['product.product'].search([('name', '=', self.name)])
    #     if len(matching_products) > 1:
    #         raise Warning(_('You already have a product with this name. Please dont recreate it'))
    #     return record

    class ResPartner(models.Model):
        _inherit = 'res.partner'

        pos_box = fields.Char(string='PO Box', store=True)
        postal_code = fields.Char(string='POSTAL CODE', store=True)