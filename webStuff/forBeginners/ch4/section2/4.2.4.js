var compVal = 8;

function check(num){
    console.log(num);

    if(num > compVal){
        message(num + ' is more than ' + compVal);
    }
    else if(num == compVal){
        message(num + ' is equal to ' + compVal);
    }
    else{
        message(num + ' is less than ' + compVal);
    }
}

function message(msg){
    document.querySelector('h2').innerHTML = msg;
}

