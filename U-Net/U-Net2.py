import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image

def load_and_preprocess_image(image_path):
    image = Image.open(image_path).convert('L')  # Преобразование в градации серого
    image = image.resize((256, 256))  # Изменение размера под вашу модель
    image_array = np.array(image) / 255.0  # Нормализация
    return np.expand_dims(image_array, axis=-1)  # Добавление канала

def segment_image(model, image_array):
    prediction = model.predict(np.expand_dims(image_array, axis=0))
    segmented = (prediction > 0.5).astype(np.uint8) * 255  # Бинаризация
    return segmented[0, ..., 0]

def main():
    model = load_model('your_model.h5')
    input_image_path = 'path_to_your_image.jpg'
    
    preprocessed_image = load_and_preprocess_image(input_image_path)
    segmented_image = segment_image(model, preprocessed_image)
    
    # Сохранение сегментированного изображения
    segmented_image_pil = Image.fromarray(segmented_image)
    segmented_image_pil.save('segmented_image.png')

if __name__ == "__main__":
    main()