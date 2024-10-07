import ezdxf
import matplotlib.pyplot as plt

def dwg_to_png(dwg_file, png_file):
    doc = ezdxf.readfile(dwg_file)
    msp = doc.modelspace()
    
    # Создаем изображение на основе векторной графики
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    for entity in msp:
        # Можно добавить фильтрацию по типу объектов (линии, круги и т.д.)
        if entity.dxftype() == 'LINE':
            ax.plot([entity.dxf.start.x, entity.dxf.end.x], 
                    [entity.dxf.start.y, entity.dxf.end.y], color='black')

    plt.axis('equal')
    plt.axis('off')
    plt.savefig(png_file, bbox_inches='tight')
    plt.close()

dwg_to_png('example.dwg', 'example.png')