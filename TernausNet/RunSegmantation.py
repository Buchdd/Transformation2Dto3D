import tensorflow as tf
from ternausnet import TernausNet
from keras.preprocessing.image import ImageDataGenerator

# Создание модели TernausNet
model = TernausNet(input_shape=(256, 256, 3), weights='imagenet')

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model

datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

train_generator = datagen.flow_from_directory(
    'data/train',  # Путь к данным
    target_size=(256, 256),
    batch_size=32,
    class_mode='categorical',
    subset='training'
)

validation_generator = datagen.flow_from_directory(
    'data/validate',  # Путь к данным
    target_size=(256, 256),
    batch_size=32,
    class_mode='categorical',
    subset='validation'
)