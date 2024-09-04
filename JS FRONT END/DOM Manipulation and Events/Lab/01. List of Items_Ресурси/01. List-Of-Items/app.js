function addItem() {
  let newElementHTML = document.getElementById("newItemText");
  // console.log(newElementHTML.value)

  let itemsHTML = document.getElementById("items");
  // console.log(itemsHTML.innerHTML)

  let newLiElement = document.createElement("li");
  newLiElement.textContent = newElementHTML.value;
  // console.log(newLiElement)

  newElementHTML.value = "";
  itemsHTML.append(newLiElement);
}
