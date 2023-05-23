$(document).ready(function(){
    $("input[name='name']").keydown(function(e){
        console.log('pressed');
        console.log(e.keyCode);
        if(e.keyCode == 13){
            console.log('Enter!');
        }
    })

    $("input[name='name']").keyup(function(e){
        console.log('pressed');
        console.log(e.keyCode);
        if(e.keyCode == 13){
            console.log('Enter!');
        }
    })

    $("input").keypress(function(e){
        console.log(e);
    })

})
