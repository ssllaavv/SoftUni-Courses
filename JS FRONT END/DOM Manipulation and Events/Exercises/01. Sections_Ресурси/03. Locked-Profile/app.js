function lockedProfile() {
  let profileDivHTML = Array.from(document.querySelectorAll(".profile"));

  for (const div of profileDivHTML) {
    let button = div.querySelector("button");
    button.addEventListener("click", showHideHandler);
  }

  function showHideHandler(e) {
    let currentTarget = e.currentTarget;
    let profileDiv = currentTarget.parentElement;
    let hiddenDiv = profileDiv.querySelector("div");

    console.log(profileDiv);

    let inputs = Array.from(profileDiv.querySelectorAll("input"));

    console.log(inputs);

    if (inputs[0].checked === false) {
      if (hiddenDiv.style.display === "none") {
        hiddenDiv.style.display = "block";
      } else {
        hiddenDiv.style.display = "none";
      }
    }
  }
}
