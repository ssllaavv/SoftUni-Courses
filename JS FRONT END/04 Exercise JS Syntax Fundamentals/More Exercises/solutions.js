// // 1.	*Validity Checker

// function solve(x1, y1, x2, y2) {
//   let first = Math.sqrt(x1 ** 2 + y1 ** 2);
//   let second = Math.sqrt(x2 ** 2 + y2 ** 2);
//   let third = Math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2);

//   let fiorstBool = "invalid";
//   let secondBool = "invalid";
//   let thirdBool = "invalid";

//   if (Number.isInteger(first)) {
//     fiorstBool = "valid";
//   }
//   if (Number.isInteger(second)) {
//     secondBool = "valid";
//   }
//   if (Number.isInteger(third)) {
//     thirdBool = "valid";
//   }

//   let result =
//     `{${x1}, ${y1}} to {0, 0} is ${fiorstBool}` +
//     `\n{${x2}, ${y2}} to {0, 0} is ${secondBool}` +
//     `\n{${x1}, ${y1}} to {${x2}, ${y2}} is ${thirdBool}`;

//   return result;
// }

// console.log(solve(2, 1, 1, 1))

// 2.	*Words Uppercase

// function solve(word) {
//   result = word
//     .toUpperCase()
//     .replace(/[^\w]/g, " ")
//     .trim()
//     .replace(/\s+/g, " ")
//     .split(" ")
//     .join(", ");
//   return result;
// }

// function wordToUpperCase(sentence) {

//   let sentenceUpper = sentence.wordToUpperCase();
//   let pattern = /\w+/g;
//   let sentenceArray = [...sentenceUpper.match(pattern)];

//   console.log(sentenceArray.join(", "));

//   // let result = []

//   // for (let i = 0; i < sentenceArray.length; i ++) {
//   //     result.push(sentenceArray[i][0].toUpperCase())
//   // }

//   // console.log(result.join(", "))
// }

// console.log(wordToUpperCase("Hi, how are you?"));

// function calculator(x, operatop, y) {
//   return eval(`x ${operatop} y`).toFixed(2);
// }

// console.log(calculator(25.5, "-", 3));

// 04. Gladiator Expenses

// function gladiator(
//   fightsCount,
//   helmetPrice,
//   swordPrice,
//   shiledPrice,
//   armorPrice
// ) {

//   let helmetCount = 0;
//   let swordCount = 0;
//   let shieldCount = 0;
//   let armorCount = 0;

//   for (let fightsCounter = 1; fightsCounter <= fightsCount; fightsCounter++) {
//     if (fightsCounter % 2 === 0) {
//       helmetCount++;
//     }
//     if (fightsCounter % 3 === 0) {
//       swordCount++;
//     }
//     if (fightsCounter % 6 === 0) {
//       shieldCount++;
//     }
//     if (fightsCounter % 12 === 0) {
//       armorCount++;
//     }
//   }
//   let expenses =
//     helmetCount * helmetPrice +
//     swordCount * swordPrice +
//     shieldCount * shiledPrice +
//     armorCount * armorPrice;

//   return `Gladiator expenses: ${expenses.toFixed(2)} aureus`;
// }

// console.log(gladiator(7, 2, 3, 4, 5));

// 5.	*Spice Must Flow

// 5.	*Spice Must Flow

function spice(yield) {

  let yieldTotal = 0;
  let days = 0;

  while (true) {

    if (yield >= 100) {
      yieldTotal += yield;
      yield -= 10;
      days++;

      if (yieldTotal >= 26) {
        yieldTotal -= 26;
      }
    } else {
      break;
    }
  }

  if (days > 0) {
    
    if (yieldTotal >= 26) {
      yieldTotal -= 26;
    }
  }

  return `${days}\n${yieldTotal}`
}

console.log(spice(450))
