using Autodesk.Revit.UI;
using Autodesk.Revit.DB;
using Autodesk.Revit.Attributes;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Drawing;
using Transformation2Dto3DLib.Family;
using System;
using System.Runtime.InteropServices;

namespace Transformation2Dto3DLib
{

    public class SegmentTo3D// : IExternalCommand
    {
        public Result Execute(ExternalCommandData commandData, ElementSet elements)
        {
            // Путь к сегментированному изображению
            string segmentedImagePath = "path_to_your_segmented_image.png";
        
            // Загружаем изображение
            Bitmap bitmap = new Bitmap(segmentedImagePath);

            // Создайте экземпляр Python класса
           Type converterType = Type.GetTypeFromProgID("YourPythonNamespace.Converter");
           dynamic converter = Activator.CreateInstance(converterType);

           // Вызываем метод
           converter.convert_dwg_to_jpg(@"C:\path\to\input.dwg", @"C:\path\to\output.jpg");


            // Создайте новую транзакцию
            using (Transaction transaction = new Transaction(commandData.Application.ActiveUIDocument.Document, "Create 3D Model"))
            {
                transaction.Start();

                // Простой пример создания 3D-объекта на основе сегментации
                for (int y = 0; y < bitmap.Height; y++)
                {
                    for (int x = 0; x < bitmap.Width; x++)
                    {
                        System.Drawing.Color pixelColor = bitmap.GetPixel(x, y);
                        if (pixelColor.R == 255) // Проверка белого пикселя
                        {
                            // Создание куба или другого 3D-объекта в Revit
                            XYZ point = new XYZ(x, y, 0);
                            // Далее добавьте код для создания объекта, например, стены или колонны
                        }
                    }
                }

                transaction.Commit();
            }

            return Result.Succeeded;
        }
    }
    [Transaction(TransactionMode.Manual)]
    public class Command : IExternalCommand
    {
        public Result Execute(
            ExternalCommandData commandData,
            ref string message,
            ElementSet elements)
        {
            UIApplication uiApp = commandData.Application;
            UIDocument uiDoc = uiApp.ActiveUIDocument;

            ModelBuilder builder = new ModelBuilder(uiDoc);
            builder.BuildModel();

            return Result.Succeeded;
        }
    }
}