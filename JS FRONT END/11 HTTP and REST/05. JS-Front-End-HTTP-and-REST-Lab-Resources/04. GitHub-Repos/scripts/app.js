function loadRepos() {
  let resultHTML = document.getElementById("res");
  let result = '';

  fetch("https://api.github.com/users/testnakov/repos")
   .then((response) => response.text()
   .then((res) => resultHTML.textContent = res)
  );
}
