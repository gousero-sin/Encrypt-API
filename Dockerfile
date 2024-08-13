# Usando uma imagem oficial do Python como base
FROM python:3.9-slim

# Definindo o diretório de trabalho dentro do container
WORKDIR /app

# Copiando os arquivos de requisitos e instalando dependências
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiando o código da aplicação
COPY . .

# Expondo a porta em que a aplicação irá rodar
EXPOSE 5000

# Comando para iniciar a aplicação
CMD ["python", "app.py"]
