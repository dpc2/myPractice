var output1 = document.getElementById("output1");
var output2 = document.getElementById("output2");


var temp = {
    "firstName": "John",
    "lastName": "Doe",
    "age": 40
}

var tempString = JSON.stringify(temp);
console.log("My stringified object: \n" + tempString);

// localStorage.setItem('test', tempString);
var tempObj = localStorage.getItem('test');

var obj2 = JSON.parse(tempObj);
console.log("My parsed object:");
console.log(obj2);

output1.innerHTML = obj2.firstName;