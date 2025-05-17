$(document).ready(function(){
   $("#course_input").hide()
   


    $("#userType").change(function(){
        var selectedType = $(this).val()
        var randomstring = Math.random().toString(36).slice(-8)
        if (selectedType == "STUDENT"){
            $("#course_input").show()
            $("#course-field").attr("required","required")
            $("#username_label").text("USN:")
            $("#userName").attr("placeholder","Enter USN")
            $("#password").val(randomstring)
        }
        else{
            $("#course_input").hide()
            $("#course-field").removeAttr("required")
            $("#username_label").text("Username:")
            $("#userName").attr("placeholder","Enter username")
            $("#password").val(randomstring)
        }
    })
})