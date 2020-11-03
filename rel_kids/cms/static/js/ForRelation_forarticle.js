$('document').ready(function(){
    $('select#id_pages').attr('size', 20)
    $('select#id_pages').change(function(){
        var options = []
        $('select#id_pages option:selected').each(function(){
            options.push($(this))
            if (options.length > 4){alert('Превышен порог выбраных статей. Отобразятся только первые 4.\nВыберите не более 4-х статей')}
        })
    })
})