jQuery(document).ready(function ($) {
function img_prop() {
    $('.intro-child img').each( function(){
            if ($(this).width() < $(this).height()) {
                $(this).addClass('img-ver');
            } else {
                $(this).addClass('img-hor');
            }

    console.log('function img_prop working');
});}

$(window).on('load', img_prop);

    console.log('js working');
})