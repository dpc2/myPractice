$("img").attr("src",
"https://via.placeholder.com/728x90?text=TEST+TEST+12");

$("#name").val("hello! From the script");

$("input:text[name=name]").val("Hello World!");


// jQuery check boxes
// This doesn't work
$("#checkBox1").attr("checked");

// This does
$("#checkBox1").prop("checked")
console.log($("#checkBox1").prop("checked"));

$("#checkBox1").prop("checked", false);


// jQuery select elements
$("select").val("Two");
console.log($("select").val());
