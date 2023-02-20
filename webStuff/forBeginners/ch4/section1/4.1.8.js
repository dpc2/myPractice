var b = 0;

mySum = add(100,1);

function message(a){
    var b = 0;
    b++;
    console.log(a);

    var output = a + ' ' + b;

    document.querySelector('h2').innerHTML = output;
}

function add(a,b){
    return a + b;
}