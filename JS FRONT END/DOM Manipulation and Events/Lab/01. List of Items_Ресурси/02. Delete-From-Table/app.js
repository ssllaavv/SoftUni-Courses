function deleteByEmail() {
  let tableRowsHTML = Array.from(document.querySelectorAll("#customers  tr"));
  let searchedEmail = document.querySelector("input").value;
  let resultHTML = document.getElementById("result");

  let emailExists = false;
  for (const row of tableRowsHTML) {
    if (row.innerHTML.includes(searchedEmail)) {
      console.log(row);
      row.parentElement.removeChild(row);
      resultHTML.textContent = "Deleted.";
      emailExists = true;
    }
  }
  if (!emailExists) {
    resultHTML.textContent = "Not found.";
  }
}
