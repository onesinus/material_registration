from odoo import models, fields, api

class Material(models.Model):
    _name = 'material_registration.material'
    _description = 'Material Registration'

    material_code = fields.Char(string='Material Code', required=True)
    material_name = fields.Char(string='Material Name', required=True)
    material_type = fields.Selection([
        ('fabric', 'Fabric'),
        ('jeans', 'Jeans'),
        ('cotton', 'Cotton')],
        string='Material Type', required=True)
    material_buy_price = fields.Float(string='Material Buy Price', required=True, digits=(10, 2))
    related_supplier = fields.Many2one('res.partner', string='Related Supplier', required=True)

    @api.constrains('material_buy_price')
    def _check_material_buy_price(self):
        for record in self:
            if record.material_buy_price < 100:
                raise ValueError("Material Buy Price should not be less than 100.")