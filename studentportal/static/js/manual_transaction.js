$(document).ready(function(){

    $("#payment_purpose").hide()
    $("#transaction option[value='']").prop("disabled", true);
    $("#amount_paid").prop("disabled",true)
    $("#payment_purpose_other").attr("required", true)
    
    $("#transaction").change(function(){
        var transactionType = $(this).val()
        
        switch(transactionType){
            case "TUITION FEE":
                $("#payment_purpose").hide()
                $("#amount_paid").prop("disabled",false).prop("readonly",false).val("")
                $("#payment_purpose_other").attr("required", false)

                break;
                
            case "CERTIFICATE OF GRADES":
                $("#payment_purpose").hide()
                $("#amount_paid").prop("disabled",false).prop("readonly",true).val(90)
                $("#payment_purpose_other").attr("required", false)
  
                break;
                
                
                case "CERTIFICATE OF GOOD MORALE":
                $("#payment_purpose").hide()
                $("#amount_paid").prop("disabled",false).prop("readonly",true).val(90)
                $("#payment_purpose_other").attr("required", false)

                break;
                
            case "CERTIFICATE OF ENROLLMENT":
                $("#payment_purpose").hide()
                $("#amount_paid").prop("disabled",false).prop("readonly",true).val(90)
                $("#payment_purpose_other").attr("required", false)
       
                break;
            case "OTHER":        
                $("#payment_purpose").show()
                $("#amount_paid").prop("disabled",false).prop("readonly",false).val("")
                $("#payment_purpose_other").attr("required", true)
          
                break;    

      }


    })

   /* let selection = $(this).val()

    if (selection == "OTHER"){
        $("#payment_purpose").show()
        $("#payment_purpose_other").attr("required", true)
    }

    else{
        $("#payment_purpose").hide()
        $("#payment_purpose_other").removeAttr("required")
    }
    
    */

})