// 01. Ages

// function solve(age) {
//   let result;

//   switch (true) {
//     case age >= 0 && age <= 2:
//       result = "baby";
//       break;
//     case age >= 3 && age <= 13:
//       result = "child";
//       break;
//     case age >= 14 && age <= 19:
//       result = "teenager";
//       break;
//     case age >= 20 && age <= 65:
//       result = "adult";
//       break;
//     case age >= 0 && age <= 2:
//       result = "baby";
//       break;
//     case age >= 66:
//       result = "elder";
//       break;
//     default:
//       result = "out of bounds";
//   }
//   console.log(result);
// }

// solve(-1)

// 02. Vacation

// function solve(count, type, day) {
//   let price;
//   let totalPrice;

//   switch (type) {
//     case "Students":
//       switch (day) {
//         case "Friday":
//           price = 8.45;
//           break;

//         case "Saturday":
//           price = 9.8;
//           break;

//         case "Sunday":
//           price = 10.46;
//           break;
//       }
//       totalPrice = count * price;
//       if (count >= 30) {
//         totalPrice *= 0.85;
//       }
//       break;

//     case "Business":
//       switch (day) {
//         case "Friday":
//           price = 10.9;
//           break;

//         case "Saturday":
//           price = 15.6;
//           break;

//         case "Sunday":
//           price = 16;
//           break;
//       }

//       if (count >= 100) {
//         count -= 10;
//       }
//       totalPrice = count * price;
//       break;

//     case "Regular":
//       switch (day) {
//         case "Friday":
//           price = 15;
//           break;

//         case "Saturday":
//           price = 20;
//           break;

//         case "Sunday":
//           price = 22.5;
//           break;
//       }
//       totalPrice = count * price;
//       if (count >= 10 && count <= 20) {
//         totalPrice *= 0.95;
//       }
//       break;
//   }
//   console.log(`Total price: ${totalPrice.toFixed(2)}`);
// }

// solve(40, "Regular", "Saturday");

03. Leap Year

function checkLeapYear(year) {
  if ((year % 4 === 0 && year % 100 !== 0) || year % 400 === 0) {
    console.log("yes");
  } else {
    console.log("no");
  }
}

checkLeapYear(4)

04. Print And Sum

function solve(start, end) {
  let numbers = [];
  let sum = 0;

  for (let i = start; i <= end; i++) {
    numbers.push(i);
    sum += i;
  }
  console.log(`${numbers.join(" ")} \nSum: ${sum}`);
}

solve(0, 26);

05. Multiplication Table

function solve(num){
    let result = ""

    for (let i = 1; i <= 10; i++){
        result += `${num} X ${i} = ${num * i}\n`
    }
    console.log(result)
}

solve(5)

// 06. Sum Digits

// function solve(num) {
//   let numArray = num.toString().split("");
//   let result = 0;
//   numArray.forEach((el) => {
//     result += parseInt(el);
//   });
//   console.log(result);
// }

// solve(245678);

// 07. Chars to String

// function solve(a, b, c) {
//   let result = a + b + c;
//   console.log(result);
// }

// solve("1", "5", "p");

// 08. Reversed Chars

// function solve(a, b, c) {
//   result = c + " " + b + " " + a;
//   console.log(result);
// }

// solve("A", "B", "C");

// 09. Fruit

// function solve(fruit, weight, price) {
//   money = (weight * price) / 1000;
//   console.log(
//     `I need $${money.toFixed(2)} to buy ${(weight / 1000).toFixed(
//       2
//     )} kilograms ${fruit}.`
//   );
// }

// solve('apple', 1563, 2.35)

// 10. Same Numbers

// function solve(number) {
//   let numnerArray = number.toString().split("");
//   let isSameNum = true;
//   let sum = 0;

//   for (let i = 0; i <= numnerArray.length - 1; i++) {
//     if (numnerArray[i] !== numnerArray[0]) {
//       isSameNum = false;
//     }
//     sum += parseInt(numnerArray[i]);
//   }
//   console.log(`${isSameNum}\n${sum}`);
// }

// solve(1234);

// 11. Road Radar

// function solve(speed, area) {
//   let areasAndLimits = {
//     motorway: 130,
//     interstate: 90,
//     city: 50,
//     residential: 20,
//   };

//   let severity = {
//     twenty: "speeding",
//     forty: "excessive speeding",
//     more: "reckless driving",
//   };

//   let limit = areasAndLimits[area];
//   let diff = speed - limit;
//   let status;
//   if (diff <= 0) {
//     console.log(`Driving ${speed} km/h in a ${limit} zone`);
//   } else {
//     if (diff <= 20) {
//       status = severity.twenty;
//     } else if (diff <= 40) {
//       status = severity.forty;
//     } else {
//       status = severity.more;
//     }
//     console.log(
//       `The speed is ${diff} km/h faster than the allowed speed of ${limit} - ${status}`
//     );
//   }
// }

// solve(120, "interstate");

// 12. Cooking by Numbers

// function solve(num, ...others) {
//   operations = {
//     chop: "num / 2",
//     dice: "Math.sqrt(num)",
//     spice: "num + 1",
//     bake: "num * 3",
//     fillet: "num * .8",
//   };

//   num = parseInt(num);
//   while (others.length > 0) {
//     num = eval(operations[others.shift()]);
//     console.log(num);
//   }
// }


// solve('9', 'dice', 'spice', 'chop', 'bake', 'fillet')