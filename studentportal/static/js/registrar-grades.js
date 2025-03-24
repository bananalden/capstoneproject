//EDIT MODAL POPULATION



//TABLE DATA START
$(document).ready(function (){
    let currentPage= 1;
    let searchQuery = "";

   



    function loadGrades(page = 1, query= "", semester=""){
        $(".table-tbody").html('<tr class="table-tr"><td colspan="8">Loading grades...</td></tr>');
        $.ajax({
            url:`/api/get-grades/?page=${page}&q=${query}&filter=${semester}`,
            type: "GET",
            dataType: "json",
            success: function(response){
                var grade_list = response.grade;
                var table_body = $(".grade-data")
                table_body.empty()
                
                if (grade_list.length == 0){
                    table_body.append('<tr class="table-tr"><td colspan="8">No grades found...</td></tr>')
                }
                else{
                    $.each(grade_list, function(index, grade_list){
                        table_body.append(`
                        <tr class="registrar-table-row">
                            <td class="registrar-table-data">${grade_list.student_usn}</td>
                            <td class="registrar-table-data">${grade_list.subject_code}</td>
                            <td class="registrar-table-data">${grade_list.subject_name}</td>
                            <td class="registrar-table-data">${grade_list.year}</td>
                            <td class="registrar-table-data">${grade_list.semester}</td>
                            <td class="registrar-table-data">${grade_list.grade_value}</td>
                            <td class="registrar-table-data actions unique-actions">
                                    <button class="unique-btn unique-btn-view registrar-view-button">
                                        <i class="fas fa-eye view-icon"></i>
                                    </button>
                                    <button class="unique-btn unique-btn-approve registrar-approve-button">
                                        <i class="fas fa-circle-check approve-icon"></i>
                                    </button>
                                    <button class="unique-btn unique-btn-reject registrar-reject-button">
                                        <i class="fas fa-ban reject-icon"></i>
                                    </button>
                            </td>
                        </tr>`)
                    })
                }
              $("#registrar-pagination").html(`
                    <button class="btn" id="prev-btn" ${response.page == 1 ? "disabled" : ""}>Previous</button>
                    <span> Page ${response.page} of ${response.total_pages} </span>
                    <button class="btn" id="next-btn" ${response.page == response.total_pages ? "disabled" : ""}>Next</button>
              
              
              
              `)
            },
            error: function(){
                alert("Data could not be retrieved")
                table_body.html('<tr class="table-tr"><td colspan="8">Could not load data...</td></tr>')
            }

        });
        
        
    }

    loadGrades()
   
    $("#second-pagination").on("click", "#next-btn", function() {
        currentPage++;
        loadGrades(currentPage);
    
    });
  

    $("#second-pagination").on("click", "#prev-btn", function() {
        if (currentPage > 1) {
            currentPage--;
            loadTransactions(currentPage);
        }
    });

    $("#searchButton").on("click", function(){
        var searchVal = $("#searchInput").val()
        var currentPage = 1
        loadTransactions(currentPage, searchVal)
    })
    
    $("#filterPurpose").on("change",function(){
        var purposeVal = $(this).val()
        var currentPage = 1
        var searchVal = $("#searchInput").val()
        loadTransactions(currentPage,searchVal,purposeVal)
    })






})


//TABLE DATA END


//REVIEW PAYMENT BUTTON START
$(document).on("click",".btn-review", function(){
    var itemID = $(this).data('id');
    console.log(itemID)
    $("#student-info").html(`<div class="spinner-border text-primary" role="status"> <span class="visually-hidden">Loading...</span></div>`); 
    $("#pay-proof").html(`<div class="spinner-border text-primary" role="status"> <span class="visually-hidden">Loading...</span></div>`); 
    $('#confirmPayment').prop("disabled",true)
    
    $("#preview-payment-header").html("");
    $.ajax({
        url: `/api/get-payment-data/${itemID}`,
            type: "GET",
            dataType: "json",
            success: function(data){
                var paymentProof = `<button type="button" class="btn btn-primary open-payment-proof" data-bs-toggle="modal" data-bs-target="#paymentPreview" data-bs-dismiss="modal"> Open Payment Proof</button>
                `
                var studentInfo = `
                <div class="review-student-info">
                <input type="hidden" name="trans_id" id="trans_id" value="${itemID}">
                <p><strong>Student USN:</strong> ${data.student_usn}</p>
                <p><strong>Student Name:</strong> ${data.student_name}</p>
                        <p><strong>Payment Purpose:</strong> ${data.payment_purpose}</p>
                        <p><strong>Amount:</strong> ₱${data.amount}</p>
                        <button type="button" class="btn btn-primary open-payment-proof" data-bs-toggle="modal" data-bs-target="#paymentPreview" data-bs-dismiss="modal"> Open Payment Proof</button>
                    </div>
                    `
                    
                    $('#confirmPayment').prop("disabled",false)
                    var payment_proof = `<img src="${data.payment_proof}" alt="Payment Proof" style="max-height: 800px; border: solid 1px black"/>`


                $('#student-info').html(studentInfo);
                $('#preview-payment-header').html(paymentProof)
                $("#pay-proof").html(payment_proof); 

                
                
            },
            error: function(){
                console.log("Data didn't load")
            }
        })

})
//REVIEW PAYMENT BUTTON END

$(document).on("click",".payment-info", function(){
    $("#student-info").html(""); 
})



$(document).on("click","#reviewPayment .btn-primary", function(){
    $('#reviewPayment').modal('hide');  // Close the "Review Payment" modal
    setTimeout(function() {
      $('#paymentPreview').modal('show');  // Open the "Proof of Payment" modal after a small delay to avoid UI glitches
    }, 200);
 
})

$(document).on("click",".proof-payment", function(){
    $('#paymentPreview').modal('hide');  // Close the "Proof of Payment" modal
    setTimeout(function() {
      $('#reviewPayment').modal('show');  // Reopen the "Review Payment" modal after a small delay
    }, 200);
})




$(document).ready(function (){
  
    })

