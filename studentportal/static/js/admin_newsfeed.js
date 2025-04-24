$(document).ready(function(){
    let currentPage = 1;  // Track current page

    function loadNews(page,query="",sort="desc") {
        $("#newsfeed").html('<div id="loading-spinner">Loading news... <span class="spinner"></span></div>');

        $.ajax({
            url: `/api/get-news-page/?page=${page}&q=${query}&sort=${sort}`, 
            type: "GET",
            dataType: "json",
            success: function(response) {
                var newsItems = response.news
                $("#newsfeed").empty();
                if (newsItems.length == 0){
                    var newsComponent = `
                   <div id="loading-spinner">No news... <span class="spinner"></span></div>
                    `;
                    $("#newsfeed").append(newsComponent);
                }
                else{
                    $.each(newsItems, function(index, news_list){
                        var newsComponent = `
                    <div class="announcement_list">
                    <div class="announcement_item" data-teacher="Ms. Reyes">
                        <h3 class="announcement_title">
                            <a href="#" class="announcement_link">${news_list.title}</a>
                        </h3>
                        <p class="announcement_description">
                            ${news_list.body}
                        </p>
                        <p class="announcement_post_info">Posted: ${news_list.formatted_date} | Posted by: ${news_list.author}</p>
                        <button type="button" class="btn edit-newsfeed" data-bs-toggle="modal" data-id="${news_list.id}" data-bs-target="#edit-newsitem">Edit</button>
                        <button type="button" class="btn delete-newsfeed" data-bs-toggle="modal" data-id="${news_list.id}" data-bs-target="#delete-newsitem">Delete</button>
                       
                    </div>
                </div>
                    `;
                    $("#newsfeed").append(newsComponent);
                    })
                }


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
        var searchValue = $("#search-input").val()
        var sort = $("#filterDropdown").val()
        if (currentPage > 1) {
            currentPage--;
            loadNews(currentPage,searchValue, sort);
        }
    });
    
    
    $("#pagination").on("click", "#nextPage", function() {
        var searchValue = $("#search-input").val()
        var sort = $("#filterDropdown").val()
        currentPage++;
        loadNews(currentPage, searchValue, sort);
    });

    $("#search-btn").on("click",function(){
        var currentPage = 1
        var searchValue = $("#search-input").val()
        var sort = $("#filterDropdown").val()
        loadNews(currentPage,searchValue, sort)

    })

    $("#filterDropdown").on("change",function(){
        console.log("I changed!")
        var currentPage = 1
        var searchValue = $("#search-input").val()
        var sort = $("#filterDropdown").val()
        loadNews(currentPage, searchValue, sort)
    })
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