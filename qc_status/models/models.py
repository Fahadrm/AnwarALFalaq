# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import json
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    qc_status = fields.Boolean(string="QC Status", default=False,track_visibility='always')
    identify = fields.Boolean(string="QC Identifier", default=False,)


    # @api.onchange('qc_status')
    # def onchange_qc_status(self):
    #     self.message_post(body=_("QC Status: %s ") % (self.qc_status),
    #                          message_type='comment',
    #                         # message_type='notification',
    #                           subtype_xmlid='mail.mt_comment',)
    #     return

    def write(self, values):
        res = super(PurchaseOrder, self).write(values)
        if self.qc_status:
            if self.identify==False:
                self.message_post(body=_("QC Status: %s ") % (self.qc_status), subtype_xmlid='mail.mt_comment',
                              author_id=self.create_uid.partner_id.id)
            # Set the flag to false so we post the message only once
                self.identify = True
        return res
