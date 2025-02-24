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
  
    $(document).ready(function () {
        $("input[type='file']").change(function () {
            let fileName = $(this).val().split("\\").pop(); // Get file name
            if (fileName) {
                $("#file-name").text(fileName); // Update the span
            } else {
                $("#file-name").text("No file chosen");
            }
        });
    });
        
        
    })
