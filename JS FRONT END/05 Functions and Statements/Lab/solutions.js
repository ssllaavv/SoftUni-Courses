// // 1. Format Grade

// function printGrade(grade) {
//   let output = "";

//   if (grade >= 5.5) {
//     output = `Excellent (${grade.toFixed(2)})`;
//   } else if (grade >= 4.5) {
//     output = `Very good (${grade.toFixed(2)})`;
//   } else if (grade >= 3.5) {
//     output = `Good (${grade.toFixed(2)})`;
//   } else if (grade >= 3) {
//     output = `Poor (${grade.toFixed(2)})`;
//   } else {
//     output = `Fail (2)`;
//   }
//   return output;
// }

// console.log(printGrade(4.24));

// 02. Math cunction

// function  mathPower(num, power) {
//     return num ** power
// }

// console.log(mathPower(2, 8))

// 03. Repeat String

// function repeatString(text, times) {
//   return text.repeat(times);
// }

// console.log(repeatString("abc", 3));

// 04. Orders

// function orders(product, count) {
//   let coffee = 1.5;
//   let water = 1.0;
//   let coke = 1.4;
//   let snacks = 2.0;

//   return (eval(product) * count).toFixed(2);
// }

// console.log(orders("coffee", 2))

// 05. Simple Calculator

// function simpleCalculator(a, b, operator) {
//   let operators = {
//     multiply: "*",
//     divide: "/",
//     add: "+",
//     subtract: "-",
//   };

//   return eval(`a ${operators[operator]} b`);
// }

// console.log(simpleCalculator(40, 8, "divide"));

// 06. Sign Check

function checkSing(a, b, c) {
  let output = "";
  let nums = [a, b, c];
  if (
    nums.every((num) => num > 0) ||
    nums.every((num) => num < 0) ||
    (a > 0 && b > 0) ||
    (a > 0 && c > 0) ||
    (b > 0 && c > 0)
  ) {
    output = "Negative";
  } else {
    output = "Positive";
  }
  return output;
}

console.log(checkSing(-6, -12, 14));
