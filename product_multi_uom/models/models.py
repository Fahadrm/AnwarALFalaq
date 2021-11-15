from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"



    @api.depends('sec_uom_ids')
    def _compute_uom(self):
        for line in self:
            new_terms_lines = self.env['product.template.uom.line']
            vals_list = []
            if line.sec_uom_ids:

                multi_uom_line = []
                for sec in line.sec_uom_ids:
                    print('sec', sec)
                    already_exists = line.multi_uom_line_ids.filtered(lambda line: line.uom_id.id == sec.ids[0])
                    if already_exists:
                        line.multi_uom_line_ids = line.multi_uom_line_ids - already_exists


                    _update_stk = (line.qty_available) / (sec.factor_inv)
                    vals_list.append(
                        (
                            0,
                            0,
                            {
                                 'uom_id': sec.ids[0],
                                'product_tmpl_id': line.ids[0],
                                'no_of_pkt': _update_stk,

                            },
                        )
                    )


            else:
                line.multi_uom_line_ids = line.multi_uom_line_ids


        self.multi_uom_line_ids = vals_list








    sec_uom_ids = fields.Many2many('uom.uom', string="Multi UOM")
    multi_uom_line_ids = fields.One2many('product.template.uom.line', 'product_tmpl_id',compute='_compute_uom', string='Multi Uom Line',store=True)






class product_template_uom_line(models.Model):
    _name = 'product.template.uom.line'
    _description = 'multi_uom_line'
    product_tmpl_id = fields.Many2one('product.template',readonly=True,index=True)
    uom_id = fields.Many2one('uom.uom', string="Unit of Measure")
    no_of_pkt = fields.Integer(string="Number of Packet")



























