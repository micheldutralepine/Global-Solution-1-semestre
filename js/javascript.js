function submitForm() {
  var name = document.getElementById("name").value;
  var email = document.getElementById("email").value;
  var subject = document.getElementById("subject").value;
  var messageContainer = document.getElementById("message");
  if (name !== "" && email !== "") {
    messageContainer.innerHTML =
      "Agradecemos o contato! Por favor, preencha com seus dados!";
    messageContainer.style.color = "green";
    document.getElementById("contactForm").reset();
  } else {
    messageContainer.innerHTML = "Por favor, preencha os campos Nome e Email.";
    messageContainer.style.color = "red";
  }
  messageContainer.style.display = "block";
  setTimeout(function () {
    messageContainer.style.display = "none";
  }, 4000);
}
