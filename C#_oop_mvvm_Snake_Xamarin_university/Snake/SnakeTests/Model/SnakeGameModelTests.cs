using Microsoft.VisualStudio.TestTools.UnitTesting;
using Snake.Model;
using Snake.Persistence;
using System;
using System.Collections.Generic;
using System.Text;
using Moq;

namespace Snake.Model.Tests
{
    [TestClass()]
    public class SnakeGameModelTests
    {
        private SnakeGameModel _model;
        private FieldObject[,] _mockedField;
        private Mock<ISnakeDataAccess> _mock;
        private Int32 _steps;//Hányszor mozgott a kígyó amíg ment a játék.
        [TestInitialize]
        public void Initialize()
        {
            
            _mockedField = new FieldObject[11,11];
            _mockedField[5,9] = Wall.getInstance();
            
            _mock = new Mock<ISnakeDataAccess>();
            _mock.Setup(mock => mock.Load(It.IsAny<String>()))
                .Returns(() => _mockedField);
            

            _model = new SnakeGameModel(_mock.Object);
            _mock.Verify(access => access.Load("map1.txt"), Times.Once());

            _model.GameAdvanced += new EventHandler<SnakeEventArgs>(Model_GameAdvanced);
            _model.GameOver += new EventHandler<SnakeEventArgs>(Model_GameOver);
            _steps = 0;
        }

        [TestMethod()]
        public void SnakeGameModelConstructorTest()
        {
            Assert.AreEqual(_model.GameMap, GameMap.Small);
            Assert.AreEqual(_model.IsGameOver, true);
            Assert.AreEqual(_steps, 0);
        }

        [TestMethod()]
        public void SwitchMapTest()
        {
            _model.SwitchMap(GameMap.Medium);
            Assert.AreEqual(GameMap.Medium, _model.GameMap);
            _mock.Verify(access => access.Load("map2.txt"), Times.Once());
            _model.SwitchMap(GameMap.Small);
            Assert.AreEqual(GameMap.Small, _model.GameMap);
            _mock.Verify(access => access.Load("map1.txt"), Times.Exactly(2));
            _model.SwitchMap(GameMap.Large);
            Assert.AreEqual(GameMap.Large, _model.GameMap);
            _mock.Verify(access => access.Load("map3.txt"), Times.Once());
        }

        [TestMethod()]
        public void NewGameTest()
        {
            Assert.AreEqual(0, _steps);
            _model.NewGame();
            Assert.AreEqual(1, _steps); // első "0." lépésben kígyót spawnol és tojást generál, erre a későbbiekben figyeljünk.
            Assert.AreEqual(GameMap.Small, _model.GameMap);
            Assert.AreEqual(false, _model.IsGameOver);
            Assert.AreEqual(5, _model.Field.SnakeLength);
            Assert.AreEqual(0, _model.ConsumedEggs);
            Assert.AreEqual(Direction.East, _model.Field.Direction);
        }
        
