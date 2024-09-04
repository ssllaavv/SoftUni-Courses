// 1.	Multiply the Number by 2

// function solve(number) {
//     console.log(2 * number)
// }

// solve(2)

// 2.	Student Information

// function solve(name, age, grade) {
//     console.log(`Name: ${name}, Age: ${age}, Grade: ${grade.toFixed(2)}`);
// };

// solve('John', 15, 5.54678)

// 03. Excellent grade

// function solve(grade) {
//     if (grade >= 5.5) {
//         console.log("Excellent")
//     }
//     else {
//         console.log("Not excellent")
//     }
// }

// solve(5.22)

// 4.	Month Printer

// function solve(num) {
//     switch(num) {
//         case 1:
//             console.log("January");
//             break;

//         case 2:
//             console.log("February");
//             break;
//         case 3:
//             console.log("March");
//             break;
//         case 4:
//             console.log("April");
//             break;
//         case 5:
//             console.log("May");
//             break;
//         case 6:
//             console.log("June");
//             break;
//         case 7:
//             console.log("July");
//             break;
//         case 8:
//             console.log("August");
//             break;
//         case 9:
//             console.log("September");
//             break;
//         case 10:
//             console.log("October");
//             break;
//         case 11:
//             console.log("November");
//             break;
//         case 12:
//             console.log("December");
//             break;
//         default:
//             console.log("Error!")
//     }
// }

// solve(12)

// 5.	Math Operations

// function solve(x, y, operator) {

//     let result;
//     switch (operator) {
//         case "+":
//             result = (x + y);
//             break;
//         case "-":
//             result = (x - y);
//             break;
//         case "*":
//             result = (x * y);
//             break;
//         case "**":
//             result = (x ** y);
//             break;
//         case "/":
//             result = (x / y);
//             break;
//         case "%":
//             result = (x % y);
//             break;
//     }
//     console.log(result)
// }

// solve(3, 5.5, '*')

// 06. Largest Number

// function solve(x, y, z) {

//     let result;

//     if (x > y && x > z) {
//         result = x;
//     } else if (z > y && z > x) {
//         result = z
//     } else if (y > x && y > z) {
//         result = y;
//     }
//     console.log(`The largest number is ${result}.`)
// }

// solve(6, 6, 5)

// 7.	Theatre Promotions

// function solve(day, age) {
//   let price;

//   switch (day) {
//     case "Weekday":
//       switch (true) {
//         case 0 <= age && age <= 18:
//           price = 12;
//           break;
//         case 18 < age && age <= 64:
//           price = 18;
//           break;
//         case 64 < age && age <= 122:
//           price = 12;
//           break;
//       }
//       break;
//     case "Weekend":
//       switch (true) {
//         case 0 <= age && age <= 18:
//           price = 15;
//           break;
//         case 18 < age && age <= 64:
//           price = 20;
//           break;
//         case 64 < age && age <= 122:
//           price = 15;
//           break;
//       }
//       break;
//     case "Holiday":
//       switch (true) {
//         case 0 <= age && age <= 18:
//           price = 5;
//           break;
//         case 18 < age && age <= 64:
//           price = 12;
//           break;
//         case 64 < age && age <= 122:
//           price = 10;
//           break;
//       }
//       break;
//   }
//   if ((price === undefined)) {
//     console.log("Error!");
//   } else {
//     console.log(`${price}$`);
//   }
// }

// solve('Holiday', 15);

// 8.	Circle Area

// function calculateCircleArea(radius) {

//     let result;

//     if (typeof radius === "number") {
//         result = Math.PI * (radius ** 2)
//     }

//     if (result === undefined) {
//         console.log(`We can not calculate the circle area, because we receive a ${typeof radius}.`)
//     } else {
//         console.log(result.toFixed(2))
//     }
// }

// calculateCircleArea(5)

// 09. Numbers from 1 to 5

// function solve() {
//   for (let i = 1; i <= 5; i++) {
//     console.log(i);
//   }
// }

// solve();

// 10. Numbers from M to N

function solve(m, n) {
  for (let i = m; i >= n; i--) {
    console.log(i);
  }
}

solve(4, 1);
