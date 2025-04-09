//EDIT MODAL POPULATION



//TABLE DATA START
$(document).ready(function (){
    let currentPage= 1;
    let searchQuery = "";

   



    function loadGrades(page = 1, query= "", semester=""){
        $(".table-tbody").html('<tr class="table-tr"><td colspan="7">Loading grades...</td></tr>');
        $.ajax({
            url:`/api/get-grades/?page=${page}&q=${query}&filter=${semester}`,
            type: "GET",
            dataType: "json",
            success: function(response){
                var grade_list = response.grade;
                var table_body = $(".grade-data")
                table_body.empty()
                
                if (grade_list.length == 0){
                    table_body.append('<tr class="table-tr"><td colspan="7">No grades found...</td></tr>')
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
                                    <button class="unique-btn unique-btn-view registrar-view-button edit-grade"  data-id="${grade_list.id}" data-bs-toggle="modal" data-bs-target="#editGrade">
                                        <i class="fas fa-pen-to-square view-icon"></i>
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
   
    $("#registrar-pagination").on("click", "#next-btn", function() {
        var semester = $("#filter-request").val()
        var searchVal = $("#registrar-search-request").val()
        currentPage++;
        loadGrades(currentPage, searchVal,semester);
    
    });
  

    $("#registrar-pagination").on("click", "#prev-btn", function() {
        var semester = $("#filter-request").val()
        var searchVal = $("#registrar-search-request").val()
        if (currentPage > 1) {
            currentPage--;
            loadGrades(currentPage,searchVal,semester);
        }
    });

    $("#searchButton").on("click", function(){
        var semester = $("#filter-request").val()
        var searchVal = $("#registrar-search-request").val()
        var currentPage = 1
        loadGrades(currentPage, searchVal,semester)
    })
    
    $("#filter-request").on("change",function(){
        var semester = $("#filter-request").val()
        console.log(semester)
        var currentPage = 1
        var searchVal = $("#searchInput").val()
        loadGrades(currentPage,searchVal,semester)
    })





})

$(document).on("click", ".edit-grade", function(){
    var gradeID = $(this).data("id")

    $("#gradeID").val(gradeID)
    $.ajax({
        url:`/api/get-grade-object/${gradeID}`,
        type: "GET",
        dataType: "json "
        //success: function(data){},
        
    })
})

//TABLE DATA END

