// Example starter JavaScript for disabling form submissions if there are invalid fields
(() => {
  'use strict'

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  const forms = document.querySelectorAll('.needs-validation')
  const correo =document.getElementById('email')
  const correo2 =document.getElementById('email2')
  const label =document.getElementById('label-hide')
  const password = document.getElementById('inputPassword')
  const password2 = document.getElementById('inputPassword2')
  const label2 = document.getElementById('label2')
  const button =document.getElementById('btn-sub')
  const label_password =document.getElementById('label-invalid')
  const phone =document.getElementById('phone')
  const pqr=document.getElementById('ENVIAR')
  
  
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
  


//validar contraseña//
  password2.addEventListener('keyup', event=>{
    if(password2.value == password.value){
      password.classList.toggle('is-valid')
      password2.classList.remove('is-invalid')
      password2.classList.add('is-valid')
    }
    if(password2.value !=password.value){
      password2.classList.toggle('is-invalid')
      label_password.classList.remove('hide')
      label2.classList.remove('hide')
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
 button.addEventListener('click', event=>{
  Swal.fire({
    title: 'REGISTRO COMPLETADO',
    text: 'Se han enviado los datos',
    icon: 'success'
  })
 })
 pqr.addEventListener('click', event=>{
  Swal.fire({
    title: 'PETICION ENVIADA CON EXITO',
    text: 'Su peticion sera contestada de dos a 3 dias',
    icon: 'success'
  })
 })


})()

