# Usa uma imagem base oficial do Python
FROM python:3.9-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Instala utilitários necessários e configura o timezone para GMT-3 (América/Sao_Paulo)
RUN apt-get update && \
    apt-get install -y tzdata && \
    ln -fs /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata && \
    apt-get clean

# Copia o arquivo requirements.txt para o contêiner
COPY requirements.txt .

# Instala as dependências necessárias
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código da aplicação para o contêiner
COPY . .

# Expõe a porta em que a aplicação será executada
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "wsgi.py"]
