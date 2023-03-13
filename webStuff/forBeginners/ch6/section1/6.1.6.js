var myObj = {
    "people": [
        {
            "firstName": "Mike",
            "lastName": "Smith",
            "age": 30
        },
        {
            "firstName": "John",
            "lastName": "Jones",
            "age": 40
        },
        {
            "firstName": "Linda",
            "lastName": "JonesSmith",
            "age": 50
        },
        {
            "firstName": "Steve",
            "lastName": "SmithJones",
            "age": 45
        }
    ],
    "places": [
        {
        "location": "Toronto",
        "lat": 87,
        "long": 140
        },
        {
        "location": "New York",
        "lat": 65,
        "long": 110
        }
    ]
};

console.log(myObj);

var nameVar = "Name";
var output1 = document.getElementById("output1");
var output2 = document.getElementById("output2");


for (i=0; i < myObj.people.length; i++){
    output1.innerHTML += "<br>" + myObj.people[i].firstName + " " + myObj.people[i].lastName;
}

for (i=0; i < myObj.places.length; i++){
    output2.innerHTML += "<br>" + myObj.places[i].location + " Lat: " + myObj.places[i].lat + " Long: " + myObj.places[i].long;
}


var myTemplate = {
    "firstName": "Hello",
    "lastName": "World",
    "age": 40
}

myObj.people.push(myTemplate);