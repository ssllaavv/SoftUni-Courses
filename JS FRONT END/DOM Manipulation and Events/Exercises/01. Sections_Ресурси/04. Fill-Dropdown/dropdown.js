function addItem() {
  let dropDownHTML = document.getElementById("menu");
  let newOptionHTML = document.createElement("option");

  let value = document.getElementById("newItemValue");
  let name = document.getElementById("newItemText");

  newOptionHTML.value = value.value;
  newOptionHTML.textContent = name.value;

  dropDownHTML.appendChild(newOptionHTML);

  value.value = "";
  name.value = "";
}
