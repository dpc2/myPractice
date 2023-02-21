

function check(val){
    console.log(val);

    switch(val){
        case 'one':
            message('was one');
            break;
        case 'hello':
            message('was hello!');
            break;
        case 'two':
        case '2':
            message('was two');
            break;
        default:
            message('nothing was matched');
    }
}

function message(msg){
    document.querySelector('h2').innerHTML = msg;
}

