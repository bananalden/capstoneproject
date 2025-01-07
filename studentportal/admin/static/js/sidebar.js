// Sidebar toggle functionality
const toggleBtn = document.getElementById("toggle-btn");
const closeBtn = document.getElementById("close-btn");
const sidebar = document.getElementById("sidebar");

toggleBtn.addEventListener("click", () => {
  sidebar.classList.add("open");
  toggleBtn.style.display = "none";
  closeBtn.style.display = "block";
});

closeBtn.addEventListener("click", () => {
  sidebar.classList.remove("open");
  toggleBtn.style.display = "block";
  closeBtn.style.display = "none";

  // Reset dropdowns when closing the sidebar
  $('.dropdown-menu').slideUp(300);
});

// JavaScript to toggle dropdown visibility
$(document).ready(function() {
  $('.dropdown-toggle').click(function(event) {
    event.preventDefault();  // Prevent the page from reloading

    // Toggle the visibility of the next dropdown menu
    $(this).next('.dropdown-menu').slideToggle(300);

    // Close any other open dropdowns
    $('.dropdown-menu').not($(this).next()).slideUp(300);
  });
});


