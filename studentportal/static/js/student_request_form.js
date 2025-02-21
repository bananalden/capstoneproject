$(document).ready(function (){
    $("#payment_other").hide()
    $("#transaction option[value='']").prop("disabled", true);

    $("#transaction").change(function(){
 
        if ($(this).val() == "OTHER"){
            $("#payment_other").show()
            $("#payment_purpose_other").attr("required", true)
        }
        else{
            $("#payment_other").hide()
            $("#payment_purpose_other").removeAttr("required")
        }
    })
  

        
        
    })
