import cv2
from skimage.transform import resize
import numpy as np
def main():
    imagem = '4_jpg.rf.50b4513640bdd96ec86921b9a71aa393'

    entrada_img = 'D:/Pimenta_dataset/dataset/test/imagens/'+ imagem+'.jpg'

    foto_imagem = cv2.imread(entrada_img,3)

    foto_imagem = resize(foto_imagem, (512, 512),mode='constant', preserve_range=False)

    cv2.imshow("Image", foto_imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()