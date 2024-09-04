function extractText() {
  let ul = document.querySelector("#items");
  let result = document.querySelector("#result");

  for (const li of ul.children) {
    result.textContent += li.textContent + "\n";
  }
}
