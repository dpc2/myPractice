var clicker = document.getElementById('clicker');
var mainList = document.querySelector('ul');
var allListItems = document.querySelectorAll('li');

for (var x=0; x<allListItems.length; x++){
    allListItems[x].addEventListener('click', myList);
}

function myList(){
    console.log('click');
    this.classList.toggle('red');
}

clicker.addEventListener('click', function(){
    var li = document.createElement('li');
    li.addEventListener('click', myList); 
    var textValue = 'test ' + (allListItems.length + 1)
    var tempNode = document.createTextNode(textValue);
    li.appendChild(tempNode);
    mainList.appendChild(li);
})