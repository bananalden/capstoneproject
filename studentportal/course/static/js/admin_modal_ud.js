//EDIT MODAL POPULATION
$(document).ready(function (){
    $('.edit-btn').on('click', function(){
        var itemID = $(this).data('id');

        console.log(itemID)

        $.ajax({
            url: '/api/get-admin-object/' + itemID,
            type: 'GET',
            dataType: 'json',
            success: function(data){
                
               $('#first_name').val(data.first_name)
               $('#last_name').val(data.last_name)
               $('#email').val(data.email)
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

