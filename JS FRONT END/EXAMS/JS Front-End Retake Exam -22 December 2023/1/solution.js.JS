function solve(inputData) {
  let message = inputData.shift();

  for (const commandInput of inputData) {
    let commandToken = commandInput.split("?");
    let command = commandToken.shift();

    if (command === "TakeEven") {
      let result = "";
      for (let i = 0; i < message.length; i += 2) {
        result += message[i];
      }
      message = result;
      console.log(message);
    } else if (command === "ChangeAll") {
      let [substring, replacement] = commandToken;
      while (message.includes(substring)) {
        message = message.replace(substring, replacement);
      }
      console.log(message);
    } else if (command === "Reverse") {
      let substring = commandToken[0];
      let reversedSubstring = substring.split("").reverse().join("");

      if (message.includes(substring)) {
        message = message.replace(substring, "");
        message += reversedSubstring;
        console.log(message);
      } else {
        console.log("error");
      }
    } else if (command === "Buy") {
      console.log(`The cryptocurrency is: ${message}`);
      break;
    }
  }
}

solve([
  "PZDfA2PkAsakhnefZ7aZ",
  "TakeEven",
  "TakeEven",
  "TakeEven",
  "ChangeAll?Z?X",
  "ChangeAll?A?R",
  "Reverse?PRX",
  "Buy",
]);
