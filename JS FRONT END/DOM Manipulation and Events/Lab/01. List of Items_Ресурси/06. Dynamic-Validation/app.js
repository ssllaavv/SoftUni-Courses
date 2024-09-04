function validate() {
  let inputHTML = document.getElementById("email");
  inputHTML.addEventListener("mouseout", blurHandler);

  function blurHandler(e) {
    let currentTarget = e.currentTarget;
    let value = currentTarget.value;
    let regex = /^[a-z]+@[a-z]+\.[a-z]+$/;
    let emailIsValid = regex.test(value);

    if (!emailIsValid && !inputHTML.classList.contains("error")) {
      inputHTML.classList.add("error");
    } else if (emailIsValid && inputHTML.classList.contains("error")) {
      inputHTML.classList.remove('error');
    }
  }
}
