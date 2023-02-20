var guitar = {
    strings:6,
    color:'red',
    pickups:'humbucker',
    age:15,
    bodyStyle:'Strat'
}

console.log(guitar)

document.querySelector('h2').innerHTML =
guitar.color + ' ' + guitar.bodyStyle;