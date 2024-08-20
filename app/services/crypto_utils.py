from datetime import datetime
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding, hashes
from cryptography.hazmat.backends import default_backend
import os
import pytz

KEYS_DIR = "myapp/keys"

def generate_random_key_with_name(bits=128):
    if bits not in [128, 256, 512]:
        raise ValueError("Invalid key size. Supported sizes are 128, 256, and 512 bits.")
    
    if bits == 512:
        key = os.urandom(64)
        digest = hashes.Hash(hashes.SHA512(), backend=default_backend())
        digest.update(key)
        key = digest.finalize()[:32]  # Trunca para 32 bytes (256 bits) após o SHA-512
    else:
        key = os.urandom(bits // 8)
    
    key_name = datetime.now().strftime("%Y%m%d_%H%M%S")
    save_key(key, key_name)
    return key, key_name

def encrypt_data(data, key):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data.encode()) + padder.finalize()

    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    return iv + encrypted_data

def decrypt_data(encrypted_data, key):
    iv = encrypted_data[:16]
    encrypted_data_bytes = encrypted_data[16:]

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    decrypted_padded_data = decryptor.update(encrypted_data_bytes) + decryptor.finalize()

    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    decrypted_data = unpadder.update(decrypted_padded_data) + unpadder.finalize()

    return decrypted_data.decode()

def key_exists(key_name):
    """Verifica se a chave com o nome fornecido existe no diretório 'keys'."""
    key_path = os.path.join(KEYS_DIR, f"{key_name}.key")
    return os.path.exists(key_path)

def load_key(key_name):
    """Carrega a chave do diretório 'keys'."""
    key_path = os.path.join(KEYS_DIR, f"{key_name}.key")
    with open(key_path, "rb") as key_file:
        return key_file.read()

def save_key(key, key_name):
    """Salva a chave no diretório 'keys'."""
    if not os.path.exists(KEYS_DIR):
        os.makedirs(KEYS_DIR)
    key_path = os.path.join(KEYS_DIR, f"{key_name}.key")
    with open(key_path, "wb") as key_file:
        key_file.write(key)
