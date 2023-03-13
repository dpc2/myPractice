const url = "http://cors-anywhere.herokuapp.com/https://randomuser.me/api/?results=10";
const output = document.getElementById("output");

fetch(url).then(response=>{
    return response.json();
}).then(data=>{
    console.log(data);
    console.log(data.results[0].name)
}).catch(error=>{
    console.log(error);
})