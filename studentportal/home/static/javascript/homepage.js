// Select all elements with the class "arrow"
const arrows = document.querySelectorAll(".arrow");

// Add click event listeners to each arrow
arrows.forEach(arrow => {
  arrow.addEventListener("click", (e) => {
    const arrowParent = e.target.closest('li'); // Select the closest parent <li> element
    arrowParent.classList.toggle("showMenu"); // Toggle the "showMenu" class
  });
});

// Toggle sidebar on menu click
const menuIcon = document.querySelector('.bx-menu'); // Icon to toggle sidebar
const sidebar = document.querySelector('.sidebar');
const homeSection = document.querySelector('.home-section');

menuIcon.addEventListener('click', () => {
  sidebar.classList.toggle('close');
  homeSection.classList.toggle('close');
});

