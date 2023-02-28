var el1 = document.getElementById('one');
console.log(el1);
el1.style.background = "yellow";


var el2 = document.getElementsByTagName('li');
console.log(el2);
// el2.style.background = "green";


var el3 = document.getElementsByClassName('highlight');
console.log(el3);
// el3.style.background = "green";


var el4 = document.querySelector('.highlight');
console.log(el4);
el4.style.background = "green";


var el5 = document.querySelectorAll('.highlight');
console.log(el5);
// el5.style.background = "red";