// 1.	*Login

// function solve(loginData) {
//   let username = loginData.shift();
//   let password = username.split("").reverse().join("");

//   for (let i = 0; i < loginData.length; i++) {
//     if (i === 3) {
//       if (password === loginData[i]) {
//         console.log(`User ${username} logged in.`);
//         break;
//       } else {
//         console.log(`User ${username} blocked!`);
//         break;
//       }
//     } else if (password === loginData[i]) {
//       console.log(`User ${username} logged in.`);
//       break;
//     } else {
//       console.log("Incorrect password. Try again.");
//     }
//   }
// }

// solve(['momo','omom']);

// 02. Bitcoin "Mining"

// function solve(golds) {
//   let bitcoins = 0;
//   let firstDay = 0;
//   let money = 0;

//   let goldPrice = 67.51;
//   let bitcoinPrice = 11949.16;

//   for (let i = 1; i <= golds.length; i++) {
//     if (i === 3) {
//       money += golds[i - 1] * goldPrice * 0.7;
//     } else {
//       money += golds[i - 1] * goldPrice;
//     }

//     // 1
//     while (money >= bitcoinPrice) {
//       if (firstDay === 0) {
//         firstDay = i;
//       }
//       bitcoins++;
//       money -= bitcoinPrice;
//     }
//     // 1

//     // // 0r 2
//     // if (firstDay === 0 && ~~ (money / bitcoinPrice) > 0) {
//     //     firstDay = i;
//     // }
//     // bitcoins += ~~ (money / bitcoinPrice)
//     // money %= bitcoinPrice
//     // // 2

//   }
//   console.log(`Bought bitcoins: ${bitcoins}`)
//   if (bitcoins > 0) {
//     console.log(`Day of the first purchased bitcoin: ${firstDay}`)
//   }
//   console.log(`Left money: ${money.toFixed(2)} lv.`)
// }

// solve(
//     [3124.15, 504.212, 2511.124]
// )

// 3.	* The Pyramid of King Djoser

function pyramid(base, increment) {
  let stone = 0;
  let marble = 0;
  let lapisLazuli = 0;
  let gold = 0;

  let height = Math.ceil(base / 2);

  for (let i = 1; i <= height; i++) {
    if ((base - 2 * i) > 0) {
      stone += (base - 2 * i) ** 2;
    }
    if (i === height) {
      gold = (base - 2 * i + 2) ** 2;
    } else if (i % 5 === 0) {
      lapisLazuli += (base - 2 * i + 1) * 4;
    } else {
      marble += (base - 2 * i + 1) * 4;
    }
  }

  stone = Math.ceil(stone * increment);
  marble = Math.ceil(marble * increment);
  lapisLazuli = Math.ceil(lapisLazuli * increment);
  gold = Math.ceil(gold * increment);

  height = Math.floor(height * increment);

  let output =
    `Stone required: ${stone}` +
    `\nMarble required: ${marble}` +
    `\nLapis Lazuli required: ${lapisLazuli}` +
    `\nGold required: ${gold}` +
    `\nFinal pyramid height: ${height}`;

  return output;
}

console.log(pyramid(23, 0.5));
