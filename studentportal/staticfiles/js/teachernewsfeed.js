function sortNews() {
  const sortOption = document.getElementById("sort-filter").value;
  const newsFeed = document.querySelector(".newsfeed");
  const newsItems = Array.from(document.querySelectorAll(".news-item"));
  const now = new Date();

  newsItems.sort((a, b) => {
      const dateA = new Date(a.dataset.date);
      const dateB = new Date(b.dataset.date);

      if (sortOption === "new") {
          return Math.abs(now - dateA) - Math.abs(now - dateB);
      } 
      if (sortOption === "recent") {
          return dateB - dateA;
      } 
      if (sortOption === "relevant") {
          return b.textContent.length - a.textContent.length;
      }
  });

  newsFeed.innerHTML = "";
  newsItems.forEach(item => newsFeed.appendChild(item));
}
