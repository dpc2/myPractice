var myJSON = {};

myJSON.car1 = "black"
console.log(myJSON);
myJSON.car2 = "blue"
console.log(myJSON);


var myJSON = {};

myJSON["car1"] = "black"
console.log(myJSON);
myJSON["car2"] = "blue"
console.log(myJSON);


var myJSON = {"car1": "black", "car2": "blue"};
console.log(myJSON);


var output1 = document.getElementById('output1');
var output2 = document.getElementById('output2');
var myObj = {"firstName": "Danny", "lastName": "C", "age": 31};
console.log(myObj);

output1.innerHTML = myObj.firstName;
output2.innerHTML = myObj.lastName;
output3.innerHTML = myObj.age;

// OR

var myVar = 'Name';
output2.innerHTML = myObj['last' + myVar];
