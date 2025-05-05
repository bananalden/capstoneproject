


$(document).ready(function (){
    $('.purpose-btn').on('click', function(){
        var itemID = $(this).data('id');
     $.ajax({
            url: '/api/get-payment-purpose/' + itemID,
            type: 'GET',
            dataType: 'json',
            success:function(data){
                $('#edit_id').val(itemID)
                $('#payment_purpose').val(data.payment_purpose)
                $('#payment_price').val(data.payment_price)
            },
            error:function(){

            },
        })
        console.log(itemID)
        $('#edit_id').val(itemID)
    
            })
        })


        $(document).ready(function (){
            $('.purpose-delete-btn').on('click', function(){
                var itemID = $(this).data('id');
        
               
        
                console.log(itemID)
                $('#delete_id').val(itemID)
        
                })
            })