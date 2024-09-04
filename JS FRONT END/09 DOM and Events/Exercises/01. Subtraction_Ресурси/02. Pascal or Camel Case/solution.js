function solve() {
  let text = document.getElementById("text").value;
  let namingConvention = document.getElementById("naming-convention").value;
  let result = document.getElementById("result");
  let words = text.split(" ");
  let processedText = "";

  if (namingConvention === "Pascal Case") {
    for (const word of words) {
      let processedWord =
        word.charAt(0).toUpperCase() + word.slice(1).toLowerCase();
      processedText += processedWord;
    }
  } else if (namingConvention === "Camel Case") {
    for (let i = 0; i < words.length; i++) {
      if (i === 0) {
        processedText += words[i].toLowerCase();
      } else {
        processedText +=
          words[i].charAt(0).toUpperCase() + words[i].slice(1).toLowerCase();
      }
    }
  } else {
    processedText = "Error!";
  }
  result.textContent = processedText;
  console.log(result);
}
