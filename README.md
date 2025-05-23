# 🖼️ WebFiltros - Plataforma Web de Filtros de Imagem (Computação Gráfica)

Este projeto é uma aplicação web simples que permite ao usuário fazer upload de uma imagem e aplicar diferentes **filtros de Computação Gráfica** utilizando a biblioteca **Pillow (PIL)**.

---

## Funcionalidades

- Upload de imagens `.jpg` ou `.png`
- Aplicação de filtros:
  - Negativo
  - Mediana
  - Gaussiano
  - Preto e Branco (filtro personalizado)
- Exibição lado a lado da imagem original e da processada
- Botão para download da imagem processada
- Pré-visualização da imagem antes de aplicar o filtro
- Estrutura modular do código

---

## Tecnologias e Bibliotecas

- Python 3  
- Flask  
- Pillow (PIL)  
- HTML5 + CSS3  
- JavaScript (para pré-visualização da imagem)  
- Docker e Docker Compose  

---

## Como Executar com Docker

1. Clone o repositório

git clone https://github.com/fer-oliveiraa/WebFiltros.git

2. Construa e execute com Docker Compose

docker-compose up --build

3. Acesse no navegador

http://127.0.0.1:5000

---
