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
               console.log(data.id)
               console.log(data.first_name)
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

