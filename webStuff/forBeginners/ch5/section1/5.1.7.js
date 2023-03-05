var el1 = document.getElementsByTagName('a');
console.log(el1[0]);

var el2 = document.getElementsByTagName('img');
console.log(el2[1]);

var temp = el1[0].getAttribute('href');
el1[0].setAttribute('href','http://www.google.com');


var chal1 = document.getElementsByTagName('img');
console.log(chal1);
console.log(chal1[0]);
console.log(chal1[1]);
var myTemp = chal1[0].getAttribute('src');
console.log(myTemp);
chal1[0].setAttribute('src', chal1[1].getAttribute('src'));
chal1[1].setAttribute('src', myTemp);
