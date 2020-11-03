function reloadarticles(id){
    $.ajax({
        url:'/pomog/get_pages/',
        data:{'categories':id},
        success:function(data){
            data = JSON.parse(data)
            $('div.row.articles').empty()
            var count = 0
            $.each(data[0], function(key, val){
                count += 1
                if((count + 2) % 3 == 0){$('div.row.articles').append('<a href="/' + val[1] + '" class="col-lg-4 col-md-4 col-sm-6 col-xs-6 left header-kids"><div><img class="articles-image center-block"  width="100%" height="auto" src="' + val[0] + '" alt=""></div><div class="title-kids"><h3>' + key + '</h3></div><div class="articles-button"><p>Читать</p></div></a>')}
                if((count + 1) % 3 == 0){$('div.row.articles').append('<a href="/' + val[1] + '" class="col col-lg-4 col-md-4  col-sm-6  col-xs-6 header-teenagers"><div><img class="articles-image center-block"  width="100%" height="auto" src="' + val[0] + '" alt=""></div><div class="title-kids"><h3>' + key + '</h3></div><div class="articles-button"><p>Читать</p></div></a>')}
                if(count % 3 == 0){$('div.row.articles').append('<a href="/' + val[1] + '" class="col col-lg-4 col-md-4  col-sm-6  col-xs-6 right header-adults"><div><img class="articles-image center-block"  width="100%" height="auto" src="' + val[0] + '" alt=""></div><div class="title-kids"><h3>' + key + '</h3></div><div class="articles-button"><p>Читать</p></div></a>')}
                if(count % 6 == 0){
                    $('div.row.articles').append('<div class="col col-lg-12 col-md-12 col-sm-12   breakdown-articles center-block "><h2 class="text-center center-block">Разговор помогает! Мы здесь для вас </h2><p class="text-center center-block">Никакая проблема не является слишком большой или слишком маленькой. Мы здесь 24 часа в сутки, 7 дней в неделю</p><a  href="tel:' + data[1] + '" class="text-center breakdown-articles-buttons  center-block "><div  class="phone-number "><img src="/static/page_with_article/images/breakdown-phone.svg" alt=""><h5>' + data[1] + '</h5></div></a></div>')
                }



                jQuery(function($) {
                    function fix_size() {
                    var images = $('.articles a div img');
                    images.each(setsize);

                    function setsize() {
                    var img = $(this),
                    img_dom = img.get(0),
                    container = img.parents('.articles a div');
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










            })
            console.log(data)
        }
    })
}

$(document).on('ready', function() {
  $.ajax({
    url:'/pomog/get_girls/',
    data:{'url':window.location.pathname},
    success:function(data){
      var ajaxResult= data
      ajaxResult=JSON.parse(ajaxResult);
      var $countKeysAfterResult=Object.keys(ajaxResult).length;
      var $keysForCategories=[];
      var keysFullNames=[];
      for (var keys in ajaxResult) {
         $keysForCategories.push(keys.split(","));
         keysFullNames.push(keys);
      }
      var id_for_categories=[];
      var title_for_categories=[];
      var href_for_categories=[];
      for (var i = 0; i < $keysForCategories.length; i++) { //Запись ключей по значениям их в логике
      id_for_categories.push($keysForCategories[i][0]);
       title_for_categories.push($keysForCategories[i][1]);
       href_for_categories.push($keysForCategories[i][2]);
      }


    var $valuesForCategories=[];
    var id_for_tab=[];
    var title_for_tab=[];
    var common=[];

      $.each(ajaxResult,function(key,val){
          if (val.length){common.push(val[0].length);}
      });

    function generateAllCategories(){
      for (var i = 0; i < $countKeysAfterResult; i++) {
          $("#categories").append($(`<div id=${$keysForCategories[i][0]} ><a ><img src=${$keysForCategories[i][2]}></a><p>${$keysForCategories[i][1]}</p></div>`));
      }
    }
    function generateAllTabs(){
      $(".categories_data .for-slick").append($('<div class="row tags totalTabs"></div>'));
      $.each(ajaxResult,function(key,val){
        for (var i = 0; i < val.length; i++) {
              $('.totalTabs').append($(`<div id=${val[i][0]} title=${val[i][1]} class="tag-primary"><input type="radio"   name="radios"><label for="radio1">${val[i][1]} </label></div>`));
        }
      });
    }
    function generateCategariesTabs(){
    var counter=0;
      $.each(ajaxResult,function(key,val){
        counter++;
        $(".categories_data .for-slick").append($('<div class="row tags regularTabs"></div>'));
            for (var j = 0; j <val.length; j++) {
              $('.regularTabs').eq(counter-1).append($(`<div id=${val[j][0]} title=${val[j][1]}  class="tag-primary"><input type="radio"  name="radios"><label for="radio1">${val[j][1]} </label></div>`));
              }
      });
    }
     generateAllCategories();
    generateAllTabs();
    generateCategariesTabs()
      $(".regularTabs").css("display", "none");
      $("#categories div ").click(function() {
        var width=screen.width;
          reloadarticles($(this).attr('id'))
          var $count = $(this).index();
            $(".categories div a").css("border", "3px solid #f2f2f2");
            $(this).find("a ").css("border", "3px solid #EB3450");
          if (width<'590') {
              $('.categories_data .tags').css("display","none");
          }
          $(".regularTabs").css("display", "none");
          $(".regularTabs").eq($count).css("display", "block");
          $(".totalTabs").css("display", "none");
      })
        $(".tags div input[type=radio]+label ").click(function() {
            $(".tags div input[type=radio]+label ").css("background-color","#fff");
            $(".tags div input[type=radio]+label ").css("color","#EB3450");
            $(this).css("background-color","#EB3450");
            $(this).css("color","#fff");
        });
        $(".tag-primary ").click(function() {
            $(".tag-primary").css("background-color","#fff");
            $(this).css("background-color","#EB3450");
            reloadarticles($(this).attr('id'))
        });
        if ($(window).width()<'590') {
            $('.categories_data .tags').css("display","none");
        }     
      $('.categories').slick({
        slidesToShow: 5,
        infinite: false,
        slidesToScroll: 1,
        variableWidth: true,
        arrows: true,
        responsive: [{
            breakpoint: 1199,
            settings: {
              slidesToShow: 3,
              slidesToScroll: 1,
              infinite: false, centerMode: true,
            }
          },
          {
            breakpoint: 991,
            settings: {
              slidesToShow: 2,
              slidesToScroll: 1,
              infinite: false, centerMode: true,
            }
          },
          {
            breakpoint: 769,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1,
              infinite: false, centerMode: true,
            }
          }, {
            breakpoint: 641,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1,
              infinite: false, centerMode: true,
            }
          },
        ]
      });
      $('.tags').slick({
        dots: false,
        arrows: true,
        infinite: false,
        speed: 1500,
        slidesToShow: 3,
        slidesToScroll: 3,
        centerMode: false,
        variableWidth: true,
        responsive: [{
            breakpoint: 1199,
            settings: {
              slidesToShow: 2,
              slidesToScroll: 2,
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
          }
        ]
      });
      jQuery(function($) {
        function fix_size() {
          var images = $('.articles a div img');
          images.each(setsize);
          function setsize() {
            var img = $(this),
              img_dom = img.get(0),
              container = img.parents('.articles a div');
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
    }
  })
});