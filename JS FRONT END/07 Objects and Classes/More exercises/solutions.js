// // 01. Class Storage

// class Storage {
//   constructor(capacity) {
//     this.capacity = capacity;
//     this.storage = [];
//     let totalCost;
//     this.totalCost = 0;
//   }
//   addProduct(product) {
//     this.storage.push(product);
//     this.totalCost += product.price * product.quantity;
//     this.capacity -= product.quantity;
//   }
//   getProducts() {
//     let result = "";
//     for (const product of this.storage) {
//       result += JSON.stringify(product) + "\n";
//     }
//     return result.trim();
//   }
// }

// let productOne = {name: 'Tomato', price: 0.90, quantity: 19};
// let productTwo = {name: 'Potato', price: 1.10, quantity: 10};
// let storage = new Storage(30);
// storage.addProduct(productOne);
// storage.addProduct(productTwo);
// console.log(storage.totalCost);

// // 02. Catalogue

// function createCatalogue(inputData) {
//   let catalogue = [];
//   let result = "";

//   for (const productPrice of inputData) {
//     let [product, price] = productPrice.split(" : ");
//     catalogue.push([product, price]);
//   }
//   let sortedCatalogue = catalogue.sort((a, b) => a[0].localeCompare(b[0]));
//   let currentInitial = "";
//   result += currentInitial + "\n";

//   for (const productPrice of sortedCatalogue) {
//     if (productPrice[0].charAt(0) !== currentInitial) {
//       currentInitial = productPrice[0].charAt(0);
//       result += currentInitial + "\n";
//     }
//     result += `  ${productPrice[0]}: ${productPrice[1]}\n`;
//   }
//   return result;
// }

// console.log(
//   createCatalogue([
//     "Appricot : 20.4",
//     "Fridge : 1500",
//     "TV : 1499",
//     "Deodorant : 10",
//     "Boiler : 300",
//     "Apple : 1.25",
//     "Anti-Bug Spray : 15",
//     "T-Shirt : 10",
//   ])
// );

// // 03. Class Laptop

// class Laptop {
//   constructor(info, quality) {
//     this.info = info;
//     this.quality = quality;
//     this.isOn = false;
//   }
//   turnOn() {
//     if (!this.isOn) {
//       this.isOn = true;
//       this.quality -= 1;
//     }
//   }
//   turnOff() {
//     if (this.isOn) {
//       this.isOn = false;
//       this.quality -= 1;
//     }
//   }
//   showInfo() {
//     return JSON.stringify(this.info);
//   }
//   get price() {
//     return 800 - this.info.age * 2 + this.quality * 0.5;
//   }
// }

// let info = {producer: "Lenovo", age: 1, brand: "Legion"}
// let laptop = new Laptop(info, 10)
// laptop.turnOn()
// console.log(laptop.showInfo())
// laptop.turnOff()
// laptop.turnOn()
// laptop.turnOff()
// console.log(laptop.isOn)

// // 04. Flight Schedule

// function flightsInfo(inputData) {
//   let [flightsInput, changedInput, requiredStatus] = inputData;
//   let flights = [];
//   result = "";

//   for (const f of flightsInput) {
//     let flight = {};
//     let destinationAndNumber = f.split(" ");
//     flight.number = destinationAndNumber.shift();
//     flight.destination = destinationAndNumber.join(" ");
//     flight.status = "initial";
//     flights.push(flight);
//   }

//   for (const f of changedInput) {
//     let numberAndStatus = f.split(" ");
//     let flightNumber = numberAndStatus.shift();
//     let flightStatus = numberAndStatus.join(" ");
//     for (const flight of flights) {
//       if (flight.number === flightNumber) {
//         flight.status = flightStatus;
//       }
//     }
//   }
//   if (requiredStatus[0] === "Ready to fly") {
//     for (const flight of flights) {
//       if (flight.status === "initial") {
//         flight.status = "Ready to fly";
//         result += `{ Destination: '${flight.destination}', Status: '${flight.status}' }\n`;
//       }
//     }
//   } else {
//     for (const flight of flights) {
//       if (flight.status !== "initial") {
//         result += `{ Destination: '${flight.destination}', Status: '${flight.status}' }\n`;
//       }
//     }
//   }
//   return result;
// }

