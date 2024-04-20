import cv2

def pos_add(p1, p2):
    return (p1[0] + p2[0], p1[1] + p2[1])

def squared_dist(p1, p2):
    return ((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2)

def collision_point_rect(point, rect):
    if (point[0] > rect.x and point[0] < rect.x + rect.width and
        point[1] > rect.y and point[1] < rect.y + rect.height):
        return True
    return False

def modify_images(img): # AINDA NÃO ESTÁ SENDO UTILIZADA
    # Função usada para modificar os dados na coleta de dados 
    # e também para a imagem para prever.

    # 1. Crop (para deixar o número mais centralizado e maior)
    shrink = True
    cropped = img
    while shrink:
        cropped = cropped[1:-1, 0:-1]
        # Vê se tocou no desenho
        for i in range(len(cropped)):
            if cropped[0][i] == 0 or cropped[i][0] == 0:
                shrink = False
    # Canto superior direito
    shrink = True
    while shrink:
        cropped = cropped[1:-1, 0:-2]
        # Vê se tocou no desenho
        for i in range(len(cropped)):
            if cropped[0][i] == 0 or cropped[i][-1] == 0:
                shrink = False
    # Canto inferior esquerdo
    shrink = True
    while shrink:
        cropped = cropped[0:-2, 1:-1]
        for i in range(len(cropped)):
            if cropped[-1][i] == 0 or cropped[i][0] == 0:
                shrink = False
    shrink = True
    while shrink:
        cropped = cropped[0:-2, 0:-2]
        for i in range(len(cropped)):
            if cropped[-1][i] == 0 or cropped[i][-1] == 0:
                shrink = False
    
    # 2. Resize (Compromisso entre qualidade e quantidade de parâmetros)
    cropped = cv2.resize(cropped, (50, 50))

    # 3. Threshold (Trocar a cor do fundo, para o fundo ser 0)
    _, cropped = cv2.threshold(cropped, 127, 255, cv2.THRESH_BINARY_INV)

    return cropped
