$(document).ready(function(){
   $("#course_input").hide()


    $("#userType").change(function(){
        var selectedType = $(this).val()

        if (selectedType == "STUDENT"){
            $("#course_input").show()
            $("#course-field").attr("required","required")
            $("#username_label").text("USN:")
            $("#userName").attr("placeholder","Enter USN")
        }
        else{
            $("#course_input").hide()
            $("#course-field").removeAttr("required")
            $("#username_label").text("Username:")
            $("#userName").attr("placeholder","Enter username")
        }
    })
})