// console.log(
//   flightsInfo([
//     [
//       "WN269 Delaware",
//       "FL2269 Oregon",
//       "WN498 Las Vegas",
//       "WN3145 Ohio",
//       "WN612 Alabama",
//       "WN4010 New York",
//       "WN1173 California",
//       "DL2120 Texas",
//       "KL5744 Illinois",
//       "WN678 Pennsylvania",
//     ],
//     [
//       "DL2120 Cancelled",
//       "WN612 Cancelled",
//       "WN1173 Cancelled",
//       "SK330 Cancelled",
//     ],
//     ["Ready to fly"],
//   ])
// );

// // 05. School Register

// function schoolRegister(inputData) {
//   let students = [];
//   let result = "";
//   let currentGrade = 100;

//   for (const studentEntry of inputData) {
//     let token = studentEntry.split(", ");
//     let student = {};

//     student.name = token[0].split(": ")[1];
//     student.nextGrade = Number(token[1].split(": ")[1]) + 1;
//     student.score = Number(token[2].split(": ")[1]);

//     if (student.score >= 3) {
//       students.push(student);
//       if (student.nextGrade < currentGrade) {
//         currentGrade = student.nextGrade;
//       }
//     }
//   }
//   let studentsArray = [];
//   for (const s of students) {
//     studentsArray.push(Object.entries(s));
//   }
//   let sortedStudents = studentsArray.sort((a, b) => a[1][1] - b[1][1]);

//   students = [];

//   for (const student of sortedStudents) {
//     students.push(Object.fromEntries(student));
//   }

//   let sumOfScores = 0;
//   let studentsCount = 0;
//   studentsOfCurrentGrade = [];

//   result += `${currentGrade} Grade\nList of students: `;

//   for (const student of students) {
//     if (student.nextGrade === currentGrade) {
//       studentsOfCurrentGrade.push(student.name);
//       sumOfScores += student.score;
//       studentsCount += 1;
//     } else {
//       let averageScore = (sumOfScores / studentsCount).toFixed(2);
//       sumOfScores = student.score;
//       studentsCount = 1;
//       currentGrade = student.nextGrade;
//       result +=
//         studentsOfCurrentGrade.join(", ") +
//         `\nAverage annual score from last year: ${averageScore}\n\n${currentGrade} Grade\nList of students: `;

//       studentsOfCurrentGrade = [student.name];
//     }
//   }
//   let averageScore = (sumOfScores / studentsCount).toFixed(2);
//   result +=
//     studentsOfCurrentGrade.join(", ") +
//     `\nAverage annual score from last year: ${averageScore}`;

//   studentsOfCurrentGrade = [];

//   return result;
// }

// console.log(
//   schoolRegister(
//     [
//         'Student name: George, Grade: 5, Graduated with an average score: 2.75',
//         'Student name: Alex, Grade: 9, Graduated with an average score: 3.66',
//         'Student name: Peter, Grade: 8, Graduated with an average score: 2.83',
//         'Student name: Boby, Grade: 5, Graduated with an average score: 4.20',
//         'Student name: John, Grade: 9, Graduated with an average score: 2.90',
//         'Student name: Steven, Grade: 2, Graduated with an average score: 4.90',
//         'Student name: Darsy, Grade: 1, Graduated with an average score: 5.15'
//         ]

//   )
// );

// // 06. Browser History

// function browserHistoryManager(browserHistory, inputCommands) {
//   let result = "";
//   for (const command of inputCommands) {
//     let token = command.split(" ");
//     let action = token.shift();
//     let site = token.join(" ");

//     if (action === "Open") {
//       browserHistory["Open Tabs"].push(site);
//       browserHistory["Browser Logs"].push(command);

