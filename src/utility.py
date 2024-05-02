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
    # Imagens recebidas serão exclusivamente quadradas e em grayscale

    
    # 1. Threshold (Imagem binária: fundo=0; tinta=1)
    _, new_img = cv2.threshold(img, 127, 1, cv2.THRESH_BINARY_INV)

    # 2. Crop (para deixar o número mais centralizado e maior)
    # 2.1 Canto superior esquerdo
    shrink = True
    while shrink:
        # Vê se tocou no desenho
        for i in range(len(new_img)):
            if new_img[0][i] == 1 or new_img[i][0] == 1:
                shrink = False
        # Diminui
        if shrink:
            new_img = new_img[1:, 1:]
    # 2.2 Canto superior direito
    shrink = True
    while shrink:
        # Vê se tocou no desenho
        for i in range(len(new_img)):
            if new_img[0][i] == 1 or new_img[i][-1] == 1:
                shrink = False
        # Diminui
        if shrink:
            new_img = new_img[1:, :-1] # -1 no topo, -1 da direita 
    # 2.3 Canto inferior esquerdo
    shrink = True
    while shrink:
        for i in range(len(new_img)):
            if new_img[-1][i] == 1 or new_img[i][0] == 1:
                shrink = False
        if shrink:
            new_img = new_img[:-1, 1:]
    # 2.4 Canto inferior direito
    shrink = True
    while shrink:
        for i in range(len(new_img)):
            if new_img[-1][i] == 1 or new_img[i][-1] == 1:
                shrink = False
        if shrink:
            new_img = new_img[:-1, :-1]
    
    # 3. Resize (Para o treino não ser muito demorado, mas ainda ser possível
    #            identificar os números).
    new_img = cv2.resize(new_img, (50, 50), interpolation=cv2.INTER_CUBIC)

    return new_img
