// // 1.	Sum First and Last Array Elements

// function solve(numArray) {
//     let first =  numArray[0]
//     let last = numArray[numArray.length -1]
//     return first + last
// }

// console.log(solve([10, 17, 22, 33]))

// 2.	Reverse an Array of Numbers

// function solve(count, numArray) {
//   return numArray
//     .slice(0, count)
//     .reverse()
//     .join(" ");
// }

// console.log(solve(3, [10, 20, 30, 40, 50]));

// 3. Even and Odd Subtraction

// function solve(numArray) {
//   let evens = 0;
//   let odds = 0;
//   for (const el of numArray) {
//     if (el % 2 === 0) {
//       evens += el;
//     } else {
//       odds += el;
//     }
//   }

//   return evens - odds;
// }

// console.log(solve([1, 2, 3, 4, 5, 6]));

// // 4. Substring

// function solve(text, start, count) {
//   let result = String(text.slice(start, count + 1));
//   console.log(result)
// }

// solve('Some sentence, Just for test. Ok !!!', 4, 24);

// // 5. Censored Words

// function solve(sentence, word) {
//   let result = sentence;

//   while (result.includes(word)) {
//     result = result.replace(word, "*".repeat(word.length));
//   }

//   return result;
// }

// console.log(solve("A small sentence with some small words", "small"));


// 6.	Count String Occurrences



function solve(sentence, word) {

    let counter = 0;
    sentenceArray = sentence.split(" ")

    for (w of sentenceArray) {
        if (w === word) {
            counter += 1 
        }
    }
    return counter
}


console.log(solve(
    'This is a word and it also is a sentence',
    'is'
    

))









