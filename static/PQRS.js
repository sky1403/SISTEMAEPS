
(() => {
    'use strict'
  
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    const forms = document.querySelectorAll('.needs-validation')
    const correo =document.getElementById('email')
    const correo2 =document.getElementById('email2')
    const label =document.getElementById('label-hide')
    const button =document.getElementById('ENVIAR')
    const phone =document.getElementById('phone')
    
    
    window.addEventListener("load", function(event) {
      button.classList.add('disabled')
    })
    
  
  
  
  
    // Loop over them and prevent submission
    Array.from(forms).forEach(form => {
      form.addEventListener('submit', event => {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }
        form.classList.add('was-validated')
      }, false)
    })
  
    
  
  //validar correo//
    correo2.addEventListener('keyup', event=>{
      if(correo2.value == correo.value){
        correo.classList.toggle('is-valid')
        correo2.classList.remove('is-invalid')
        correo2.classList.toggle('is-valid')
      }
      if(correo2.value !=correo.value){
        correo2.classList.toggle('is-invalid')
        label.classList.remove('hide')
      }
    })
    
  
  
  
    
    // activar boton para envio//
   phone.addEventListener('keyup', function(event){
    if(phone.value !=""){
      button.classList.remove('disabled')
    }else{
      button.classList.add('disabled')
    }
   })
  
  
  //alerta con swalert//
   button.addEventListener('click', function(event){
    Swal.fire({
        title: 'PETICION ENVIADA CON EXITO',
        text: 'Su peticion sera contestada de dos a 3 dias',
        icon: 'success'
      })
   })

   
  })()