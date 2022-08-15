using System;
using System.Collections.ObjectModel;
using System.Drawing;
using Snake.Model;

namespace Snake.ViewModel
{
    /// <summary>
    /// Snake nézetmodell típusa.
    /// </summary>
    public class SnakeViewModel : ViewModelBase
    {
        #region Fields
        
        private SnakeGameModel _model; // modell

        #endregion

        #region Properties

        /// <summary>
        /// Új játék kezdése parancs lekérdezése.
        /// </summary>
        public DelegateCommand NewGameCommand { get; private set; }

        /// <summary>
        /// Játék betöltése parancs lekérdezése.
        /// </summary>
        public DelegateCommand HelpCommand { get; private set; }

        /// <summary>
        /// Kilépés parancs lekérdezése.
        /// </summary>
        public DelegateCommand ExitCommand { get; private set; }


        /// <summary>
        /// Billentyűparancs: W
        /// </summary>
        public DelegateCommand TurnUp { get; private set; }

        /// <summary>
        /// Billentyűparancs: S
        /// </summary>
        public DelegateCommand TurnDown { get; private set; }

        /// <summary>
        /// Billentyűparancs: A
        /// </summary>
        public DelegateCommand TurnLeft { get; private set; }

        /// <summary>
        /// Billentyűparancs: D
        /// </summary>
        public DelegateCommand TurnRight { get; private set; }

        /// <summary>
        /// Billentyűparancs: F9, ESC
        /// </summary>
        public DelegateCommand Pause { get; private set; }

        

        /// <summary>
        /// Játékmező gyűjtemény lekérdezése.
        /// </summary>
        public ObservableCollection<SnakeFieldUnit> Fields { get; set; }

        /// <summary>
        /// Lépések számának lekérdezése.
        /// </summary>
        public Int32 GameConsumedEggs { get { return _model.ConsumedEggs; } }

        /// <summary>
        /// Fennmaradt játékidő lekérdezése.
        /// </summary>
        public Boolean GameOver { get { return _model.IsGameOver; } }

        /// <summary>
        /// A játéktábla aktuális mérete
        /// </summary>
        public Int32 GameMapSize { get { return _model.Field.Size; } }

        /// <summary>
        /// Alacsony nehézségi szint állapotának lekérdezése.
        /// </summary>
        public Boolean IsGameMapSmall
        {
            get { return _model.GameMap == GameMap.Small; }
            set
            {
                if (_model.GameMap == GameMap.Small)
                    return;

                _model.SwitchMap(GameMap.Small);
                OnPropertyChanged("IsGameMapSmall");
                OnPropertyChanged("IsGameMapMedium");
                OnPropertyChanged("IsGameMapLarge");
                OnPropertyChanged("GameMapSize");
                InitTable();
                RefreshTable();
            }
        }

        /// <summary>
        /// Közepes nehézségi szint állapotának lekérdezése.
        /// </summary>
        public Boolean IsGameMapMedium
        {
            get { return _model.GameMap == GameMap.Medium; }
            set
            {
                if(_model.GameMap == GameMap.Medium)
                    return;

                _model.SwitchMap(GameMap.Medium);
                OnPropertyChanged("IsGameMapSmall");
                OnPropertyChanged("IsGameMapMedium");
                OnPropertyChanged("IsGameMapLarge");
                OnPropertyChanged("GameMapSize");
                InitTable();
                RefreshTable();
            }
        }

        /// <summary>
        /// Magas nehézségi szint állapotának lekérdezése.
        /// </summary>
        public Boolean IsGameMapLarge
        {
            get { return _model.GameMap == GameMap.Large; }
            set
            {
                if (_model.GameMap == GameMap.Large)
                    return;

                _model.SwitchMap(GameMap.Large);
                OnPropertyChanged("IsGameMapSmall");
                OnPropertyChanged("IsGameMapMedium");
                OnPropertyChanged("IsGameMapLarge");
                OnPropertyChanged("GameMapSize");
                InitTable();
                RefreshTable();
            }
        }

        #endregion

        #region Events

        /// <summary>
        /// Új játék eseménye.
        /// </summary>
        public event EventHandler NewGame;

        /// <summary>
        /// Játék betöltésének eseménye.
        /// </summary>
        public event EventHandler Help;


        /// <summary>
        /// Elfordulás eseménye.
        /// </summary>
        public event EventHandler UserTurn;

        /// <summary>
        /// Játékszünet/Újraindítás eseménye.
        /// </summary>
        public event EventHandler GamePause;

        /// <summary>
        /// Játékból való kilépés eseménye.
        /// </summary>
        public event EventHandler ExitGame;

        #endregion

        #region Constructors

