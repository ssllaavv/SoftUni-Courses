function extract(content) {
    
  let targetText = document.getElementById(content).textContent;
  let regex = /\(([^)]+)\)/g;
  let matches = targetText.match(regex);
  matches = matches.map((match) => match.slice(1, -1));

  return matches.join("; ");
}

console.log(extract("content"));
