using Microsoft.VisualStudio.TestTools.UnitTesting;
using System;
using System.Collections.Generic;
using System.Text;
using Snake.Persistence;
using Snake.Model;
using Moq;
namespace Snake.Model.Tests
{
    [TestClass()]
    public class SnakeFieldTests
    {

        private SnakeField _field;
        private MockSnakeField _mockField;
        private FieldObject[,] _mockedField;
        private List<Location> _mockedSnake;

        
        [TestInitialize]
        public void Initialize()
        {

            _mockedField = new FieldObject[11, 11];
            _mockedField[5, 9] = Wall.getInstance();
            _mockedField[5, 8] = Egg.getInstance();
            _mockedSnake = new List<Location>();
            for (int i = 7; i >= 3; i--)
            {
                Location l;
                l.x = 5; l.y = i;
                _mockedSnake.Add(l);
                _mockedField[5, i] = SnakeUnit.getInstance();

            }

            _field = new SnakeField(10);
            _mockField = new MockSnakeField(ref _mockedField,ref _mockedSnake);
            
            Assert.AreEqual(5, _mockField.SnakeLength);
        }

        [TestMethod()]
        public void SnakeFieldNoParamConstructorTest()
        {
            _field = new SnakeField();
            Assert.AreEqual(10, _field.Size);
            Assert.AreEqual(0, _field.SnakeLength);
        }

        [TestMethod()]
        public void SnakeFieldConstructorTest1()
        {
            _field = new SnakeField(12);
            Assert.AreEqual(12, _field.Size);
            Assert.AreEqual(0, _field.SnakeLength);
        }

        [TestMethod()]
        [ExpectedException(typeof(ArgumentOutOfRangeException))]
        public void SnakeFieldConstructorTest2()
        {
            _field = new SnakeField(9);
        }
        [TestMethod()]
        public void GetValueTest()
        {

            Assert.ThrowsException<ArgumentOutOfRangeException>(() => _field.GetValue(-1,-1));
            Assert.ThrowsException<ArgumentOutOfRangeException>(() => _field.GetValue(10, 10));
            Assert.AreEqual(null, _field.GetValue(0, 0));
            
            Assert.AreEqual(Egg.getInstance(), _mockField.GetValue(5, 8));
            Assert.AreEqual(SnakeUnit.getInstance(), _mockField.GetValue(5, 7));
            Assert.AreEqual(SnakeUnit.getInstance(), _mockField.GetValue(5, 6));
            Assert.AreEqual(SnakeUnit.getInstance(), _mockField.GetValue(5, 5));
            Assert.AreEqual(SnakeUnit.getInstance(), _mockField.GetValue(5, 4));
            Assert.AreEqual(SnakeUnit.getInstance(), _mockField.GetValue(5, 3));
            Assert.AreEqual(Wall.getInstance(), _mockField.GetValue(5, 9));
        }

        [TestMethod()]
        public void SetValueTest()
        {
            Assert.AreEqual(null, _field.GetValue(0, 0));
            Assert.ThrowsException<ArgumentException>(() => _field.SetValue(0, 0, SnakeUnit.getInstance()));
            Assert.ThrowsException<ArgumentOutOfRangeException>(() => _field.SetValue(-1, -1, Wall.getInstance()));
            Assert.ThrowsException<ArgumentOutOfRangeException>(() => _field.SetValue(10, 10, Wall.getInstance()));
            _field.SetValue(0, 0, Wall.getInstance());
            Assert.AreEqual(Wall.getInstance(), _field.GetValue(0,0));


            //Már van ott valami
            Assert.ThrowsException<ArgumentException>(() => _field.SetValue(0, 0, Egg.getInstance()));
           
        }

        [TestMethod()]
        public void SetHeadTest()
        {

            Location l;
            l.x = 4; l.y = 8;

            Assert.AreEqual(5, _mockField.SnakeLength);
            Assert.ThrowsException<InvalidOperationException>(() => _mockField.SetHead(l)); // nem szabad tudni beszúrni, sarkosan se

            l.x = -1;l.y = 10;            
            Assert.ThrowsException<ArgumentOutOfRangeException>(() => _mockField.SetHead(l));

            l.x = 4; l.y = 7;
            
            _mockField.SetHead(l); //referencia lista, itt is meg kell változzon
            Assert.AreEqual(l, _mockField.Snake[0]);
            Assert.AreEqual(SnakeUnit.getInstance(), _mockField.Field[4,7]);

        }

        [TestMethod()]
        public void GetHeadTest()
        {
            Location l;
            l.x = 5; l.y = 7;
            Assert.AreEqual(l, _mockField.GetHead());
            _mockField.BaseSnake = new List<Location>();
            Assert.ThrowsException<InvalidOperationException>(() =>_mockField.GetHead());
        }

