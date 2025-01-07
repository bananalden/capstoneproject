//EDIT MODAL POPULATION
$(document).ready(function (){
    $('.edit-btn').on('click', function(){
        var itemID = $(this).data('id');

        console.log(itemID)

        $.ajax({
            url: '/schoolmanagement/get-course-data/' + itemID,
            type: 'GET',
            dataType: 'json',
            success: function(data){
               
              
                $('#course_id').val(itemID),
                $('#course_name').val(data.name)
            },
            error: function(){
                console.log('Got the wrong URL?')
            }




        })
    })

})

$(document).ready(function (){
    $('.delete-btn').on('click', function(){
        var itemID = $(this).data('id');

        console.log(itemID)
        $('#delete_id').val(itemID)

        })
    })

