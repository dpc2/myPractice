var myStr1 = "Hello World 1...2...3...World World World";
console.log(myStr1.length);

var needleLast = myStr1.lastIndexOf('World');
console.log(needleLast);

var needleFind = myStr1.indexOf('World', 10);
console.log(needleLast);

var needleSearch = myStr1.search('World');
console.log(needleSearch);



function mySearch(srch){
    var searchResult = myStr1.indexOf(srch);
    console.log(searchResult);
    if(searchResult > -1){
        message(searchResult);
    }
    else{
        document.querySelector('h2').innerHTML = 'Not found :(';
    }
}

function message(msg){
    document.querySelector('h2').innerHTML = msg;
}