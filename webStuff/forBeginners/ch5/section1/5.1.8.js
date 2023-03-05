var myUL = document.querySelector('ul');
myUL.addEventListener('click', function(){
    console.log('click');
    myUL.style.backgroundColor = getRandomColor();
})

function getRandomColor(){
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    console.log(color);
    return color;
}