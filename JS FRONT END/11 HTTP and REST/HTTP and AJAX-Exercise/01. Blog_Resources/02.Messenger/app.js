function attachEvents() {
  let messagesHTML = document.getElementById("messages");
  let [authorHTML, messageContentHTML] = Array.from(
    document.querySelectorAll("#controls > div > input")
  );
  let submitBtn = document.getElementById("submit");
  let refreshBtn = document.getElementById("refresh");

  const BASE_URL = "http://localhost:3030/jsonstore/messenger";

  submitBtn.addEventListener("click", submitHandler);
  refreshBtn.addEventListener("click", refreshHandler);

  function submitHandler(e) {
    let message = {};
    message.author = authorHTML.value;
    message.content = messageContentHTML.value;

    let httpHeaders = {
      method: "POST",
      body: JSON.stringify(message),
    };

    fetch(BASE_URL, httpHeaders)
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok " + response.statusText);
        }
        authorHTML.value = "";
        messageContentHTML.value = "";
        return response.json(); // Parse the response as JSON
      })
      .then((data) => {
        console.log("Success:", data); // Handle the response data
    
      })
      .catch((error) => {
        console.error("There was a problem with the fetch operation:", error); // Handle errors
      });
  }

  function refreshHandler(e) {
    messagesHTML.textContent = "";
    let messageContent = ""
    fetch(BASE_URL)
      .then((response) => response.json())
      .then((result) => Object.values(result))
      .then((messages) => {
        for (const message of messages) {
          console.log(message.author);
          console.log(message.content);

          messageContent += `${message.author}: ${message.content}\n`;
         
        }
        messagesHTML.textContent = messageContent.trim()
      });
  }
}

attachEvents();
