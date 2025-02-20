
$(document).ready(function (){
    $('.btn-review').on('click', function(){
        var itemID = $(this).data('id');

        $.ajax({
            url: `/api/get-payment-data/${itemID}`,
            type: "GET",
            dataType: "json",
            success: function(data){
                var paymentProof = `
                <div class="review-payment-header">
                    <img src="${data.payment_proof}" alt="Payment Proof" />
                    <p><strong>Payment Purpose:</strong> ${data.payment_purpose}</p>
                </div>
                `
                var studentInfo = `
                    <div class="review-student-info">
                        <p><strong>Student USN:</strong> ${data.student_usn}</p>
                        <p><strong>Student Name:</strong> ${data.student_name}</p>
                    </div>
                `
                $('#student-info').append(studentInfo)
                $('#payment-proof').append(paymentProof)


            },
            error: function(){
                console.log("Uh oh poopoo")
            }
        })

      

 })

 $('.modal').on('hidden.bs.modal', function () {
    $('#student-info').empty();  // Clears all appended content
    $('#payment-proof').empty(); // Clears all appended content
});

})


