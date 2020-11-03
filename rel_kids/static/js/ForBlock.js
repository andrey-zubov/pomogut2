$(document).ready(function(){
	//for block
	$('select#id_picture option').each(function(){
        if($(this).text().split('.')[1] != 'svg' & $(this).text().split('.')[1] != 'jpg' & $(this).text().split('.')[1] != 'png' & $(this).text().split('.')[1] != 'bmp' & $(this).text() != '---------')
        {$(this).remove()}
    });

	$("select#id_categories").attr('size',20)
	$("select#id_pages").attr('size',20)
	$("select#id_categories").on('click', function(){
		var selectedCategory = [];
		$.each($("select#id_categories option:selected"), function(){
        selectedCategory.push($(this).val());
    });
    selectedCategory = JSON.stringify(selectedCategory)
		$.ajax({
  			type:"GET",
    		url:"/pomog/get_my_please_pages/",
    		data:{"categories":selectedCategory},
    		dataType:'text',
    		success: function (data) {
    		$("select#id_pages").find('option').remove().end()
    			data = JSON.parse(data)
    			$.each(data, function(key, value){
    				$("select#id_pages").append('<option value=' + key + '>' + value + '</option>');
    			})
   			}
		})
  	})
});
