import paddle
import paddleseg
from paddleseg import inference
from paddleseg.utils import get_model, get_config
from paddleseg.core.get_prediction import get_prediction
import cv2
import numpy as np

# Определите конфигурацию модели
config = get_config('DeepLabV3+_ResNet50_bs16_512x512')
model = get_model(config)

# Загрузка предобученных весов
model.set_state_dict(paddle.load('DeepLabV3+_ResNet50_bs16_512x512.pdparams'))
model.eval()

# Загрузка изображения с использованием OpenCV
image = cv2.imread('path_to_your_image.jpg')
image = cv2.resize(image, (512, 512))  # Изменение размера для соответствия модели

# Предпроцессинг изображения (настройка формата и нормализация)
image = image.astype(np.float32) / 255.0
image = np.transpose(image, (2, 0, 1))  # Изменяем размерность на (C, H, W)
image = np.expand_dims(image, axis=0)  # Добавляем размерность батча

# Проход изображения через модель
with paddle.no_grad():
    pred = model(image)

# Получение предсказаний (разделение классов)
pred = get_prediction(pred)

# Ресайзим предсказанную маску обратно к исходным размерам
pred_mask = cv2.resize(pred[0], (image.shape[2], image.shape[1]))

# Визуализация результатов
colored_mask = cv2.applyColorMap((pred_mask * 255).astype(np.uint8), cv2.COLORMAP_JET)  # Применяем цветовую карту
result = cv2.addWeighted(image[0].transpose(1, 2, 0), 0.5, colored_mask, 0.5, 0)

cv2.imshow('Segmented Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()