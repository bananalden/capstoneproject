let selectedCourseId = null;
let currentPage = 1;
const coursesPerPage = 8;  // Display 8 courses per page

// Dummy data for courses
let courses = [
    { id: 1, name: "Web Development" },
];

// Function to render the courses table
function displayCourses() {
    const searchQuery = document.getElementById('search-course').value.toLowerCase(); // Get search query
    const courseList = document.getElementById('course-list');
    courseList.innerHTML = ''; // Clear previous content

    // Filter courses based on search query
    const filteredCourses = courses.filter(course => course.name.toLowerCase().includes(searchQuery));

    // Determine the slice of courses to show on the current page
    const startIndex = (currentPage - 1) * coursesPerPage;
    const endIndex = startIndex + coursesPerPage;
    const coursesToDisplay = filteredCourses.slice(startIndex, endIndex);

    coursesToDisplay.forEach(course => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${course.id}</td>
            <td>${course.name}</td>
            <td>
                <button class="action-btn edit-btn" onclick="openEditModal(${course.id})">
                    <i class="fas fa-edit"></i> Edit
                </button>
                <button class="action-btn delete-btn" onclick="openDeleteModal(${course.id})">
                    <i class="fas fa-trash-alt"></i> Delete
                </button>
            </td>
        `;
        courseList.appendChild(row);
    });

    updatePagination(filteredCourses.length);  // Update pagination based on filtered courses
}

// Function to update pagination controls
function updatePagination(filteredCoursesLength) {
    const totalPages = Math.ceil(filteredCoursesLength / coursesPerPage);
    const paginationContainer = document.getElementById('pagination');
    paginationContainer.innerHTML = '';  // Clear existing pagination buttons

    // Create previous button
    const prevButton = document.createElement('button');
    prevButton.innerText = 'Previous';
    prevButton.disabled = currentPage === 1;
    prevButton.onclick = () => changePage(currentPage - 1);
    paginationContainer.appendChild(prevButton);

    // Create page number buttons
    for (let i = 1; i <= totalPages; i++) {
        const pageButton = document.createElement('button');
        pageButton.innerText = i;
        pageButton.classList.toggle('active', i === currentPage);  // Highlight active page
        pageButton.onclick = () => changePage(i);
        paginationContainer.appendChild(pageButton);
    }

    // Create next button
    const nextButton = document.createElement('button');
    nextButton.innerText = 'Next';
    nextButton.disabled = currentPage === totalPages;
    nextButton.onclick = () => changePage(currentPage + 1);
    paginationContainer.appendChild(nextButton);
}

// Function to handle page change
function changePage(page) {
    if (page < 1 || page > Math.ceil(courses.length / coursesPerPage)) return;  // Prevent invalid page change
    currentPage = page;
    displayCourses();
}

// Open the Edit Modal
function openEditModal(id) {
    selectedCourseId = id;
    const course = courses.find(c => c.id === id);
    if (course) {
        document.getElementById('edit-course-name').value = course.name;
        document.getElementById('edit-modal').style.display = 'flex';
    }
}

// Open the Delete Modal
function openDeleteModal(id) {
    selectedCourseId = id;
    document.getElementById('delete-modal').style.display = 'flex';
}

// Close all open modals
function closeModals() {
    document.querySelectorAll('.modal').forEach(modal => {
        modal.style.display = 'none';
    });
}

// Save changes in the Edit Modal
function saveEdit() {
    const newName = document.getElementById('edit-course-name').value.trim();
    if (newName) {
        const course = courses.find(c => c.id === selectedCourseId);
        if (course) {
            course.name = newName;
            displayCourses(); // Re-render the table
            closeModals(); // Close the modal
        }
    } else {
        alert('Course name cannot be empty.');
    }
}

// Confirm course deletion
function confirmDelete() {
    courses = courses.filter(c => c.id !== selectedCourseId);
    displayCourses(); // Re-render the table
    closeModals(); // Close the modal
}

// Open the Add Course Modal
document.getElementById('add-course-btn').addEventListener('click', function() {
    document.getElementById('add-course-modal').style.display = 'flex';
});

// Close the Add Course Modal
document.getElementById('close-add-course-modal').addEventListener('click', function() {
    document.getElementById('add-course-modal').style.display = 'none';
});

// Save the New Course
document.getElementById('save-new-course-btn').addEventListener('click', function() {
    const courseName = document.getElementById('new-course-name').value.trim();

    if (courseName) {
        const newCourse = {
            id: courses.length + 1, // Generate a new ID
            name: courseName
        };
        courses.push(newCourse); // Add the new course to the array
        document.getElementById('new-course-name').value = ''; // Clear input field

        displayCourses(); // Re-render the table
        document.getElementById('add-course-modal').style.display = 'none'; // Close the modal
    } else {
        alert('Course name cannot be empty.');
    }
});

// Initialize the course table on page load
document.addEventListener('DOMContentLoaded', () => {
    displayCourses();

    // Attach modal close handlers
    document.getElementById('close-edit-modal').onclick = closeModals;
    document.getElementById('close-delete-modal').onclick = closeModals;

    // Add event listener for save button in the edit modal
    document.getElementById('save-edit-btn').onclick = saveEdit;
    // Add event listener for confirm delete button
    document.getElementById('confirm-delete-btn').onclick = confirmDelete;

    // Add event listener for search functionality
    document.getElementById('search-course').addEventListener('input', function() {
        displayCourses();  // Re-render the courses when search input changes
    });
});
