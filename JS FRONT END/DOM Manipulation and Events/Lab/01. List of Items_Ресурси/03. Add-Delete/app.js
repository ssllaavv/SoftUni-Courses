// function addItem() {
//     let inputHTML = document.getElementById('newItemText');
//     let mainHTML = document.querySelector('main');
//     let newUl = document.createElement('ul');
//     newUl.id = 'items';
//     let ulHTML = document.getElementById('items');
//     if (!ulHTML) {
//         mainHTML.prepend(newUl);
//         ulHTML = newUl
//     }

//     if (inputHTML.value.trim().trim() !== "") {
//         let newLi = document.createElement('li');
//         newLi.textContent = inputHTML.value.trim();
//         newUl.appendChild(li);
//         inputHTML.value.trim() = "";
//     }

// }

function addItem() {
  let newElementHTML = document.getElementById("newItemText");
  // console.log(newElementHTML.value)

  let itemsHTML = document.getElementById("items");
  // console.log(itemsHTML.innerHTML)

  let newLiElement = document.createElement("li");
  newLiElement.textContent = newElementHTML.value;
  // console.log(newLiElement)

  newElementHTML.value = "";

  let newA = document.createElement("a");
  newA.textContent = "[Delete]";
  newA.href = "#";
  newLiElement.appendChild(newA);
  itemsHTML.appendChild(newLiElement);

  newA.addEventListener("click", deleteHandler);

  function deleteHandler(e) {
    let aElement = e.currentTarget;
    console.log(aElement);

    let currentLiElement = aElement.parentElement;
    console.log(currentLiElement);

    console.log(currentLiElement.parentElement);

    currentLiElement.parentElement.removeChild(currentLiElement);
  }
}
