var el1 = document.getElementsByClassName('test');
console.log(el1);
console.log(el1[0]);

var tempEl = el1[0];
console.dir(el1[0]);

tempEl.style.backgroundColor = "Green";
tempEl.style.color = "white";
tempEl.style.border = "5px dotted purple";
tempEl.style.fontSize = "40px";
tempEl.style.display = "none";
tempEl.style.display = "block";