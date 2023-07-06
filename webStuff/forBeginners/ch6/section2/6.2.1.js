const url = "http://cors-anywhere.herokuapp.com/https://randomuser.me/api/?results=10";
const output = document.getElementById("output");

fetch(url).then(response=>{
    return response.json();
}).then(data=>{

    // console.log(data);

    // for (i=0; i<data.results.length; i++){
    //     let person = data.results[i].name;
    //     console.log(person);
    //     output.innerHTML += person.first + " " + person.last + "<br>";
    // }
    
    data.results.forEach(function(person){
        console.log(person);
        var temp = person.name;
        output.innerHTML += temp.first + " " + temp.last + " " +
        "<img src=\""+ person.picture.medium + "\">" + "<br>";

        console.log(person.picture);
    })

}).catch(error=>{
    console.log(error);
})