from pyautocad import Autocad, APoint
from Segmentation.ConvertDWGtoPNG import dwg_to_png

# Инициализация AutoCAD
acad = Autocad(create_if_not_exists=True)

# Пример создания нового слоя
def create_layer(layer_name):
    if layer_name not in acad.doc.Layers:
        acad.doc.Layers.Add(layer_name)

def convert3DTo2D(addresDWG, addresJPG):
    dwg_to_png(addresDWG, addresJPG)

def usingPaggleSeg(addesJPG):
    PaggleSeg(addresJPG)

# Основная функция
def main():
    addresDWG = "pathToFileDWG"
    addresJPG = "pathToFileJPG"
    convert3DTo2D(addresDWG, addresJPG)
    #PaggleSeg

    create_layer("NewLayer")

if __name__ == "__main__":
    main()