function solve() {
  let input = document.getElementById("input");
  let output = document.getElementById("output");
  let result = "";

  console.log(input.value);

  let sentences = input.value.split(".");

  let counter = 1;
  let paragraph = [];
  for (const sentence of sentences) {
    console.log(sentence);
    if (counter === 3 && sentence.trim() !== "") {
      paragraph.push(sentence.trim());
      counter = 1;
      result += `<p>${paragraph.join(". ") + "."}</p>`;
      paragraph = [];
    } else if (sentence.trim() !== "") {
      paragraph.push(sentence.trim());
      counter += 1;
    }
  }
  result += `<p>${paragraph.join(". ") + "."}</p>`;
  output.innerHTML = result;
}
