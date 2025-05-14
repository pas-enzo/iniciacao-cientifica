import cv2
import numpy as np

# Função para recortar baseado no conteúdo
def crop_radiografia(imagem_path, margem=20, tamanho_saida=(512, 512)):
    # Ler a imagem
    imagem = cv2.imread(imagem_path, cv2.IMREAD_GRAYSCALE)
    
    # Aplicar suavização para reduzir ruído
    imagem_suavizada = cv2.GaussianBlur(imagem, (5, 5), 0)
    
    # Limiarização adaptativa para binarizar a imagem
    _, thresh = cv2.threshold(imagem_suavizada, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Encontrar contornos
    contornos, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Encontrar o maior contorno (assumindo que é a região de interesse)
    maior_contorno = max(contornos, key=cv2.contourArea)
    
    # Obter o retângulo delimitador
    x, y, w, h = cv2.boundingRect(maior_contorno)
    
    # Adicionar margem ao redor da região
    x = max(x - margem, 0)
    y = max(y - margem, 0)
    w = min(w + 2 * margem, imagem.shape[1] - x)
    h = min(h + 2 * margem, imagem.shape[0] - y)
    
    # Centralizar a região
    centro_x, centro_y = x + w // 2, y + h // 2
    novo_x = max(centro_x - tamanho_saida[0] // 2, 0)
    novo_y = max(centro_y - tamanho_saida[1] // 2, 0)
    
    # Garantir que o recorte não ultrapasse os limites da imagem
    novo_x2 = min(novo_x + tamanho_saida[0], imagem.shape[1])
    novo_y2 = min(novo_y + tamanho_saida[1], imagem.shape[0])
    novo_x = novo_x2 - tamanho_saida[0]
    novo_y = novo_y2 - tamanho_saida[1]
    
    # Recortar a imagem
    imagem_recortada = imagem[novo_y:novo_y2, novo_x:novo_x2]
    
    # Redimensionar para o tamanho desejado (se necessário)
    imagem_recortada = cv2.resize(imagem_recortada, tamanho_saida, interpolation=cv2.INTER_AREA)
    
    return imagem_recortada

# Exemplo de uso
imagem_path = 'radiografia.png'  # Substitua pelo caminho da sua imagem
imagem_recortada = crop_radiografia(imagem_path)

# Salvar ou exibir o resultado
cv2.imwrite('radiografia_recortada.png', imagem_recortada)
cv2.imshow('Imagem Recortada', imagem_recortada)
cv2.waitKey(0)
cv2.destroyAllWindows()