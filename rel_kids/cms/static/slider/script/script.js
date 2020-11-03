$(document).on('ready', function() {
  $('.single-item').slick({
    dots: true,
    infinite: false,
      variableWidth: true,
    responsive: [  {
        breakpoint: 768,
        variableWidth: true,

      }, {
        breakpoint: 480,
        variableWidth: true,

      },
    ]
  });




});
