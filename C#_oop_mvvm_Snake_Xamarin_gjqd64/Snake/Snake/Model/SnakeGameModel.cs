using System;
using System.Collections.Generic;
using System.Text;
using Snake.Persistence;

namespace Snake.Model
{

    /// <summary>
    /// A beolvasandó mapet jelölő felsorolási típusa.
    /// </summary>
    public enum GameMap { Small, Medium, Large }

    /// <summary>
    /// Snake játék típusa.
    /// </summary>
    public class SnakeGameModel
    {

        #region Fields

        private ISnakeDataAccess _dataAccess; // adatelérés
        private SnakeField _snakefield; // játékmező
        private Location _egg;
        private GameMap _map; // kiválasztott map
        private Int32 _consumedEggs;

        #endregion

        #region Properties

        /// <summary>
        /// Kígyó hosszának lekérdezése.
        /// </summary>
        public Int32 SnakeLength { get { return _snakefield.SnakeLength; } }


        /// <summary>
        /// Játéktábla lekérdezése.
        /// </summary>
        public SnakeField Field { get { return _snakefield; } }

        /// <summary>
        /// Játék végének lekérdezése és beállítása.
        /// </summary>
        public Boolean IsGameOver { get; set ; }

        /// <summary>
        /// Elfogyaszott tojások számának lekérdezése.
        /// </summary>
        public Int32 ConsumedEggs { get { return _consumedEggs; } }

        /// <summary>
        /// Map lekérdezése.
        /// </summary>
        public GameMap GameMap { get { return _map; } set { SwitchMap(value); } }



        #endregion

        #region Events

        /// <summary>
        /// Játék előrehaladásának eseménye.
        /// </summary>
        public event EventHandler<SnakeEventArgs> GameAdvanced;

        /// <summary>
        /// Játék végének eseménye.
        /// </summary>
        public event EventHandler<SnakeEventArgs> GameOver;

        /// <summary>
        /// Játék létrehozásának eseménye.
        /// </summary>
        public event EventHandler<SnakeEventArgs> GameCreated;

        #endregion

        #region constructor
        /// <summary>
        /// Snake játék példányosítása.
        /// </summary>
        /// <param name="dataAccess">Az adatelérés.</param>
        public SnakeGameModel(ISnakeDataAccess dataAccess)
        {
            _dataAccess = dataAccess;
            IsGameOver = true;
            SwitchMap(GameMap.Small);
        }

        #endregion
        #region Public game methods

        public void SwitchMap(GameMap map)
        {
            _map = map;
            FieldObject[,] data;
            switch (_map)
            {
                case GameMap.Small:
                    data = _dataAccess.Load("map1.txt");
                    _snakefield = new SnakeField(data.GetLength(0));
                    _snakefield.Field = data;
                    break;
                case GameMap.Medium:
                    data = _dataAccess.Load("map2.txt");
                    _snakefield = new SnakeField(data.GetLength(0));
                    _snakefield.Field = data;
                    break;
                case GameMap.Large:
                    data = _dataAccess.Load("map3.txt");
                    _snakefield = new SnakeField(data.GetLength(0));
                    _snakefield.Field = data;
                    break;
            }
        }

        /// <summary>
        /// Új játék kezdése.
        /// </summary>
        public void NewGame()
        {
            //SwitchMap(_map);
            _consumedEggs = 0;
            IsGameOver = false;
            while (_snakefield.SnakeLength > 0) _snakefield.RemoveTail();
            try
            {
                if (_snakefield[_egg.x, _egg.y] == Egg.getInstance()) _snakefield.RemoveEgg(_egg.x, _egg.y);
            }
            catch (ArgumentOutOfRangeException) { }
            
            for (int i = (_snakefield.Size / 2) - 2; i < (_snakefield.Size / 2) + 3; i++)
            {
                Location l;
                l.x = _snakefield.Size / 2;
                l.y = i;
                _snakefield.SetHead(l);
            }
            _snakefield.Direction = Direction.East;

            

            try
            {
                _egg = _snakefield.generateEggLocation(); // a tojás generálása
                _snakefield.PlaceEgg(_egg.x, _egg.y);
                OnGameAdvanced();
            }
            catch (InvalidOperationException)
            {
                //Megtelt a tábla, vége a játéknak.
                OnGameOver();
                return;
            }
        }

       


