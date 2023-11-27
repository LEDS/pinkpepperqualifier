from MobilenetUnet import MobileNetV1
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
    
if __name__ == "__main__":
    main()