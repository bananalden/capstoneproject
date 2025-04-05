//EDIT MODAL POPULATION



//TABLE DATA START
$(document).ready(function (){
    let currentPage= 1;
    let searchQuery = "";


   



    function loadTransactions(page = 1, query= "", semester=""){
        $(".table-tbody").html('<tr class="table-tr"><td colspan="6">Loading grades...</td></tr>');
        $.ajax({
            url:`/api/get-registrar-transaction-page/?page=${page}&q=${query}&filter=${semester}`,
            type: "GET",
            dataType: "json",
            success: function(response){
                var registrar_request = response.registrar_list;
                var table_body = $(".request-list")
                table_body.empty()
                
                if (registrar_request.length == 0){
                    table_body.append('<tr class="table-tr"><td colspan="6">No Transaction was found...</td></tr>')
                }
                else{
                    $.each(registrar_request, function(index, registrar_request){
                        table_body.append(`
                        <tr class="registrar-table-row">
                            <td class="registrar-table-data">${registrar_request.student_usn}</td>
                            <td class="registrar-table-data">${registrar_request.student_name}</td>
                            <td class="registrar-table-data">${registrar_request.payment_purpose}</td>
                            <td class="registrar-table-data">${registrar_request.date_time}</td>
                            <td class="registrar-table-data">${registrar_request.registrar_status}</td>
                            <td class="registrar-table-data actions unique-actions">
                                    <button class="unique-btn unique-btn-view registrar-view-button process-document" data-id="${registrar_request.id}" data-bs-toggle="modal" data-bs-target="#processRequest">
                                        <i class="fas fa-eye view-icon"></i>
                                    </button>
                                    <button class="unique-btn unique-btn-approve registrar-approve-button" data-id="${registrar_request.id}" data-bs-toggle="modal" data-bs-target="#approveRequest">
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
                table_body.html('<tr class="table-tr"><td colspan="8">Could not load data...</td></tr>')
            }

        });
        
        
    }

    loadTransactions()
   
    $("#registrar-pagination").on("click", "#next-btn", function() {
        var searchVal = $("#registrar-search-request").val()
        currentPage++;
        loadTransactions(currentPage,searchVal);
    
    });
  

    $("#registrar-pagination").on("click", "#prev-btn", function() {
        var searchVal = $("#registrar-search-request").val()
        if (currentPage > 1) {
            currentPage--;
            loadTransactions(currentPage,searchVal);
        }
    });

    $("#searchButton").on("click", function(){
        var searchVal = $("#registrar-search-request").val()
        var currentPage = 1
        loadTransactions(currentPage, searchVal)
    })
    
    $("#filter-purpose").on("click",function(){
        var purposeVal = $("#filter-request").val()
        console.log(purposeVal)
        var currentPage = 1
        var searchVal = $("#registrar-search-request").val()
        loadTransactions(currentPage,searchVal,purposeVal)
    })

 




})

$(document).on("click", "#process-request", function(e){
    
    e.preventDefault()

    let form = $("#certificate-form");
    let formData = new FormData(form[0]);
    let url = form.attr("action")

    $.ajax({
        url: url,
        type: "POST",
        data: formData,
        processData: false,
        contentType: false,
        xhrFields: {
            responseType:'blob'
        },
        success: function(data){
            let blob = new Blob([data], { type: "application/pdf" });
            let url = window.URL.createObjectURL(blob);
            window.open(url, "_blank");
            window.location.href = "/home/registrar/gen-cert-success/"
        },
        error: function(xhr, status, error){
            let reader = new FileReader();
            reader.onload = function(){
                let response = JSON.parse(reader.result);
                alert("An error occurred: " + response.message);
        }
        reader.readAsText(xhr.responseText)
        }
    })
})


$(document).on("click", ".registrar-approve-button",function(){
    var transID = $(this).data("id");
    console.log(transID)
    
    $.ajax({
        url:`/api/get-payment-data/${transID}`,
        type: 'GET',
        dataType:"json",
        success:function(data){
            var registrarStatus = data.registrar_status
            console.log(registrarStatus)

            if (registrarStatus != "AVAILABLE"){
                $(".complete-request").prop("disabled", true)
                $(".doc-request-message").html(`
                <p>Request has not been processed yet, please generate to set as completed.</p>
                `)
            }

            else{
                $(".complete-request").prop("disabled", false)
                $(".doc-request-message").html(`
                <input type="hidden" name="transID" value="${transID}">
                <p>Mark transaction as completed?</p>
                `) 
            }


        },
        error:function(){
            alert("Could not get Transaction data")
        }


    })

})

$(document).on("click", ".process-document",function(){
    var transID = $(this).data("id");
    
    $.ajax({
        url:`/api/get-payment-data/${transID}`,
        type: 'GET',
        dataType:"json",
        success:function(data){
            $("#transID").val(transID)
            $("#student-usn").val(data.student_usn)
            $("#student-name").val(data.student_name)
            $("#document-type").val(data.payment_purpose)
            $("#date-requested").val(data.date_time)


        },
        error:function(){
            alert("Could not get Transaction data")
        }


    })

})

//TABLE DATA END




