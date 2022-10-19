(function(){

    var home=document.getElementById('home');
    var agenda=document.getElementById('agenda');
    var html=document.getElementById('content');
    var Rcar=document.getElementById('Rcar')
    var Rlab=document.getElementById('Rlab')
    var Au=document.getElementById('Au')
    var Cer=document.getElementById('Cer')
    var Update=document.getElementById('Updatedata')



    home.addEventListener('click', event=>{

        var xhr=new XMLHttpRequest();
        xhr.onreadystatechange= function(){
            if(xhr.status==200){
                html.innerHTML=xhr.responseText;
            };
        };
        xhr.open("get","/agenda", true);
        xhr.send();
    });

    function Ajax(html,Button,url){
        Button.addEventListener('click',event=>{
            var xhr=new XMLHttpRequest();
            xhr.onreadystatechange= function(){
                if(xhr.status==200){
                    html.innerHTML=xhr.responseText;
            };
        };
        xhr.open("get",url, true);
        xhr.send();
        });
    }


    Ajax(html,agenda,"/agenda")
    Ajax(html,home,"/home")
    Ajax(html,Rcar,"/rcar")
    Ajax(html,Rlab,"/rlab")
    Ajax(html,Au,"/au")
    Ajax(html,Cer,"/cer")
    Ajax(html,Update,"/update")


})();