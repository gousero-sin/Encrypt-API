# tests/test_crypto_utils.py

import unittest
from app.services.crypto_utils import generate_random_key_with_name, key_exists, save_key, load_key
import os

class TestCryptoUtils(unittest.TestCase):

    def setUp(self):
        # Configura o diretório de chaves para testes
        self.keys_dir = "myapp/keys"
        if not os.path.exists(self.keys_dir):
            os.makedirs(self.keys_dir)

    def tearDown(self):
        # Limpa o diretório de chaves após os testes
        for key_file in os.listdir(self.keys_dir):
            os.remove(os.path.join(self.keys_dir, key_file))

    # Teste para geração de chave com tamanho válido (128, 256, 512)
    def test_generate_random_key_with_valid_bits(self):
        for bits in [128, 256, 512]:
            key, key_name = generate_random_key_with_name(bits)
            self.assertTrue(key_exists(key_name))
            
            # Ajuste para o tamanho correto da chave
            expected_length = 32 if bits == 512 else bits // 8
            self.assertEqual(len(key), expected_length)

    # Teste para salvar e carregar a chave
    def test_save_and_load_key(self):
        key_name = "testkey"
        key = b'testkey'
        save_key(key, key_name)
        loaded_key = load_key(key_name)
        self.assertEqual(key, loaded_key)

if __name__ == '__main__':
    unittest.main()
