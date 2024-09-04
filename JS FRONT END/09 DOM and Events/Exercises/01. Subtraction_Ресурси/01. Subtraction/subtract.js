function subtract() {
    let firstNumber = document.getElementById('firstNumber');
    let secondNumber = document.getElementById('secondNumber');
    let result = document.getElementById('result');
    result.textContent = Number(firstNumber.value) - Number(secondNumber.value);

    // console.log(firstNumber.value);
    // console.log(secondNumber.value);
    // console.log(result);
}