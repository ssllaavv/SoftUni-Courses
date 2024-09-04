// // 01. Person Info

// function createPerson(firstName, lastName, age) {
//   let person = {};
//   person.firstName = firstName;
//   person.lastName = lastName;
//   person.age = age;

//   return person;
// }

// console.log(createPerson("Peter", "Pan", "20"));

// // 02. City

// function createCity(cityObject) {
//   let city = cityObject;

//   let keys = Object.keys(city);
//   // console.log(keys);

//   let values = Object.values(city);
//   // console.log(values);

//   let entries = Object.entries(city);
//   // for (const prop of entries) {
//   //     console.log(prop);
//   // }

//   for (const key of keys) {
//     console.log(`${key} -> ${city[key]}`);
//   }

//   // for (const entry of entries) {
//   //     console.log(`${entry[0]} -> ${entry[1]}`)
//   // }
// }

// createCity({
//   name: "Sofia",
//   area: 492,
//   population: 1238438,
//   country: "Bulgaria",
//   postCode: "1000",
// });

// // 03. Convert to Object

// function printObjectEntries(jsonStr) {
//   city = JSON.parse(jsonStr);
//   result = "";
//   for (const entry of Object.entries(city)) {
//     result += `${entry[0]}: ${entry[1]}\n`;
//   }
//   return result;
// }

// console.log(
//   printObjectEntries('{"name": "Peter", "age": 35, "town": "Plovdiv"}')
// );

// // 04. Convert to JSON

// function convertToJson(name, lastName, hairColor) {
//     let person = {};
//     person.name = name;
//     person.lastName = lastName;
//     person.hairColor = hairColor;

//     return JSON.stringify(person)
// }

// console.log(convertToJson(
//     'George', 'Jones', 'Brown'
// ))

// // 05. Phone Book

// function printPhoneBook(data) {
//   let phoneBook = {};
//   let result = "";

//   for (const record of data) {
//     token = record.split(" ");
//     phoneBook[token[0]] = token[1];
//   }

//   for (const entry of Object.entries(phoneBook)) {
//     result += `${entry[0]} -> ${entry[1]}\n`;
//   }
//   return result;
// }

// console.log(printPhoneBook(
//     ['Tim 0834212554',
//  'Peter 0877547887',
//  'Bill 0896543112',
//  'Tim 0876566344']

// ))

// // 06. Meetings

// function makeSchedule(data) {
//   let schedule = {};

//   for (const entry of data) {
//     token = entry.split(" ");
//     if (!schedule.hasOwnProperty(token[0])) {
//       schedule[token[0]] = token[1];
//       console.log(`Scheduled for ${token[0]}`);
//     } else {
//       console.log(`Conflict on ${token[0]}!`);
//     }
//   }
//   for (const entry of Object.entries(schedule)) {
//     console.log(`${entry[0]} -> ${entry[1]}`);
//   }
// }

// makeSchedule(["Monday Peter", "Wednesday Bill", "Monday Tim", "Friday Tim"]);

// // 07. Address Book

// function sortAddressBook(data) {
//   let addressBook = {};

//   for (const entry of data) {
//     let token = entry.split(":");
//     addressBook[token[0]] = token[1];
//   }

//   let addressBookArray = Object.entries(addressBook);
//   let sortedAddressBookArray = addressBookArray.sort((a, b) => a[0].localeCompare(b[0]));

//   let result = "";

//   for (const entry of sortedAddressBookArray) {
//     result += `${entry[0]} -> ${entry[1]}\n`;
//   }

//   return result;
// }

// console.log(
//   sortAddressBook([
//     "Bob:Huxley Rd",
//     "John:Milwaukee Crossing",
//     "Peter:Fordem Ave",
//     "Bob:Redwing Ave",
//     "George:Mesta Crossing",
//     "Ted:Gateway Way",
//     "Bill:Gateway Way",
//     "John:Grover Rd",
//     "Peter:Huxley Rd",
//     "Jeff:Gateway Way",
//     "Jeff:Huxley Rd",
//   ])
// );

// // 08. Cats

// function meowingCats(data) {
//   class Cat {
//     constructor(name, age) {
//       this.name = name;
//       this.age = age;
//     }
//     meow() {
//       return `${this.name}, age ${this.age} says Meow`;
//     }
//   }

//   let catsList = [];

//   for (const entry of data) {
//     let [name, age] = entry.split(" ");
//     let cat = new Cat(name, age);
//     catsList.push(cat);
//   }

//   catsList.forEach((cat) => {
//     console.log(cat.meow());
//   });
// }

// meowingCats(
//     ['Candy 1', 'Poppy 3', 'Nyx 2']
// );

// 9. Songs

function findSongs(data) {
  let count = data.shift();
  let target = data.pop();
  let songsList = [];
  let result = "";

  class Song {
    constructor(typeList, name, time) {
      this.typeList = typeList;
      this.name = name;
      this.time = time;
    }
  }

  for (const entry of data) {
    songsList.push(new Song(...entry.split("_")));
  }

  for (const song of songsList) {
    if (song.typeList === target || target === "all") {
      result += `${song.name}\n`;
    }
  }
  return result;
}

console.log(findSongs([2, "like_Replay_3:15", "ban_Photoshop_3:48", "all"]));
