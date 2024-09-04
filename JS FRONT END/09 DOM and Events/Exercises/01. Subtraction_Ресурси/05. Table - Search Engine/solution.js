function solve() {
  document.querySelector("#searchBtn").addEventListener("click", onClick);

  function onClick() {
    let allRows = Array.from(
      document.querySelector(".container tbody").children
    );
    for (const row of allRows) {
      row.removeAttribute("class");
      console.log(row.textContent);
    }
    let searchField = document.getElementById("searchField");
    if (searchField.value.trim() !== "") {
      for (const row of allRows) {
        if (row.textContent.includes(searchField.value))
          row.className = "select";
      }
    }
    searchField.value = "";
  }
}
