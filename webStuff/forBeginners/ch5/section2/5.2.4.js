var inputSelect = document.querySelector('input[name="newItem"]');

inputSelect.addEventListener('keypress', function(event){
    if(event.keyCode === 13){
        console.log(event.keyCode);
        makeNew();
    }
    console.log(event.keyCode);
})

var clicker = document.getElementById('clicker');
var mainList = document.querySelector('ul');
var allListItems = document.querySelectorAll('li');


for (var x=0; x<allListItems.length; x++){
    allListItems[x].addEventListener('click', myList);
}


function myList(){
    // Boolean variable temp
    var temp = this.classList.toggle('red');
    console.log(temp);

    if(temp){
        var span = document.createElement('span');
        span.textContent = ' x';
        span.addEventListener('click', function(){
            this.parentElement.remove();
        })
        this.appendChild(span);
    }
    else{
        this.getElementsByTagName('span')[0].remove();
    }
}


function makeNew(){
    var li = document.createElement('li');
    li.addEventListener('click', myList); 
    var textValue = inputSelect.value;
    inputSelect.value = '';
    var tempNode = document.createTextNode(textValue);
    li.appendChild(tempNode);
    mainList.appendChild(li);
}