//     } else if (action === "Close") {
//       const index = browserHistory["Open Tabs"].indexOf(site);
//       if (index > -1) {
//         browserHistory["Open Tabs"].splice(index, 1);
//         browserHistory["Recently Closed"].push(site);
//         browserHistory["Browser Logs"].push(command);
//       }

//     } else if (command === "Clear History and Cache") {
//       browserHistory["Open Tabs"] = [];
//       browserHistory["Recently Closed"] = [];
//       browserHistory["Browser Logs"] = [];
//     }
//   }

//   result +=
//     browserHistory["Browser Name"] +
//     `\nOpen Tabs: ${browserHistory["Open Tabs"].join(", ")}` +
//     `\nRecently Closed: ${browserHistory["Recently Closed"].join(", ")}` +
//     `\nBrowser Logs: ${browserHistory["Browser Logs"].join(", ")}`;

//   return result;
// }

// console.log(
//   browserHistoryManager(
//     {
//       "Browser Name": "Google Chrome",
//       "Open Tabs": ["Facebook", "YouTube", "Google Translate"],
//       "Recently Closed": ["Yahoo", "Gmail"],
//       "Browser Logs": [
//         "Open YouTube",
//         "Open Yahoo",
//         "Open Google Translate",
//         "Close Yahoo",
//         "Open Gmail",
//         "Close Gmail",
//         "Open Facebook",
//       ],
//     },
//     ["Close Facebook", "Open StackOverFlow", "Open Google"]
//   )
// );

// // 07. Sequences

// function arraysSort(inputData) {
//   let arrays = [];
//   let result = "";

//   for (const str of inputData) {
//     let arr = eval(str);
//     let sortedArr = arr.sort((a, b) => b - a);
//     if (!arrays.includes(sortedArr.join(", "))) {
//       arrays.push(sortedArr.join(", "));
//     }
//   }
//   let sortedArrays = arrays.sort((a, b) => a.length - b.length);

//   for (const el of sortedArrays) {
//     result += `[${el}]\n`;
//   }

//   return result.trim();
// }

// console.log(
//   arraysSort([
//     "[-3, -2, -1, 0, 1, 2, 3, 4]",
//     "[10, 1, -17, 0, 2, 13]",
//     "[4, -3, 3, -2, 2, -1, 1, 0]",
//   ])
// );

// // 08. Garage

// function solve(inputData) {
//   let garages = {};
//   let result = "";

//   for (const entry of inputData) {
//     let token = entry.split(" - ");
//     let garage = Number(token.shift());
//     if (!garages.hasOwnProperty(garage)) {
//       garages[garage] = [];
//     }
//     let properties = token[0].split(", ");
//     let car = {};

//     for (const property of properties) {
//       [key, value] = property.split(": ");
//       car[key] = value;
//     }
//     garages[garage].push(car);
//   }

//   let entries = Object.entries(garages)
//   for( let [key, cars] of entries) {
//     result += `Garage № ${key}\n`;
//     for (const car of cars) {
//       result += "--- ";
//       carsProperties = [];
//      for (let [prop, value] of  Object.entries(car)) {
//         carsProperties.push(`${prop} - ${value}`);
//       }
//       result += carsProperties.join(", ") + "\n";
//     }
//   }

//   return result;
// }

// console.log(
//   solve([
//     "1 - color: blue, fuel type: diesel",
//     "1 - color: red, manufacture: Audi",
//     "2 - fuel type: petrol",
//     "4 - color: dark blue, fuel type: diesel, manufacture: Fiat",
//   ])
// );

// // 09. Armies

// function createArmies(inputData) {
//   let leadersAndArmies = [];
//   let result = "";

