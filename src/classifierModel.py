import pickle
import cv2
import numpy as np
import matplotlib.pyplot as plt

class ClassifierModel:
    def __init__(self, path_to_pickled_model):
        # Carrega o modelo pré-treinado
        with open(path_to_pickled_model, 'rb') as f:
            self.model = pickle.load(f)
        
    def predict(self, file_to_jpeg):
        # Processa a imagem para poder utilizá-la no modelo
        image = cv2.imread(file_to_jpeg, cv2.IMREAD_GRAYSCALE)
        
        image = cv2.resize(image, (16, 16))
        _, image = cv2.threshold(image, 127, 1, cv2.THRESH_BINARY_INV)
        
        # Deixa ela unidimensional
        image = np.reshape(image, (1, -1))

        # Faz a classificação
        return self.model.predict(image)  

if __name__ == "__main__":
    cm = ClassifierModel("adivinha.pkl")
    print(cm.predict("data/to_predict.jpg"))
