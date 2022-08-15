using System;
using System.Collections.Generic;
using System.Text;
using Snake.Persistence;

namespace Snake.Model
{
    /// <summary>
    /// Egy x,y koordináta reprezentációja.
    /// </summary>
    public struct Location
    {
        public Int32 x;
        public Int32 y;
    }

    /// <summary>
    /// Enum típus az égtájoknak.
    /// </summary>
    public enum Direction { North, East, South, West }

    /// <summary>
    /// A játékmező típusa.
    /// Definiálja egy adott játék objektumait, illetve az objektumoknak az típus-invariáns tartó műveleteit.
    /// </summary>
    public class SnakeField
    {
        /// <summary>
        /// Az adott égtájok felé koordínáló segédvektorok.
        /// </summary>
        public static readonly Int32[,] dirs = new Int32[,] { { -1, 0 }, { 0 , 1 }, { 1, 0 }, { 0, -1 } };

        #region Fields

        /// <summary>
        /// Mező objektumok egy mátrixban.
        /// </summary>
        public FieldObject[,] Field { get; internal set; }

        /// <summary>
        /// A kígyó állapotlistája Location típusú koordinátákkal.
        /// </summary>
        public List<Location> Snake { get; internal set; }

        /// <summary>
        /// Representing a quarter:
        /// 0-North
        /// 1-East
        /// 2-South
        /// 3-West
        /// </summary>
        public Direction Direction { get; set; }

        #endregion

        #region queries
        /// <summary>
        /// Játéktábla méretének lekérdezése.
        /// </summary>
        public Int32 Size { get { return Field.GetLength(0); } }

        /// <summary>
        /// Kígyó hosszának lekérdezése
        /// </summary>
        public Int32 SnakeLength { get { return Snake.Count; } }


        /// <summary>
        /// Mező értékének lekérdezése.
        /// </summary>
        /// <param name="x">Vízszintes koordináta.</param>
        /// <param name="y">Függőleges koordináta.</param>
        /// <returns>A mező értéke: null vagy a FieldObject objektum.</returns>
        public FieldObject this[Int32 x, Int32 y] { get { return GetValue(x, y); } }
        #endregion

        #region public methods
        /// <summary>
        /// Snake játéktábla példányosítása.
        /// </summary>
        public SnakeField() : this(10) {  }

        /// <summary>
        /// Snake játéktábla példányosítása.
        /// </summary>
        /// <param name="tableSize">Játéktábla mérete.</param>
        public SnakeField(Int32 tableSize)
        {
            if (tableSize < 10)
                throw new ArgumentOutOfRangeException("The table size is less than 10.", "tableSize");

            Field = new FieldObject[tableSize, tableSize];
            Snake = new List<Location>();
        }

        /// <summary>
        /// Mező értékének lekérdezése.
        /// </summary>
        /// <param name="x">Vízszintes koordináta.</param>
        /// <param name="y">Függőleges koordináta.</param>
        /// <returns>A mező értéke: null vagy a FieldObject objektum.</returns>
        public FieldObject GetValue(Int32 x, Int32 y)
        {
            if (x < 0 || x >= Field.GetLength(0))
                throw new ArgumentOutOfRangeException("x", "The X coordinate is out of range.");
            if (y < 0 || y >= Field.GetLength(1))
                throw new ArgumentOutOfRangeException("y", "The Y coordinate is out of range.");

            return Field[x, y];
        }

        /// <summary>
        /// Mező értékének beállítása.
        /// Nem állítható be SnakeUnitra közvetlenül.
        /// </summary>
        /// <param name="x">Vízszintes koordináta.</param>
        /// <param name="y">Függőleges koordináta.</param>
        /// <param name="value">Mit akarunk elhelyezni.</param>
        public void SetValue(Int32 x, Int32 y, FieldObject value)
        {
            if (x < 0 || x >= Field.GetLength(0))
                throw new ArgumentOutOfRangeException("x", "The X coordinate is out of range.");
            if (y < 0 || y >= Field.GetLength(1))
                throw new ArgumentOutOfRangeException("y", "The Y coordinate is out of range.");
            if (value == SnakeUnit.getInstance())
                throw new ArgumentException("Snake state must be modified through the snake operations SetHead and RemoveTail.");
            if (Field[x, y]!=null)
                throw new ArgumentException("The field already contains a value!");

            Field[x, y] = value;
        }

        /// <summary>
        /// Új fejet kap a kígyó.
        /// </summary>
        /// <param name="loc">Lokáció</param>
        public void SetHead(Location loc)
        { 
            if (loc.x < 0 || loc.x >= Field.GetLength(0))
                throw new ArgumentOutOfRangeException("x", "The X coordinate is out of range.");
            if (loc.y < 0 || loc.y >= Field.GetLength(1))
                throw new ArgumentOutOfRangeException("y", "The Y coordinate is out of range.");
            if (Field[loc.x, loc.y] != null)
                throw new ArgumentException("The field already contains a value!");

            //Csak egy koordinátában és csak eggyel változhat a fej pozíciója
            if (!(Snake.Count==0)
                &&
                !( Math.Abs(loc.x-Snake[0].x) == 1 ^ (Math.Abs(loc.y - Snake[0].y) == 1)))
                throw new InvalidOperationException("Head can only be appended to a side of the previous head!");
            Snake.Insert(0, loc);
            Field[loc.x, loc.y] = SnakeUnit.getInstance();
        }

