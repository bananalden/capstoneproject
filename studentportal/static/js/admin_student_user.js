$(document).ready(function(){
    let currentPage = 1;
    let searchQuery = ""

    function load_students(page = 1, query=""){
        $(".student-list").html('<tr><td colspan="4">Loading student users...</td></tr>')
        $.ajax({
            url:`/api/get-students/?page=${page}&q=${query}`,
            type: "GET",
            dataType: "json",
            success: function(response){
                var student_user = response.student_list
                var table_body = $(".student-list")
                table_body.empty()

                if (student_user.length == 0){
                    table_body.append('<tr><td colspan="4">No student found...</td></tr>')
                }
                else{
                    $.each(student_user, function(index,student_user){
                        table_body.append(`
                            <tr>
                                <td>${student_user.first_name} ${student_user.last_name}</td>
                                <td>${student_user.username}</td>
                                <td>${student_user.email}</td>
                        <td>
                                <div class="buttons">
                                    <button class="action-btn edit-btn edit-data" data-id="${student_user.id}" data-bs-toggle="modal" data-bs-target="#editCourse">
                                        <i class="fas fa-edit"></i> Edit
                                    </button>
                                    <button type="button" data-id="${student_user.id}" class="action-btn delete-btn delete-data" data-bs-toggle="modal" data-bs-target="#deleteCourse">
                                        <i class="fas fa-trash-alt"></i> Delete
                                    </button>
                                </div>
                        </td>
                            </tr>

                            `)
                    })
                }
                $("#pagination").html(`
                    <button id="prev-btn" class="btn pagination-btn prev-btn" aria-label="Previous page" ${response.page == 1 ? "disabled" : ""}>Previous</button>
                    <span> Page ${response.page} of ${response.total_pages} </span>
                    <button id="next-btn" class="btn pagination-btn next-btn" aria-label="Next page" ${response.page == response.total_pages ? "disabled" : ""}>Next</button>
                    `)

            },
            error: function(){
                table_body.html('<tr><td colspan="4">Could not load cashiers...</td></tr>')
            }

        })
        //END OF AJAX
    }
    load_students()

    $("#pagination").on("click","#next-btn", function(){
        var searchVal = $("#search-course").val();
        currentPage++
        load_students(currentPage,searchVal)
    });
    
    $("#pagination").on("click","#prev-btn", function(){
        var searchVal = $("#search-course").val();
        if (currentPage > 1){
            currentPage--;
            load_students(currentPage, searchVal)
        }
        
    })
    
    $("#search-button").on("click", function(){
        var searchVal = $("#search-course").val();
        load_students(currentPage, searchVal)

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

