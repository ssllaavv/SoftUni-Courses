window.addEventListener("load", solve);

function solve() {
  let animalTypeHTML = document.getElementById("type");
  let animalAgeHTML = document.getElementById("age");
  let animalGenderHTML = document.getElementById("gender");

  let adoptBtn = document.getElementById("adopt-btn");

  let adoptionInfoUl = document.getElementById("adoption-info");
  let adoptedListUl = document.getElementById("adopted-list");

  adoptBtn.addEventListener("click", addHandler);

  function addHandler(e) {
    e.preventDefault();

    if (
      animalTypeHTML.value !== "" &&
      animalAgeHTML.value !== "" &&
      animalGenderHTML.value !== ""
    ) {
      let newLi = document.createElement("li");
      newLi.innerHTML = `<article>
          <p>Pet:${animalTypeHTML.value}</p>
          <p>Gender:${animalGenderHTML.value}</p>
          <p>Age:${animalAgeHTML.value}</p>
      </article>
        <div class="buttons">
          <button class="edit-btn">Edit</button>
          <button class="done-btn">Done</button>
      </div>`;

      adoptionInfoUl.appendChild(newLi);

      let allLiElement = Array.from(adoptionInfoUl.querySelectorAll("li"));
      let lastLiElement = allLiElement[allLiElement.length - 1];
      let [editBtn, doneBtn] = Array.from(
        lastLiElement.querySelectorAll("button")
      );

      editBtn.addEventListener("click", editHandler);
      doneBtn.addEventListener("click", doneHandler);

      animalTypeHTML.value = "";
      animalAgeHTML.value = "";
      animalGenderHTML.value = "";
    }
  }

  function editHandler(e) {
    let editBtn = e.currentTarget;

    let currentLi = editBtn.parentElement.parentElement;
    let paragraphs = Array.from(currentLi.querySelectorAll("p"));

    let pet = paragraphs[0].textContent.split(":")[1];
    let gender = paragraphs[1].textContent.split(":")[1];
    let age = paragraphs[2].textContent.split(":")[1];

    currentLi.parentElement.removeChild(currentLi);

    animalTypeHTML.value = pet;
    animalAgeHTML.value = age;
    animalGenderHTML.value = gender;
  }

  function doneHandler(e) {
    let editBtn = e.currentTarget;

    let currentLi = editBtn.parentElement.parentElement;
    currentLi.parentElement.removeChild(currentLi);

    let buttonsDiv = currentLi.querySelector(".buttons");
    currentLi.removeChild(buttonsDiv);

    let clearBtn = document.createElement("button");
    clearBtn.classList.add("clear-btn");
    clearBtn.textContent = "Clear";

    currentLi.appendChild(clearBtn);

    adoptedListUl.appendChild(currentLi);

    clearBtn.addEventListener("click", clearHandler);
  }

  function clearHandler(e) {
    let currentLi = e.currentTarget.parentElement;
    currentLi.parentElement.removeChild(currentLi);
  }
}
