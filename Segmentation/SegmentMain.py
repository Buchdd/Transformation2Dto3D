import numpy as np
import ezdxf
from tensorflow.keras.preprocessing import image
from UnetModel import model

def segment_image(model, img_path):
    img = image.load_img(img_path, target_size=(256, 256), color_mode='grayscale')
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    
    pred = model.predict(img_array)
    pred_mask = (pred[0] > 0.5).astype(np.uint8)

    return pred_mask

def save_layers_to_dwg(mask, dwg_file):
    doc = ezdxf.new()
    msp = doc.modelspace()
    
    for row in range(mask.shape[0]):
        for col in range(mask.shape[1]):
            if mask[row, col] > 0:
                # Создание элементов в DWG в зависимости от сегментации
                msp.add_line(start=(col, row), end=(col + 1, row))

    doc.saveas(dwg_file)

mask = segment_image(model, 'example.png')
save_layers_to_dwg(mask, 'segmented_output.dwg')