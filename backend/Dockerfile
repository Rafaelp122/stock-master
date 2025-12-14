# Usa uma imagem leve do Python 3.11
FROM python:3.11-slim

# Evita que o Python crie arquivos .pyc e bufferize logs
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Define a pasta de trabalho dentro do container
WORKDIR /app

# Instala dependências do sistema necessárias para o PostgreSQL
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Instala as dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o projeto para dentro do container
COPY . .