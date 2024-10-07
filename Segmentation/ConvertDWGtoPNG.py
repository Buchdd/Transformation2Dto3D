import aspose.cad as cad
#import aspose.cad.image as cad_image

def dwg_to_png(dwg_file, png_file):
    image = cad.Image.load(dwg_file)
    rasterizationOptions = cad.imageoptions.CadRasterizationOptions()
    rasterizationOptions.layouts = ["Model"]

    pdfOptions = cad.imageoptions.PdfOptions()
    pdfOptions.vector_rasterization_options = rasterizationOptions

    image.save(png_file, pdfOptions)