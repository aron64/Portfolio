using Android.App;
using Android.Content;
using Android.OS;
using Android.Runtime;
using Android.Views;
using Android.Widget;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Snake.Persistence;
using Snake.Droid.Persistence;
using System.IO;
using Xamarin.Forms;

[assembly: Dependency(typeof(DroidSnakeFileAccess))]
namespace Snake.Droid.Persistence
{
    class DroidSnakeFileAccess : ISnakeDataAccess
     {

        /// <summary>
        /// A fájl betöltése.
        /// </summary>
        /// <param name="path"> A fájl elérési útvonala.</param>
        /// <returns>A fájlból beolvasott, falak helyzeteit tartalmaző mátrix.</returns>
        public FieldObject[,] Load(String path)
        {

            try
            {
                using (StreamReader reader = new StreamReader(Android.App.Application.Context.Assets.Open(path))) // fájl megnyitása
                {

                    String line = reader.ReadLine();
                    Int32 tableSize = Int32.Parse(line); // beolvassuk a mező méretét
                    FieldObject[,] fieldValues = new FieldObject[tableSize, tableSize]; // létrehozzuk a mezőt

                    line = reader.ReadLine();
                    Int32 wallsCount = Int32.Parse(line); // beolvassuk a falak számát
                    for (Int32 i = 0; i < wallsCount; i++)
                    {
                        line = reader.ReadLine();
                        Int32[] numbers = Array.ConvertAll(line.Split(' '), Int32.Parse);
                        fieldValues[numbers[0], numbers[1]] = Wall.getInstance();
                    }

                    return fieldValues;
                }
            }
            catch // A fájl feldolgozása sikertelen
            {
                throw new SnakeDataException();
            }
        }
    }
}