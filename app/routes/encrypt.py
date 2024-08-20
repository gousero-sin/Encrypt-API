# app/routes/encrypt_routes.py

from flask import Blueprint, request, jsonify
from app.services.crypto_utils import (
    generate_random_key_with_name, 
    encrypt_data,
    key_exists,  # Verifica se a chave existe
    load_key     # Carrega uma chave existente
)

# Inicializa o blueprint para as rotas de criptografia
encrypt_bp = Blueprint('encrypt', __name__)

@encrypt_bp.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.json.get('data')
    bits = request.json.get('bits', 128)  # Padrão para 128 bits
    key_name = request.json.get('key')    # Nome da chave opcional
    
    if not data:
        return jsonify({"msg": "No data provided"}), 400

    try:
        bits = int(bits)
        
        if key_name:
            if key_exists(key_name):
                # Se a chave existe, carregue-a
                key = load_key(key_name)
            else:
                # Se a chave não existir, retorne um erro 404
                return jsonify({"msg": "Key not found"}), 404
        else:
            # Se nenhuma chave for fornecida, gere uma nova
            key, key_name = generate_random_key_with_name(bits)
        
        encrypted_data = encrypt_data(data, key)

        return jsonify({
            "encrypted_data": encrypted_data.hex(),
            "key_name": key_name,
            "bits": bits
        }), 200

    except ValueError as e:
        return jsonify({"msg": str(e)}), 400
    except Exception as e:
        return jsonify({"msg": str(e)}), 500