        /// <summary>
        /// A kígyó fejének helyzetének lekérdezése.
        /// </summary>
        public Location GetHead()
        {
            if(Snake.Count == 0) // Nem logikus, hogy előfordulhasson, de megkönnyíti a modellező dolgát
            {
                throw new InvalidOperationException("Snake is not present yet.");
            }
            else
            {
                return Snake[0];
            }
        }

        /// <summary>
        /// A kígyó fejtől számított index-edik elemének helyzetének lekérdezése.
        /// </summary>
        /// <param name="index">Az index nullától indexelve.</param>
        public Location GetSnakeAt(Int32 index)
        {
            if (Snake.Count <= index || index <0) 
            {
                throw new ArgumentOutOfRangeException("x", "The index is out of range.");
            }
            else
            {
                return Snake[index];
            }
        }

        /// <summary>
        /// A kígyó utolsó elemének eltávolítása a pályáról és a kígyóból egyaránt.
        /// </summary>
        public void RemoveTail()
        {
            if (Snake.Count < 1)
            {
                throw new InvalidOperationException("The snake is less than 2 long.");
            }
            else
            {
                Location l = Snake[Snake.Count - 1];
                Field[l.x, l.y] = null;
                Snake.RemoveAt(Snake.Count - 1);
            }
        }

        /// <summary>
        /// Egy tojás eltávolítása.
        /// A modelltől függ, hogy hány tojás lehet egyszerre, ezért koordináta szükséges.
        /// </summary>
        /// <param name="x">Vízszintes koordináta.</param>
        /// <param name="y">Függőleges koordináta.</param>
        /// <returns>A mező értéke.</returns>
        public void RemoveEgg(Int32 x, Int32 y)
        {
            if (x < 0 || x >= Field.GetLength(0))
                throw new ArgumentOutOfRangeException("x", "The X coordinate is out of range.");
            if (y < 0 || y >= Field.GetLength(1))
                throw new ArgumentOutOfRangeException("y", "The Y coordinate is out of range.");
            if (Field[x, y] != Egg.getInstance())
                throw new ArgumentException("The old field doesn't contain an Egg!");


            Field[x, y] = null;
        }


        /// <summary>
        /// Egy tojás elhelyezése.
        /// </summary>
        /// <param name="x">Vízszintes koordináta.</param>
        /// <param name="y">Függőleges koordináta.</param>
        /// <returns>A mező értéke.</returns>
        public void PlaceEgg(Int32 x, Int32 y)
        {
            if (x < 0 || x >= Field.GetLength(0))
                throw new ArgumentOutOfRangeException("x", "The X coordinate is out of range.");
            if (y < 0 || y >= Field.GetLength(1))
                throw new ArgumentOutOfRangeException("y", "The Y coordinate is out of range.");
            if (Field[x, y] != null)
                throw new ArgumentException("The new field is blocked by another objecct!");
            Field[x, y] = Egg.getInstance();
        }

        /// <summary>
        /// Eldönti, hogy van-e üres hely a mezőn.
        /// </summary>
        /// <returns>true/false</returns>
        public Boolean IsFull()
        {
            foreach (FieldObject value in Field)
                if (value == null)
                    return false;
            return true;
            
        }
        /// <summary>
        /// Keres egy üres helyet egy tojásnak.
        /// </summary>
        /// <returns></returns>
        public Location generateEggLocation()
        {
            if (IsFull())
            {
                //elviekben megtörténhet, hogy épp megnőtt a kígyó, és ezzel betelt a pálya
                throw new InvalidOperationException("No avaliable location.");
            }
            Random r = new Random();
            Location loc;
            do
            {
                loc.x = r.Next(0, Size);
                loc.y = r.Next(0, Size);
            }
            while (Field[loc.x, loc.y] != null);
            return loc;
        }

        /// <summary>
        /// Kiszámolja a következő lépés után a kígyó elejének pozicióját.
        /// </summary>
        public Location nextHeadLocation()
        {
            Location dl, l;
            l = GetHead();
            dl.x = l.x + SnakeField.dirs[(Int32)Direction, 0];
            dl.y = l.y + SnakeField.dirs[(Int32)Direction, 1];
            return dl;
        }

        #endregion
    }

    /// <summary>
    /// Teszteléshez segédosztály.
    /// </summary>
    public class MockSnakeField : SnakeField
    {
        public MockSnakeField(ref FieldObject[,] field, ref List<Location> snake) : base(10)
        {
            base.Field = field;
            base.Snake = snake;
        }
        public List<Location> BaseSnake { get { return Snake; } set { Snake = value; } }
    }
}
