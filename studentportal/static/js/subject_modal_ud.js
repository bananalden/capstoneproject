//EDIT MODAL POPULATION
$(document).ready(function (){
    $('.edit-btn').on('click', function(){
        var itemID = $(this).data('id');

        console.log(itemID)

        $.ajax({
            url: '/api/get-subject-object/' + itemID,
            type: 'GET',
            dataType: 'json',
            success: function(data){
               
              console.log(data.id)
              console.log(data.name)
              console.log(data.course_id)
              console.log(data.semester_id)

              $('#name').val(data.name)
              $('#edit_id').val(itemID)
              populate_courses_(data.course_id)
              populate_semester_(data.semester_id)
                
            },
            error: function(){
                console.log('Got the wrong URL?')
            }

           

        }) 
    })

})


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


function populate_semester_(semesterSelected){
    $.ajax({
        url: '/api/get-semester-list',
        type: 'GET',
        dataType: 'json',
        success: function(data){
            var selectSemester = $('#semester')
            selectSemester.empty()
            selectSemester.append('<option disabled value="">-----</option>');

            $.each(data, function(index, semester){
                var isSelected = semester.id == semesterSelected ? 'selected' : ''
                selectSemester.append('<option value="' + semester.id + '"' + isSelected + '>' + semester.semester_code + '</option>')
            })
        }


    })

}

//EDIT MODAL POPULATION
$(document).ready(function (){
    $('.delete-btn').on('click', function(){
        var itemID = $(this).data('id');

        $('#delete_id').val(itemID)

      
    })

})
