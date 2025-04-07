$(document).ready(function(){
    let currentPage = 1;
    let searchQuery = ""

    function load_teachers(page = 1, query=""){
        $(".teacher-list").html('<tr><td colspan="4">Loading teacher users...</td></tr>')
        $.ajax({
            url:`/api/get-teachers/?page=${page}&q=${query}`,
            type: "GET",
            dataType: "json",
            success: function(response){
                var teacher_user = response.teacher_list
                var table_body = $(".teacher-list")
                table_body.empty()

                if (teacher_user.length == 0){
                    table_body.append('<tr><td colspan="4">No cashiers found...</td></tr>')
                }
                else{
                    $.each(teacher_user, function(index,teacher_user){
                        table_body.append(`
                            <tr>
                                <td>${teacher_user.first_name} ${teacher_user.last_name}</td>
                                <td>${teacher_user.username}</td>
                                <td>${teacher_user.email}</td>
                        <td>
                                <div class="buttons">
                                    <button class="action-btn edit-btn edit-data" data-id="${teacher_user.id}" data-bs-toggle="modal" data-bs-target="#editCourse">
                                        <i class="fas fa-edit"></i> Edit
                                    </button>
                                    <button type="button" data-id="${teacher_user.id}" class="action-btn delete-btn delete-data" data-bs-toggle="modal" data-bs-target="#deleteCourse">
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
                table_body.html('<tr><td colspan="4">Could not load teachers...</td></tr>')
            }

        })
        //END OF AJAX
    }
    load_teachers()

    $("#pagination").on("click","#next-btn", function(){
        var searchVal = $("#search-course").val();
        currentPage++
        load_teachers(currentPage,searchVal)
    });
    
    $("#pagination").on("click","#prev-btn", function(){
        var searchVal = $("#search-course").val();
        if (currentPage > 1){
            currentPage--;
            load_teachers(currentPage, searchVal)
        }
        
    })
    
    $("#search-button").on("click", function(){
        var searchVal = $("#search-course").val();
        load_teachers(currentPage, searchVal)

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

