function solve() {
  let addButtonsHTML = document.querySelectorAll(".add-product");
  for (const button of addButtonsHTML) {
    button.addEventListener("click", addHandler);
    console.log(button);
  }

  let checkoutButtonHTML = document.querySelector("button.checkout");
  checkoutButtonHTML.addEventListener("click", checkoutHandler);

  let products = [];
  let resultHTML = document.querySelector("textarea");

  function addHandler(e) {
    let product = null;
    let currentTarget = e.currentTarget;
    let productDivHTML = currentTarget.parentElement.parentElement;

    let price = Number(
      productDivHTML.querySelector(".product-line-price").textContent
    );
    let name = productDivHTML.querySelector(".product-title").textContent;
    for (const p of products) {
      if (p.name === name) {
        product = p;
        product.quantity += 1;
        break;
      }
    }

    if (!product) {
      product = {};
      product.name = name;
      product.price = price;
      product.quantity = 1;
      products.push(product);
    }

    console.table(products);
    resultHTML.textContent += `Added ${product.name} for ${product.price.toFixed(
      2
    )} to the cart.\n`;
  }

  function checkoutHandler(e) {
    let addButtonsHTML = document.querySelectorAll("button");
    for (const button of addButtonsHTML) {
      button.disabled = true;
    }
    let productsList = [];
    let totalPrice = 0;
    for (const p of products) {
      productsList.push(p.name);
      totalPrice += p.price * p.quantity;
    }
    resultHTML.textContent += `You bought ${productsList.join(
      ", "
    )} for ${totalPrice.toFixed(2)}.`;
  }
}
