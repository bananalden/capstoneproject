$(document).ready(function (){
    $('.edit-btn').on('click', function(){

        $tr =$(this).closest('tr')
        var data = $tr.children('td').map(function(){
            return $(this).text();
        })
            console.log(data)
            $('#editcoursename').val(data[1]);
    })



})