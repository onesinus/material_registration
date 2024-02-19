from odoo.tests import TransactionCase


class TestMaterial(TransactionCase):

    def setUp(self):
        super(TestMaterial, self).setUp()
        self.material_model = self.env['your_module.material']
        self.supplier_model = self.env['res.partner']

    def test_create_material(self):
        material_data = {
            'material_code': 'M001',
            'material_name': 'Test Material',
            'material_type': 'fabric',
            'material_buy_price': 120.0,
            'related_supplier': self.supplier_model.create({'name': 'Supplier A', 'supplier': True}).id
        }
        material = self.material_model.create(material_data)
        self.assertEqual(material.material_code, 'M001')

    def test_read_material(self):
        material = self.material_model.create({
            'material_code': 'M002',
            'material_name': 'Test Material 2',
            'material_type': 'jeans',
            'material_buy_price': 150.0,
            'related_supplier': self.supplier_model.create({'name': 'Supplier B', 'supplier': True}).id
        })
        read_data = material.read(['material_code', 'material_name', 'material_type', 'material_buy_price', 'related_supplier'])
        self.assertEqual(read_data[0]['material_code'], 'M002')
        self.assertEqual(read_data[0]['material_name'], 'Test Material 2')
        self.assertEqual(read_data[0]['material_type'], 'jeans')
        self.assertEqual(read_data[0]['material_buy_price'], 150.0)

    def test_update_material(self):
        material = self.material_model.create({
            'material_code': 'M003',
            'material_name': 'Test Material 3',
            'material_type': 'cotton',
            'material_buy_price': 80.0,
            'related_supplier': self.supplier_model.create({'name': 'Supplier C', 'supplier': True}).id
        })
        material.write({'material_buy_price': 200.0})
        self.assertEqual(material.material_buy_price, 200.0)

    def test_delete_material(self):
        material = self.material_model.create({
            'material_code': 'M004',
            'material_name': 'Test Material 4',
            'material_type': 'fabric',
            'material_buy_price': 90.0,
            'related_supplier': self.supplier_model.create({'name': 'Supplier D', 'supplier': True}).id
        })
        material.unlink()
        self.assertFalse(self.material_model.search([('material_code', '=', 'M004')]))
