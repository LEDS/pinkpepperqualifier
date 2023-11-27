import numpy as np
import tensorflow as tf
import cv2
import json

def ContaFrutos(pred):
    count_fruits = [0,0,0]
    unique, counts = np.unique(pred, return_counts=True)
    unique = unique[1:]
    for i in unique:
        
        matriz = np.where(pred != i, 0, pred)#colocar um for para percorrer cada um dos valores ate contar todos
        unique, counts = np.unique(matriz, return_counts=True)
        thresh = cv2.adaptiveThreshold(matriz+255, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 255, 19)
        thresh = cv2.bitwise_not(thresh)
        
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(7,7))
        img_dilation = cv2.dilate(thresh, kernel, iterations=1)

        
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(7,7))
        img_erode = cv2.erode(img_dilation,kernel, iterations=1)
        img_erode = cv2.medianBlur(img_erode, 3)
        
        ret, labels = cv2.connectedComponents(img_erode)
        label_hue = np.uint8(179 * labels / np.max(labels))
        blank_ch = 255 * np.ones_like(label_hue)
        labeled_img = cv2.merge([label_hue, blank_ch, blank_ch])
        labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_HSV2BGR)
        labeled_img[label_hue == 0] = 0
        if(i == 1):
            count_fruits[i-1] = ret-1
        elif(i == 2):
            count_fruits[i-1] = ret-1
        elif(i == 3):
            count_fruits[i-1] = ret-1
    return count_fruits

def print_max_predictions(pred):

    pred = np.argmax(pred[0], axis=-1)
    pred = pred.astype(np.uint8)

    return pred

def saida_contagem(lista_frutos):
    file = "contagem_frutos.txt"
    frutos = {}
    frutos['Verdes'] = lista_frutos[2]
    frutos['Amadurecendo'] = lista_frutos[0]
    frutos['Maduros'] = lista_frutos[1]

    with open(file, "w") as arquivo:
        json.dump(frutos, arquivo)
    print(f"O dicionário foi salvo em {file}")

def image_equilize(directory):

    image = cv2.imread(directory,3)    
    image[0] = cv2.equalizeHist(image[0])
    image[1] = cv2.equalizeHist(image[1])
    image[2] = cv2.equalizeHist(image[2])

    return image[np.newaxis, :, :]