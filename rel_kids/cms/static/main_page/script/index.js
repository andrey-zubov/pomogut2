$(document).on('ready', function() {

  jQuery(function($) {
    function fix_size() {
      var images = $('.block-1 .col .block-1-img img');
      images.each(setsize);

      function setsize() {
        var img = $(this),
          img_dom = img.get(0),
          container = img.parents('.block-1 .col .block-1-img ');
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
      var images = $('.sections .container .row div a .inside-block-section img');
      images.each(setsize);

      function setsize() {
        var img = $(this),
          img_dom = img.get(0),
          container = img.parents('.sections .container .row div a .inside-block-section');
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
      var images = $('.block-2 .container .block-2-img  r img');
      images.each(setsize);

      function setsize() {
        var img = $(this),
          img_dom = img.get(0),
          container = img.parents('.block-2 .container .block-2-img');
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

});
