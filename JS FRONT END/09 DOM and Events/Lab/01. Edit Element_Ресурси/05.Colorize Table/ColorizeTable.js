function colorize() {
  let tableRows = Array.from(document.querySelectorAll("tr"));
  for (let i = 0; i < tableRows.length - 1; i += 2) {
    tableRows[i + 1].style.backgroundColor = "Teal";
  }
}
