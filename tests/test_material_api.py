import requests
import json
from odoo.tests import HttpCase

class TestMaterialAPI(HttpCase):

    def setUp(self):
        super(TestMaterialAPI, self).setUp()
        self.base_url = 'http://localhost:8069'
        self.auth_token = '5c5a50d2-a7b6-4a95-8492-8b06139e3e7f' # Change this to a valid token
        self.session_id = self.authenticate()

    def authenticate(self):
        url = f'{self.base_url}/web/session/authenticate'
        headers = {'Content-Type': 'application/json'}
        data = {
            "jsonrpc": "2.0",
            "method": "call",
            "params": {},
            "id": 1,
            "method": "login",
            "params": {
                "db": "admin", # change this to true db name
                "login": "admin", # change this to username
                "password": "admin" # change this to password
            }
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
        return response.cookies.get('session_id')

    def test_get_materials(self):
        url = f'{self.base_url}/material_registration/materials'
        headers = {'Authorization': self.auth_token, 'Cookie': f'session_id={self.session_id}'}
        response = requests.get(url, headers=headers)
        self.assertEqual(response.status_code, 200)


    def test_get_material_by_id(self):
        material_id = 1
        url = f'{self.base_url}/material_registration/material/{material_id}'
        headers = {'Authorization': self.auth_token, 'Cookie': f'session_id={self.session_id}'}
        response = requests.get(url, headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_create_material(self):
        url = f'{self.base_url}/material_registration/material'
        headers = {'Authorization': self.auth_token, 'Content-Type': 'application/json', 'Cookie': f'session_id={self.session_id}'}
        data = {
            "material_code": "wkwkw",
            "material_name": "wkwkwk",
            "material_type": "cotton",
            "material_buy_price": 200,
            "supplier_id": 1
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
        self.assertEqual(response.status_code, 200)

    def test_update_material(self):
        material_id = 2
        url = f'{self.base_url}/material_registration/material/{material_id}'
        headers = {'Authorization': self.auth_token, 'Content-Type': 'application/json', 'Cookie': f'session_id={self.session_id}'}
        data = {
            "material_code": "wkwkw",
            "material_name": "wkwkwk",
            "material_type": "cotton",
            "material_buy_price": 200,
            "supplier_id": 1
        }
        response = requests.put(url, headers=headers, data=json.dumps(data))
        self.assertEqual(response.status_code, 200)

    def test_delete_material(self):
        material_id = 1
        url = f'{self.base_url}/material_registration/material/{material_id}'
        headers = {'Authorization': self.auth_token, 'Cookie': f'session_id={self.session_id}'}
        response = requests.delete(url, headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_unauthorized_request(self):
        url = f'{self.base_url}/material_registration/materials'
        response = requests.get(url)
        self.assertEqual(response.status_code, 401)
        self.assertIn('Unauthorized', response.text)
