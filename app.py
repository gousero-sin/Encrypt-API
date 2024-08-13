from flask import Flask, request, jsonify
from cryptography.fernet import Fernet
import os
from datetime import datetime

app = Flask(__name__)

# Função para gerar uma chave de criptografia única com nome baseado na data e hora
def generate_random_key_with_name():
    encryption_key = Fernet.generate_key()
    key_name = datetime.now().strftime("%Y%m%d_%H%M%S")
    return encryption_key, key_name

# Rota para criptografar dados, usando uma chave específica se fornecida ou gerando uma nova
@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.json.get('data')
    key_name = request.json.get('key')
    
    if not data:
        return jsonify({"msg": "No data provided"}), 400

    try:
        if key_name:
            # Se uma chave for fornecida, tente carregar a chave do arquivo
            try:
                with open(f"keys/{key_name}.key", "rb") as key_file:
                    encryption_key = key_file.read()
            except FileNotFoundError:
                return jsonify({"msg": "Key not found"}), 404
        else:
            # Se nenhuma chave for fornecida, gera uma nova chave
            encryption_key, key_name = generate_random_key_with_name()
            if not os.path.exists('keys'):
                os.makedirs('keys')
            with open(f"keys/{key_name}.key", "wb") as key_file:
                key_file.write(encryption_key)

        # Criptografa os dados
        fernet = Fernet(encryption_key)
        encrypted_data = fernet.encrypt(data.encode())

        # Retorna os dados criptografados, a chave usada e o nome da chave
        return jsonify({
            "encrypted_data": encrypted_data.decode(),
            "key_name": key_name
        }), 200

    except Exception as e:
        return jsonify({"msg": str(e)}), 500

# Rota para descriptografar dados usando uma chave específica
@app.route('/decrypt', methods=['POST'])
def decrypt():
    encrypted_data = request.json.get('encrypted_data')
    key_name = request.json.get('key')

    if not encrypted_data:
        return jsonify({"msg": "No encrypted data provided"}), 400

    if not key_name:
        return jsonify({"msg": "No key name provided"}), 400

    try:
        # Carrega a chave do arquivo correspondente
        with open(f"keys/{key_name}.key", "rb") as key_file:
            encryption_key = key_file.read()

        # Usa a chave para descriptografar os dados
        fernet = Fernet(encryption_key)
        decrypted_data = fernet.decrypt(encrypted_data.encode()).decode()
        return jsonify({"decrypted_data": decrypted_data}), 200
    except FileNotFoundError:
        return jsonify({"msg": "Key file not found"}), 404
    except Exception as e:
        return jsonify({"msg": str(e)}), 400

# Rota para gerar e armazenar uma chave com um nome específico
@app.route('/generate_key', methods=['POST'])
def generate_key():
    key_name = request.json.get('key_name')
    if not key_name:
        # Gera uma nova chave com nome baseado na data e hora
        encryption_key, key_name = generate_random_key_with_name()
    else:
        encryption_key = Fernet.generate_key()

    # Armazenamento da chave em um arquivo
    if not os.path.exists('keys'):
        os.makedirs('keys')
    with open(f"keys/{key_name}.key", "wb") as key_file:
        key_file.write(encryption_key)

    return jsonify({"msg": f"Key '{key_name}' generated successfully!"}), 200

if __name__ == '__main__':
    if not os.path.exists('keys'):
        os.makedirs('keys')
    app.run(host='0.0.0.0', port=5000, debug=True)
