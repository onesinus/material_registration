import json


from datetime import datetime
from odoo import http
from odoo.http import request, Response

from ..utils.auth_utils import authenticate


class MaterialController(http.Controller):
    @http.route('/material_registration/materials', auth='public', methods=['GET'])
    # @authenticate
    def get_materials(self, material_type=None):
        domain = [('material_type', '=', material_type)] if material_type else []
        materials = request.env['material_registration.material'].search(domain)
        
        material_data = []
        for material in materials:
            material_data.append({
                'id': material.id,
                'material_code': material.material_code,
                'material_name': material.material_name,
                'material_type': material.material_type,
                'material_buy_price': material.material_buy_price,
                'related_supplier': material.related_supplier.name,
                # Add other fields as needed
            })

        return Response(json.dumps(material_data), content_type='application/json')

    @http.route('/material_registration/material/<int:material_id>', auth='public', methods=['GET'])
    def get_material(self, material_id):
        material = request.env['material_registration.material'].browse(material_id)
        
        # Serialize datetime objects to strings using a custom function
        def custom_serializer(obj):
            if isinstance(obj, datetime):
                return obj.strftime('%Y-%m-%d %H:%M:%S')
            raise TypeError(f'Type {type(obj)} not serializable')

        # Use custom_serializer for serialization
        material_data = json.dumps(material.read(), default=custom_serializer)
        
        return Response(material_data, content_type='application/json')

    @http.route('/material_registration/material', auth='public', methods=['POST'], csrf=False)
    def create_material(self, **kwargs):
        try:
            request_data = json.loads(request.httprequest.data.decode('utf-8'))

            material_code = request_data.get('material_code')
            material_name = request_data.get('material_name')
            material_type = request_data.get('material_type')
            material_buy_price = request_data.get('material_buy_price')
            supplier_id = request_data.get('supplier_id')

            if not all([material_code, material_name, material_type, material_buy_price, supplier_id]):
                return Response("Bad Request: Missing required parameters", status=400)

            material = request.env['material_registration.material'].create({
                'material_code': material_code,
                'material_name': material_name,
                'material_type': material_type,
                'material_buy_price': material_buy_price,
                'related_supplier': int(supplier_id),
            })

            return Response(json.dumps(material.read()), content_type='application/json')

        except Exception as e:
            return Response(f"There is an error occured: {str(e)}", status=400)

    @http.route('/material_registration/material/<int:material_id>', auth='public', methods=['PUT'])
    def update_material(self, material_id, **kwargs):
        material = request.env['material_registration.material'].browse(material_id)
        material.write(kwargs)
        return Response(json.dumps(material.read()), content_type='application/json')

    @http.route('/material_registration/material/<int:material_id>', auth='public', methods=['DELETE'])
    def delete_material(self, material_id):
        material = request.env['material_registration.material'].browse(material_id)
        material.unlink()
        return {'status': 'success'}