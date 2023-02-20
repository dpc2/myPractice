var person = {};

person.first = "Laurence";
person.last = "Svekis";

function func1(){
    console.log('hello, 1!')
}

var func2 = function(){
    console.log('hello, 2!');
}

person.message = function(){
    return 'hello ' + this.first;
}

person.age = 30;
person.alive = true;


var person1 = {
    first:'Danny',
    last:'C'
}

console.log(person1.first)
console.log(person1['first'])


//--------------------------------------------------

var guitar = {
    strings:6,
    color:'red',
    pickups:'humbucker',
    age:15,
    bodyStyle:'Strat'
}

console.log(guitar)