        /// <summary>
        /// Játékidő léptetése.
        /// </summary>
        public void AdvanceTime()
        {
            if (IsGameOver) // ha már vége, nem folytathatjuk
                return;
            Move(); // haladunk a kígyóval
        }


        /// <summary>
        /// Lépés végrehajtása, amennyiben lehetséges.
        /// Különben vége a játéknak.
        /// </summary>
        public void Move()
        {

            if (IsGameOver) // ha már vége, nem folytathatjuk
                return;

            Location newLoc = _snakefield.nextHeadLocation();
            switch (getMove(newLoc))
            {
                case null:
                    _snakefield.SetHead(newLoc);
                    _snakefield.RemoveTail();
                    break;
                case Egg _:
                    _consumedEggs++;
                    _snakefield.RemoveEgg(newLoc.x, newLoc.y);
                    _snakefield.SetHead(newLoc);
                    try
                    {
                        _egg = _snakefield.generateEggLocation();
                        _snakefield.PlaceEgg(_egg.x, _egg.y);
                    }
                    catch (InvalidOperationException)
                    {
                        //Megtelt a tábla, vége a játéknak.
                        OnGameAdvanced();
                        OnGameOver();
                        return;
                    }
                    break;
                case Wall _:
                    OnGameOver();
                    return;
                case SnakeUnit _:
                    if (newLoc.Equals(_snakefield.GetSnakeAt(SnakeLength - 1))) // "Kergetheti a farkát"
                    {
                        _snakefield.RemoveTail();
                        _snakefield.SetHead(newLoc);
                        break;
                    }
                    else
                    {
                        OnGameOver();
                        return;
                    }
                
            }
            OnGameAdvanced();
        }

        /// <summary>
        /// Elfordul a kígyó egy adott irányba, azaz el is mozdul rögtön.
        /// Nem fordulhat magába. :(
        /// </summary>
        /// <param name="dir">A megfelelő égtáj.</param>
        public void MoveInDirection(Direction dir)
        {
            if (IsGameOver) // ha már vége, nem folytathatjuk
                return;


            if(dir == _snakefield.Direction) //Erőltetett lépés a jelenlegi irányba, szabadjon
            {
                Move();
                return;
            }
            else
            {
                switch (_snakefield.Direction)
                {
                    case Direction.North:
                        if (dir == Direction.South) return; //Nem fordulhat hátra a fej.
                        _snakefield.Direction = dir;
                        break;
                    case Direction.South:
                        if (dir == Direction.North) return; //Nem fordulhat hátra a fej.
                        _snakefield.Direction = dir;
                        break;
                    case Direction.East:
                        if (dir == Direction.West) return; //Nem fordulhat hátra a fej.
                        _snakefield.Direction = dir;
                        break;
                    case Direction.West:
                        if (dir == Direction.East) return; //Nem fordulhat hátra a fej.
                        _snakefield.Direction = dir;
                        break;
                }
                Move();
            }
            
        }

        /// <summary>
        /// Mire lépnénk.
        /// </summary>
        /// <returns>Fieldobject vagy null.</returns>
        public FieldObject getMove(Location newHead)
        {
            try
            {
                return _snakefield[newHead.x, newHead.y];
            }
            catch (ArgumentOutOfRangeException) // A pályán kívüli helyek mind falnak számítanak.
            {
                return Wall.getInstance();
            }
        }

        #endregion


        #region Private event methods

        /// <summary>
        /// Játékidő változás eseményének kiváltása.
        /// </summary>
        private void OnGameAdvanced()
        {
            GameAdvanced?.Invoke(this, new SnakeEventArgs(false, _consumedEggs));
        }

        /// <summary>
        /// Játék vége eseményének kiváltása.
        /// </summary>
        private void OnGameOver()
        {
            IsGameOver = true;
            GameOver?.Invoke(this, new SnakeEventArgs(true, _consumedEggs));
        }
        /// <summary>
	    /// Játék létrehozás eseményének kiváltása.
	    /// </summary>
	    private void OnGameCreated()
        {
            if (GameCreated != null)
                GameCreated(this, new SnakeEventArgs(false, _consumedEggs));
        }

        #endregion
    }
}