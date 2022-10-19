$('#submitButton').click(function(){
    var Name =document.getElementById('name').value
    var doc =document.getElementById('doc').value
    var email =document.getElementById('email').value
    var phone =document.getElementById('phone').value
    var PQRS =document.getElementById('message').value

    var data ="Name="+Name+"&Doc="+doc+"&Email="+email+"&tel"+phone+"$Pq="+PQRS

    $.ajax({
        url:'/data-successfully',
        type:'POST',
        data:data
    })
    .done(console.log("enviados"))
    .fail(console.log("error"))
    .always(console.log("completo"))


})