from odoo import http
from odoo.http import request

class MaterialController(http.Controller):

    @http.route('/material_registration/materials', auth='public', methods=['GET'])
    def get_materials(self, material_type=None):
        domain = [('material_type', '=', material_type)] if material_type else []
        materials = request.env['material_registration.material'].search(domain)
        return materials.read()

    @http.route('/material_registration/material/<int:material_id>', auth='public', methods=['GET'])
    def get_material(self, material_id):
        material = request.env['material_registration.material'].browse(material_id)
        return material.read()

    @http.route('/material_registration/material', auth='public', methods=['POST'])
    def create_material(self, **kwargs):
        material = request.env['material_registration.material'].create(kwargs)
        return material.read()

    @http.route('/material_registration/material/<int:material_id>', auth='public', methods=['PUT'])
    def update_material(self, material_id, **kwargs):
        material = request.env['material_registration.material'].browse(material_id)
        material.write(kwargs)
        return material.read()

    @http.route('/material_registration/material/<int:material_id>', auth='public', methods=['DELETE'])
    def delete_material(self, material_id):
        material = request.env['material_registration.material'].browse(material_id)
        material.unlink()
        return {'status': 'success'}