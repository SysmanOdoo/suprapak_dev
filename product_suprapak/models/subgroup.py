from odoo import models, api, fields

class ProductTemplateSubgroup(models.Model):
    _name = 'product.template.subgroup'

    name = fields.Char('Name')
    categ_id = fields.Many2one('product.category', string='Categoria')
    sec = fields.Char(string="Service Number", readonly=True, required=True, copy=False, default='New')
    sequence_products_id = fields.Many2one('ir.sequence', string='Secuencia de productos')


    @api.model
    def create(self,values):

        categ_id = self.env['product.category'].browse(values.get('categ_id'))
        values['sec'] = categ_id.sequence_subgroups_id._next()
        res=super(ProductTemplateSubgroup,self).create(values)

        seq_id = self.env['ir.sequence'].create({'name':'Secuencia Productos de '+ res.name or res.sec,
                                                'implementation': 'no_gap',
                                                'prefix': res.sec + '-',
                                                'padding': 4,
                                                'number_increment': 1,
                                                'number_next_actual': 1})
        res.sequence_products_id = seq_id.id
    
        return res