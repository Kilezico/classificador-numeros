import cv2
import numpy as np
import matplotlib.pyplot as plt

class dataStorer:
    def __init__(self):
        pass

# imagem = cv2.imread("data/to_predict.jpg", cv2.IMREAD_GRAYSCALE)


with open("data/data.bin", 'rb') as data:
    imagem = np.frombuffer(data.read(), dtype='uint8').reshape((400, 400))

plt.imshow(imagem, cmap=plt.cm.gray_r)
plt.show()
