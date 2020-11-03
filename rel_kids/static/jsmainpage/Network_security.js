$(document).ready(function(){
    $('select#id_mediafile option').each(function(){
            if($(this).text().split('.')[1] != 'svg' & $(this).text().split('.')[1] != 'jpg' & $(this).text().split('.')[1] != 'png' & $(this).text().split('.')[1] != 'bmp' & $(this).text() != '---------')
            {$(this).remove()}
        });
});