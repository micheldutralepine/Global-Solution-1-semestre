function submitForm() {
  var name = document.getElementById("name").value;
  var email = document.getElementById("email").value;
  var subject = document.getElementById("subject").value;
  var messageContainer = document.getElementById("message");
  if (name !== "" && email !== "") {
    messageContainer.innerHTML = "Agradecemos o contato!";
    messageContainer.style.color = "green";
    document.getElementById("contatoForm").reset();
  } else {
    messageContainer.innerHTML = "Por favor, preencha os campos Nome e Email.";
    messageContainer.style.color = "red";
  }
  messageContainer.style.display = "block";
  setTimeout(function () {
    messageContainer.style.display = "none";
  }, 5000);
}
