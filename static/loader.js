(function(){

    var cuerpo = document.getElementById('cuerpo')
    var loader = document.getElementById('heart')

    window.onload = function(){

        cuerpo.classList.remove('ocultar')
        loader.classList.remove('heart')
        loader.classList.add('ocultar')
      };


})();