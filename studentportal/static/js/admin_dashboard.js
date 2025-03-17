$(document).ready(function(){
   $("#course_input").hide()


    $("#userType").change(function(){
        var selectedType = $(this).val()

        if (selectedType == "STUDENT"){
            $("#course_input").show()
            $("#course-field").attr("required","required")
        }
        else{
            $("#course_input").hide()
            $("#course-field").removeAttr("required")
        }
    })
})