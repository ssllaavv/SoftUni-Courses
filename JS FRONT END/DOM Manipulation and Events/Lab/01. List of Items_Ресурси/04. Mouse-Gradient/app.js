// function attachGradientEvents() {
//   let gradientElementHTML = document.getElementById("gradient-box");
//   let resultHTML = document.getElementById("result");

//   gradientElementHTML.addEventListener("mousemove", mouseMoveHandler);

//   function mouseMoveHandler(e) {
//     const rect = gradientElementHTML.getBoundingClientRect();
//     const xPos = e.clientX - rect.left;
//     const xPercent = (xPos / rect.width) * 100;

//     resultHTML.textContent = Math.round(xPercent) + '%';
//   }
// }


function attachGradientEvents() {

  let bar = document.getElementById("gradient")
  let result = document.getElementById("result")
  p = document.createElement("p")
  result.appendChild(p)

  bar.addEventListener("mousemove", getColor)

  function getColor(e) {
      let x = e.offsetX;
      p.textContent = `${Math.floor((x / 3))}%`
  }
}