$(document).ready(function (){
    $("#transaction option[value=''").prop("disabled",true)
    $('#transaction').change(function(){
        let selected_value = $(this).val();

        $.ajax({
            url: '/api/get-payment-purpose/' + selected_value,
            type: 'GET',
            dataType: 'json',
            success: function(data){
                let selected_value = data.payment_purpose.toLowerCase()
                if (selected_value.includes("tuition")){
                    $(".student-payment-info strong").text("Please see your Billing Statement");
                }
                else{
                    $(".student-payment-info strong").text("₱"+`${data.payment_price}`);
                }
            }
        })
        
    })
})