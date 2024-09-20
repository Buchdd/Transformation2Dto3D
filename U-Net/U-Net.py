import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np
import ezdxf
import matplotlib.pyplot as plt

def unet_model(input_shape):
    inputs = layers.Input(shape=input_shape)

    # Encoder
    c1 = layers.Conv2D(64, (3, 3), activation='relu', padding='same')(inputs)
    c1 = layers.Conv2D(64, (3, 3), activation='relu', padding='same')(c1)
    p1 = layers.MaxPooling2D((2, 2))(c1)

    c2 = layers.Conv2D(128, (3, 3), activation='relu', padding='same')(p1)
    c2 = layers.Conv2D(128, (3, 3), activation='relu', padding='same')(c2)
    p2 = layers.MaxPooling2D((2, 2))(c2)

    c3 = layers.Conv2D(256, (3, 3), activation='relu', padding='same')(p2)
    c3 = layers.Conv2D(256, (3, 3), activation='relu', padding='same')(c3)
    p3 = layers.MaxPooling2D((2, 2))(c3)

    c4 = layers.Conv2D(512, (3, 3), activation='relu', padding='same')(p3)
    c4 = layers.Conv2D(512, (3, 3), activation='relu', padding='same')(c4)
    p4 = layers.MaxPooling2D((2, 2))(c4)

    c5 = layers.Conv2D(1024, (3, 3), activation='relu', padding='same')(p4)
    c5 = layers.Conv2D(1024, (3, 3), activation='relu', padding='same')(c5)

    # Decoder
    u6 = layers.Conv2DTranspose(512, (2, 2), strides=(2, 2), padding='same')(c5)
    u6 = layers.concatenate([u6, c4])
    c6 = layers.Conv2D(512, (3, 3), activation='relu', padding='same')(u6)
    c6 = layers.Conv2D(512, (3, 3), activation='relu', padding='same')(c6)

    u7 = layers.Conv2DTranspose(256, (2, 2), strides=(2, 2), padding='same')(c6)
    u7 = layers.concatenate([u7, c3])
    c7 = layers.Conv2D(256, (3, 3), activation='relu', padding='same')(u7)
    c7 = layers.Conv2D(256, (3, 3), activation='relu', padding='same')(c7)

    u8 = layers.Conv2DTranspose(128, (2, 2), strides=(2, 2), padding='same')(c7)
    u8 = layers.concatenate([u8, c2])
    c8 = layers.Conv2D(128, (3, 3), activation='relu', padding='same')(u8)
    c8 = layers.Conv2D(128, (3, 3), activation='relu', padding='same')(c8)

    u9 = layers.Conv2DTranspose(64, (2, 2), strides=(2, 2), padding='same')(c8)
    u9 = layers.concatenate([u9, c1])
    c9 = layers.Conv2D(64, (3, 3), activation='relu', padding='same')(u9)
    c9 = layers.Conv2D(64, (3, 3), activation='relu', padding='same')(c9)

    outputs = layers.Conv2D(3, (1, 1), activation='softmax')(c9)

    model = models.Model(inputs=[inputs], outputs=[outputs])
    return model

def load_and_rasterize_dxf(file_path):
    # Открываем DXF файл
    doc = ezdxf.readfile('path_to_your_file.dxf')
    msp = doc.modelspace()

    # Настройка фигуры для сохранения заготовки
    fig, ax = plt.subplots()

    # Обход элементов в чертеже
    for entity in msp:
        if entity.dxftype() == 'LINE':
            x0, y0 = entity.dxf.start.x, entity.dxf.start.y
            x1, y1 = entity.dxf.end.x, entity.dxf.end.y
            ax.plot([x0, x1], [y0, y1], color='black')

    # Настройка изображение
    ax.set_aspect('equal')
    ax.set_axis_off()  # Отключаем оси
    plt.savefig('output_image.png', bbox_inches='tight', dpi=300)

    return plt
    plt.close()  # Закрываем фигуру для освобождения памяти



def main():
    model = unet_model(input_shape=(256, 256, 3))
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    # Пример использования метода
    images = load_and_rasterize_dxf('path_to_your_file.dxf')

    history = model.fit(images, masks, validation_split=0.1, epochs=50, batch_size=16)

    # Оцените модель
    # model.evaluate(test_images, test_masks)

    # Визуализация
    # 
    predictions = model.predict(test_images)

    # Пример визуализации
    plt.figure(figsize=(15, 5))
    for i in range(5):
        plt.subplot(1, 5, i + 1)
        plt.imshow(predictions[i])  # Отображение результата сегментации
        plt.axis('off')
    plt.show()