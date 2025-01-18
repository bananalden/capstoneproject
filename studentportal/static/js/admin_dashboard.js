$(document).ready(function(){
    $('#course').hide()
    $('#teacher').hide()

    $('#userType').change(function(){
        if ($('#userType').val() == "TEACHER"){
            $('#course').show().find('select').attr('required',true);
            $('#teacher').hide().find('select').removeAttr('required');
            populate_courses();
            
            
          
        }
        else if ($('#userType').val() == "STUDENT"){
            $('#course').show().find('select').attr('required',true);
            $('#teacher').show().find('select').attr('required',true);
            populate_courses()
            populate_teacher()
        }
        else{
            $('#course').hide().find('select').removeAttr('required');
            $('#teacher').hide().find('select').removeAttr('required');
            var teacherDropdown = $('#teacherDropdown')
            teacherDropdown.empty()
            var courseDropdown = $('#courseDropdown')
            courseDropdown.empty()
        }

    })
})

function populate_courses(){
    $.ajax({
        url:'/api/get-course-list',
        type: 'GET',
        dataType: 'json',
        success: function(data){
            var courseDropdown = $('#courseDropdown')
            courseDropdown.empty()
            courseDropdown.append('<option disabled selected value="">Select a course</option>')

            $.each(data,function(index,course){
                courseDropdown.append('<option value="' + course.id + '"' + '>' + course.name + '</option>')
            })

        },
        error: function(xhr, status, error){
            console.log("Couldn't get it :(")
        }
    
    })
}


function populate_teacher(){
    $.ajax({
        url:'/api/get-teacher-list',
        type:'GET',
        dataType:'json',
        success: function(data){
            var teacherDropdown = $('#teacherDropdown')
            teacherDropdown.empty()
            teacherDropdown.append('<option disabled selected value="">Select a Teacher</option>')

            $.each(data,function(index,teacher){
                teacherDropdown.append('<option value="' + teacher.id + '"' + '>' + teacher.first_name +' '+ teacher.last_name + '</option>')
            })
        
        },
        error: function(xhr,status,error){
            console.log("Couldn't get it :(")
        }
    })
}