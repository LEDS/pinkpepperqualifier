from tensorflow.keras.layers import GlobalAveragePooling3D, Dense, AveragePooling2D
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Concatenate, Conv2D, MaxPooling2D, UpSampling2D
import tensorflow as tf

def MobileNetV1(input_shape=(224, 224,3), num_classes=4):
    #Definindo as dimensões dos meus dados
    encoder_input = Input(shape=(224, 224,3))
    #importando o modelo base neste caso o MobileNet
    base_model = tf.keras.applications.MobileNet(
                        input_shape=(224,224,3),
                        alpha=1.0,
                        depth_multiplier=1,
                        dropout=0.001,
                        include_top=False,
                        weights="imagenet",
                        input_tensor=encoder_input,
                        pooling=None,
                        classes=num_classes,
                        classifier_activation="softmax")
    #encoder_output é definido com base na camada da rede neural que queremos pegar
    #a mobilenet permite pegar até o conv_pw_13_relu pulando de 2 em 2 nas linhas 
    #que se seguem damos sequencia a essa construção
    #upsampling2d aumenta as dimensões de entrada da proxima camada como esta configurado
    #(2,2) iremos aumentar em 2x em x e y
    
    encoder_output = base_model.get_layer("conv_pw_7_relu").output
    #s = tf.keras.layers.Lambda(lambda x: x / 255) (encoder_output) somente util se declarar os dados como int
    concat1 = tf.keras.layers.BatchNormalization(axis=1)(encoder_output)
    concat1 = tf.keras.layers.Activation('relu')(concat1)
    concat1 = tf.keras.layers.Conv2DTranspose(filters=512, kernel_size=(2, 2), strides=(2, 2), padding='same')(concat1)
    concat1 = tf.keras.layers.Conv2D(512, (3, 3), activation='relu', padding='same')(concat1)
    concat1 = tf.keras.layers.Dropout(0.1)(concat1)
    concat1 = tf.keras.layers.Conv2D(512, (3, 3), activation='relu', padding='same')(concat1)
    concat1 = Concatenate()([base_model.get_layer('conv_pw_5_relu').output, concat1])

    
    concat1 = tf.keras.layers.BatchNormalization(axis=1)(concat1)
    concat1 = tf.keras.layers.Activation('relu')(concat1)
    concat2 = tf.keras.layers.Conv2DTranspose(filters=256, kernel_size=(2, 2), strides=(2, 2), padding='same')(concat1)
    concat2 = tf.keras.layers.Conv2D(256, (3, 3), activation='relu', padding='same')(concat2)
    concat2 = tf.keras.layers.Dropout(0.1)(concat2)
    concat2 = tf.keras.layers.Conv2D(256, (3, 3), activation='relu', padding='same')(concat2)
    concat2 = Concatenate()([base_model.get_layer('conv_pw_3_relu').output, concat2])
    
    
    concat2 = tf.keras.layers.BatchNormalization(axis=1)(concat2)
    concat2 = tf.keras.layers.Activation('relu')(concat2)
    concat3 = tf.keras.layers.Conv2DTranspose(filters=128, kernel_size=(2, 2), strides=(2, 2), padding='same')(concat2)
    concat3 = tf.keras.layers.Conv2D(128, (3, 3), activation='relu', padding='same')(concat3)
    concat3 = tf.keras.layers.Dropout(0.1)(concat3)
    concat3 = tf.keras.layers.Conv2D(128, (3, 3), activation='relu', padding='same')(concat3)
    concat3 = Concatenate()([base_model.get_layer('conv_pw_1_relu').output, concat3])    
    
    
    concat3 = tf.keras.layers.BatchNormalization(axis=1)(concat3)
    concat3 = tf.keras.layers.Activation('relu')(concat3)
    concat4 = tf.keras.layers.Conv2DTranspose(filters=64, kernel_size=(2, 2), strides=(2, 2), padding='same')(concat3)
    concat4 = tf.keras.layers.Conv2D(64, (3, 3), activation='relu', padding='same')(concat4)
    concat4 = tf.keras.layers.Dropout(0.1)(concat4)
    concat4 = tf.keras.layers.Conv2D(64, (3, 3), activation='relu', padding='same')(concat4)
    #No output temos a ativação softmax pois se trata de multiclassficação, caso dossem so 2 podemos utilizar sigmoid
    output = tf.keras.layers.Conv2D(num_classes,kernel_size=(1,1),strides=(1,1),padding="same",activation='softmax')(concat4)
    # Crie o modelo
    model = Model(inputs=encoder_input, outputs=output)

    return model

# Parâmetros do modelo
#input_shape = (image_dimension, image_dimension,3)
#num_classes = 4

# Construa o modelo
#model = MobileNetV1(input_shape=input_shape, num_classes=num_classes)

# Compile o modelo

#preditor = "MobileUnetV1"
#model.summary()