// // 01. Employees

// function createListOfEmployees(data) {
//   class Employee {
//     constructor(name) {
//       this.name = name;
//       this.personalNumber = name.length;
//     }
//   }

//   let listOfEmployees = [];

//   for (const name of data) {
//     listOfEmployees.push(new Employee(name));
//   }

//   let result = "";
//   for (const employee of listOfEmployees) {
//     result += `Name: ${employee.name} -- Personal Number: ${employee.personalNumber}\n`;
//   }

//   return result;
// }

// console.log(
//   createListOfEmployees([
//     "Samuel Jackson",
//     "Will Smith",
//     "Bruce Willis",
//     "Tom Holland",
//   ])
// );

// // 02. Towns

// function createTownsObjects(inputData) {
//   class Town {
//     constructor(name, latitude, longitude) {
//       this.town = name;
//       this.latitude = Number(latitude).toFixed(2);
//       this.longitude = Number(longitude).toFixed(2);
//     }
//   }

//   let townsList = [];

//   for (const townData of inputData) {
//     let [name, latitude, longitude] = townData.split(" | ");
//     townsList.push(new Town(name, latitude, longitude));
//   }

//   for (const town of townsList) {
//     console.log(JSON.parse(JSON.stringify(town)));
//   }
// }

// createTownsObjects([
//   "Sofia | 42.696552 | 23.32601",
//   "Beijing | 39.913818 | 116.363625",
// ]);

// // 03. Store Provision

// function storeStockManager(onStock, toOrder) {
//   let store = {};

//   for (let i = 0; i < onStock.length; i += 2) {
//     store[onStock[i]] = Number(onStock[i + 1]);
//   }

//   for (let i = 0; i < toOrder.length; i += 2) {
//     if (store.hasOwnProperty(toOrder[i])) {
//       store[toOrder[i]] += Number(toOrder[i + 1]);
//     } else {
//       store[toOrder[i]] = Number(toOrder[i + 1]);
//     }
//   }

//   let result = "";
//   for (const entry of Object.entries(store)) {
//     result += `${entry[0]} -> ${entry[1]}\n`;
//   }

//   return result;
// }

// console.log(
//   storeStockManager(

//   )
// );

// // 04. Movies

// function cerateMovies(inputData) {
//   moviesList = [];
//   result = "";

//   for (const command of inputData) {
//     if (command.includes("addMovie ")) {
//       movie = {};
//       movie.name = command.replace("addMovie ", "");
//       moviesList.push(movie);
//     } else if (command.includes("directedBy")) {
//       let [name, director] = command.split(" directedBy ");
//       let moveExists = false;
//       let movie;

//       for (const m of moviesList) {
//         if (m.name === name) {
//           moveExists = true;
//           movie = m;
//           break;
//         }
//       }
//       if (moveExists) {
//         movie.director = director;
//       }
//     } else if (command.includes("onDate")) {
//       let [name, date] = command.split(" onDate ");
//       let moveExists = false;
//       let movie;

//       for (const m of moviesList) {
//         if (m.name === name) {
//           moveExists = true;
//           movie = m;
//           break;
//         }
//       }
//       if (moveExists) {
//         movie.date = date;
//       }
//     }
//   }
//   for (const movie of moviesList) {
//     if (movie.hasOwnProperty("director") && movie.hasOwnProperty("date")) {
//       result += JSON.stringify(movie) + "\n";
//     }
//   }
//   return result;
// }

// console.log(
//   cerateMovies([
//     "addMovie The Avengers",
//     "addMovie Superman",
//     "The Avengers directedBy Anthony Russo",
//     "The Avengers onDate 30.07.2010",
//     "Captain America onDate 30.07.2010",
//     "Captain America directedBy Joe Russo",
//   ])
// );

// // 05. Inventory

// function heroesSort(inputDate) {
//   let heroesList = [];
//   let result = "";

//   for (const heroData of inputDate) {
//     let [name, level, items] = heroData.split(" / ");
//     let hero = {};
//     hero.name = name;
//     hero.level = level;
//     hero.items = items.split(", ");
//     heroesList.push(hero);
//   }

//   heroesArrays = [];
//   for (const hero of heroesList) {
//     heroesArrays.push(Object.entries(hero));
//   }

//   heroesArrays.sort((a, b) => a[1][1] - b[1][1]);

//   for (const hero of heroesArrays) {
//     result +=
//       `Hero: ${hero[0][1]}\n` +
//       `level => ${hero[1][1]}\n` +
//       `items => ${hero[2][1].join(", ")}\n`;
//   }
//   return result.trim();
// }

