window.addEventListener("load", solve);

function solve() {
  let expenseHTML = document.getElementById("expense");
  let amountHTML = document.getElementById("amount");
  let dateHTML = document.getElementById("date");

  let addBtn = document.getElementById("add-btn");
  addBtn.addEventListener("click", addHandler);

  let previewListUl = document.getElementById("preview-list");
  let expensesListUl = document.getElementById("expenses-list");

  let deleteAllBtn = document.querySelector("#expenses > button.delete");
  deleteAllBtn.addEventListener("click", deleteAllHandler);

  function clearInputs() {
    expenseHTML.value = "";
    amountHTML.value = "";
    dateHTML.value = "";
  }

  function validateInputs() {
    if (
      expenseHTML.value !== "" &&
      amountHTML.value !== "" &&
      dateHTML.value !== ""
    ) {
      return true;
    } else {
      return false;
    }
  }

  function addHandler(e) {
    if (validateInputs()) {
      let expense = expenseHTML.value;
      let amount = amountHTML.value;
      let date = dateHTML.value;

      let newLi = document.createElement("li");
      newLi.classList.add("expense-item");
      newLi.innerHTML = `<article>
            <p>Type: ${expense}</p>
            <p>Amount: ${amount}$</p>
            <p>Date: ${date}</p>
      </article>
      <div class="buttons">
            <button class="btn edit">edit</button>
            <button class="btn ok">ok</button>
      </div>`;
      previewListUl.appendChild(newLi);
      clearInputs();
      addBtn.disabled = true;

      let editBtn = newLi.querySelector(".btn.edit");
      let okBtn = document.querySelector(".btn.ok");
      editBtn.addEventListener("click", editHandler);
      okBtn.addEventListener("click", okHandler);
    }
  }

  function deleteAllHandler(e) {
    expensesListUl.innerHTML = "";
    location.reload(true);
  }

  function editHandler(e) {
    let btn = e.currentTarget;

    let currentLi = btn.parentElement.parentElement;
    let paragraphs = Array.from(currentLi.querySelectorAll("p"));

    let expense = paragraphs[0].textContent.split(": ")[1];
    let amount = Number(paragraphs[1].textContent.split(": ")[1].slice(0, -1));
    let date = paragraphs[2].textContent.split(": ")[1];

    currentLi.parentElement.removeChild(currentLi);

    expenseHTML.value = expense;
    amountHTML.value = amount;
    dateHTML.value = date;

    addBtn.disabled = false;
  }

  function okHandler(e) {
    let btn = e.currentTarget;
    let currentLi = btn.parentElement.parentElement;
    buttonsDiv = currentLi.querySelector(".buttons");
    buttonsDiv.parentElement.removeChild(buttonsDiv);
    currentLi.parentElement.removeChild(currentLi);
    expensesListUl.appendChild(currentLi);

    clearInputs();
    addBtn.disabled = false;
  }
}
