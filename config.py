# myapp/config.py

import os
from pathlib import Path

# Define a raiz do projeto
BASE_DIR = Path(__file__).resolve().parent

# Configuração global de logs
LOG_DIR = BASE_DIR / "logs"
if not LOG_DIR.exists():
    LOG_DIR.mkdir(parents=True)

# Configuração de logs
LOG_FILE = LOG_DIR / "myapp.log"
LOG_LEVEL = os.environ.get('LOG_LEVEL', 'DEBUG')  # Padrão: DEBUG

# Outras variáveis globais
SECRET_KEY = os.environ.get('SECRET_KEY', 'you-will-never-guess')
API_URL = os.environ.get('API_URL', 'https://api.example.com')

# Adicione outras configurações globais aqui
