FROM python:3.11-slim

# Define o diretório de trabalho
WORKDIR /app


COPY . .

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta 5000
EXPOSE 5000

# Comando para iniciar a aplicação
CMD ["python", "app.py"]
