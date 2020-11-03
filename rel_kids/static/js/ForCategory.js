$(document).ready(function(){
    $('select#id_mediafile option').each(function(){
        if($(this).text().split('.')[1] != 'svg' & $(this).text().split('.')[1] != 'jpg' & $(this).text().split('.')[1] != 'png' & $(this).text().split('.')[1] != 'bmp' & $(this).text() != '---------')
        {$(this).remove()}
    });

    function full(data){
		$.ajax({
			type:"GET",
			url:'/pomog/get_level_category/',
			data:{"element":data},
			success:function(dat){
				if (dat >= 1){
	  				$("select#id_mediafile").parent().parent().parent().hide()
	  				$("select#id_mediafile" + " option[value=" + $("select#id_mediafile").val() + "]").prop('selected', false);
	  			}else{
	  				$("select#id_mediafile").parent().parent().parent().show()
	  			}
			}
		})
	}

	function empty(){
	  	$("select#id_parent").change(function(){
	  		var element = $(this).val()
	  		$.ajax({
	  			type:'GET',
	  			url:'/pomog/get_level_category/',
	  			data:{"element":element},
	  			dataType:'text',
	  			success:function(data){
	  				if(data > -1){
	  				    $("#id_flag").parent().parent().hide()
	  				    $("#id_flag").attr('checked', false)
	  				}//////////////bool
	  			    if(element == ''){$("#id_flag").parent().parent().show()}///////////bool
	  				if (data >= 1){
	  					$("select#id_mediafile").parent().parent().parent().hide()
	  					$("select#id_mediafile" + " option[value=" + $("select#id_mediafile").val() + "]").prop('selected', false);
	  				}else{
	  					$("select#id_mediafile").parent().parent().parent().show()
	  				}
	  				if(data >= 2){
	  					$("select#id_parent :selected").prop('selected', false)
	  					$("#id_flag").parent().parent().show()///////////////////////////bool
	  					$("select#id_parent").css('border', '2.5px solid #ff0000')
	  					$("select#id_mediafile").parent().parent().parent().show()
	  				}else{
	  				    $("select#id_parent").css('border', 'none')
	  				}
	  			}
	  		})
	  	})
	}

	var data = $("select#id_parent").val()
	if (data){
		full(data)
		empty()
	}else{
		empty()
	}

});