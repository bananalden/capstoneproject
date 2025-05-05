
$(document).ready(function (){
    $('.btn-review').on('click', function(){
        var itemID = $(this).data('id');
        console.log(itemID)
        
        $("#loadingSpinner").show();
        $("#student-info").html(""); // Clear old content
        $("#preview-payment-header").html("");

        $.ajax({
            url: `/api/get-payment-data/${itemID}`,
            type: "GET",
            dataType: "json",
            success: function(data){
                var paymentProof = `
                <div class="review-payment-header">
                    <img src="${data.payment_proof}"  alt="Payment Proof"  style="height:800px; border: solid 1px black;"/>
                </div>
                `
                var studentInfo = `
                    <div class="review-student-info">
                        <p><strong>Student USN:</strong> ${data.student_usn}</p>
                        <p><strong>Student Name:</strong> ${data.student_name}</p>
                    </div>
                `
                $('#student-info').html(studentInfo);
                $('#payment-proof').html(paymentProof)


            },
            error: function(){
                console.log("Uh oh poopoo")
            }
        })

      

 })


})


