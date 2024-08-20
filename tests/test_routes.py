# tests/test_routes.py
import os
import unittest
from app import create_app
from app.services.crypto_utils import save_key

class TestRoutes(unittest.TestCase):

    def setUp(self):
        self.app = create_app('TestingConfig')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

        # Salva uma chave de teste com um tamanho válido para AES (32 bytes = 256 bits)
        key = os.urandom(32)  # 32 bytes = 256 bits
        save_key(key, 'testkey')

    def tearDown(self):
        self.app_context.pop()

    def test_encrypt_with_existing_key(self):
        response = self.client.post('/encrypt', json={
            'data': 'hello world',
            'key': 'testkey'
        })

        # Verifique se o status code é 200
        self.assertEqual(response.status_code, 200, msg=f"Erro: {response.get_json().get('msg', '')}")
        
        # Verifique se 'encrypted_data' está presente na resposta
        encrypted_data = response.get_json().get('encrypted_data')
        self.assertIsNotNone(encrypted_data, "Criptografia falhou, 'encrypted_data' é None")

    def test_decrypt_with_existing_key(self):
        # Primeiro, criptografamos os dados
        encrypt_response = self.client.post('/encrypt', json={
            'data': 'hello world',
            'key': 'testkey'
        })

        # Verifique se a criptografia foi bem-sucedida
        self.assertEqual(encrypt_response.status_code, 200, msg=f"Erro na criptografia: {encrypt_response.get_json().get('msg', '')}")
        encrypted_data = encrypt_response.get_json().get('encrypted_data')
        self.assertIsNotNone(encrypted_data, "Criptografia falhou, 'encrypted_data' é None")
        
        # Tentamos descriptografar os dados usando a chave
        decrypt_response = self.client.post('/decrypt', json={
            'encrypted_data': encrypted_data,
            'key': 'testkey'
        })
        self.assertEqual(decrypt_response.status_code, 200)
        self.assertEqual(decrypt_response.get_json()['decrypted_data'], "hello world")

if __name__ == '__main__':
    unittest.main()
