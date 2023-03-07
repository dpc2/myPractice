var clicker = document.getElementById('clicker');
var mainList = document.querySelector('ul');


clicker.addEventListener('click', function(){
    console.log('Hello!');
    var li = document.createElement('li');
    // li.innerHTML = "NewContent";
    var allListItems = document.querySelectorAll('li');
    var textValue = 'test ' + (allListItems.length + 1)
    var tempNode = document.createTextNode(textValue);
    li.appendChild(tempNode);
    mainList.appendChild(li);
})