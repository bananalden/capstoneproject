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
                       
                    </div>
                </div>
                    `;
                    $("#newsfeed").append(newsComponent);
                    })
                }

                $("#pagination").html(`
                    <button id="prevPage" class="btn" ${response.page == 1 ? "disabled" : ""}>Previous</button>
                    <span> Page ${response.page} of ${response.total_pages} </span>
                    <button id="nextPage" class="btn" ${response.page == response.total_pages ? "disabled" : ""}>Next</button>
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

    $("#form").submit(function(){
        if ($.trim($("#title-announcement").val()) == "" || $.trim($("#tweetInput").val()) == ""){
            alert("Fields are empty, please fill them when making an announcement!")
            return false;
        }
    });

    $("#pagination").on("click", "#nextPage", function() {
        currentPage++;
        loadNews(currentPage);
    });

    $("#sort-filter").on("change",function(){
        console.log("I changed!")
        var currentPage = 1
        var searchValue = $("#search-input").val()
        var sort = $("#sort-filter").val()
        loadNews(currentPage, searchValue, sort)
    })
});


