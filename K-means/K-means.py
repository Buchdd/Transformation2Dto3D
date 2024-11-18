import ezdxf
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def segment_dwg(file_path, n_clusters):
    # Чтение DWG файла
    doc = ezdxf.readfile(file_path)
    msp = doc.modelspace()
    
    # Сбор параметров: тип, толщина, цвет, местонахождение
    data = []

    for entity in msp:
        if entity.dxftype() in ['LINE', 'CIRCLE', 'POLYLINE']:  # Учитываем только некоторые типы
            entity_type = entity.dxftype()
            thickness = entity.dxf.lineweight or 0  # Толщина (линейный вес)
            color = entity.dxf.color or 7  # Цвет по умолчанию (7 - белый)
            location = entity.get_point()  # Получение местоположения (например, первая точка)

            # Добавляем данные в массив
            data.append([entity_type, thickness, color] + list(location))

    # Преобразование данных в подходящий формат для K-средних
    # Преобразуем текстовые данные в числовые, например, кодируем тип
    type_to_int = {t: i for i, t in enumerate(set(row[0] for row in data))}
    processed_data = []

    for row in data:
        processed_row = [
            type_to_int[row[0]],  # Кодируем тип
            row[1],               # Толщина
            row[2],               # Цвет
            row[3][0],            # X координата
            row[3][1]             # Y координата
        ]
        processed_data.append(processed_row)

    # Преобразуем в массив NumPy
    X = np.array(processed_data)

    # Применение K-средних
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(X)

    # Получаем метки кластеров
    labels = kmeans.labels_

    # Визуализация (при необходимости, зависит от ваших данных)
    plt.figure(figsize=(10, 8))
    plt.scatter(X[:, 3], X[:, 4], c=labels, cmap='viridis')
    plt.title('Сегментация DWG-чертежа')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.colorbar()
    plt.show()

    return labels

# Пример использования
file_path = 'path/to/your/drawing.dxf'  # Укажите путь к вашему DXF-файлу
n_clusters = 5  # Количество кластеров
segment_labels = segment_dwg(file_path, n_clusters)
print(segment_labels)