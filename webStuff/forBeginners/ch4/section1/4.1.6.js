var b = 0;

function message(a){
    b++;
    console.log(a);

    var output = a + ' ' + b;

    document.querySelector('h2').innerHTML = output;
}