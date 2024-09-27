using Autodesk.Revit.Attributes;
using Autodesk.Revit.DB;
using Autodesk.Revit.UI;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Transformation2Dto3DLib.Family
{
    [Transaction(TransactionMode.Manual)]
    public class CreateWallsBasedOnHeight : IExternalCommand
    {
        public Result Execute(ExternalCommandData commandData, ref string message, ElementSet elements)
        {
            Document doc = commandData.Application.ActiveUIDocument.Document;

            // Начинаем транзакцию
            using (Transaction tx = new Transaction(doc, "Create Walls Based on Height"))
            {
                tx.Start();

                // Используем FilteredElementCollector для получения всех стен
                FilteredElementCollector collector = new FilteredElementCollector(doc);
                collector.OfClass(typeof(Wall));
                List<Wall> walls = new List<Wall>();

                // Перебираем стены и получаем их высоту
                foreach (Wall wall in collector)
                {
                    // Получение незакрепленной высоты стены
                    Parameter heightParam = wall.get_Parameter(BuiltInParameter.WALL_HEIGHT_TYPE);
                    if (heightParam != null && heightParam.HasValue)
                    {
                        double height = heightParam.AsDouble(); // Высота в футах

                        // Получаем местоположение стены
                        LocationCurve? locationCurve = wall.Location as LocationCurve;
                        if (locationCurve != null)
                        {
                            Line? line = locationCurve.Curve as Line;
                            if (line != null)
                            {
                                // Создание стены по указанным данным
                                Wall newWall = Wall.Create(doc, line, wall.WallType.Id, wall.LevelId, height, 0, false, false);
                            }
                        }
                    }
                }

                tx.Commit();
            }

            return Result.Succeeded;
        }

    }
}
