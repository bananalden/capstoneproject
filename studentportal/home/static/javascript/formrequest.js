$(document).ready(function (){
    $('.otherpurpose').hide();

    $('#purpose-select').change(function (){
        if ($('#purpose-select').val() == "OTHER"){
            $('.otherpurpose').show();
        }
    })
});