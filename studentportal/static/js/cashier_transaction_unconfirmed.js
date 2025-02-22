//EDIT MODAL POPULATION
$(document).ready(function (){
    let currentPage= 1;
    let searchQuery = "";

    function loadTransactions(page = 1, query= ""){
        $(".table-tbody").append('<tr class="table-tr"><td colspan="7">Loading transaction...</td></tr>');
        $.ajax({
            url:`/api/get-transaction-page-unconfirmed/?page=${page}&q=${query}`,
            type: "GET",
            dataType: "json",
            success: function(response){
                var transaction_list = response.transaction;
                var table_body = $(".table-tbody")
                table_body.empty()

                if (transaction_list.length == 0){
                    table_body.append('<tr class="table-tr"><td colspan="7">No transactions found...</td></tr>')
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
                        <td>${transaction_list.is_confirmed ? "Confirmed" : "Not Confirmed"}</td>
                        <td><button class="btn btn-primary btn-review" type="button" data-bs-toggle="modal" data-bs-target="#reviewPayment" data-id="${transaction_list.id}">Review Payment </button></td>
                        </tr>`)
                    })
                    
                }
                
            }
        });
    
    }

    loadTransactions()

})

$(document).ready(function (){
  
    })

