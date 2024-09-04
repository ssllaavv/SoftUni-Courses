function encodeAndDecodeMessages() {
  let [encodeBtn, decodeBtn] = Array.from(document.querySelectorAll("button"));

  encodeBtn.addEventListener("click", encodeHandler);
  decodeBtn.addEventListener("click", decodeHandler);

  let [senderHTML, receiverHTML] = Array.from(
    document.querySelectorAll("textarea")
  );

  function encodeHandler(e) {
    if (senderHTML.value !== "") {
      let message = senderHTML.value;
      senderHTML.value = "";
      receiverHTML.value = "";

      let encodedMessage = "";
      for (const letter of message) {
        let encodedLetter = String.fromCharCode(letter.charCodeAt(0) + 1);
        receiverHTML.value += encodedLetter;
      }
    }
  }

  function decodeHandler(e) {
    if (receiverHTML.value !== "") {
      let message = receiverHTML.value;
      receiverHTML.value = "";

      let decodedMessage = "";
      for (const letter of message) {
        let encodedLetter = String.fromCharCode(letter.charCodeAt(0) - 1);
        receiverHTML.value += encodedLetter;
      }
    }
  }
}
