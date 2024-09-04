function solve() {
  let [inputTextarea, outputTextarea] = document.querySelectorAll("textarea");
  let [generateBtn, buyBtn] = document.querySelectorAll("button");
  let tbodyHTML = document.querySelector("table > tbody");

  generateBtn.addEventListener("click", generateHandler);
  buyBtn.addEventListener("click", buyHandler);

  function generateHandler(e) {
    let products = eval(inputTextarea.value);
    console.log(products);
    for (const product of products) {
      let newTr = document.createElement("tr");
      newTr.innerHTML = `<td><img src=${product["img"]}></td><td><p>${[
        product["name"],
      ]}</p></td><td><p>${product["price"]}</p></td><td><p>${
        product["decFactor"]
      }</p></td><td><input type="checkbox" /></td>`;
      tbodyHTML.appendChild(newTr);
    }
  }

  function buyHandler(e) {
    let allCheckBoxes = Array.from(
      document.querySelectorAll("table tbody tr input")
    );
    let checkedCheckboxes = allCheckBoxes.filter((a) => a.checked);

    console.log(checkedCheckboxes);
    let allCheckedRows = [];

    for (const checkBox of checkedCheckboxes) {
      let row = checkBox.parentElement.parentElement;
      allCheckedRows.push(row);
    }
    let furnitureList = [];
    let totalPrice = 0;
    let averageDecoration = 0;

    for (const r of allCheckedRows) {
      let paragraphs = Array.from(r.querySelectorAll("p"));
      let name = paragraphs[0].textContent;
      let price = Number(paragraphs[1].textContent);
      let decoration = Number(paragraphs[2].textContent);

      furnitureList.push(name);
      totalPrice += price;
      averageDecoration += decoration;
    }
    averageDecoration /= allCheckedRows.length;

    console.log(furnitureList);
    console.log(totalPrice);
    console.log(averageDecoration);

    outputTextarea.value =
      `Bought furniture: ${furnitureList.join(", ")}\n` +
      `Total price: ${totalPrice.toFixed(2)}\n` +
      `Average decoration factor: ${averageDecoration}`;
  }
}
