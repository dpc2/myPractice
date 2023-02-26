var a = "one";  //global

function test(){
    var a = "two";  //function
}

{
    let a = "test";
    console.log(a);
}

for(let i = 0;i<5;i++){
    console.log(i);
}
for(var y=0;y<5;y++){
    console.log(y);
}

{
    let a = "test";
    a = "world";
}