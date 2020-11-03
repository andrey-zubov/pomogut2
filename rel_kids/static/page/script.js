$(document).ready(function(){

    $('#id_in_navigation').prop("checked", true)
    $('select#id_mediafile option').each(function(){
        if($(this).text().split('.')[1] != 'svg' & $(this).text().split('.')[1] != 'jpg' & $(this).text().split('.')[1] != 'png' & $(this).text().split('.')[1] != 'bmp' & $(this).text() != '---------')
        {$(this).remove()}
    });

	$("select#id_category").attr('id', "id_category1")
	$("select#id_category1").removeAttr('name')
	$('select#id_category1').parent()
	.append("<label for='category1'>Раздел</label><select multiple='multiple' name='category' id='id_category2'></select><label for='category'>Категория</label><select multiple='multiple' name='category' id='id_category3'></select><label for='category'>Тег</label>")
	function empty(){
	    function add_content_by_ajax(data, url, selectname){
	    	    $.ajax({
			        type:'GET',
			        url:url,
			        data:data,
			        dataType:'text',
			        success:function(data){
			            data = JSON.parse(data)
			            $(selectname).find('option').remove().end()
			            $.each(data, function(key, value){
			                $(selectname).append('<option value=' + value + '>' + key + '</option>')
			            })
			        }
			    })
	    }

	    add_content_by_ajax({"lvl":0}, "/pomog/category1/", "select#id_category1")

	    $('select#id_category1').on('click', function(){
	    	$("select#id_category3").find('option').remove().end()
	        var selectedCategory = [];
	        $.each($("select#id_category1 option:selected"), function(){
		        selectedCategory.push($(this).val());
		    });
		    selectedCategory = JSON.stringify(selectedCategory)
		    add_content_by_ajax({"categories": selectedCategory}, "/pomog/category2/", "select#id_category2")
	    })

	    $("select#id_category2").on("click",function(){
	        var selectedCategory = [];
	        $.each($("select#id_category2 option:selected"), function(){
	            selectedCategory.push($(this).val());
	        });
	        selectedCategory = JSON.stringify(selectedCategory)
	        add_content_by_ajax({"categories": selectedCategory}, "/pomog/category2/", "select#id_category3")
	    })
	}

	function full(){
		$("select#id_category1").find('option').remove().end()
		var slug = $('input#id_slug').val();
		$.ajax({
			type:"GET",
			url:"/pomog/getcategory/",
			data:{"slug": slug},
			dataType:'text',
			success:function(data){
				data = JSON.parse(data)
				$.each(data, function(element, value){
					$.each(value, function(key,value){
						$(element).append('<option value=' + value + '>' + key + '</option>')
						$(element + " option[value=" + value + "]").prop('selected', true);
					})
				})
			}
		})
	}

    if ($('input#id_title').val()){
		full()
		empty()
	}else{
		empty()
	}
	$("label.required[for=id_category]").html("Раздел - Категория - Тег");
	$("label[for=id_mediafile]").html("Материалы")
})