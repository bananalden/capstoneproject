$(document).ready(function (){
    $("#payment_other").hide()
    $("#transaction option[value='']").prop("disabled", true);
    $("#amount_paid").prop("disabled", true)
    
    $("#transaction").change(function(){
        var transType = $(this).val()
        
        switch (transType){
            
            case "TUITION FEE":
                $("#amount_paid").prop("disabled", false).prop("readonly",false).val("")
                $("#payment_other").hide()
                $("#payment_purpose_other").removeAttr("required")
                break;
                
            case "CERTIFICATE OF GRADES":
                $("#amount_paid").prop("disabled", false).prop("readonly",true).val(90)
                $("#payment_other").hide()
                $("#payment_purpose_other").removeAttr("required") 
                break;
                
            case "CERTIFICATE OF GOOD MORALE":
                $("#amount_paid").prop("disabled", false).prop("readonly",true).val(90)
                $("#payment_other").hide()
                $("#payment_purpose_other").removeAttr("required")   
                break;
                        
            case "CERTIFICATE OF ENROLLMENT":    
                $("#amount_paid").prop("disabled", false).prop("readonly",true).val(90)
                $("#payment_other").hide()
                $("#payment_purpose_other").removeAttr("required")   
            break;
                        
            case "OTHER": 
                $("#amount_paid").prop("disabled", false).prop("readonly",false).val("")
                $("#payment_other").show()
                $("#payment_purpose_other").attr("required", true)
            break;
        }

 
    })
  
    $(document).ready(function () {
        $("#paymentproof").change(function () {
            let fileName = $(this).val().split("\\").pop(); // Get file name
            if (fileName) {
                $("#file-name").text(fileName); // Update the span
            } else {
                $("#file-name").text("No file chosen");
            }
        });
    });
        
        
    })
