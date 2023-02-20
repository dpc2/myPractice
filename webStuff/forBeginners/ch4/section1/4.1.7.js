// var count1 = 0
// var count2 = 0
// var count3 = 0

var count1, count2, count3;
count1 = count2 = count3 = 0;

function myFunc1(){
    count1++;
    output = count1 + count2 + count3;
    message();
}

function myFunc2(){
    count2++;
    output = count1 + count2 + count3;
    message();
}

function myFunc3(){
    count3++;
    output = count1 + count2 + count3;
    message();
}

function message(){
    document.querySelector('h2').innerHTML = count1 + ' ' + count2 + ' ' + count3;
}