from odoo.tests import TransactionCase


class TestMaterial(TransactionCase):

    def setUp(self):
        super(TestMaterial, self).setUp()
        self.material_model = self.env['material_registration.material']
        self.supplier_model = self.env['res.partner']

    def test_create_material(self):
        material_data = {
            'material_code': 'M001',
            'material_name': 'Test Material',
            'material_type': 'fabric',
            'material_buy_price': 120.0,
            'related_supplier': self.supplier_model.create({'name': 'Supplier A'}).id
        }
        material = self.material_model.create(material_data)
        self.assertEqual(material.material_code, 'M001')

    def test_read_material(self):
        material = self.material_model.create({
            'material_code': 'M002',
            'material_name': 'Test Material 2',
            'material_type': 'jeans',
            'material_buy_price': 150.0,
            'related_supplier': self.supplier_model.create({'name': 'Supplier B'}).id
        })
        read_data = material.read(['material_code', 'material_name', 'material_type', 'material_buy_price', 'related_supplier'])
        self.assertEqual(read_data[0]['material_code'], 'M002')
        self.assertEqual(read_data[0]['material_name'], 'Test Material 2')
        self.assertEqual(read_data[0]['material_type'], 'jeans')
        self.assertEqual(read_data[0]['material_buy_price'], 150.0)

    def test_update_material_positive(self):
        material = self.material_model.create({
            'material_code': 'M003',
            'material_name': 'Test Material 3',
            'material_type': 'cotton',
            'material_buy_price': 120.0,
            'related_supplier': self.supplier_model.create({'name': 'Supplier C'}).id
        })
        material.write({'material_buy_price': 200.0})
        self.assertEqual(material.material_buy_price, 200.0)

    def test_update_material_negative(self):
        with self.assertRaises(ValueError) as context:
            material = self.material_model.create({
                'material_code': 'M004',
                'material_name': 'Test Material 4',
                'material_type': 'fabric',
                'material_buy_price': 120.0,
                'related_supplier': self.supplier_model.create({'name': 'Supplier D'}).id
            })
            material.write({'material_buy_price': 50.0})  # This should trigger the error
        self.assertEqual(str(context.exception), "Material Buy Price should not be less than 100.")

    def test_delete_material(self):
        material = self.material_model.create({
            'material_code': 'M004',
            'material_name': 'Test Material 4',
            'material_type': 'fabric',
            'material_buy_price': 101,
            'related_supplier': self.supplier_model.create({'name': 'Supplier D'}).id
        })
        material.unlink()
        self.assertFalse(self.material_model.search([('material_code', '=', 'M004')]))
