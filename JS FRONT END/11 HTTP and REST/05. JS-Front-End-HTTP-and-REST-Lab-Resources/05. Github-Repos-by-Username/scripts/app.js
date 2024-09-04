function loadRepos() {
	let username = document.getElementById('username').value;
	let reposHTML = document.getElementById('repos');

	reposHTML.innerHTML = "";



	fetch(`https://api.github.com/users/${username}/repos`)
		.then((response) => 
			response.json()
		)
		.then((data) =>{
			console.log(data)
			for (const repo of data) {
				let repoLink = repo.html_url;
				let repoName = repo.full_name;
				let newLi = document.createElement('li');
				let newA = document.createElement('a');
				newLi.appendChild(newA);

				newA.href = repoLink;
				newA.textContent = repoName;

				reposHTML.appendChild(newLi);
			}
	
		})

}