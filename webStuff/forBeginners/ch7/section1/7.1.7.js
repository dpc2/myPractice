$("h1").click(function(){
    console.log("Click!");
    //$("h1").text("Clicked");
    $(this).text("Clicked");
});

$("li").click(function(){
    console.log("Clicky click!");

    // All li's are affected by this:
    //$("li").text("Clicked");

    console.log($(this));
    $(this).text("Clicked");
    //$(this).addClass("green");
    $(this).toggleClass("green");

});