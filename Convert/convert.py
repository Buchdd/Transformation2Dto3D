import pythoncom
import win32com.server
import aspose.cad as cad

class Converter:
    def dwg_to_png(dwg_file, png_file):
        image = cad.Image.load(dwg_file)
        rasterizationOptions = cad.imageoptions.CadRasterizationOptions()
        rasterizationOptions.layouts = ["Model"]

        pdfOptions = cad.imageoptions.PdfOptions()
        pdfOptions.vector_rasterization_options = rasterizationOptions

        image.save(png_file, pdfOptions)

if __name__ == '__main__':
    import win32com.server.register
    win32com.server.register.UseCommandLine(Converter)