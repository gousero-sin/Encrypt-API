# myapp/app/config.py

import os

class Config:
    """Configurações base, comuns a todos os ambientes."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DEBUG = False
    TESTING = False
    # Outras configurações globais podem ser adicionadas aqui

class DevelopmentConfig(Config):
    """Configurações usadas durante o desenvolvimento."""
    DEBUG = True
    FLASK_ENV = 'development'
    # Configurações específicas para o ambiente de desenvolvimento podem ser adicionadas aqui

class TestingConfig(Config):
    """Configurações usadas durante os testes."""
    TESTING = True
    FLASK_ENV = 'testing'
    # Configurações específicas para o ambiente de testes podem ser adicionadas aqui

class ProductionConfig(Config):
    """Configurações usadas em produção."""
    FLASK_ENV = 'production'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # Configurações específicas para o ambiente de produção podem ser adicionadas aqui
