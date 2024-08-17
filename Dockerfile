# Usando uma imagem oficial do Python como base
FROM python:3.9-slim

# Configurar o fuso horário (exemplo para São Paulo, Brasil)
ENV TZ=America/Sao_Paulo
RUN apt-get update && apt-get install -y tzdata && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone && \
    dpkg-reconfigure -f noninteractive tzdata

# Definindo o diretório de trabalho dentro do container
WORKDIR /app

# Copiando os arquivos de requisitos e instalando dependências
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiando o código da aplicação
COPY . .

# Criando o diretório de chaves
RUN mkdir -p /app/keys

# Expondo a porta em que a aplicação irá rodar
EXPOSE 5000

# Definindo a variável de ambiente para desenvolvimento
ENV FLASK_ENV=development

# Comando para iniciar a aplicação
CMD ["python", "app.py"]