        /// <summary>
        /// Snake nézetmodell példányosítása.
        /// </summary>
        /// <param name="model">A modell típusa.</param>
        public SnakeViewModel(SnakeGameModel model)
        {
            // játék csatlakoztatása
            _model = model;
            _model.GameAdvanced += new EventHandler<SnakeEventArgs>(Model_GameAdvanced);
            _model.GameOver += new EventHandler<SnakeEventArgs>(Model_GameOver);

            // parancsok kezelése
            NewGameCommand = new DelegateCommand((p) => GameOver, param => OnNewGame());
            HelpCommand = new DelegateCommand((p) => GameOver, param => OnHelp());
            ExitCommand = new DelegateCommand((p) => GameOver, param => OnExitGame());
            TurnDown = new DelegateCommand((p) => true, param => OnTurnDown());
            TurnUp = new DelegateCommand((p) => true, param => OnTurnUp());
            TurnLeft = new DelegateCommand((p) => true, param => OnTurnLeft());
            TurnRight = new DelegateCommand((p) => true, param => OnTurnRight());
            Pause = new DelegateCommand((p) => !GameOver, param => OnPause());
            Fields = new ObservableCollection<SnakeFieldUnit>();

            InitTable();
            
            RefreshTable();
        }

		#endregion

		#region Private methods

        private void InitTable()
        {
            Fields.Clear();
            for (Int32 i = 0; i < _model.Field.Size; i++) // inicializáljuk a mezőket
            {
                for (Int32 j = 0; j < _model.Field.Size; j++)
                {
                    Fields.Add(new SnakeFieldUnit
                    {
                        Color = "Green",
                        X = i,
                        Y = j,
                    });
                }
            }
        }
         
		/// <summary>
		/// Tábla frissítése.
		/// </summary>
		private void RefreshTable()
        {
            foreach (SnakeFieldUnit field in Fields) // inicializálni kell a mezőket is
            {
                if(_model.Field[field.X, field.Y]==Persistence.SnakeUnit.getInstance() && _model.Field.Snake[0].x == field.X && _model.Field.Snake[0].y == field.Y)
                {
                    field.Color = "Orange";
                }
                else
                {
                    if (_model.Field[field.X, field.Y] != null)
                    {
                        field.Color = _model.Field[field.X, field.Y].ToString();
                    }
                    else
                    {
                        field.Color = "Black";
                    }

                }

            }

            OnPropertyChanged("GameTime");
        }


        #endregion

        #region Game event handlers

        /// <summary>
        /// Játék végének eseménykezelője.
        /// </summary>
        private void Model_GameOver(object sender, SnakeEventArgs e)
        {
            OnPropertyChanged("GameOver");

        }

        /// <summary>
        /// Játék előrehaladásának eseménykezelője.
        /// </summary>
        private void Model_GameAdvanced(object sender, SnakeEventArgs e)
        {
            RefreshTable();
        }

	    /// <summary>
	    /// Játék létrehozásának eseménykezelője.
	    /// </summary>
		private void Model_GameCreated(object sender, SnakeEventArgs e)
	    {
		    RefreshTable();
	    }

		#endregion

		#region Event methods

		/// <summary>
		/// Új játék indításának eseménykiváltása.
		/// </summary>
		private void OnNewGame()
        {
            if (NewGame != null)
                NewGame(this, EventArgs.Empty);
            OnPropertyChanged("GameOver");
        }



        /// <summary>
        /// Segítségkérés eseménykiváltása.
        /// </summary>
        private void OnHelp()
        {
            if (Help != null)
                Help(this, EventArgs.Empty);
        }

 

        /// <summary>
        /// Játékból való kilépés eseménykiváltása.
        /// </summary>
        private void OnExitGame()
        {
            if (ExitGame != null)
                ExitGame(this, EventArgs.Empty);
        }

        /// <summary>
        /// Jobbra fordulás eseménykiváltása.
        /// </summary>
        private void OnTurnRight()
        {
            _model.MoveInDirection(Direction.East);
            UserTurn?.Invoke(this, EventArgs.Empty);
        }

        /// <summary>
        /// Balra fordulás eseménykiváltása.
        /// </summary>
        private void OnTurnLeft()
        {
            _model.MoveInDirection(Direction.West);
            UserTurn?.Invoke(this, EventArgs.Empty);

        }
        /// <summary>
        /// Lefelé eseménykiváltása.
        /// </summary>
        private void OnTurnUp()
        {
            _model.MoveInDirection(Direction.North);
            UserTurn?.Invoke(this, EventArgs.Empty);

        }
        /// <summary>
        /// Játékból való kilépés eseménykiváltása.
        /// </summary>
        private void OnTurnDown()
        {
            _model.MoveInDirection(Direction.South);
            UserTurn?.Invoke(this, EventArgs.Empty);
        }
        /// <summary>
        /// Játékból való kilépés eseménykiváltása.
        /// </summary>
        private void OnPause()
        {
            if (GameOver)
            {
                return;
            }
            foreach (var item in Fields)
            {
                switch (item.Color)
                {
                    case "Black":
                        item.Color = "DarkGray";
                        break;
                    case "Orange":
                    case "Blue":
                        item.Color = "Gray";
                        break;
                    case "Red":
                    case "White": item.Color = "LightGray";break;
                    default:
                        break;
                }
            }
            GamePause?.Invoke(this, EventArgs.Empty);
        }
        #endregion
    }
}
