$('document').ready(function(){
		$('button.btn.center-block').on('click', function(){
			if(grecaptcha.getResponse()){
				$('.g-recaptcha').css( {'border': '2px solid #ffffff'})
				if($('input#checkbox-id').is( ":checked" )){
					$('label#checkbox-id2').css({'border': '2px solid #ffffff'})
					if($('input#phone').val()){
						$('input#phone').css({'border': '2px solid #BDC3C7'})
						if($('input#email').val()){
							$('input#email').css({'border': '2px solid #BDC3C7'})
							if($('input#name').val()){
								$('input#name').css({'border': '2px solid #BDC3C7'})
								$.ajax({
									url:'/pomog/widget_form_connect_with_us/',
									data:{'name':$('input#name').val(),
										 'email':$('input#email').val(),
										 'phone':$('input#phone').val(),
										 'sell':$('select#sel1').find('option:selected').text(),
										 'comment':$('textarea#comment').val()},
									success:function(data){
										if(data == 'error_email'){
											$('input#email').css({'border': '2px solid #ff0000'})
										}else{
											$('input#email').css({'border': '2px solid #BDC3C7'})
											if(data == 'error_phone'){
												$('input#phone').css({'border': '2px solid #ff0000'})
											}else{
												$('input#phone').css({'border': '2px solid #BDC3C7'})
												$('input#name').val('')
												$('input#email').val('')
												$('input#phone').val('')
												$('textarea#comment').val('')
												grecaptcha.reset()
												$('input#checkbox-id').prop('checked', false)
												$('#btn-hidden-for-modal').trigger( "click" )
											}
										}
									}
								})
							}else{
								$('input#name').css({'border': '2px solid #ff0000'})
							}
						}else{
							$('input#email').css({'border': '2px solid #ff0000'})
						}
					}else{
						$('input#phone').css({'border': '2px solid #ff0000'})
					}
				}else{
					$('label#checkbox-id2').css({'border': '2px solid #ff0000'})
				}
			}else{
				$('.g-recaptcha').css({'border': '2px solid #ff0000'})
			}
		})
	})