const output = document.getElementById('output');
const testBtn = document.getElementById('testBtn');

testBtn.addEventListener('click', checkVal);

function checkVal(){
    let val = document.querySelector('input[name="myNum"]').value;
    console.log(val);
    output.innerHTML = numChecker(val);
}


function numChecker(num){
    let message;
    if(num % 2){
        message = 'Odd';
    }
    else{
        message = 'Even';
    }
    return message;

}