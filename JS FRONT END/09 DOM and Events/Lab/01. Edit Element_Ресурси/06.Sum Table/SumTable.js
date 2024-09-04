function sumTable() {
  let sumCell = document.getElementById("sum");
  let tableRows = Array.from(document.querySelectorAll("tr"));

  tableRows.pop();
  tableRows.shift();
  let sum = 0;

  for (const el of tableRows) {
    // console.log(el.children[1].textContent);
    sum += Number(el.children[1].textContent);
    // console.log(sum);
  }
  sumCell.textContent = sum;
}
