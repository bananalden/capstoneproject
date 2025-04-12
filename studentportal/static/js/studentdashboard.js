let currentMonth = new Date().getMonth();
let currentYear = new Date().getFullYear();

function generateCalendar(month, year) {
  const calendarDays = document.getElementById("calendar-days");
  const calendarTitle = document.getElementById("calendar-title");
  calendarDays.innerHTML = ""; // Clear previous content

  const today = new Date();
  const dateToday = today.getDate();
  const firstDay = new Date(year, month, 1).getDay();
  const totalDays = new Date(year, month + 1, 0).getDate();

  const monthNames = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
  ];
  
  calendarTitle.textContent = `${monthNames[month]} ${year}`;

  // Special events (modify as needed)
  const events = {
    "2-5": "Semester Starts",
    "2-10": "Career Fair"
  };

  // Add empty slots for alignment
  for (let i = 0; i < firstDay; i++) {
    let emptyDiv = document.createElement("div");
    emptyDiv.classList.add("empty");
    calendarDays.appendChild(emptyDiv);
  }

  // Generate calendar days
  for (let day = 1; day <= totalDays; day++) {
    let dayDiv = document.createElement("div");
    dayDiv.classList.add("calendar-day");
    dayDiv.textContent = day;

    // Highlight today's date only in the current month and year
    if (day === dateToday && month === today.getMonth() && year === today.getFullYear()) {
      dayDiv.classList.add("today");
    }

    // Check for events
    let eventKey = `${month + 1}-${day}`;
    if (events[eventKey]) {
      dayDiv.classList.add("event");
      dayDiv.innerHTML = `${day} <span class="event-text">${events[eventKey]}</span>`;
    }

    calendarDays.appendChild(dayDiv);
  }
}

// Handle previous and next month buttons
document.getElementById("prev-month").addEventListener("click", () => {
  currentMonth--;
  if (currentMonth < 0) {
    currentMonth = 11;
    currentYear--;
  }
  generateCalendar(currentMonth, currentYear);
});

document.getElementById("next-month").addEventListener("click", () => {
  currentMonth++;
  if (currentMonth > 11) {
    currentMonth = 0;
    currentYear++;
  }
  generateCalendar(currentMonth, currentYear);
});

// Run calendar generator on page load
generateCalendar(currentMonth, currentYear);


// NOTIFICATION SECTION

document.addEventListener("DOMContentLoaded", () => {
  const btn = document.querySelector(".notification-btn");
  const dropdown = document.querySelector(".notif-dropdown");
  const clearBtn = document.querySelector(".clear-all");
  const badge = document.querySelector(".notif-badge");

  btn.addEventListener("click", e => {
    e.stopPropagation();
    dropdown.classList.toggle("active");
  });

  document.addEventListener("click", e => {
    if (!dropdown.contains(e.target) && !btn.contains(e.target)) {
      dropdown.classList.remove("active");
    }
  });

  clearBtn?.addEventListener("click", () => {
    dropdown.classList.remove("active");

    document.querySelectorAll(".notif-item").forEach(item => {
      item.classList.remove("unread");
      item.classList.add("read");
    });

    if (badge) {
      badge.textContent = "0";
      badge.style.display = "none";
    }
  });
});


