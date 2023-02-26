const myBtn = document.querySelector('#testButton');
const myEle = document.querySelector('h2');

myBtn.addEventListener('click', message);


function message(){
    let temp = document.getElementById('myInput');
    output(temp.value)
}


function output(msg){
    myEle.innerHTML = msg;
}