document.querySelector('h2').innerHTML =
document.URL;

const myElement = document.querySelector('h2');

function message(){
    let temp = document.getElementById('myInput');
    output(temp.value)
}


function output(msg){
    myElement.innerHTML = msg;
}