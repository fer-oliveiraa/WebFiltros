from PIL import Image, ImageOps, ImageFilter

def aplicar_filtro(caminho, filtro):
    imagem = Image.open(caminho)

    if filtro == 'negativo':
        return ImageOps.invert(imagem.convert('RGB'))

    elif filtro == 'mediana':
        return imagem.filter(ImageFilter.MedianFilter(size=3))

    elif filtro == 'gaussiano':
        return imagem.filter(ImageFilter.GaussianBlur(radius=2))

    elif filtro == 'pretoebranco':
        imagem_pb = imagem.convert('L')
        limiar = 128  # Define threshold para binarização
        return imagem_pb.point(lambda p: 255 if p > limiar else 0)

    else:
        # Se filtro não é reconhecido, retorna a imagem original sem alterações
        return imagem
