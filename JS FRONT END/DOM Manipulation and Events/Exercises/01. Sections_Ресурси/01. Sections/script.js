function create(words) {
  let contentHTML = document.getElementById("content");

  for (const word of words) {
    newDiv = document.createElement("div");
    newParagraph = document.createElement("p");
    newParagraph.textContent = word;
    newDiv.appendChild(newParagraph);
    contentHTML.appendChild(newDiv);
    newParagraph.style.display = "none";
    newDiv.addEventListener("click", clickHandler);
  }
  function clickHandler(e) {
    currentTarget = e.currentTarget.querySelector("p");
    currentTarget.style.display = "block";
  }
}
