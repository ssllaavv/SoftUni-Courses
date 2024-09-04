// // 01. Smallest of Three Numbers

// // solution 1
// function findSmallest(a, b, c) {
//   return Math.min(a, b, c);
// }

// // solution 2
// function findSmallest(a, b, c) {
//     let smallestNumber = 999999999999
//     for (const num of [a, b, c]) {
//         if (num < smallestNumber) {
//             smallestNumber = num
//         }
//     }
//     return smallestNumber
// }

// console.log(findSmallest(
//     600,
//     342,
//     123
//     ));

// 02. Add and Subtract

// function addAmdSubtract(a, b, c) {
//   function addTwoNumbers(a, b) {
//     return a + b;
//   }

//   function subtractTwoNumbers(a, b) {
//     return a - b;
//   }

//   return subtractTwoNumbers(addTwoNumbers(a, b), c);
// }

// console.log(addAmdSubtract(1, 17, 30));

// // 03. Characters in Range

// function getAllCharactersBetween(a, b) {
//   let asciiA = a.charCodeAt(0);
//   let asciiB = b.charCodeAt(0);

//   let firstCode = Math.min(asciiA, asciiB);
//   let lastCode = Math.max(asciiA, asciiB);

//   let output = [];

//   for (let i = firstCode + 1; i < lastCode; i++) {
//     output.push(String.fromCharCode(i));
//   }

//   return output.join(" ");
// }

// console.log(getAllCharactersBetween("a", "d"));

// // 04. Odd And Even Sum

// function getEvensAndOddsSums(number) {
//   let stringNum = String(number);
//   let oddsSum = 0;
//   let evensSum = 0;

//   for (const n of stringNum) {
//     if (Number(n) % 2 === 0) {
//       evensSum += Number(n);
//     } else {
//       oddsSum += Number(n);
//     }
//   }

//   output = ` Odd sum = ${oddsSum}, Even sum = ${evensSum}`;
//   return output;
// }

// console.log(getEvensAndOddsSums(  3495892137259234));

// // 05. Palindrome Integers
// function checkForPalindromes(numbers) {
//   let output = [];

//   numbers.forEach((n) => {
//     output.push(Number(String(n).split("").reverse().join("")) === n);
//   });

//   return output.join("\n");
// }

// console.log(checkForPalindromes([123, 323, 421, 121]));

// // 06. Password Validator

// function checkIfPasswordIsValid(password) {
//   function checkLengthIsValid(password) {
//     return password.length >= 6 && password.length <= 10;
//   }

//   function checkIfPasswordContainsOnlyLettersAndDigits(password) {
//     let regex = /^[A-Za-z0-9]+$/;
//     return regex.test(password);
//   }

//   function checkIfPasswordContainsAtLeastTwoDigits(password) {
//     let regex = /\d/g;
//     numberOfDigits = (password.match(regex) || []).length;
//     return numberOfDigits >= 2;
//   }

//   let output = "";

//   if (!checkLengthIsValid(password)) {
//     output += "Password must be between 6 and 10 characters\n";
//   }
//   if (!checkIfPasswordContainsOnlyLettersAndDigits(password)) {
//     output += "Password must consist only of letters and digits\n";
//   }
//   if (!checkIfPasswordContainsAtLeastTwoDigits(password)) {
//     output += "Password must have at least 2 digits\n";
//   }
//   if (
//     [
//       checkIfPasswordContainsAtLeastTwoDigits(password),
//       checkIfPasswordContainsOnlyLettersAndDigits(password),
//       checkLengthIsValid(password),
//     ].every((x) => x === true)
//   ) {
//     output = "Password is valid";
//   }

//   return output;
// }

// console.log(checkIfPasswordIsValid('Pa$s$s'));

// // 07. NxN Matrix

// function getMatrix(n) {
//   let matrix = Array(n)
//     .fill((`${n} `.repeat(n).trim()));
//   return matrix.join("\n")

// }

// console.log(getMatrix(5));

// // 08. Perfect Number

// function checkIfNumberIsPerfect(number) {
//   let sumOdDivisors = 0;

//   for (let i = 1; i <= number / 2 + 1; i++) {
//     if (number % i === 0) {
//       sumOdDivisors += i;
//     }
//   }

//   if (sumOdDivisors === number) {
//     return "We have a perfect number!";
//   } else {
//     return "It's not so perfect.";
//   }
// }

// console.log(checkIfNumberIsPerfect(1236498));

// //09. Loading Bar

// function printLoadingBar(percents) {
//     let output = `${percents}% [${"%".repeat(percents / 10)}${".".repeat((100 - percents ) / 10)}]`
//     if (percents === 100) {
//         output = "100% Complete!"
//     } else {
//         output += "\nStill loading..."
//     }
//     return output
// }

// console.log(printLoadingBar(90))

// // 10. Factorial Division

// function twoFactorialsDivision(a, b) {
//   function findFactorial(n) {
//     if (n === 1) {
//       return 1;
//     }
//     return n * findFactorial(n - 1);
//   }

//   return (findFactorial(a) / findFactorial(b)).toFixed(2);
// }

// console.log(twoFactorialsDivision(6, 2));
