//EDIT MODAL POPULATION
$(document).ready(function (){
    $('.edit-btn').on('click', function(){
        var itemID = $(this).data('id');

        console.log(itemID)

        $.ajax({
            url: '/api/get-user-object/' + itemID,
            type: 'GET',
            dataType: 'json',
            success: function(data){
                console.log("Populated data")
               $('#edit_id').val(itemID)
               $('#first_name').val(data.first_name)
               $('#last_name').val(data.last_name)
               $('#email').val(data.email)
               $('#username').val(data.username)
                populate_courses_(data.course_id)
            },
            error: function(){
                console.log('Got the wrong URL?')
            }

        })
    })

})

function get_course_from_profile(courseprofileid){
    $.ajax({
        url:'/api/get-teacher-profile/' + courseprofileid,
        type: 'GET',
        dataType: 'json',
        success: function(data){
            course_profile_id = data.course_id
            console.log("Found it! :D ", data.course_id)
        },
        error: function(){
            console.log("can't find the user profiel :(")
        }
    })

return course_profile_id
}



function populate_courses_(courseSelected){
    $.ajax({
        url: '/api/get-course-list',
        type: 'GET',
        dataType: 'json',
        success: function(data){
            var selectCourse = $('#course')
            selectCourse.empty()
            selectCourse.append('<option disabled value="">-----</option>');

            $.each(data, function(index, course){
                var isSelected = course.id == courseSelected ? 'selected' : ''
                selectCourse.append('<option value="' + course.id + '"' + isSelected + '>' + course.name + '</option>')
            })
        }


    })
}


$(document).ready(function (){
    $('.delete-btn').on('click', function(){
        var itemID = $(this).data('id');

        console.log(itemID)
        $('#delete_id').val(itemID)

        })
    })
