$(document).ready(function(){

    $("#payment_purpose").hide()
    $("#transaction option[value='']").prop("disabled", true);

    $("#transaction").change(function(){
        let selection = $(this).val()

        if (selection == "OTHER"){
            $("#payment_purpose").show()
            $("#payment_purpose_other").attr("required", true)
        }

        else{
            $("#payment_purpose").hide()
            $("#payment_purpose_other").removeAttr("required")
        }
        


    })

})