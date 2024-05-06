import pickle
import cv2
import numpy as np
import matplotlib.pyplot as plt

from . import utility

class ClassifierModel:
    def __init__(self, path_to_pickled_model):
        # Carrega o modelo pré-treinado
        with open(path_to_pickled_model, 'rb') as f:
            self.model = pickle.load(f)
        
    def predict(self, file_to_jpeg):
        # Lê a imagem
        image = cv2.imread(file_to_jpeg, cv2.IMREAD_GRAYSCALE)
        
        # Processa a imagem para poder utilizá-la no modelo
        image = utility.modify_images(image)

        # # Mostra a imagem para propósitos de debugging
        # plt.imshow(image, cmap='gray')
        # plt.show()

        image = np.reshape(image, (1, -1))

        # Faz a classificação
        return self.model.predict(image)  

if __name__ == "__main__":
    cm = ClassifierModel("adivinha.pkl")
    print(cm.predict("data/to_predict.jpg"))
