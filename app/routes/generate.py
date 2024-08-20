# app/routes/generate.py

from flask import Blueprint, request, jsonify
from app.services.crypto_utils import generate_random_key_with_name, save_key, key_exists

generate_bp = Blueprint('generate', __name__)

@generate_bp.route('/generate-key', methods=['POST'])
def generate_key():
    key_name = request.json.get('key_name')
    bits = request.json.get('bits', 128)  # Padrão para 128 bits

    bits = int(bits)

    if not key_name:
        return jsonify({"msg": "Key name is required"}), 400

    if key_exists(key_name):
        return jsonify({"msg": "Key with this name already exists"}), 400

    try:
        # Gera a chave usando o número de bits especificado
        key, _ = generate_random_key_with_name(bits)
        save_key(key, key_name)
        return jsonify({"msg": f"Key '{key_name}' generated successfully!"}), 200

    except ValueError as e:
        return jsonify({"msg": str(e)}), 400
    except Exception as e:
        return jsonify({"msg": str(e)}), 500
    