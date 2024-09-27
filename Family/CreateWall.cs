using Autodesk.Revit.DB;
using Autodesk.Revit.UI;

namespace Transformation2Dto3DLib.Family
{
    class CreateWall
    {
        private readonly UIDocument _uiDoc;
        private readonly Document _doc;

        public CreateWall(UIDocument uiDoc)
        {
            _uiDoc = uiDoc;
            _doc = uiDoc.Document;
        }
        public void CreateWalls()
        {

            using (Transaction trans = new Transaction(_doc, "Create Walls"))
            {
                trans.Start();

                // Пример создания стены
                WallType wallType = GetWallType("Basic Wall");
                Level level = GetLevel("Level 1");

                if (wallType != null && level != null)
                {
                    // Координаты начала и конца стены (можно заменить на нужные вам)
                    XYZ start = new XYZ(0, 0, 0);
                    XYZ end = new XYZ(10, 0, 0);
                    Line line = Line.CreateBound(start, end);

                    // Создание стены
                    Wall wall = Wall.Create(_doc, line, wallType.Id, level.Id, 10, 0, false, false);
                }

                trans.Commit();
            }
        }

        private WallType GetWallType(string wallTypeName)
        {
            FilteredElementCollector collector = new FilteredElementCollector(_doc);
            collector.OfClass(typeof(WallType));

            foreach (WallType wallType in collector)
            {
                if (wallType.Name.Equals(wallTypeName))
                {
                    return wallType;
                }
            }

            return null; // Если не найден тип стены
        }

        private Level GetLevel(string levelName)
        {
            FilteredElementCollector collector = new FilteredElementCollector(_doc);
            collector.OfClass(typeof(Level));

            foreach (Level level in collector)
            {
                if (level.Name.Equals(levelName))
                {
                    return level;
                }
            }

            return null; // Если не найден уровень
        }
    }
}