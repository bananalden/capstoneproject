const emojis = [
  // Smileys & Emotions
  "😀","😃","😄","😁","😆","😅","😂","🤣","😊","😇","🙂","🙃","😉","😌","😍","🥰","😘","😗","😙","😚","🤗",
  "🤩","🤔","🤨","😐","😑","😶","🙄","😏","😣","😥","😮","🤐","😯","😪","😫","😴","😌","😛","😜","😝","🤤",
  "😒","😓","😔","😕","🙃","🤑","🤠","🤡","🤥","🤭","🤫","🤨","🤯","🧐","🤩","🤪","🤬","🤮","🤢","🤕","🤒","🤧",
  "😷","🥵","🥶","😰","😥","😓","🤗","🤔","🤨","😐","😑","😶","🙄","😏","😣","😥","😮","🤐","😯","😪","😫",
  "😴","😌","😛","😜","😝","🤤","😒","😓","😔","😕","🙃","🤑","🤠","🤡","🤥","🤭","🤫","🤨","🤯","🧐","🤩",
  "🤪","🤬","🤮","🤢","🤕","🤒","🤧","😷",

  // Hearts
  "❤️","🧡","💛","💚","💙","💜","🖤","🤍","🤎","💔","💕","💞","💓","💗","💖","💘","💝","💟",

  // Food & Drinks
  "🍎","🍊","🍌","🍉","🍇","🍓","🍒","🍑","🥭","🍍","🥥","🥝","🍆","🥑","🥦","🥕","🌽","🌶️","🥒","🥬",
  "🥔","🍠","🥐","🍞","🥖","🥨","🥯","🧀","🥚","🍳","🥞","🥓","🥩","🍗","🍖","🌭","🍔","🍟","🍕","🥪",
  "🥗","🍿","🧂","🥫","🍝","🍣","🍤","🍪","🎂","🍰","🧁","🍩","🍫","🍬","🍭","☕","🍵","🥤","🍹","🍷","🍺","🍻",

  // Activities
  "⚽","🏀","🏈","⚾","🥎","🎾","🏐","🏉","🎱","🏓","🏸","🥊","🥋","🎽","⛸️","🥌","🛷","🛹","🎿","🏂",
  "🏋️","🤼","🤸","⛹️","🤺","🏌️","🏄","🚣","🏊","🎭","🎨","🎬","🎤","🎧","🎼","🎹","🥁","🎷","🎺","🎸","🪕","🎻",

  // Travel & Places
  "🚗","🚕","🚙","🚌","🚎","🏎️","🚓","🚑","🚒","🚐","🛻","🚚","🚛","🚜","🚲","🛴","🛵","🏍️","🛩️","✈️","🚀",
  "🚁","🚤","⛵","🚢","🛳️","🗽","🗼","🏰","🏯","🎡","🎢","🎠","🏟️","🏛️","⛩️","🏗️","🏠","🏡","🏢","🏬",
  "🏥","🏦","🏪","🕌","⛪","🕍","🛕","🛤️","🌋","🏜️","🏝️","🌃","🌆","🌉","🌇","🗾",

  // Objects & Symbols
  "⌚","📱","💻","🖥️","🖨️","⌨️","🖱️","🖲️","💾","💿","📀","📷","📸","🎥","📽️","🎞️","📞","☎️","📟","📠",
  "📡","📺","📻","🎙️","🎚️","🎛️","🧭","⏳","⏰","🕰️","🔋","🔌","💡","🔦","🕯️","🪔","📜","📃","📄","📑",
  "📊","📈","📉","🗒️","📅","📆","🗂️","📇","🗃️","🗳️","🗄️","📋","📌","📎","🖊️","🖋️","✒️","📝","✏️","🔍","🔎",
  "🔏","🔐","🔒","🔓","💰","💵","💴","💶","💷","💳","💸","💎","⚖️","🛒","🚪","🛏️","🛋️","🚽","🚿","🛁",
  "🪑","🎁","🎈","🎉","🎊","🧨","🎎","🎏","🎐","🎀","🧧","🖼️","🛍️","📿","💎","🧲","📯","🎵","🎶","📢","📣",

  // Flags (Just a few samples, add more as needed)
  "🇺🇸","🇨🇦","🇬🇧","🇦🇺","🇫🇷","🇩🇪","🇯🇵","🇰🇷","🇵🇭","🇮🇳","🇮🇹","🇪🇸","🇧🇷","🇲🇽","🇷🇺","🇨🇳"
];



// Function para ipakita o itago ang emoji list
function toggleEmojiList() {
  const emojiList = document.getElementById("emojiList");
  emojiList.style.display = (emojiList.style.display === "block") ? "none" : "block";
}

// Function para dynamically maglagay ng emojis sa picker
function loadEmojis() {
  const emojiListDiv = document.getElementById("emojiList");
  emojiListDiv.innerHTML = "";
  emojis.forEach(emoji => {
      let span = document.createElement("span");
      span.innerText = emoji;
      span.onclick = function() { addEmoji(emoji); };
      emojiListDiv.appendChild(span);
  });
}

// Function para idagdag ang emoji sa input box
function addEmoji(emoji) {
  const tweetInput = document.getElementById("tweetInput");
  tweetInput.value += emoji;
}

// Load emojis pag nag-load ang page
window.onload = loadEmojis;

function toggleEmojiList() {
  document.getElementById("emojiList").classList.toggle("active");
}

// Teacher Dashboard Styling //
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


// UPLOAD GRADES SECTION

function updateFileName() {
  const fileInput = document.getElementById("file-upload");
  const fileName = document.getElementById("file-name");

  if (fileInput.files.length > 0) {
    fileName.textContent = fileInput.files[0].name;
  } else {
    fileName.textContent = "No file chosen";
  }
}




