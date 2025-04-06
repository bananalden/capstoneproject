$(document).ready(function(){
    let currentPage = 1;
    let searchQuery = ""

    function load_cashiers(page = 1, query=""){
        $(".cashier-list").html('<tr><td colspan="4">Loading cashier users...</td></tr>')
        $.ajax({
            url:`/api/get-cashiers/?page=${page}&q=${query}`,
            type: "GET",
            dataType: "json",
            success: function(response){
                var cashier_user = response.cashier_list
                var table_body = $(".cashier-list")
                table_body.empty()

                if (cashier_user.length == 0){
                    table_body.append('<tr><td colspan="4">No cashiers found...</td></tr>')
                }
                else{
                    $.each(cashier_user, function(index,cashier_user){
                        table_body.append(`
                            <tr>
                                <td>${cashier_user.first_name} ${cashier_user.last_name}</td>
                                <td>${cashier_user.username}</td>
                                <td>${cashier_user.email}</td>
                        <td>
                                <div class="buttons">
                                    <button class="action-btn edit-btn edit-data" data-id="${cashier_user.id}" data-bs-toggle="modal" data-bs-target="#editCourse">
                                        <i class="fas fa-edit"></i> Edit
                                    </button>
                                    <button type="button" data-id="${cashier_user.id}" class="action-btn delete-btn delete-data" data-bs-toggle="modal" data-bs-target="#deleteCourse">
                                        <i class="fas fa-trash-alt"></i> Delete
                                    </button>
                                </div>
                        </td>
                            </tr>

                            `)
                    })
                }
                $("#pagination").html(`
                    <button id="prev-btn" class="btn pagination-btn" aria-label="Previous page" ${response.page == 1 ? "disabled" : ""}>Previous</button>
                    <span> Page ${response.page} of ${response.total_pages} </span>
                    <button id="next-btn" class="btn pagination-btn" aria-label="Next page" ${response.page == response.total_pages ? "disabled" : ""}>Next</button>
                    `)

            },
            error: function(){
                table_body.html('<tr><td colspan="4">Could not load cashiers...</td></tr>')
            }

        })
        //END OF AJAX
    }
    load_cashiers()

    $("#pagination").on("click","#next-btn", function(){
        var searchVal = $("#search-course").val();
        currentPage++
        load_cashiers(currentPage,searchVal)
    });
    
    $("#pagination").on("click","#prev-btn", function(){
        var searchVal = $("#search-course").val();
        if (currentPage > 1){
            currentPage--;
            load_cashiers(currentPage, searchVal)
        }
        
    })
    
    $("#search-button").on("click", function(){
        var searchVal = $("#search-course").val();
        load_cashiers(currentPage, searchVal)

    })



})

$(document).on("click",".edit-data",function(){
    var itemID = $(this).data('id');
  

    $.ajax({
        url:`/api/get-user-object/${itemID}`,
        type:"GET",
        dataType:"json",
        success: function(data){
            $('#edit_id').val(itemID)
            $('#first_name').val(data.first_name)
            $('#last_name').val(data.last_name)
            $('#email').val(data.email)
            $('#username').val(data.username)
        },
        error: function(){
            alert("Could not GET data")
        }
    })

})


$(document).on("click",".delete-data",function(){
    var itemID = $(this).data('id');
    $('#delete_id').val(itemID)
   

})

