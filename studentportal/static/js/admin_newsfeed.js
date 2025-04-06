$(document).ready(function(){
    let currentPage = 1;  // Track current page

    function loadNews(page) {
        $("#newsfeed").html('<div id="loading-spinner">Loading news... <span class="spinner"></span></div>');

        $.ajax({
            url: `/api/get-news-page/?page=${page}`, 
            type: "GET",
            dataType: "json",
            success: function(response) {
                $("#loading-spinner").remove();
                $("#newsfeed").empty();

                response.news.forEach(function(newsItem) {
                    var newsComponent = `
                    <div class="announcement_list">
                    <div class="announcement_item" data-teacher="Ms. Reyes">
                        <h3 class="announcement_title">
                            <a href="#" class="announcement_link">${newsItem.title}</a>
                        </h3>
                        <p class="announcement_description">
                            ${newsItem.body}
                        </p>
                        <p class="announcement_post_info">Posted: ${newsItem.formatted_date} | Posted by: ${newsItem.author}</p>
                        <button type="button" class="btn edit-newsfeed" data-bs-toggle="modal" data-id="${newsItem.id}" data-bs-target="#edit-newsitem">Edit</button>
                        <button type="button" class="btn delete-newsfeed" data-bs-toggle="modal" data-id="${newsItem.id}" data-bs-target="#delete-newsitem">Delete</button>
                    </div>
                </div>
                    `;
                    $("#newsfeed").append(newsComponent);
                });


                $("#pagination").html(`
                    <button class="btn" id="prevPage" ${response.page == 1 ? "disabled" : ""}>Previous</button>
                    <span> Page ${response.page} of ${response.total_pages} </span>
                    <button class="btn" id="nextPage" ${response.page == response.total_pages ? "disabled" : ""}>Next</button>
                `);
            },
            error: function() {
                $("#newsfeed").html("<p>Failed to load news.</p>");
            }
        });
    }


    loadNews(currentPage);

    $("#pagination").on("click", "#prevPage", function() {
        if (currentPage > 1) {
            currentPage--;
            loadNews(currentPage);
        }
    });


    $("#pagination").on("click", "#nextPage", function() {
        currentPage++;
        loadNews(currentPage);
    });
});

$(document).on("click",".edit-newsfeed", function(){
    var newsID = $(this).data("id")

    console.log(newsID)
    $("#newsID").val(newsID)

    $.ajax({
        url:`/api/get-news-object/${newsID}`,
        type: "GET",
        dataType: "json",
        success: function(data){

            $("#title_edit").val(data.title)
            $("#body_edit").val(data.body)

        }
    })
})

$(document).on("click",".delete-newsfeed", function(){
    var newsID = $(this).data("id")
    console.log(newsID)
    $("#deleteID").val(newsID)

   
})