// console.log(
//   heroesSort([
//     "Batman / 2 / Banana, Gun",
//     "Superman / 18 / Sword",
//     "Poppy / 28 / Sentinel, Antara",
//   ])
// );

// // 06. Word Tracker

// function wordTracker(inputData) {
//   let words = inputData.shift().split(" ");
//   let wordsList = [];
//   result = "";

//   for (const w of words) {
//     let word = {};
//     word.name = w;
//     word.count = 0;

//     for (const el of inputData) {
//       if (el === w) {
//         word.count += 1;
//       }
//     }
//     wordsList.push(word);
//   }

//   let wordsArray = [];
//   for (const word of wordsList) {
//     wordsArray.push(Object.entries(word));
//   }
//   let sortedWordsArray = wordsArray.sort((a, b) => -a[1][1] + b[1][1]);
//   for (const word of sortedWordsArray) {
//     result += `${word[0][1]} - ${word[1][1]}\n`;
//   }

//   return result.trim();
// }

// console.log(
//   wordTracker([
//     "is the",
//     "first",
//     "sentence",
//     "Here",
//     "is",
//     "another",
//     "the",
//     "And",
//     "finally",
//     "the",
//     "the",
//     "sentence",
//   ])
// );

// // 07. Odd Occurrences

// function extractOddOccurrences(inputData) {
//   let dataArray = inputData.split(" ");
//   let dataArrayToLower = [];
//   for (const word of dataArray) {
//     dataArrayToLower.push(word.toLowerCase());
//   }
//   let oddOccurrences = [];

//   for (const word of dataArrayToLower) {
//     let count = 0;
//     for (const el of dataArrayToLower) {
//       if (word === el) {
//         count += 1;
//       }
//     }
//     if (count % 2 != 0 && !oddOccurrences.includes(word)) {
//       oddOccurrences.push(word);
//     }
//   }

//   return oddOccurrences.join(" ");
// }

// console.log(extractOddOccurrences('Cake IS SWEET is Soft CAKE sweet Food'));

// // 08. Piccolo

// function parkingManager(inputData) {
//   parkingState = [];

//   for (const carData of inputData) {
//     let [command, car] = carData.split(", ");
//     if (command === "IN" && !parkingState.includes(car)) {
//       parkingState.push(car);
//     } else if (command === "OUT") {
//       parkingState = parkingState.filter((item) => item !== car);
//     }
//   }

//   sortedParking = parkingState.sort((a, b) => a.localeCompare(b));
//   if (sortedParking.length > 0) {
//     return parkingState.join("\n");
//   } else {
//     return "Parking Lot is Empty";
//   }
// }

// console.log(
//   parkingManager([
//     "IN, CA2844AA",
//     "IN, CA1234TA",
//     "OUT, CA2844AA",
//     "OUT, CA1234TA",
//   ])
// );

// // 09. Make a Dictionary

// function makeDictionary(inputData) {
//   let dictionary = {};
//   let result = "";

//   for (const entry of inputData) {
//     let wordObj = JSON.parse(entry);
//     dictionary[Object.keys(wordObj)[0]] = Object.values(wordObj)[0];
//   }

//   let sortedDictionaryArray = Object.entries(dictionary).sort((a, b) =>
//     a[0].localeCompare(b[0])
//   );

//   for (const [term, description] of sortedDictionaryArray) {
//     result += `Term: ${term} => Definition: ${description}\n`;
//   }

//   return result.trim();
// }

// console.log(
//   makeDictionary([
//     '{"Coffee":"A hot drink made from the roasted and ground seeds (coffee beans) of a tropical shrub."}',
//     '{"Bus":"A large motor vehicle carrying passengers by road, typically one serving the public on a fixed route and for a fare."}',
//     '{"Boiler":"A fuel-burning apparatus or container for heating water."}',
//     '{"Tape":"A narrow strip of material, typically used to hold or fasten something."}',
//     '{"Microphone":"An instrument for converting sound waves into electrical energy variations which may then be amplified, transmitted, or recorded."}',
//   ])
// );

// // 10. Class Vehicle

// class Vehicle {
//   constructor(type, model, parts, fuel) {
//     this.type = type;
//     this.model = model;
//     this.parts = parts;
//     this.parts.quality = this.parts.engine * this.parts.power;
//     this.fuel = fuel;
//   }
//   drive(decreaseFuel) {
//     this.fuel -= decreaseFuel;
//   }
// }

// let parts = { engine: 9, power: 500 };
// let vehicle = new Vehicle("l", "k", parts, 840);
// vehicle.drive(20);
// console.log(vehicle.fuel);
