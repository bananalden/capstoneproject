$(document).ready(function(){
    $("#newsfeed").html('<div id="loading-spinner">Loading news... <span class="spinner"></span></div>');

    $.ajax({
        url: "/api/get-news/",
        type: "GET",
        dataType: "json",
        success: function(data) {
            $("#loading-spinner").remove();
            data.forEach(function(newsItem) {
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
        },
        error: function() {
            $("#loading-spinner").html("<p>Failed to load news.</p>");
        }
    });
});