//   for (const command of inputData) {
//     if (command.includes(" arrives")) {
//       leaderName = command.replace(" arrives", "");
//       let leader = {};
//       leader.name = leaderName;
//       leader.totalCount = 0;
//       leader.armies = [];
//       leadersAndArmies.push(leader);
//     } else if (command.includes(" + ")) {
//       let [army, count] = command.split(" + ");
//       for (const leader of leadersAndArmies) {
//         for (let i = 0; i < leader.armies.length; i++) {
//           if (leader.armies[i][0] === army) {
//             leader.armies[i][1] += Number(count);
//             leader.totalCount += Number(count);
//             break;
//           }
//         }
//       }
//     } else if (command.includes(": ")) {
//       let commandToken = command.split(": ");
//       let leaderName = commandToken.shift();
//       let [army, count] = commandToken[0].split(", ");
//       for (const leader of leadersAndArmies) {
//         if (leader.name === leaderName) {
//           leader.armies.push([army, Number(count)]);
//           leader.totalCount += Number(count);
//           break;
//         }
//       }
//     } else if (command.includes(" defeated")) {
//       let leaderName = command.replace(" defeated", "");

//       for (const leader of leadersAndArmies) {
//         if (leader.name === leaderName) {
//           let index = leadersAndArmies.indexOf(leader);
//           leadersAndArmies.splice(index, 1);
//         }
//       }
//     }
//   }
//   // console.table(leadersAndArmies);

//   for (const leader of leadersAndArmies) {
//     leader.armies.sort((a, b) => b[1] - a[1]);
//   }

//   leadersAndArmies.sort((a, b) => b.totalCount - a.totalCount);

//   for (const leader of leadersAndArmies) {
//     result += `${leader.name}: ${leader.totalCount}\n`;
//     for (const army of leader.armies) {
//       result += `>>> ${army[0]} - ${army[1]}\n`;
//     }
//   }
//   return result;
// }

// console.log(
//   createArmies([
//     "Rick Burr arrives",
//     "Findlay arrives",
//     "Rick Burr: Juard, 1500",
//     "Wexamp arrives",
//     "Findlay: Wexamp, 34540",
//     "Wexamp + 340",
//     "Wexamp: Britox, 1155",
//     "Wexamp: Juard, 43423",
//   ])
// );

// // 10. Comments

// function showComments(inputData) {
//   let users = [];
//   let articles = [];
//   let result = "";

//   for (const inputCommand of inputData) {
//     if (inputCommand.startsWith("user ")) {
//       users.push(inputCommand.replace("user ", ""));
//     } else if (inputCommand.startsWith("article ")) {
//       let articleName = inputCommand.replace("article ", "");
//       let article = {};
//       article.name = articleName;
//       article.comments = [];
//       articles.push(article);
//     } else {
//       let token = inputCommand.split(" posts on ");
//       let userName = token.shift();
//       token = token[0].split(": ");
//       let articleNme = token.shift();
//       token = token[0].split(", ");
//       let [commentTitle, commentContent] = token;
//       if (users.includes(userName)) {
//         for (const article of articles) {
//           if (article.name === articleNme) {
//             article.comments.push([userName, commentTitle, commentContent]);
//             break;
//           }
//         }
//       }
//     }
//     articles.sort((a, b) => b.comments.length - a.comments.length);

//     for (const article of articles) {
//       article.comments.sort((a, b) => a[0].localeCompare(b[0]));
//     }
//   }
//   for (const article of articles) {
//     result += `Comments on ${article.name}\n`;
//     for (const comment of article.comments) {
//       result += `--- From user ${comment[0]}: ${comment[1]} - ${comment[2]}\n`;
//     }
//   }
//   return result;
// }

// console.log(
//   showComments([
//     "user Mark",
//     "Mark posts on someArticle: NoTitle, stupidComment",
//     "article Bobby",
//     "article Steven",
//     "user Liam",
//     "user Henry",
//     "Mark posts on Bobby: Is, I do really like them",
//     "Mark posts on Steven: title, Run",
//     "someUser posts on Movies: Like",
//   ])
// );

// // 11. Book Shelf

// function sortLibrary(inputData) {
//   let library = [];
//   let result = "";

