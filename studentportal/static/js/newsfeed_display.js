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
                        <div class="news-item" data-date="${newsItem.formatted_date}">
                            <h2>${newsItem.title}</h2>
                            <p>${newsItem.body}</p>
                            <span class="date">${newsItem.formatted_date}</span>
                            <p><strong>Author:</strong> ${newsItem.author}</p>
                        </div>
                    `;
                    $("#newsfeed").append(newsComponent);
                });


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
});


