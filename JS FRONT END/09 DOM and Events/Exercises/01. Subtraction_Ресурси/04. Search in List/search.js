function search() {
  let towns = Array.from(document.getElementById("towns").children);
  let searchText = document.getElementById("searchText").value;
  let result = document.getElementById("result");
  let matchesCount = 0;

  for (const town of towns) {
    town.style.textDecoration = "unset";
    town.style.fontWeight = "unset";
  }

  for (const town of towns) {
    if (town.textContent.includes(searchText) && searchText.trim() !== "") {
      matchesCount += 1;
      town.style.textDecoration = "underline";
      town.style.fontWeight = "bold";
    }
    //  console.log(matchesCount);
  }
  if (searchText !== "") {
    result.textContent = `${matchesCount} matches found`;
  } else {
    result.textContent = "";
  }
}
