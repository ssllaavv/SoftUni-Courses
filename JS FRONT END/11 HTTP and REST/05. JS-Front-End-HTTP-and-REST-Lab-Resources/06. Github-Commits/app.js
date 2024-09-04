function loadCommits() {
  let userName = document.getElementById("username").value;
  let repoName = document.getElementById("repo").value;
  let resultHTML = document.getElementById("commits");
  resultHTML.innerHTML = "";

  fetch(`https://api.github.com/repos/${userName}/${repoName}/commits`)
    .then((response) => response.json())
    .then((data) => {
      for (const commit of data) {
        console.log(commit.commit);

        let newLi = document.createElement("li");
        newLi.textContent = `${commit.commit.author.name}: ${commit.commit.message}`;
        resultHTML.appendChild(newLi);
      }
    })
    .catch((error) => {
      let newLi = document.createElement("li");
      newLi.textContent = `Error: ${error} (Not Found)`;
      resultHTML.appendChild(newLi);
    });
}
