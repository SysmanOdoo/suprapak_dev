from odoo import models, api, fields

class ProductTemplateCateg(models.Model):
    _inherit = 'product.category'

    sec = fields.Char(string="Service Number", readonly=True, required=True, copy=False, default='New')
    sequence_subgroups_id = fields.Many2one('ir.sequence', string='Secuencia de sub categorias')
    subgroups_ids = fields.One2many('product.template.subgroup', 'categ_id', string='Sub-Group')
   
    @api.model
    def create(self,values):
        values['sec'] = self.env.ref("product_suprapak.product_categ_sequence")._next()

        res=super(ProductTemplateCateg,self).create(values)

        seq_id = self.env['ir.sequence'].create({'name':'Secuencia subgrupos de '+ res.name or res.sec,
                                                'implementation': 'no_gap',
                                                'prefix': res.sec+'.',
                                                'padding': 0,
                                                'number_increment': 1,
                                                'number_next_actual': 1})
        res.sequence_subgroups_id = seq_id.id
    
        return res
