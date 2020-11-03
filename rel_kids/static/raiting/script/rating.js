$(document).on('ready', function() {

  $(".my-rating").starRating({
    starSize:50,
    totalStars: 5,
    strokeColor: 'gold',
    strokeWidth:80,
    strokeLoction:"inside",
    starShape: 'rounded',
    emptyColor: '#00AEEF',
    hoverColor: 'gold',
    activeColor: 'gold',
    ratedColor:'gold',
    disableAfterRate:false,
    useGradient: false,
    useFullStars:true

  });

})