        [TestMethod()]
        public void NewGameTest2()
        {
            // He tele van kezdésnél a pálya, véget ér a játék.
            for (int i = 0; i < _mockedField.GetLength(0) ; i++)
            {
                for (int j = 0; j < _mockedField.GetLength(1); j++)
                {
                    if (i!=5 || (j< (_mockedField.GetLength(1)/2-2)  || j>= (_mockedField.GetLength(1)/2+3)))
                    {
                        _mockedField[i, j] = Wall.getInstance();
                    }
                }
            }
           
            Assert.AreEqual(0, _steps);
            _model.NewGame();
            Assert.AreEqual(0, _steps); // első "0." lépésben kígyót spawnol és tojást generálna, de nem tud.
            //Assert.ThrowsException<InvalidOperationException>()
            Assert.AreEqual(GameMap.Small, _model.GameMap);
            Assert.AreEqual(true, _model.IsGameOver);
            Assert.AreEqual(5, _model.SnakeLength);
            Assert.AreEqual(0, _model.ConsumedEggs);
            Assert.AreEqual(Direction.East, _model.Field.Direction);
        }
        [TestMethod()]
        public void AdvanceTimeTest()
        {
            Location head;

            _model.Move(); // nem vagyunk játékban
            Assert.AreEqual(0, _steps);

            _model.NewGame(); //Falba ütközünk majd
            head = _model.Field.GetHead();
            Assert.AreEqual(7, head.y);
            Assert.AreEqual(5, head.x);

            while (!_model.IsGameOver)
            {
                _model.AdvanceTime(); //Event utáni állapot tesztelve lentebb.
            }
            head = _model.Field.GetHead();// fal van előttünk, amikor véget ért a játék
            Assert.AreEqual(_model.Field[head.x, head.y + 1], Wall.getInstance());
            Assert.AreEqual(2, _steps);

            _steps = 0;

            _model.NewGame();

            head = _model.Field.GetHead();

            // visszakerült e a fej a kezdőállásba
            Assert.AreEqual(7, head.y);
            Assert.AreEqual(5, head.x);

            
            _model.MoveInDirection(Direction.North);        // Északnak lépünk, pálya széléig rohanunk.
            Assert.AreEqual(2, _steps);
            Assert.AreEqual(Direction.North, _model.Field.Direction); // Nem lenne kötelező ebben az egységben tesztelni. (MoveInDirectionTest)
            while (!_model.IsGameOver)
            {
                Assert.AreEqual(Direction.North, _model.Field.Direction);
                _model.AdvanceTime(); //Event utáni állapot tesztelve lentebb.
            }
            head = _model.Field.GetHead();// vagy a pálya széle, vagy fal van előttünk, amikor véget ért a játék
            // Hol és hány lépésben lett vége a játéknak.
            Assert.AreEqual(0, head.x);
            Assert.AreEqual(7, head.y);
            Assert.AreEqual(6, _steps);

        }


        [TestMethod()]
        public void MoveTest()
        {

            _model.Move(); // nem vagyunk játékban
            Assert.AreEqual(0, _steps);


            _model.NewGame();
            Assert.AreEqual(1, _steps);
            
            _model.Move(); // Egy sikeres lépés
            Assert.AreEqual(2, _steps);

            _model.Move(); // Egy falba lépés
            Assert.AreEqual(2, _steps);
            Assert.IsTrue(_model.IsGameOver);
            Assert.AreEqual(5, _model.SnakeLength);

            _steps = 0;
            _model.NewGame();
            _mockedField[5, 8] = Egg.getInstance();

            _model.Move(); // Egy tojásra lépés
            Assert.AreEqual(2, _steps);
            Assert.AreEqual(1, _model.ConsumedEggs);
            Assert.AreEqual(6, _model.SnakeLength);


            _steps = 0;
            _model.NewGame();
            _mockedField[5, 8] = SnakeUnit.getInstance();
            _model.Move(); // Egy Kígyó mezőre lépés
            Assert.AreEqual(1, _steps);
            Assert.IsTrue(_model.IsGameOver);
            Assert.AreEqual(5, _model.SnakeLength);

            _steps = 0;
            _model.NewGame();
            //Megjegyzés: Kicsit kiheckeljük a kígyóinvariánst a teszt kedvéért,
            //de a lépés által ennek is helyre kell állnia, ezért nem fog szólni az eventhandler assert.
            _model.Field.RemoveTail();
            _mockedField[5, 8] = SnakeUnit.getInstance();
            Location l; l.x = 5; l.y = 8;
            _model.Field.Snake.Add(l);
            _model.Move(); // Egy Kígyó mezőre lépés, ha az a farka.
            Assert.AreEqual(2, _steps);
            Assert.IsFalse(_model.IsGameOver);
            Assert.AreEqual(5, _model.SnakeLength);


        }

