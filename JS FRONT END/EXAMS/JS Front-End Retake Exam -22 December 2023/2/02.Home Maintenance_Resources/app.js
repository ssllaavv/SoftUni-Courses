window.addEventListener("load", solve);

function solve() {
  let placeHTML = document.getElementById("place");
  let actionHTML = document.getElementById("action");
  let personHTML = document.getElementById("person");

  let addBtn = document.getElementById("add-btn");
  addBtn.addEventListener("click", addHandler);

  let taskListUl = document.getElementById("task-list");
  let doneListUl = document.getElementById("done-list");

  function clearInputs() {
    placeHTML.value = "";
    actionHTML.value = "";
    personHTML.value = "";
  }

  function addHandler(e) {
    if (
      placeHTML.value.trim() !== "" &&
      actionHTML.value.trim() !== "" &&
      personHTML.value.trim() !== ""
    ) {
      let place = placeHTML.value.trim();
      let action = actionHTML.value.trim();
      let person = personHTML.value.trim();

      let newLi = document.createElement("li");
      newLi.classList.add("clean-task");
      newLi.innerHTML = `<article>
                <p>Place:${place}</p>
                <p>Action:${action}</p>
                <p>Person:${person}</p>
            </article>
            <div class="buttons">
                <button class="edit">Edit</button>
                <button class="done">Done</button>
            </div>`;

      let editBtn = newLi.querySelector(".edit");
      let doneBtn = newLi.querySelector(".done");

      editBtn.addEventListener("click", editHandler);
      doneBtn.addEventListener("click", doneHandler);

      taskListUl.appendChild(newLi);
      clearInputs();
    }
  }

  function editHandler(e) {
    let editBtn = e.currentTarget;

    let currentLi = editBtn.parentElement.parentElement;
    // let buttonsDiv = editBtn.parentElement;
    // buttonsDiv.parentElement.removeChild(buttonsDiv);

    let paragraphs = Array.from(currentLi.querySelectorAll("p"));

    let place = paragraphs[0].textContent.split(":")[1];
    let action = paragraphs[1].textContent.split(":")[1];
    let person = paragraphs[2].textContent.split(":")[1];

    currentLi.parentElement.removeChild(currentLi);

    placeHTML.value = place;
    actionHTML.value = action;
    personHTML.value = person;
  }

  function doneHandler(e) {
    let doneBtn = e.currentTarget;

    let currentLi = doneBtn.parentElement.parentElement;
    let buttonsDiv = doneBtn.parentElement;
    buttonsDiv.parentElement.removeChild(buttonsDiv);

    let deleteBtn = document.createElement("button");
    deleteBtn.classList.add("delete");
    deleteBtn.textContent = "Delete";
    deleteBtn.addEventListener("click", deleteHandler);

    currentLi.appendChild(deleteBtn);
    currentLi.parentElement.removeChild(currentLi);
    doneListUl.appendChild(currentLi);
  }

  function deleteHandler(e) {
    let deleteBtn = e.currentTarget;
    let currentLi = deleteBtn.parentElement;
    currentLi.parentElement.removeChild(currentLi);
  }
}
