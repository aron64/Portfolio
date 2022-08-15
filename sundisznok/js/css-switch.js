(function () {
  'use strict';


  document.addEventListener('DOMContentLoaded', function () {
    var contrast = localStorage.getItem('high-contrast');
    
    if (contrast){
      $('#switch').bootstrapToggle('on'); 
     switchMode('high-contrast', 'alap');
    }
    });
    
   
    $(function() {
      $('#switch').change(function() {
        if (this.checked) {
          switchMode('high-contrast', 'alap');
          localStorage.setItem('high-contrast', 'true');
        } else {
          switchMode('alap', 'high-contrast');
          localStorage.removeItem('high-contrast');
        }
      })
    })

    function switchMode(newMode, prevMode) {
      console.log(prevMode);
      var link = document.querySelector('link[rel=stylesheet][href*="' + prevMode + '"]');
      link.parentNode.removeChild(link);

      link = document.createElement('link')

      link.type = 'text/css'
      link.rel = 'stylesheet'
      link.media = 'screen'
      link.href = './css/' + newMode + '.css' // Az első aposztrófpár közé elérési útvonal kerülhet

      document.head.appendChild(link)
    }
  })();


