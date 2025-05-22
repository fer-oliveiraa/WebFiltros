from flask import Flask, render_template, request
from filtros import aplicar_filtro  # Importa função que aplica filtros às imagens
from PIL import Image
import os
import uuid  # Para gerar nomes únicos para os arquivos

app = Flask(__name__)

# Define as pastas onde as imagens serão salvas
UPLOAD_FOLDER = 'static/uploads'
PROCESSED_FOLDER = 'static/processed'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER

# Garante que as pastas de upload e processed existem (cria caso não existam)
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    imagem_original = None
    imagem_processada = None

    if request.method == "POST":
        filtro = request.form["filtro"]  
        imagem_salva = request.form.get("imagem_salva")  
        imagem = request.files.get("imagem")  # Pega a imagem enviada pelo usuário

        if imagem:
           
            nome_arquivo = str(uuid.uuid4()) + os.path.splitext(imagem.filename)[1]  
            caminho_imagem = os.path.join(app.config['UPLOAD_FOLDER'], nome_arquivo)
            imagem.save(caminho_imagem)  # Salva imagem na pasta uploads
        elif imagem_salva:
           
            caminho_imagem = imagem_salva.strip('/') 
            nome_arquivo = os.path.basename(caminho_imagem)
        else:
            
            return render_template("index.html")

        
        imagem_saida = os.path.join(app.config['PROCESSED_FOLDER'], nome_arquivo)

        # Aplica o filtro selecionado e salva a imagem processada
        imagem_resultado = aplicar_filtro(caminho_imagem, filtro)
        imagem_resultado.save(imagem_saida)

        
        imagem_original = "/" + caminho_imagem.replace("\\", "/")
        imagem_processada = "/" + imagem_saida.replace("\\", "/")

        # Renderiza a página mostrando as imagens original e processada
        return render_template("index.html",
                               imagem_oficial=imagem_original,
                               original=imagem_original,
                               processed=imagem_processada)

    # Para requisições GET, apenas renderiza o formulário vazio
    return render_template("index.html")


if __name__ == "__main__":
    print("Servidor iniciado em http://127.0.0.1:5000")
    app.run(debug=True, host="0.0.0.0")
