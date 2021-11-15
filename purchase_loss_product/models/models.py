# -*- coding: utf-8 -*-
from odoo import models, fields, api,_
from ast import literal_eval



class Picking(models.Model):
    _inherit = "stock.picking"

    def button_validate(self):
        res = super(Picking, self).button_validate()
        users_from_settings = self.env['ir.config_parameter'].sudo().get_param('loss_product.user_ids') or False
        if self.picking_type_code == 'incoming':
            for move in self.move_lines:
                move.product_id._onchange_product()
                if move.product_id.loss_product == True:
                    product_user = self.env['res.users'].search([('id', 'in', literal_eval(users_from_settings))])
                    notification_ids = []
                    for purchase in product_user:
                        notification_ids.append((0, 0, {
                            'res_partner_id': purchase.partner_id.id,
                            'notification_type': 'inbox'}))

                    move.product_id.message_post(body=_("Loss Product name: %s ") % (move.product_id.name),
                                                 message_type='notification',
                                                 subtype_xmlid='mail.mt_comment',
                                                 notification_ids=notification_ids)
        return res