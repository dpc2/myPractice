const url = "http://cors-anywhere.herokuapp.com/https://randomuser.me/api/?results=10";
const output = document.getElementById("output");

fetch(url).then(function(response){
    return response.json()
}).then(function(data){
    console.log(data);

    let person = data.results[5].name;
    output.innerHTML = person.first + " " + person.last;
})
