function solve() {
  const BASE_URL = "http://localhost:3030/jsonstore/games/";

  let gamesListHTML = document.getElementById("games-list");

  let loadBtn = document.getElementById("load-games");
  loadBtn.addEventListener("click", loadHandler);

  let gameNameHTML = document.getElementById("g-name");
  let gameTypeHTML = document.getElementById("type");
  let playersHTML = document.getElementById("players");

  let addBtn = document.getElementById("add-game");
  addBtn.addEventListener("click", addHandler);

  let editBtn = document.getElementById("edit-game");
  editBtn.addEventListener("click", editHandler);

  function clearInputs() {
    gameNameHTML.value = "";
    gameTypeHTML.value = "";
    playersHTML.value = "";
  }

  function loadHandler(e) {
    fetch(BASE_URL)
      .then((response) => response.json())
      .then((result) => Object.values(result))
      .then((games) => {
        gamesListHTML.innerHTML = "";
        clearInputs();

        for (const game of games) {
          let gameDiv = document.createElement("div");
          gameDiv.classList.add("board-game");
          gameDiv.id = game._id;
          gameDiv.innerHTML = 
                    `<div class="content">
                        <p>${game.name}</p>
                        <p>${game.players}</p>
                        <p>${game.type}</p>
                    </div>
                    <div class="buttons-container">
                        <button class="change-btn">Change</button>
                        <button class="delete-btn">Delete</button>
                    </div>`;
          let changeBtn = gameDiv.querySelector(".change-btn");
          changeBtn.addEventListener("click", changeHandler);
          let deleteBtn = gameDiv.querySelector(".delete-btn");
          deleteBtn.addEventListener("click", deleteHandler);

          gamesListHTML.appendChild(gameDiv);
        }
      });
  }

  function addHandler(e) {}

  function editHandler(e) {}

  function changeHandler(e) {}

  function deleteHandler(e) {}
}

solve();
