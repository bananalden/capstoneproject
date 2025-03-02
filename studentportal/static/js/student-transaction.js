//EDIT MODAL POPULATION



//TABLE DATA START
$(document).ready(function (){
    let currentPage= 1;
    let searchQuery = "";

   



    function loadTransactions(page = 1, query= "", purpose=""){
        $(".table-tbody").html('<tr class="table-tr"><td colspan="4">Loading transaction...</td></tr>');
        $.ajax({
            url:`/api/student-transaction-history/?page=${page}&q=${query}&filter=${purpose}`,
            type: "GET",
            dataType: "json",
            success: function(response){
                var transaction_list = response.transaction;
                let table_body = $(".table-tbody")
                table_body.empty()
                
                if (transaction_list.length == 0){
                    table_body.append('<tr class="table-tr"><td colspan="4">No transactions found...</td></tr>')
                }
                else{
                    $.each(transaction_list, function(index, transaction_list){
                        let registrarStatus = (transaction_list.payment_purpose == "TUITION FEE" || "OTHER") ? "-" : transaction_list.registrar_status

                        table_body.append(`
                        <tr class="table-tr">
                        <td>${transaction_list.date_time}</td>
                        <td>${transaction_list.payment_purpose}</td>
                        <td>${transaction_list.payment_purpose_other || "-" }</td>
                        <td class="confirmation-status" data-status="${transaction_list.is_confirmed ? "Confirmed" : "Not Confirmed"}">${transaction_list.is_confirmed ? "Confirmed" : "Not Confirmed"}</td>
                        <td>${registrarStatus}</td>
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

                table_body.html('<tr class="table-tr"><td colspan="4">Could not load data...</td></tr>')
            }

        });
        
        
    }

    loadTransactions()
   
    $("#second-pagination").on("click", "#nextPage", function() {
        currentPage++;
        loadTransactions(currentPage);
    
    });
  

    $("#second-pagination").on("click", "#prevPage", function() {
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
