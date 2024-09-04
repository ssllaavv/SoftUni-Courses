function decode(inputData) {
  let message = inputData.shift();

  for (const commandToken of inputData) {
    if (commandToken === "RemoveEven") {
      let result = "";
      for (let i = 0; i < message.length; i += 2) {
        result += message[i];
      }
      message = result;
      console.log(message);
    } else if (commandToken.includes("TakePart")) {
      let commandTokenList = commandToken.split("!");

      let startIndex = Number(commandTokenList[1]);
      let endIndex = Number(commandTokenList[2]);
      message = message.slice(startIndex, endIndex);
      console.log(message);
    } else if (commandToken.includes("Reverse")) {
      let subString = commandToken.split("!")[1];
      if (message.includes(subString)) {
        message = message.replace(subString, "");
        message += subString.split("").reverse().join("");
        console.log(message);
      } else {
        console.log("Error");
      }
    } else if (commandToken === "End") {
      console.log(`The concealed spell is: ${message}`);
      break;
    }
  }
}

decode([
  "asAsl2adkda2mdaczsa",
  "RemoveEven",
  "TakePart!1!9",
  "Reverse!maz",
  "End",
]);
