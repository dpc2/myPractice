var element1 = document.querySelector('input[name="newItem"]');
var myUL = document.querySelector('ul');
element1.addEventListener('keypress', addItem);


function addItem(event){
    // console.log('add item');
    // console.log(event);
    if(event.keyCode === 13 && element1.value.length > 1){
    //  console.log(element1.value);
    //  console.log(element1.value.length);
     myUL.style.backgroundColor = randomColor(); 
    }
}

function randomColor(){
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    // console.log(color);
    return color;
}

// console.log(element1);
