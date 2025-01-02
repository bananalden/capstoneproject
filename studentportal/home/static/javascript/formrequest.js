$(document).ready(function (){
    $('.otherpurpose').hide();
    $('.tuition').hide();

    $('#purpose-select').change(function (){
        if ($('#purpose-select').val() == "OTHER"){
            $('.otherpurpose').show();
            $('.tuition').hide();
        }
        
        else if ($('#purpose-select').val() == "TUITION"){
            $('.tuition').show();
            $('.otherpurpose').hide();
        }
        else{
            $('.otherpurpose').hide();
            $('.tuition').hide();
        }
    })
});