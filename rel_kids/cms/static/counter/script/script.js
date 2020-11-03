$(document).on('ready', function() {

  jQuery(function($) {
    function fix_size() {
      var images = $('.single-column .row div .single-column-image img');
      images.each(setsize);

      function setsize() {
        var img = $(this),
          img_dom = img.get(0),
          container = img.parents('.single-column .row div .single-column-image');
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
      var images = $('.three-column .row .three-column-group .three-column-image-section img');
      images.each(setsize);

      function setsize() {
        var img = $(this),
          img_dom = img.get(0),
          container = img.parents('.three-column .row .three-column-group .three-column-image-section');
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
      var images = $('.two-column .row div .two-column-image img');
      images.each(setsize);

      function setsize() {
        var img = $(this),
          img_dom = img.get(0),
          container = img.parents('.two-column .row div .two-column-image ');
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
  $(':radio').change(function() {
  console.log('New star rating: ' + this.value);
});
jQuery(function($) {
  function fix_size() {
    var images = $('.similar-articles .similar-articles-title ul li div .similar-articles-image img');
    images.each(setsize);

    function setsize() {
      var img = $(this),
        img_dom = img.get(0),
        container = img.parents('.similar-articles .similar-articles-title ul li div .similar-articles-image ');
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
