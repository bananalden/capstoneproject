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

$(document).ready(function () {
  const $btn = $(".notification-btn");
  const $dropdown = $(".notif-dropdown");
  const $badge = $(".notif-badge");

  function getCSRFToken() {
    const cookieValue = document.cookie
      .split("; ")
      .find(row => row.startsWith("csrftoken="))
      ?.split("=")[1];
    return cookieValue || "";
  }

  function loadNotifications() {
    $.get("/api/notifications/", function (data) {
      $dropdown.empty();
      let unreadCount = 0;

      data.notifications.forEach(notification => {
        const isUnread = !notification.is_read;
        const notifClass = isUnread ? "unread" : "read";
        if (isUnread) unreadCount++;

        const notifHtml = `
          <div class="notif-item ${notifClass}">
            <div class="notif-title">${notification.title}</div>
            <div class="notif-message">${notification.message}</div>
          </div>
        `;
        $dropdown.append(notifHtml);
      });

      if (unreadCount > 0) {
        $badge.text(unreadCount).show();
      } else {
        $badge.hide();
      }

      $dropdown.append(`<div class="clear-all">Clear All</div>`);
    });
  }

  function markNotificationsAsRead() {
    $.ajax({
      url: "/api/notifications/mark-read/",
      method: "POST",
      headers: { "X-CSRFToken": getCSRFToken() },
      success: () => {
        loadNotifications(); // Refresh UI after marking as read
      }
    });
  }

  function clearNotifications(){
    $.ajax({
      url: "/api/notifications/clear-notifs/",
      method:"POST",
      headers:{"X-CSRFToken":getCSRFToken()},
      succes: () =>{
        loadNotifications()
      }
    })
  }

  // Toggle dropdown visibility
  $btn.on("click", function (e) {
    e.stopPropagation();
    const shouldShow = !$dropdown.hasClass("active");
    $dropdown.toggleClass("active");

    if (shouldShow) {
      markNotificationsAsRead(); // Only mark as read when opening
    }
  });

  // Hide on click outside
  $(document).on("click", function (e) {
    if (
      !$dropdown.is(e.target) &&
      $dropdown.has(e.target).length === 0 &&
      !$btn.is(e.target) &&
      $btn.has(e.target).length === 0
    ) {
      $dropdown.removeClass("active");
    }
  });

  // Optional: Auto-refresh every 60 seconds
  setInterval(loadNotifications, 60000);

  // Initial load
  loadNotifications();
});