$(document).ready(function(){
    $("a").each(function(){
        if($(this).hasClass("disabled"))
            $(this).removeAttr("href");
        
    });
});