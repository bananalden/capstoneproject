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


// FACULTY FUNCTIONALITY
let selectedRow = null;
let currentPage = 1;
const recordsPerPage = 5;
const students = []; // Store the students data

document.getElementById('studentForm').addEventListener('submit', function(event) {
  event.preventDefault();

  // Get the form values
  const studentName = document.getElementById('studentName').value;
  const studentEmail = document.getElementById('studentEmail').value;
  const studentCourse = document.getElementById('studentCourse').value;
  const studentStatus = document.getElementById('studentStatus').value;

  // Check if we're editing an existing row
  if (selectedRow === null) {
    // Add a new student to the students array
    students.push({ name: studentName, email: studentEmail, course: studentCourse, status: studentStatus });
  } else {
    // Update the existing student's data
    students[selectedRow.rowIndex - 1] = { name: studentName, email: studentEmail, course: studentCourse, status: studentStatus };
    selectedRow = null; // Reset the selected row
  }

  // Clear the form
  document.getElementById('studentForm').reset();

  // Update the table with the new data
  renderTable();

  // Update the "Save" button to "Add Student"
  document.querySelector('#studentForm button').textContent = 'Add Student';
});

function renderTable() {
  const tableBody = document.getElementById('studentTable').getElementsByTagName('tbody')[0];
  tableBody.innerHTML = '';

  // Get the current page's data
  const start = (currentPage - 1) * recordsPerPage;
  const end = start + recordsPerPage;
  const currentStudents = students.slice(start, end);

  // Create rows for each student on the current page
  currentStudents.forEach((student, index) => {
    const newRow = tableBody.insertRow();
    newRow.insertCell(0).textContent = student.name;
    newRow.insertCell(1).textContent = student.email;
    newRow.insertCell(2).textContent = student.course;
    newRow.insertCell(3).textContent = student.status;
    const actionCell = newRow.insertCell(4);
    addActionButtons(actionCell, newRow);
  });

  // Update pagination controls
  updatePagination();
}

function addActionButtons(cell, row) {
  const editButton = document.createElement('button');
  editButton.textContent = 'Edit';
  editButton.classList.add('edit-btn');
  editButton.onclick = function() {
    document.getElementById('studentName').value = row.cells[0].textContent;
    document.getElementById('studentEmail').value = row.cells[1].textContent;
    document.getElementById('studentCourse').value = row.cells[2].textContent;
    document.getElementById('studentStatus').value = row.cells[3].textContent;
    document.querySelector('#studentForm button').textContent = 'Save Changes';
    selectedRow = row;
  };

  const deleteButton = document.createElement('button');
  deleteButton.textContent = 'Delete';
  deleteButton.classList.add('delete-btn');
  deleteButton.onclick = function() {
    students.splice(row.rowIndex - 1, 1); // Remove student from the array
    renderTable(); // Re-render the table after deletion
  };

  cell.appendChild(editButton);
  cell.appendChild(deleteButton);
}

function updatePagination() {
  const totalPages = Math.ceil(students.length / recordsPerPage);
  const paginationContainer = document.getElementById('pagination');
  paginationContainer.innerHTML = '';

  // Previous button
  const prevButton = document.createElement('button');
  prevButton.textContent = 'Previous';
  prevButton.disabled = currentPage === 1;
  prevButton.onclick = function() {
    if (currentPage > 1) {
      currentPage--;
      renderTable();
    }
  };
  paginationContainer.appendChild(prevButton);

  // Page numbers
  for (let i = 1; i <= totalPages; i++) {
    const pageButton = document.createElement('button');
    pageButton.textContent = i;
    pageButton.disabled = currentPage === i;
    pageButton.onclick = function() {
      currentPage = i;
      renderTable();
    };
    paginationContainer.appendChild(pageButton);
  }

  // Next button
  const nextButton = document.createElement('button');
  nextButton.textContent = 'Next';
  nextButton.disabled = currentPage === totalPages;
  nextButton.onclick = function() {
    if (currentPage < totalPages) {
      currentPage++;
      renderTable();
    }
  };
  paginationContainer.appendChild(nextButton);
}

// Initial render of the table
renderTable();
