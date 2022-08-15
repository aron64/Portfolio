using System;
using Xamarin.Forms;
using Xamarin.Forms.Xaml;
using Snake.Persistence;
using Snake.Model;
using Snake.ViewModel;
using Snake.View;
namespace Snake
{

    /// <summary>
    /// Interaction logic for App.xaml
    /// </summary>
    public partial class App : Application
    {
        #region Fields

        private SnakeGameModel _model;
        private SnakeViewModel _viewModel;
        private MainPage _view;
        private bool _advanceTimer;

        #endregion

        #region Constructors

        /// <summary>
        /// Alkalmazás példányosítása.
        /// </summary>
        public App()
        {
            App_Startup();
        }

        #endregion

        #region Application event handlers

        private void App_Startup()
        {
            // modell létrehozása
            _model = new SnakeGameModel(DependencyService.Get<ISnakeDataAccess>());
            _model.GameOver += new EventHandler<SnakeEventArgs>(Model_GameOver);

            // nézemodell létrehozása
            _viewModel = new SnakeViewModel(_model);
            _viewModel.NewGame += new EventHandler(ViewModel_NewGame);
            _viewModel.Help += new EventHandler(ViewModel_Help);
            _viewModel.ExitGame += new EventHandler(ViewModel_ExitGame);
            _viewModel.UserTurn += new EventHandler(ViewModel_UserTurn);

            // nézet létrehozása
            _view = new MainPage();
            _view.BindingContext = _viewModel;
            MainPage = _view;
        }

        

        #endregion


        #region ViewModel event handlers

        /// <summary>
        /// Új játék indításának eseménykezelője.
        /// </summary>
        private void ViewModel_NewGame(object sender, EventArgs e)
        {
            _model.NewGame();
            _advanceTimer = true;
            Device.StartTimer(TimeSpan.FromMilliseconds(260), () => { _model.AdvanceTime(); return _advanceTimer; });
        }

        /// <summary>
        /// Játékos közbeavatkozásának az eseménykezelője.
        /// </summary>
        private void ViewModel_UserTurn(object sender, EventArgs e)
        {
            _advanceTimer = false;
            _advanceTimer = true;

            Device.StartTimer(TimeSpan.FromSeconds(260), () => { _model.AdvanceTime(); return _advanceTimer; });
        }

       

        /// <summary>
        /// Segítségkérés eseménykezelője.
        /// </summary>
        private async void ViewModel_Help(object sender, EventArgs e)
        {

            await MainPage.DisplayAlert("Snake - Ahol tudok ott segítek!", "Billentyűk:" + Environment.NewLine +
                              "W vagy Felfele Nyíl\t:\tFordulás Északnak." + Environment.NewLine +
                               "S vagy Lelfele Nyíl\t\t:\tFordulás Délnek." + Environment.NewLine +
                                "D vagy Jobbra Nyíl\t\t:\tFordulás Keletnek." + Environment.NewLine +
                                 "A vagy Balra Nyíl\t\t:\tFordulás Nyugatnak." + Environment.NewLine +
                                 "ESC vagy F9 \t\t:\tJáték szünet.",

                              "Ok");
        }


        /// <summary>
        /// Játékból való kilépés eseménykezelője.
        /// </summary>
        private void ViewModel_ExitGame(object sender, System.EventArgs e)
        {
            //_view.Close();
        }

        #endregion

        #region Model event handlers
        /// <summary>
        /// Játék végének eseménykezelője.
        /// </summary>
        private async void Model_GameOver(Object sender, SnakeEventArgs e)
        {
            _advanceTimer = false;


            // MainWindow.gb.Enabled = true;
            await MainPage.DisplayAlert("Snake - Game Over!", "Vége a játéknak!" + Environment.NewLine +
                                "Összesen " + e.ConsumedEggs + " tojást szedtél össze.",

                                "Ok"
                                );

        }
        #endregion

        protected override void OnStart()
        {
        }

        protected override void OnSleep()
        {
        }

        protected override void OnResume()
        {
        }
    }

}