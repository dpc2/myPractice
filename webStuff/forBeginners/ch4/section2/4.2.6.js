var myArray = [1,3,5,7,8];

for(var x=0; x<myArray.length; x++){
    console.log(myArray[x]);
}

var myObj = { first: "Danny", last: "C"};
for(var x in myObj){
    console.log(myObj[x] + ' ' + x);
}

var x = 0;
while(x<10){
    console.log(x);
    x++;
}

var i = 0;
do {
    console.log(i);
    i++;
}
while (i < 10);


function message(msg){
    document.querySelector('h2').innerHTML = msg;
}