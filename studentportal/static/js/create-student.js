const fileInput = document.getElementById('fileInput');
const fileName = document.getElementById('fileName');

fileInput.addEventListener('change', () => {
  const file = fileInput.files[0];

  if (file) {
    const allowedTypes = ['application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', 'application/vnd.ms-excel'];
    
    if (allowedTypes.includes(file.type)) {
      fileName.textContent = "✅ Selected file: " + file.name;
      fileName.style.color = "#2a9d8f"; // Optional: make success message green
    } else {
      fileName.textContent = "❌ Invalid file type. Please select an Excel file.";
      fileName.style.color = "#e63946"; // Optional: red for error
      fileInput.value = ""; // Clear invalid file
    }
  } else {
    fileName.textContent = "";
  }
});
