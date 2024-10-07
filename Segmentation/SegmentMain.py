import numpy as np
import aspose.cad as cad
from tensorflow import image
from UnetModel import model
from ConvertDWGtoPNG import dwg_to_png

def segment_image(model, img_path):
    
    """img = image.load_img(img_path)
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    
    pred = model.predict(img_array)
    pred_mask = (pred[0] > 0.5).astype(np.uint8)

    return pred_mask"""
    # Предобработка изображения
    image = preprocess_image(image)  # Ваша функция предобработки
    # Добавление размерности для модели
    image = np.expand_dims(image, axis=0)

    # Получение предсказания
    prediction = model.predict(image)
    
    # Применение порога для получения маски
    mask = (prediction > threshold).astype(np.uint8)

    return mask[0]

"""def save_layers_to_dwg(mask, dwg_file):
    doc = ezdxf.new()
    msp = doc.modelspace()
    
    for row in range(mask.shape[0]):
        for col in range(mask.shape[1]):
            if mask[row, col] > 0:
                # Создание элементов в DWG в зависимости от сегментации
                msp.add_line(start=(col, row), end=(col + 1, row))

    doc.saveas(dwg_file)"""

def save_layers_to_dwg(layers, output_dwg_file):
    # Создание нового DWG
    drawing = cad.DwgImage()
    
    for layer in layers:
        # Здесь можно добавить логику для создания объектов на слое
        # Например, создание контуров или фигур на основе маски
        # Пример: добавление прямоугольника или линии на основе маски
        # drawing.entities.add(entity)

        # Предположим, вы уже получили контуры из маски
        contours = get_contours(layer)  # Ваша функция для получения контуров
        
        for contour in contours:
            drawing.entities.add(contour)  # Добавление контуров в DWG объект

    # Сохранение DWG файла
    drawing.save(output_dwg_file)

def get_contours(mask):
    # Примерная логика для извлечения контуров из маски
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours

pathToDWG = r"C:\\Users\\Acer\\Desktop\\Севкав\\Example\\Поэтажный план Участок 472 №41 версия 2013.dwg"
pathToPNG = r"C:\\Users\\Acer\\Desktop\\Севкав\\Example\\example.png"
dwg_to_png(pathToDWG, pathToPNG)
mask = segment_image(model, pathToPNG)
save_layers_to_dwg(mask, "example.dwg")