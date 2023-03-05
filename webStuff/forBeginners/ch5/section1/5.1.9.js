// var myUL = document.querySelector('ul');
// myUL.addEventListener('click', function(){
//     console.log('click');
//     myUL.style.backgroundColor = getRandomColor();
// })

// var myList = document.querySelectorAll('li');

// for (var i = 0; i < myList.length; i++){
//     myList[i].addEventListener('click', function(){
//         console.log(this);
//         // this.classList.add('red');
//         // this.classList.toggle('red');
        
//         // This results in a Boolean indicating the toggle state
//         var temp = this.classList.toggle('red');
//         console.log(temp);
        
        
//     });
// }


var myList = document.querySelectorAll('.listItem');

for (var i = 0; i < myList.length; i++){
    myList[i].addEventListener('click', paintItRed);
}


function paintItRed(){
    console.log(this);
    // this.classList.add('red');
    // this.classList.toggle('red');
    
    // This results in a Boolean indicating the toggle state
    var temp = this.classList.toggle('red');
    console.log(temp);
}



function getRandomColor(){
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    console.log(color);
    return color;
}