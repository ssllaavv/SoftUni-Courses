function solution() {
  let recordUlHTML = document.getElementById("list");

  const BASE_URL = "http://localhost:3030/jsonstore/records/";
  let id = "";

  let loadBtn = document.getElementById("load-records");
  loadBtn.addEventListener("click", loadHandler);

  let nameHTML = document.getElementById("p-name");
  let stepsHTML = document.getElementById("steps");
  let caloriesHTML = document.getElementById("calories");

  let addRecordBtn = document.getElementById("add-record");
  let editRecordBtn = document.getElementById("edit-record");

  addRecordBtn.addEventListener("click", addHandler);
  editRecordBtn.addEventListener("click", editHandler);

  function loadHandler(e) {
    nameHTML.value = "";
    stepsHTML.value = "";
    caloriesHTML.value = "";

    addRecordBtn.disabled = false;
    editRecordBtn.disabled = true;

    fetch(BASE_URL)
      .then((response) => response.json())
      .then((result) => Object.values(result))
      .then((records) => {
        recordUlHTML.innerHTML = "";

        for (const record of records) {
          //   console.log(record);
          let name = record.name;
          let steps = record.steps;
          let calories = record.calories;
          let _id = record._id;

          //   console.log(name, steps, calories, _id)

          let newLi = document.createElement("li");
          newLi.classList.add("record");
          newLi.id = _id;
          newLi.innerHTML = `<div class="info">
                <p>${name}</p>
                <p>${steps}</p>
                <p>${calories}</p>
            </div>
            <div class="btn-wrapper">
                <button class="change-btn">Change</button>
                <button class="delete-btn">Delete</button>
            </div>`;

          recordUlHTML.appendChild(newLi);

          let changeButtons = Array.from(
            document.querySelectorAll(".change-btn")
          );
          for (const btn of changeButtons) {
            btn.addEventListener("click", changeHandler);
          }

          let deleteButtons = Array.from(
            document.querySelectorAll(".delete-btn")
          );
          for (const btn of deleteButtons) {
            btn.addEventListener("click", deleteHandler);
          }
        }
      });
  }

  function changeHandler(e) {
    let button = e.currentTarget;

    let paragraphs = Array.from(
      button.parentElement.parentElement.querySelectorAll("p")
    );
    let name = paragraphs[0].textContent;
    let steps = paragraphs[1].textContent;
    let calories = paragraphs[2].textContent;

    let currentLi = button.parentElement.parentElement;
    id = currentLi.id;
    console.log(id);

    nameHTML.value = name;
    stepsHTML.value = steps;
    caloriesHTML.value = calories;

    addRecordBtn.disabled = true;
    editRecordBtn.disabled = false;
  }

  function deleteHandler(e) {
    let button = e.currentTarget;

    let currentLi = button.parentElement.parentElement;
    id = currentLi.id;
    console.log(id);

    let httpHeaders = {
      method: "DELETE",
    };

    fetch(BASE_URL + id, httpHeaders).then((response) => {
      console.log(response);

      loadHandler();

      //   addRecordBtn.disabled = false;
      //   editRecordBtn.disabled = true;
    });
  }

  function addHandler(e) {
    e.preventDefault();

    let name = nameHTML.value;
    let steps = stepsHTML.value;
    let calories = caloriesHTML.value;
    let newRecord = {};
    newRecord.name = name;
    newRecord.steps = steps;
    newRecord.calories = calories;

    let httpHeaders = {
      method: "POST",
      body: JSON.stringify(newRecord),
    };

    fetch(BASE_URL, httpHeaders)
      .then((response) => response.json())
      .then((result) => {
        // console.log(result);
        nameHTML.value = "";
        stepsHTML.value = "";
        caloriesHTML.value = "";

        loadHandler();
      });
      
    nameHTML.value = "";
    stepsHTML.value = "";
    caloriesHTML.value = "";
  }

  function editHandler(e) {
    let name = nameHTML.value;
    let steps = stepsHTML.value;
    let calories = caloriesHTML.value;
    let newRecord = {};
    newRecord.name = name;
    newRecord.steps = steps;
    newRecord.calories = calories;
    newRecord._id = id;

    let httpHeaders = {
      method: "PUT",
      body: JSON.stringify(newRecord),
    };

    fetch(BASE_URL + id, httpHeaders).then((response) => {
      console.log(response);

      nameHTML.value = "";
      stepsHTML.value = "";
      caloriesHTML.value = "";

      loadHandler();

      addRecordBtn.disabled = false;
      editRecordBtn.disabled = true;
    });
  }
}

solution();
