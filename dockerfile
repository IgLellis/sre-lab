# Imagem base oficial do Python
FROM python:3.12-slim

# Diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos para dentro do container
COPY requirements.txt .

# Instala dependências
RUN apt-get update && apt-get install -y curl
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante da aplicação
COPY . .

# Expor porta da aplicação
EXPOSE 8000

# Comando para iniciar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]