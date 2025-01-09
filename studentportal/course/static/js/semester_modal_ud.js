$(document).ready(function (){
    $('.edit-btn').on('click', function(){
        var itemID = $(this).data('id');


        $.ajax({
            url: '/schoolmanagement/get-semester-data/' + itemID,
            type: 'GET',
            dataType: 'json',
            success: function(data){
               
                $('#semester_id').val(itemID),
                $('#semester_code').val(data.semester_code)
                $('#year').val(data.year)

                populate_courses_(data.course_id)
            },
            error: function(){
                console.log('Got the wrong URL?')
            }

        })
    })
})

function populate_courses_(courseSelected){
    $.ajax({
        url: '/schoolmanagement/api/courses',
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

