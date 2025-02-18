

$(document).ready(function (){
    $('.delete-btn').on('click', function(){
        var itemID = $(this).data('id');

        console.log(itemID)
        $('#delete_id').val(itemID)

        })
    })

    $(document).ready(function (){
        $('.edit-btn').on('click', function(){
            var itemID = $(this).data('id');
    
            console.log(itemID)
            $('#delete_id').val(itemID)
    
            })
        })

