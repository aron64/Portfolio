using System;
using System.Collections.Generic;
using System.Text;

namespace Snake.Persistence
{
    /// <summary>
    /// A játékobjektumok absztrakt, nem példányosítható osztálya.
    /// Childs: -- Wall
    ///         -- Egg
    ///         -- SnakeUnit
    /// </summary>
    abstract public class FieldObject
    {
        protected FieldObject() { }
    }

    /// <summary>
    /// Fal objektum.
    /// </summary>
    public class Wall : FieldObject
    {
        private static Wall _instance;
        private Wall() { }
        public static Wall getInstance() { if (_instance == null) _instance = new Wall(); return _instance; }
        public override string ToString()
        {
            return "White";
        }
    }

    /// <summary>
    /// Tojás objektum.
    /// </summary>
    public class Egg : FieldObject
    {
        private static Egg _instance;
        private Egg() { }
        public static Egg getInstance() { if (_instance == null) _instance = new Egg(); return _instance; }

        public override string ToString()
        {
            return "Red";
        }
    }

    /// <summary>
    /// SnakeUnit objektum. A kígyó egy "kockája".
    /// Lehetne külön a head, de a lista eleje a kígyó feje az ábrázolásomban.
    /// </summary>
    public class SnakeUnit : FieldObject
    {
        private static SnakeUnit _instance;
        private SnakeUnit() { }
        public static SnakeUnit getInstance() { if (_instance == null) _instance = new SnakeUnit(); return _instance; }
        public override string ToString()
        {
            return "Blue";
        }
    }
}
