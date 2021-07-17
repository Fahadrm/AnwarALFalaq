# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from ast import literal_eval

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    user_ids = fields.Many2many('res.users', string="Users")

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        user_ids = self.env['ir.config_parameter'].sudo().get_param('loss_product.user_ids')
        if user_ids == False:
            res.update(user_ids=[(6, 0, [])],)
        else:
            res.update(user_ids=[(6, 0, literal_eval(user_ids))],)
        # res.update(
        #     authorized_users=[(6, 0, ast.literal_eval(user_ids))],
        # )
        return res

    def set_values(self):
        res = super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].set_param('loss_product.user_ids', self.user_ids.ids)
        return res