using System;
using System.Collections.Generic;
using System.Text;

namespace Snake.Model
{
    public class SnakeEventArgs : EventArgs
    {
        private Int32 _consumedEggs;
        private Boolean _isOver;

        /// <summary>
        /// Elfogyasztott tojások számának lekérdezése.
        /// </summary>
        public Int32 ConsumedEggs { get { return _consumedEggs; } }


        /// <summary>
        /// Játék végének lekérdezése.
        /// </summary>
        public Boolean IsOver { get { return _isOver; } }

        /// <summary>
        /// Snake eseményargumentum példányosítása.
        /// </summary>
        /// <param name="isOver">Győzelem lekérdezése.</param>
        /// <param name="consumedEggs">Elfogyasztott tojások száma.</param>
        public SnakeEventArgs(Boolean isOver, Int32 consumedEggs)
        {
            _isOver = isOver;
            _consumedEggs = consumedEggs;
        }
    }
}
