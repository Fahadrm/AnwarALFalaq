# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from ast import literal_eval


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    # _inherit = 'mail.thread'

    loss_product = fields.Boolean(string="Loss",default=False)

    @api.onchange('lst_price','standard_price','list_price')
    def _onchange_loss_product(self):
        for i in self:
            if i.standard_price > i.lst_price or i.standard_price > i.list_price:
                i.loss_product = True
            else:
                i.loss_product = False

    @api.model_create_multi
    def create(self, vals_list):
        templates = super(ProductTemplate, self).create(vals_list)
        users_from_settings = self.env['ir.config_parameter'].sudo().get_param('loss_product.user_ids') or False
        for i in templates:
            if i.standard_price > i.lst_price or i.standard_price > i.list_price:
                i.loss_product = True
            else:
                i.loss_product = False
        if templates.loss_product == True:
            product_user = self.env['res.users'].search([('id', 'in' ,literal_eval(users_from_settings))])
            notification_ids = []
            for purchase in product_user:
                notification_ids.append((0, 0, {
                    'res_partner_id': purchase.partner_id.id,
                    'notification_type': 'inbox'}))

            templates.message_post(body=_("Loss Product Is created <br> Product name: %s ") % (templates.name),
                            # message_type='comment',
                            message_type='notification',
                              subtype_xmlid='mail.mt_comment',
                                # author_id=self.env.ref('base.partner_root').id,
                                # author_id='self.env.user.partner_id.id',
                              notification_ids=notification_ids)
        return templates


class ProductProduct(models.Model):
    _inherit = 'product.product'


    @api.onchange('lst_price','standard_price',)
    def _onchange_product(self):
        for i in self:
            if i.standard_price > i.lst_price:
                i.loss_product = True
            else:
                i.loss_product = False

    @api.model_create_multi
    def create(self, vals_list):
        templates = super(ProductProduct, self).create(vals_list)
        users_from_settings = self.env['ir.config_parameter'].sudo().get_param('loss_product.user_ids') or False
        for i in templates:
            if i.standard_price > i.lst_price:
                i.loss_product = True
            else:
                i.loss_product = False
        if templates.loss_product == True:
            product_user = self.env['res.users'].search([('id', 'in' ,literal_eval(users_from_settings))])
            notification_ids = []
            for purchase in product_user:
                notification_ids.append((0, 0, {
                    'res_partner_id': purchase.partner_id.id,
                    'notification_type': 'inbox'}))
            templates.message_post(body=_("Loss Product Is created <br> Product name: %s ") % (templates.name),
                                   message_type='notification',
                                   subtype_xmlid='mail.mt_comment',
                                   # author_id='self.env.user.partner_id.id',
                                   notification_ids=notification_ids)
        return templates



