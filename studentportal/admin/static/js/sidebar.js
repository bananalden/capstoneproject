const toggleBtn = document.getElementById('toggle-btn');
const sidebar = document.getElementById('sidebar');
const closeBtn = document.getElementById('close-btn');
const menuItems = document.querySelectorAll('.menu-item');

// Toggle sidebar
toggleBtn.addEventListener('click', () => {
  sidebar.classList.toggle('open');
});

// Close sidebar from the inside
closeBtn.addEventListener('click', () => {
  sidebar.classList.remove('open');
  console.log('Closed')
});

// Add "active" class when clicking a menu item
menuItems.forEach(item => {
  item.addEventListener('click', () => {
    // Remove active class from all items
    menuItems.forEach(i => i.classList.remove('active'));
    
    // Add active class to the clicked item
    item.classList.add('active');
  });
});