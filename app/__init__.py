# app/__init__.py

from flask import Flask
from .config import DevelopmentConfig, ProductionConfig, TestingConfig

def create_app(config_name='DevelopmentConfig'):
    app = Flask(__name__)
    
    # Configuração da aplicação baseada no ambiente
    if config_name == 'ProductionConfig':
        app.config.from_object(ProductionConfig)
    elif config_name == 'TestingConfig':
        app.config.from_object(TestingConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    # Registro de blueprints (rotas)
    from .routes.encrypt import encrypt_bp
    from .routes.decrypt import decrypt_bp
    from .routes.generate import generate_bp
    app.register_blueprint(encrypt_bp)
    app.register_blueprint(decrypt_bp)
    app.register_blueprint(generate_bp)

    return app
