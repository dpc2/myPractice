var el1 = document.querySelector('.highlight');
console.log(el1);

el1.textContent = "Hello";
el1.innerHTML = "World!";

el1.outerHTML = "HELLO <BR> WORLD!";
console.log(el1.textContent);
console.dir(el1);
