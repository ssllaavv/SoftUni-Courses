function solve(inputData) {
  let n = Number(inputData.shift());
  let baristas = [];

  function findBaristaByName(baristaName) {
    let barista = null;
    for (const b of baristas) {
      if (b.name === baristaName) {
        barista = b;
        break;
      }
    }
    return barista;
  }

  for (let i = 0; i < n; i++) {
    let baristaToken = inputData.shift().split(" ");
    let name = baristaToken[0];
    let shift = baristaToken[1];
    let drinks = baristaToken[2].split(",");

    let barista = { name, shift, drinks };
    baristas.push(barista);
  }

  for (const commandInput of inputData) {
    let commandToken = commandInput.split(" / ");
    let command = commandToken.shift();
    if (command === "Prepare") {
      let [name, shift, drink] = commandToken;
      let barista = findBaristaByName(name);
      if (
        barista &&
        barista.shift === shift &&
        barista.drinks.includes(drink)
      ) {
        console.log(`${barista.name} has prepared a ${drink} for you!`);
      } else {
        console.log(`${barista.name} is not available to prepare a ${drink}.`);
      }
    } else if (command === "Change Shift") {
      let [name, shift] = commandToken;
      let barista = findBaristaByName(name);
      barista.shift = shift;
      console.log(`${name} has updated his shift to: ${shift}`);
    } else if (command === "Learn") {
      let [name, drink] = commandToken;
      let barista = findBaristaByName(name);

      if (barista.drinks.includes(drink)) {
        console.log(`${name} knows how to make ${drink}.`);
      } else {
        barista.drinks.push(drink);
        console.log(`${name} has learned a new coffee type: ${drink}.`);
      }
    } else if (command === "Closed") {
      for (const b of baristas) {
        console.log(
          `Barista: ${b.name}, Shift: ${b.shift}, Drinks: ${
            (b.drinks.join(", "))
          }`
        );
      }
      break;
    }
  }
}

solve(

    ['4',
'Alice day Espresso,Cappuccino',
'Bob night Latte,Mocha',
'Carol day Americano,Mocha',
'David night Espresso',
'Prepare / Alice / day / Espresso',
'Change Shift / Bob / day',
'Learn / Carol / Latte',
'Prepare / Bob / night / Latte',
'Learn / David / Cappuccino',
'Prepare / Carol / day / Cappuccino',
'Change Shift / Alice / night',
 'Learn / Bob / Mocha',
'Prepare / David / night / Espresso',
'Closed']

);
