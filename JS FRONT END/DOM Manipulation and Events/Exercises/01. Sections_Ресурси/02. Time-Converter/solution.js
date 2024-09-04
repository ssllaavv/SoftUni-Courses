function attachEventsListeners() {
  let dayBtn = document.getElementById("daysBtn");
  let hoursBtn = document.getElementById("hoursBtn");
  let minutesBtn = document.getElementById("minutesBtn");
  let secondsBtn = document.getElementById("secondsBtn");

  let daysHTML = document.getElementById("days");
  let hoursHTML = document.getElementById("hours");
  let minutesHTML = document.getElementById("minutes");
  let secondsHTML = document.getElementById("seconds");

  dayBtn.addEventListener("click", convertFromDaysHandler);
  hoursBtn.addEventListener("click", convertFromHoursHandler);
  minutesBtn.addEventListener("click", convertFormMinutesHandler);
  secondsBtn.addEventListener("click", convertFormSecondsHandler);

  function convertFromDaysHandler(e) {
    let currentTarget = e.currentTarget;
    let value = Number(
      currentTarget.parentElement.querySelectorAll("input")[0].value
    );
    console.log(value);
    hoursHTML.value = value * 24;
    minutesHTML.value = value * 24 * 60;
    secondsHTML.value = value * 24 * 3600;
  }

  function convertFromHoursHandler(e) {
    let currentTarget = e.currentTarget;
    let value = Number(
      currentTarget.parentElement.querySelectorAll("input")[0].value
    );
    console.log(value);
    daysHTML.value = value / 24;
    minutesHTML.value = value * 60;
    secondsHTML.value = value * 3600;
  }

  function convertFormMinutesHandler(e) {
    let currentTarget = e.currentTarget;
    let value = Number(
      currentTarget.parentElement.querySelectorAll("input")[0].value
    );
    console.log(value);
    daysHTML.value = value / (60 * 24);
    hoursHTML.value = value / 60;
    secondsHTML.value = value * 60;
  }

  function convertFormSecondsHandler(e) {
    let currentTarget = e.currentTarget;
    let value = Number(
      currentTarget.parentElement.querySelectorAll("input")[0].value
    );
    console.log(value);
    daysHTML.value = value / (24 * 3600);
    hoursHTML.value = value / 3600;
    minutesHTML.value = value / 60;
  }
}
