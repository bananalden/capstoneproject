function validateLogin(event) {
  event.preventDefault();
  const username = document.getElementById("username").value.trim();
  const password = document.getElementById("password").value.trim();
  const alertContainer = document.getElementById("loginAlertContainer");
  const alertMessage = document.getElementById("loginAlertMessage");

  if (!username || !password) {
      showAlert("USN and Password are required!");
      return;
  }

  if (password !== "correctpassword") {
      showAlert("Invalid USN or Password. Please try again.");
      return;
  }

  alertContainer.style.display = "none";
  document.getElementById("loginForm").submit();
}

function showAlert(message) {
  const alertContainer = document.getElementById("loginAlertContainer");
  const alertMessage = document.getElementById("loginAlertMessage");
  alertMessage.textContent = message;
  alertContainer.style.display = "block";
}

function togglePassword() {
  const passwordField = document.getElementById("password");
  const isPassword = passwordField.type === "password";
  
  passwordField.type = isPassword ? "text" : "password";
}