//   for (const entry of inputData) {
//     if (entry.includes(" -> ")) {
//       let [id, genre] = entry.split(" -> ");
//       let shelf = {};
//       shelf.id = id;
//       shelf.genre = genre;
//       shelf.books = [];
//       let shelfIsFree = true;
//       for (const shelf of library) {
//         if (shelf.id === id) {
//           shelfIsFree = false;
//         }
//       }
//       if (shelfIsFree) {
//         library.push(shelf);
//       }
//     } else {
//       let token = entry.split(": ");
//       let [title, newToken] = token;
//       let [author, genre] = newToken.split(", ");
//       for (const shelf of library) {
//         if (shelf.genre === genre) {
//           shelf.books.push([title, author]);
//           break;
//         }
//       }
//     }
//   }
//   library.sort((a, b) => b.books.length - a.books.length);
//   for (const shelf of library) {
//     shelf.books.sort((a, b) => a[0].localeCompare(b[0]));
//   }
//   for (const shelf of library) {
//     result += `${shelf.id} ${shelf.genre}: ${shelf.books.length}\n`;
//     for (const book of shelf.books) {
//       result += `--> ${book[0]}: ${book[1]}\n`;
//     }
//   }
//   return result;
// }

// console.log(
//   sortLibrary([
//     "1 -> mystery",
//     "2 -> sci-fi",
//     "Child of Silver: Bruce Rich, mystery",
//     "Lions and Rats: Gabe Roads, history",
//     "Effect of the Void: Shay B, romance",
//     "Losing Dreams: Gail Starr, sci-fi",
//     "Name of Earth: Jo Bell, sci-fi",
//   ])
// );

// 12. SoftUni Students

function registerStudents(inputData) {
  let courses = [];
  let result = "";

  for (const entry of inputData) {
    if (entry.includes(": ")) {
      let [courseName, capacity] = entry.split(": ");
      let courseExists = false;
      for (const course of courses) {
        if (course.name === courseName) {
          course.capacity += Number(capacity);
          courseExists = true;
          break;
        }
      }
      if (!courseExists) {
        let course = {};
        course.name = courseName;
        course.capacity = Number(capacity);
        course.students = [];
        courses.push(course);
      }
    } else {
      let token = entry.split(" ");
      let [studentName, credits] = token.shift().split("[");
      credits = Number(credits.replace("]", ""));
      let courseName = token.pop();
      let email = token[2];

      let course = null;
      let student = null;

      for (const c of courses) {
        if (c.name === courseName) {
          course = c;
          for (const s of course.students) {
            if (studentName === s.name) {
              student = s;
              break;
            }
          }
          if (course) {
            break;
          }
        }
      }
      if (course && !student) {
        if (course.capacity > course.students.length) {
          student = {};
          student.name = studentName;
          student.email = email;
          student.credits = credits;
          course.students.push(student);
        }
      }
    }
  }

  //   console.table(courses);

  courses.sort((a, b) => b.students.length - a.students.length);
  for (const course of courses) {
    course.students.sort((a, b) => b.credits - a.credits);
  }

  for (const course of courses) {
    result += `${course.name}: ${
      course.capacity - course.students.length
    } places left\n`;
    for (const student of course.students) {
      result += `--- ${student.credits}: ${student.name}, ${student.email}\n`;
    }
  }
  return result.trim();
}

console.log(
  registerStudents([
    "JavaBasics: 15",
    "user1[26] with email user1@user.com joins JavaBasics",
    "user2[36] with email user11@user.com joins JavaBasics",
    "JavaBasics: 5",
    "C#Advanced: 5",
    "user1[26] with email user1@user.com joins C#Advanced",
    "user2[36] with email user11@user.com joins C#Advanced",
    "user3[6] with email user3@user.com joins C#Advanced",
    "C#Advanced: 1",
    "JSCore: 8",
    "user23[62] with email user23@user.com joins JSCore",
  ])
);