        [TestMethod()]
        public void MoveInDirectionTest()
        {
            _model.MoveInDirection(Direction.North); // nem vagyunk játékban
            Assert.AreEqual(0, _steps);

            _model.NewGame();
            _model.MoveInDirection(Direction.North);
            Assert.AreEqual(4, _model.Field.GetHead().x);
            Assert.AreEqual(7, _model.Field.GetHead().y);
            Assert.AreEqual(Direction.North, _model.Field.Direction);
            Assert.AreEqual(2, _steps);

            _steps = 0;
            _model.NewGame();
            _model.MoveInDirection(Direction.East);
            Assert.AreEqual(5, _model.Field.GetHead().x);
            Assert.AreEqual(8, _model.Field.GetHead().y);
            Assert.AreEqual(Direction.East, _model.Field.Direction);
            Assert.AreEqual(2, _steps);

            _steps = 0;
            _model.NewGame();
            _model.MoveInDirection(Direction.South);
            Assert.AreEqual(6, _model.Field.GetHead().x);
            Assert.AreEqual(7, _model.Field.GetHead().y);
            Assert.AreEqual(Direction.South, _model.Field.Direction);
            Assert.AreEqual(2, _steps);


            _steps = 0;
            _model.NewGame();
            _model.MoveInDirection(Direction.West);
            Assert.AreEqual(Direction.East, _model.Field.Direction);
            Assert.AreEqual(1, _steps);
        }

        [TestMethod()]
        public void getMoveTest()
        {
            Location l;
            _model.NewGame();

            //fal
            l.x = 5;
            l.y = 9;
            Assert.AreEqual(Wall.getInstance(), _model.getMove(l));


            //pályán kívül
            l.x = -1; l.y = -1;
            Assert.AreEqual(Wall.getInstance(), _model.getMove(l));
            l.x = 11; l.y = 11;
            Assert.AreEqual(Wall.getInstance(), _model.getMove(l));

            //Üres mezőt visszakapjuk
            l.x = 0; l.y = 0;
            Assert.AreEqual(null, _model.getMove(l));

            //Kígyó!
            l.x = 5; l.y = 3;
            Assert.AreEqual(SnakeUnit.getInstance(), _model.getMove(l));
            l.x = 5; l.y = 4;
            Assert.AreEqual(SnakeUnit.getInstance(), _model.getMove(l));
            l.x = 5; l.y = 5;
            Assert.AreEqual(SnakeUnit.getInstance(), _model.getMove(l));
            l.x = 5; l.y = 6;
            Assert.AreEqual(SnakeUnit.getInstance(), _model.getMove(l));
            l.x = 5; l.y = 7;
            Assert.AreEqual(SnakeUnit.getInstance(), _model.getMove(l));
        }

        private void Model_GameAdvanced(Object sender, SnakeEventArgs e)
        {
            _steps++;
            Assert.AreEqual(e.IsOver, false); // Ha sikeres volt a lépés, nem lehetett vége a játéknak
            if (!_model.Field.IsFull()) //Ha nincs tele a tábla akkor kell hogy legyen tojás. 
            {
                bool eggFound = false;
                for (int i = 0; i < _model.Field.Size; i++)
                {
                    for (int j = 0; j < _model.Field.Size; j++)
                    {
                        if (_model.Field[i,j] == Egg.getInstance())
                        {
                            eggFound = true;
                            break;
                        }
                    }
                    if (eggFound) break;
                }
                Assert.AreEqual(eggFound, true);
            }
            Assert.AreEqual(e.ConsumedEggs + 5, _model.SnakeLength); //Mindig megfelelő hosszúságú a kígyó

            //Kígyóalak invariáns: valóban kígyót reprezentál a lista.
            for (int i = 1; i < _model.SnakeLength; i++)
            {
                Location pred = _model.Field.GetSnakeAt(i - 1);
                Location curr = _model.Field.GetSnakeAt(i);
                Int32 dx = Math.Abs(pred.x - curr.x);
                Int32 dy = Math.Abs(pred.y - curr.y);

                Assert.AreEqual(true, (dx == 1 && dy == 0) || (dx == 0 && dy == 1)); //Csak egy irányban eggyel mozdulhat el a kígyó.
            }
        }

        private void Model_GameOver(Object sender, SnakeEventArgs e)
        {
            Assert.AreEqual(_model.ConsumedEggs, e.ConsumedEggs); // a két értéknek egyeznie kell
            Assert.AreEqual(_model.IsGameOver, e.IsOver); // a két értéknek egyeznie kell
            Assert.AreEqual(true, e.IsOver);
        }
    }
}