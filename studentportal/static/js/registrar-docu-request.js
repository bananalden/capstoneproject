$(document).ready(function(){
    $("#enrollment-goodmorale").hide()
    $('#document-type').change(function(){
        let selected_input = $(this).val()
        
        if(selected_input=="coe"){
            $("#enrollment-goodmorale").show()
            console.log("Certificate of Enrollment")
        }
        else if(selected_input=="gm"){
            $("#enrollment-goodmorale").show()
            console.log("Certificate of Good Morale")
            
        }
        
        else if(selected_input=="cog"){
            console.log("Certificate of Grades")

        }
    })
})