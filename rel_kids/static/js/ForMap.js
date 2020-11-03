ymaps.ready(init);

function init () {
    var myMap = new ymaps.Map('map', {
            center: [53.76, 27.64],
            zoom: 10
        }, {
            searchControlProvider: 'yandex#search'
        }),
        objectManager = new ymaps.ObjectManager({
            geoObjectOpenBalloonOnClick: true
        });

    myMap.geoObjects.add(objectManager);


    $.ajax({
        url: "/pomog/get_data_map/"
    }).done(function(data) {
            objectManager.add(data);
        });
}