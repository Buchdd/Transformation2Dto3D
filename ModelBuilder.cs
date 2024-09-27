using Autodesk.Revit.DB;
using Autodesk.Revit.UI;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Transformation2Dto3DLib.Family;

namespace Transformation2Dto3DLib
{
    public class ModelBuilder
    {
        private readonly UIDocument _uiDoc;
        private readonly Document _doc;

        public ModelBuilder(UIDocument uiDoc)
        {
            _uiDoc = uiDoc;
            _doc = uiDoc.Document;
        }

        public void BuildModel()
        {
            // Сборка стен, дверей и окон
            CreateWall wall = new CreateWall(_uiDoc);
            wall.CreateWalls();
            // Создайте другие методы для создания дверей и окон
        }
    }
}
