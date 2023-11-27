from MobilenetUnet import MobileNetV1
<<<<<<< HEAD
from MobilenetUnetV2 import MobileNetV2
from Unet import Unet
from ImageTreatments import print_max_predictions, ContaFrutos, saida_contagem, image_equilize
    
def main():
    model = MobileNetV1()
    
    model.load_weights('D:/Pimenta/Pimenta_codigo/github/models/MobUnet/MobileUnet.h5')

    image = '16_20_png_jpg.rf.298ab01077563147ac40c0fc28b2eefd'

    imageDirectory = f'D:/Pimenta/Pimenta_dataset/ImagensTreinoTeste/test/imagens/{image}.jpg'

    image = image_equilize(imageDirectory)

    pred = model.predict(image)
    
    pred=print_max_predictions(pred)

    contagem = ContaFrutos(pred)

    saida_contagem(contagem)
    
=======
import cv2
import numpy as np
import json


#chamar essa função na saida da rede neural
def ContaFrutos(pred):
    count_fruits = [0,0,0]
    unique, counts = np.unique(pred, return_counts=True)
    print(unique,counts)
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

def print_max_predictions(predictions):

    predictions = np.argmax(predictions, axis=-1)
    #predictions = cv2.resize(predictions, (224, 224)).astype(np.uint8)
    
    #predictions.flatten().tolist()
    
    return predictions

def saida_contagem(lista_frutos):
    file = "contagem_frutos.txt"
    frutos = {}
    frutos['Verdes'] = lista_frutos[2]
    frutos['Amadurecendo'] = lista_frutos[0]
    frutos['Maduros'] = lista_frutos[1]

    with open(file, "w") as arquivo:
        json.dump(frutos, arquivo)
    print(f"O dicionário foi salvo em {file}")

    
def main():
    model = MobileNetV1()
    model.load_weights('D:/Pimenta/Pimenta_modelos/MobUnet/MobileUnet.h5')

    imagem = '4_jpg.rf.50b4513640bdd96ec86921b9a71aa393'

    entrada_img = f'D:/Pimenta/Pimenta_dataset/ImagensTreinoTeste/test/imagens/{imagem}.jpg'

    imagem = cv2.imread(entrada_img,3)

    pred = model.predict(imagem[np.newaxis, :, :])

    pred=print_max_predictions(pred[0])
    
    pred = pred.astype(np.uint8)
    
    contagem = ContaFrutos(pred)
    
    saida_contagem(contagem)

>>>>>>> 3ed48ab6e367a8731da479fb24df74c18c6df10d
if __name__ == "__main__":
    main()