function solve() {
  const BASE_URL = "http://localhost:3030/jsonstore/gifts/";
  let currentId = "";

  let giftHTML = document.getElementById("gift");
  let forHTM = document.getElementById("for");
  let priceHTML = document.getElementById("price");

  let addBtn = document.getElementById("add-present");
  let editBtn = document.getElementById("edit-present");
  let loadBtn = document.getElementById("load-presents");

  addBtn.addEventListener("click", addHandler);
  editBtn.addEventListener("click", editHandler);
  loadBtn.addEventListener("click", loadHandler);

  let giftsListHTML = document.getElementById("gift-list");

  function clearInputs() {
    giftHTML.value = "";
    forHTM.value = "";
    priceHTML.value = "";
  }

  function loadHandler(e) {
    clearInputs();
    editBtn.disabled = true;
    addBtn.disabled = false;
    giftsListHTML.innerHTML = "";

    fetch(BASE_URL)
      .then((response) => response.json())
      .then((result) => Object.entries(result))
      .then((gifts) => {
        // console.table(gifts);

        clearInputs();
        editBtn.disabled = true;
        addBtn.disabled = false;
        giftsListHTML.innerHTML = "";

        for (const g of gifts) {
          let newDiv = document.createElement("div");
          newDiv.classList.add("gift-sock");
          newDiv.id = g[0];
          newDiv.innerHTML = `<div class="content">
                            <p>${g[1].gift}</p>
                            <p>${g[1].for}</p>
                            <p>${g[1].price}</p>
                        </div>
                        <div class="buttons-container">
                            <button class="change-btn">Change</button>
                            <button class="delete-btn">Delete</button>
                        </div>`;

          giftsListHTML.appendChild(newDiv);
          let changeBtn = newDiv.querySelector(".change-btn");
          let deleteBtn = newDiv.querySelector(".delete-btn");

          changeBtn.addEventListener("click", changeHandler);
          deleteBtn.addEventListener("click", deleteHandler);
        }
      })
      .catch((error) => console.error(error));
  }

  function addHandler(e) {
    let gift = giftHTML.value;
    let person = forHTM.value;
    let price = priceHTML.value;

    clearInputs();

    let g = {};
    g.gift = gift;
    g.for = person;
    g.price = price;

    let httpHeaders = {
      method: "POST",
      body: JSON.stringify(g),
    };

    fetch(BASE_URL, httpHeaders)
      .then((response) => response.json())
      .then((result) => {
        // console.log(result);
        loadHandler();
      })
      .catch((error) => console.error(error));
  }

  function editHandler(e) {
    let gift = giftHTML.value;
    let person = forHTM.value;
    let price = priceHTML.value;

    let g = {};
    g.gift = gift;
    g.for = person;
    g.price = price;
    g._id = currentId;

    let httpHeaders = {
      method: "PUT",
      body: JSON.stringify(g),
    };

    fetch(BASE_URL + currentId, httpHeaders)
      .then((response) => response.json())
      .then((result) => {
        
        console.log(result);
        loadHandler();
      })
      .catch((error) => console.error(error));
  }

  function changeHandler(e) {
    let btn = e.currentTarget;
    let currentGiftDiv = btn.parentElement.parentElement;
    currentId = currentGiftDiv.id;

    let paragraphs = Array.from(currentGiftDiv.querySelectorAll("p"));
    let gift = paragraphs[0].textContent;
    let person = paragraphs[1].textContent;
    let price = paragraphs[2].textContent;

    currentGiftDiv.parentElement.removeChild(currentGiftDiv);

    giftHTML.value = gift;
    forHTM.value = person;
    priceHTML.value = price;

    addBtn.disabled = true;
    editBtn.disabled = false;
  }

  function deleteHandler(e) {
    let btn = e.currentTarget;
    let currentGiftDiv = btn.parentElement.parentElement;
    currentId = currentGiftDiv.id;

    let httpHeaders = {
      method: "DELETE",
    };

    fetch(BASE_URL + currentId, httpHeaders)
      .then((response) => {
        loadHandler();
      })
      .catch((error) => console.error(error));
  }
}

solve();
