function toggle() {
  let button = document.querySelector(".button");
  let extra = document.getElementById("extra");
  let displayStyle = window.getComputedStyle(extra).display;

  if (button.textContent === "More" && displayStyle === "none") {
    extra.style.display = "block";
    button.textContent = "Less";
  } else if (button.textContent === "Less" && displayStyle === "block") {
    extra.style.display = "none";
    button.textContent = "More";
  }
}
