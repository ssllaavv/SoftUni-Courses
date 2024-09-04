function solve() {

    let inputHTML = document.getElementById('input');
    let selectMenuRoHTML = document.getElementById('selectMenuTo');
    let resultHTML = document.getElementById('result') ;
    
    let optionBinary = document.createElement('option');
    optionBinary.textContent = 'Binary';
    optionBinary.value = 'binary';

    let optionHexadecimal = document.createElement('option');
    optionHexadecimal.textContent = 'Hexadecimal';
    optionHexadecimal.value = 'hexadecimal';

    selectMenuRoHTML.appendChild(optionBinary);
    selectMenuRoHTML.appendChild(optionHexadecimal);

    let convertButton = document.querySelector('#container > button')

    convertButton.addEventListener('click', convertHandler);

    function convertHandler(e) {
        let number = parseInt(inputHTML.value)

        // console.log(number)

        let result = '';
        let resultArray = []
        if (selectMenuRoHTML.value === 'binary') {
            while (number > 0) {
                resultArray.unshift(number % 2);
                number = Math.floor(number / 2);
            }
            result = resultArray.join('')
        } else if (selectMenuRoHTML.value === 'hexadecimal') {
            let hexadecimalDict = {
                10: "A", 
                11: "B", 
                12: "C", 
                13: "D", 
                14: "E", 
                15: "F",
            };
            while (number > 0) {
                let reminder = number % 16;
                if (reminder >= 10) {
                    reminder = hexadecimalDict[reminder]  
                }
                resultArray.unshift(reminder);
                number = Math.floor(number / 16);
            }
            result = resultArray.join('')
        }

        resultHTML.value = result;
    }
}