        [TestMethod()]
        public void GetSnakeAtTest()
        {
            for (int i = 0; i < _mockedSnake.Count; i++)
            {
                Assert.AreEqual(_mockedSnake[i], _mockField.GetSnakeAt(i));
            }
        }

        [TestMethod()]
        public void RemoveTailTest()
        {

            Assert.AreEqual(5, _mockField.SnakeLength);
            _mockField.RemoveTail();
            Assert.AreEqual(4, _mockField.SnakeLength);
            for (int i = 0; i < _mockedSnake.Count-1; i++)
            {
                Assert.AreEqual(_mockedSnake[i], _mockField.GetSnakeAt(i));
            }
        }

        [TestMethod()]
        public void RemoveEggTest()
        {
            Assert.ThrowsException<ArgumentOutOfRangeException>(() => _mockField.RemoveEgg(-1,0) );
            Assert.ThrowsException<ArgumentOutOfRangeException>(() => _mockField.RemoveEgg(0,-1) );
            Assert.ThrowsException<ArgumentOutOfRangeException>(() => _mockField.RemoveEgg(11,0) );
            Assert.ThrowsException<ArgumentOutOfRangeException>(() => _mockField.RemoveEgg(0,11) );
            Assert.ThrowsException<ArgumentException>(() => _mockField.RemoveEgg(0,0) );

            //most ugrik a majom a vízbe
            Assert.AreEqual(Egg.getInstance(), _mockField.Field[5, 8]);
            _mockField.RemoveEgg(5, 8);
            Assert.AreEqual(null, _mockField.Field[5, 8]);
        }

        [TestMethod()]
        public void PlaceEggTest()
        {

            Assert.ThrowsException<ArgumentOutOfRangeException>(() => _mockField.PlaceEgg(-1, 0));
            Assert.ThrowsException<ArgumentOutOfRangeException>(() => _mockField.PlaceEgg(0, -1));
            Assert.ThrowsException<ArgumentOutOfRangeException>(() => _mockField.PlaceEgg(11, 0));
            Assert.ThrowsException<ArgumentOutOfRangeException>(() => _mockField.PlaceEgg(0, 11));
            Assert.ThrowsException<ArgumentException>(() => _mockField.PlaceEgg(5, 5));//kígyó
            Assert.ThrowsException<ArgumentException>(() => _mockField.PlaceEgg(5, 9));//fal

            //most ugrik a majom a vízbe
            Assert.AreEqual(null, _mockField.Field[0, 0]);
            _mockField.PlaceEgg(0, 0);
            Assert.AreEqual(Egg.getInstance(), _mockField.Field[0, 0]);
        }

        [TestMethod()]
        public void IsFullTest()
        {
            for (int i = 0; i < _mockField.Field.GetLength(0); i++)
            {
                for (int j = 0; j < _mockField.Field.GetLength(1); j++)
                {
                    _mockedField[i, j] = Wall.getInstance();
                }
            }
            Assert.IsTrue(_mockField.IsFull());
            _mockedField[0, 0] = null;
            Assert.IsTrue(!_mockField.IsFull());
        }

        [TestMethod()]
        public void generateEggLocationTest()
        {
            for (int i = 0; i < _mockField.Field.GetLength(0); i++)
            {
                for (int j = 0; j < _mockField.Field.GetLength(1); j++)
                {
                    _mockedField[i, j] = Wall.getInstance();
                }
            }
            //Nem generálhat helyet
            Assert.ThrowsException<InvalidOperationException>(() => _mockField.generateEggLocation());
            _mockedField[3, 3] = null;
            //Megtalálja az egyetlen üres helyet
            Location l;
            l.x = 3;l.y = 3;
            
            Assert.AreEqual(l, _mockField.generateEggLocation());

        }

        [TestMethod()]
        public void nextHeadLocationTest()
        {
            Location l;

            _mockField.Direction = Direction.East;
            l.x = 5;
            l.y = 8;
            Assert.AreEqual(l,_mockField.nextHeadLocation());

            _mockField.Direction = Direction.North;
            l.x = 4;
            l.y = 7;
            Assert.AreEqual(l, _mockField.nextHeadLocation());

            _mockField.Direction = Direction.South;
            l.x = 6;
            l.y = 7;
            Assert.AreEqual(l, _mockField.nextHeadLocation());

            l.x = 4;
            l.y = 7;
            _mockField.SetHead(l);
            _mockField.Direction = Direction.West;
            l.x = 4;
            l.y = 6;
            Assert.AreEqual(l, _mockField.nextHeadLocation());
        }
    }
}