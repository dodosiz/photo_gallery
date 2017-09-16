$(document).ready(function(){
    $('img.img-thumbnail').mouseover(function(){
        $(this).animate({
            opacity: '0.8',
        },100);
    });
    $('img.img-thumbnail').mouseout(function(){
        $(this).animate({
            opacity: '1',
        },100);
    });
})