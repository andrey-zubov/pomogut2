$('document').ready( function(){
    $('#id_phone').on('input',function(){
        var phone = $('#id_phone').val()
        $.ajax({url:'/pomog/widget_form_connect_with_us/',
                data:{'phone':phone, 'email':'123'},
                success:function(data){
                    if (data == 'error_email'){
                        $('#id_phone').css({'border': '2px solid #BDC3C7'})
                    }else{
                        $('#id_phone').css({'border': '2px solid #ff0000'})
                    }
                }})
    })
})