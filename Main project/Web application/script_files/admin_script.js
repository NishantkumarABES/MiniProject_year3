

function login() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var errorMessage = document.getElementById("error-message");
  
    // Check if the username and password match a predefined value (for demo purposes)
    if (username === "admin" && password === "password") {
      alert("Login successful!");
      location.replace("https://www.w3schools.com")
    } else {
      errorMessage.textContent = "Invalid username or password.";
    }
  }
  

    