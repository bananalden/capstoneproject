//EDIT MODAL POPULATION



//TABLE DATA START
$(document).ready(function (){
    let currentPage= 1;
    let searchQuery = "";

    function getSortOrder(){
        return $("#filterDate").val()
    }

   



    function loadTransactions(page = 1, query= "", purpose="",sort="desc"){
        $(".table-tbody").html('<tr class="table-tr"><td colspan="8">Loading transaction...</td></tr>');
        $.ajax({
            url:`/api/get-transaction-page-unconfirmed/?page=${page}&q=${query}&filter=${purpose}&sort=${sort}`,
            type: "GET",
            dataType: "json",
            success: function(response){
                var transaction_list = response.transaction;
                var table_body = $(".table-tbody")
                table_body.empty()
                
                if (transaction_list.length == 0){
                    table_body.append('<tr class="table-tr"><td colspan="8">No transactions found...</td></tr>')
                }
                else{
                    $.each(transaction_list, function(index, transaction_list){
                        table_body.append(`
                        <tr class="table-tr">
                        <td>${transaction_list.student_username}</td>
                        <td>${transaction_list.student_name}</td>
                        <td>${transaction_list.date_time}</td>
                        <td>${transaction_list.payment_purpose}</td>
                        <td>${transaction_list.payment_purpose_other || "-" }</td>
                        <td>₱${transaction_list.amount}</td>
                        <td class="confirmation-status" data-status="${transaction_list.is_confirmed ? "Confirmed" : "Not Confirmed"}">${transaction_list.is_confirmed ? "Confirmed" : "Not Confirmed"}</td>
                        <td><button class="btn btn-primary btn-review" id="btn-review" type="button" data-bs-toggle="modal" data-bs-target="#reviewPayment" data-id="${transaction_list.id}" >Review Payment </button></td>
                        </tr>`)
                    })
                }
              $("#second-pagination").html(`
                    <button class="btn" id="prevPage" ${response.page == 1 ? "disabled" : ""}>Previous</button>
                    <span> Page ${response.page} of ${response.total_pages} </span>
                    <button class="btn" id="nextPage" ${response.page == response.total_pages ? "disabled" : ""}>Next</button>
              
              
              
              `)
            },
            error: function(){
                alert("Data could not be retrieved")
                table_body.html('<tr class="table-tr"><td colspan="8">Could not load data...</td></tr>')
            }

        });
        
        
    }

    loadTransactions()
   
    $("#second-pagination").on("click", "#nextPage", function() {
        var purposeVal = $(this).val()
        var searchVal = $("#searchInput").val()
        currentPage++;
        loadTransactions(currentPage,searchVal,purposeVal);
        
    });
    
    
    $("#second-pagination").on("click", "#prevPage", function() {
        var purposeVal = $(this).val()
        var searchVal = $("#searchInput").val()
        if (currentPage > 1) {
            currentPage--;
            loadTransactions(currentPage,searchVal,purposeVal);
        }
    });
    
       // Search
       $("#searchButton").on("click", function () {
        var purposeVal = $("#filterPurpose").val();
        var searchVal = $("#searchInput").val();
        currentPage = 1;
        loadTransactions(currentPage, searchVal, purposeVal, getSortOrder());
    });

    // Filter
    $("#filterPurpose").on("change", function () {
        var purposeVal = $(this).val();
        var searchVal = $("#searchInput").val();
        currentPage = 1;
        loadTransactions(currentPage, searchVal, purposeVal, getSortOrder());
    });

    // Sort
    $("#filterDate").on("change", function () {
        var purposeVal = $("#filterPurpose").val();
        var searchVal = $("#searchInput").val();
        currentPage = 1;
        loadTransactions(currentPage, searchVal, purposeVal, getSortOrder());
    });


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

