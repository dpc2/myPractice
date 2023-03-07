var myList = document.querySelectorAll('li');

for(var x=0; x < myList.length; x++){
    console.log(myList[x]);
    myList[x].addEventListener('mouseover', myFunction);
    myList[x].addEventListener('mouseout', myOtherFunction);
}

function myFunction(){
    this.classList.add('red');
    console.log('Done!');
}

function myOtherFunction(){
    this.classList.remove('red');
}