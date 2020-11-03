

$(document).on('ready', function() {
  /////////////////////////////////////////////////////////////////   //for you


////////////////////////////////////////////////////////////////////////////////
  $('.go_to').click( function(){ // ловим клик по ссылке с классом go_to
 	var scroll_el = $(this).attr('href'); // возьмем содержимое атрибута href, должен быть селектором, т.е. например начинаться с # или .
         if ($(scroll_el).length != 0) { // проверим существование элемента чтобы избежать ошибки
 	    $('html, body').animate({ scrollTop: $(scroll_el).offset().top }, 800); // анимируем скроолинг к элементу scroll_el
         }
 	    return false; // выключаем стандартное действие
     });
     jQuery(function($) {
       function fix_size() {
         var images = $('.project-1-slider .main-section-wave .image-wave .under-image-wave-background img');
         images.each(setsize);

         function setsize() {
           var img = $(this),
             img_dom = img.get(0),
             container = img.parents('.project-1-slider .main-section-wave .image-wave .under-image-wave-background');
           if (img_dom.complete) {
             resize();
           } else img.one('load', resize);

           function resize() {
             if ((container.width() / container.height()) < (img_dom.width / img_dom.height)) {
               img.width('100%');
               img.height('auto');
               return;
             }
             img.height('100%');
             img.width('auto');
           }
         }
       }
       $(window).on('resize', fix_size);
       fix_size();
     });
     jQuery(function($) {
       function fix_size() {
         var images = $('.project-2-slider .main-section-wave .image-wave .under-image-wave-background img');
         images.each(setsize);

         function setsize() {
           var img = $(this),
             img_dom = img.get(0),
             container = img.parents('.project-2-slider .main-section-wave .image-wave .under-image-wave-background');
           if (img_dom.complete) {
             resize();
           } else img.one('load', resize);

           function resize() {
             if ((container.width() / container.height()) < (img_dom.width / img_dom.height)) {
               img.width('100%');
               img.height('auto');
               return;
             }
             img.height('100%');
             img.width('auto');
           }
         }
       }
       $(window).on('resize', fix_size);
       fix_size();
     });
  $('.project-1-slider').slick({
    dots: false,
    infinite: false,
    speed: 200,
    variableWidth: true,
    slidesToShow: 2,
    slidesToScroll: 1,
    arrows: false,
    responsive: [

    {
      breakpoint: 768,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1

      }
    }
  ]


      // You can unslick at a given breakpoint now by adding:
      // settings: "unslick"
      // instead of a settings object

  });
  $('.project-2-slider').slick({
    dots: false,
    infinite: false,
    speed: 200,
    variableWidth: true,
    slidesToShow: 2,
    slidesToScroll: 1,
    arrows: false,
    responsive: [
    {
      breakpoint: 768,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1

      }
    }
  ]


  });
  $('.about-logos').slick({
    slidesToShow: 3,
    infinite: false,
    slidesToScroll: 3,
    arrows: true,
    variableWidth: true,

    responsive: [{
        breakpoint: 1199,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 3,
          infinite: false,
        }
      },
      {
        breakpoint: 991,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
          infinite: false,
        }
      },
      {
        breakpoint: 768,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
          infinite: false,
        }
      }, {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
          variableWidth: true,
          infinite: false,
        }
      },
    ]
  });
  var countSlidersProject_1= ($('.project-1-slider .slick-slide .image-wave').length-1).toString();
  var countSlidersProject_2= ($('.project-2-slider .slick-slide .image-wave').length-1).toString();
  var childrenOfProject_1=$(".project-1-slider .slick-list .slick-track").children();
    var childrenOfProject_2=$(".project-2-slider .slick-list .slick-track").children();
    $(".arrows .next-1").css("opacity","0.3");// имитация неактивной кнопик
    $(".arrows .next-2").css("opacity","0.3");//


  $('.next-1').on('click', function() {
    $('.project-1-slider').slick('slickPrev');
    $(".arrows .prev-1").css("opacity","1.0");
    for (var i = 0; i < childrenOfProject_1.length; i++) {
      if($('.project-1-slider .slick-slide').eq(i).attr("data-slick-index")=="0" && $('.project-1-slider .slick-slide').eq(i).attr("aria-hidden")=="false" ){
        $(".arrows .next-1").css("opacity","0.3");
      }
    }
  });
  $('.prev-1').on('click', function() {
    $('.project-1-slider').slick('slickNext');
    $(".arrows .next-1").css("opacity","1");
      for (var i = 0; i < childrenOfProject_1.length; i++) {
        if($('.project-1-slider .slick-slide').eq(i).attr("data-slick-index")==countSlidersProject_1 && $('.project-1-slider .slick-slide').eq(i).attr("aria-hidden")=="false" ){

          $(".arrows .prev-1").css("opacity","0.3");
        }

      }


  });
  $('.next-2').on('click', function() {
    $('.project-2-slider').slick('slickPrev');
    $(".arrows .prev-2").css("opacity","1.0");
    for (var i = 0; i < childrenOfProject_2.length; i++) {
      if($('.project-2-slider .slick-slide').eq(i).attr("data-slick-index")=="0" && $('.project-2-slider .slick-slide').eq(i).attr("aria-hidden")=="false" ){
        $(".arrows .next-2").css("opacity","0.3");
      }


    }
  });
  $('.prev-2').on('click', function() {
    $('.project-2-slider').slick('slickNext');
    $(".arrows .next-2").css("opacity","1");
      for (var i = 0; i < childrenOfProject_2.length; i++) {
        if($('.project-2-slider .slick-slide').eq(i).attr("data-slick-index")==countSlidersProject_2 && $('.project-2-slider .slick-slide').eq(i).attr("aria-hidden")=="false" ){

          $(".arrows .prev-2").css("opacity","0.3");
        }

      }
  });


  $('.g-recaptcha div div:first-child iframe').attr('style',' border:2px solid red !important');

  ///////////////////////////////////////////
$(".arrows .next-light").css("display","none");
$(".arrows .prev-light").css("display","none");

$('#my_lovely_button').on('click', function(){
        if(grecaptcha.getResponse()){
            $('.g-recaptcha div div:first-child iframe').attr('style',' border:none !important');
            if($('#email-field').val()){
                $('#email-field').css({'border': '2px solid #BDC3C7'})
                $.ajax({url:'/add_the_information/add_the_information_about_us/',
                        data:{'email':$('#email-field').val(), 'text':$('textarea').val()},
                        success:function(data){
                            if(data == 'done'){
                                $('#email-field').val('')
                                $('textarea').val('')
                                grecaptcha.reset()
                                $('#email-field').css({'border': '2px solid #ffffff'})
                                $('#btn-hidden-for-modal').trigger( "click" );
                            }else{
                                $('#email-field').css({'border': '2px solid #ff0000'})
                            }
                        }})
            }else{
                $('#email-field').css({'border': '2px solid #ff0000'})
            }
        }else{
            $('.g-recaptcha div div:first-child iframe').attr('style',' border:2px solid red !important');
        }
    })


});
