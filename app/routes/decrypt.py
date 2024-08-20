# app/routes/decrypt_routes.py

from flask import Blueprint, request, jsonify
from app.services.crypto_utils import decrypt_data, key_exists, load_key
import binascii

# Inicializa o blueprint para as rotas de descriptografia
decrypt_bp = Blueprint('decrypt', __name__)

@decrypt_bp.route('/decrypt', methods=['POST'])
def decrypt():
    encrypted_data_hex = request.json.get('encrypted_data')
    key_name = request.json.get('key')

    if not encrypted_data_hex:
        return jsonify({"msg": "No encrypted data provided"}), 400

    if not key_name:
        return jsonify({"msg": "No key name provided"}), 400

    try:
        # Verifica se a chave existe
        if not key_exists(key_name):
            return jsonify({"msg": "Key not found"}), 404

        # Carrega a chave correspondente
        encryption_key = load_key(key_name)

        # Converte o dado criptografado de volta de hexadecimal para bytes
        encrypted_data = binascii.unhexlify(encrypted_data_hex)

        # Usa a chave para descriptografar os dados
        decrypted_data = decrypt_data(encrypted_data, encryption_key)
        
        return jsonify({"decrypted_data": decrypted_data}), 200
    
    except binascii.Error:
        return jsonify({"msg": "Invalid encrypted data format"}), 400
    except Exception as e:
        return jsonify({"msg": str(e)}), 500
