window.addEventListener("load", solve);

function solve() {
  let nameHTML = document.getElementById("name");
  let phoneHTML = document.getElementById("phone");
  let categoryHTML = document.getElementById("category");

  let addBtn = document.getElementById("add-btn");
  addBtn.addEventListener("click", addHandler);

  let checkListUl = document.getElementById("check-list");
  let contactListUl = document.getElementById("contact-list");

  function clearInputs() {
    nameHTML.value = "";
    phoneHTML.value = "";
    categoryHTML.value = "";
  }

  function addHandler(e) {
    e.preventDefault();

    let name = nameHTML.value.trim();
    let phone = phoneHTML.value.trim();
    let category = categoryHTML.value.trim();

    if (name !== "" && phone !== "" && category !== "") {
      let newLi = document.createElement("li");
      newLi.innerHTML = `<article> 
              <p>name:${name}</p>
              <p>phone:${phone}</p>
              <p>category:${category}</p>
            </article>
            <div class="buttons">
              <button class="edit-btn"></button>
              <button class="save-btn"></button>
            </div>`;

      let editBtn = newLi.querySelector(".edit-btn");
      let saveBtn = newLi.querySelector(".save-btn");

      editBtn.addEventListener("click", editHandler);
      saveBtn.addEventListener("click", saveHandler);

      checkListUl.appendChild(newLi);
      clearInputs();
    }
  }

  function editHandler(e) {
    e.preventDefault();

    let editBtn = e.currentTarget;
    let currentLi = editBtn.parentElement.parentElement;
    let paragraphs = Array.from(currentLi.querySelectorAll("p"));

    nameHTML.value = paragraphs[0].textContent.split(":")[1];
    phoneHTML.value = paragraphs[1].textContent.split(":")[1];
    categoryHTML.value = paragraphs[2].textContent.split(":")[1];

    currentLi.parentElement.removeChild(currentLi);
  }

  function saveHandler(e) {
    e.preventDefault();

    let saveBtn = e.currentTarget;
    let currentLi = saveBtn.parentElement.parentElement;

    let buttonsDiv = saveBtn.parentElement;
    buttonsDiv.parentElement.removeChild(buttonsDiv);

    let deleteBtn = document.createElement("button");
    deleteBtn.classList.add("del-btn");

    currentLi.appendChild(deleteBtn);
    deleteBtn.addEventListener("click", deleteHandler);

    currentLi.parentElement.removeChild(currentLi);
    contactListUl.appendChild(currentLi);
  }

  function deleteHandler(e) {
    e.preventDefault();

    let deleteBtn = e.currentTarget;
    let currentLi = deleteBtn.parentElement;
    currentLi.parentElement.removeChild(currentLi);
  }
}
