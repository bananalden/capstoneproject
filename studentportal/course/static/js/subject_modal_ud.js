//EDIT MODAL POPULATION
$(document).ready(function (){
    $('.edit-btn').on('click', function(){
        var itemID = $(this).data('id');

        console.log(itemID)

        $.ajax({
            url: '/schoolmanagement/get-subject-data/' + itemID,
            type: 'GET',
            dataType: 'json',
            success: function(data){
               
              console.log(data.id)
              console.log(data.name)
              console.log(data.course_id)
              console.log(data.semester_id)

              $('#name').val(data.name)
              $('#edit_id').val(itemID)
                
            },
            error: function(){
                console.log('Got the wrong URL?')
            }

        }) 
    })

})

//EDIT MODAL POPULATION
$(document).ready(function (){
    $('.delete-btn').on('click', function(){
        var itemID = $(this).data('id');

        $('#delete_id').val(itemID)

      
    })

})
