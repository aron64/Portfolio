using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;
namespace Snake.Persistence
{
    public interface ISnakeDataAccess
    {
        /// <summary>
        /// Fájl betöltése.
        /// </summary>
        /// <param name="path">Elérési útvonal.</param>
        /// <returns>A fájlból beolvasott falak helyzeteit tartalmazó mátrix.</returns>
        FieldObject[,] Load(string path);

    }
}
