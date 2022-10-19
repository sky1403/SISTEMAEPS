setInterval(function(){
    let RELOJ=document.getElementById('reloj');
    var date = new Date(),dayweek= date.getDay(),month=date.getMonth(),year=date.getFullYear(),dateday=date.getDate();
    var hours =date.getHours();
    var minutes=date.getMinutes();
    var seconds=date.getSeconds();
    var writeday = document.getElementById('dia');
    var writeme = document.getElementById('mes');
    var writeye = document.getElementById('anno');
    var week = ['Domingo', 'Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado'];
    var months=['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    
    writeday.innerText=week[dayweek]+" "+dateday;
    writeme.innerText=months[month];
    writeye.innerText=year;
    RELOJ.innerHTML = hours+":"+minutes+":"+seconds;
}) 


function saludo(){
 
    fecha = new Date(); 
    hora = fecha.getHours();
   
    if(hora >= 0 && hora < 12){
      texto = "Buenos Días";
      
    }
   
    if(hora >= 12 && hora < 18){
      texto = "Buenas Tardes";
      
    }
   
    if(hora >= 18 && hora < 24){
      texto = "Buenas Noches";
    }
   
    document.getElementById('SALUDO').innerText=texto;
   
  }saludo()







