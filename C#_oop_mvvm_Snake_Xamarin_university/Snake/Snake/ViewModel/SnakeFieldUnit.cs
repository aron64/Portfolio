using System;

namespace Snake.ViewModel
{
    /// <summary>
    /// Snake játékmező típusa.
    /// </summary>
    public class SnakeFieldUnit : ViewModelBase
    {
        private String _color;

        /// <summary>
        /// Szín lekérdezése, vagy beállítása.
        /// </summary>
        public String Color 
        {
            get { return _color; }
            set
            {
                if (_color != value)
                {
                    _color = value; 
                    OnPropertyChanged();
                }
            } 
        }

        /// <summary>
        /// Vízszintes koordináta lekérdezése, vagy beállítása.
        /// </summary>
        public Int32 X { get; set; }

        /// <summary>
        /// Függőleges koordináta lekérdezése, vagy beállítása.
        /// </summary>
        public Int32 Y { get; set; }
    }
}
