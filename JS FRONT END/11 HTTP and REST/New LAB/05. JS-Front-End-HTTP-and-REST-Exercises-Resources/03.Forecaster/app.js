function attachEvents() {
    let submitBtn = document.getElementById('submit');
    
    submitBtn.addEventListener('click', submitHandler);




    function submitHandler(e) {

        let forecastsDivHTML = document.querySelector('.forecasts');
        let forecastInfoDivHTML= document.querySelector('.forecast-info');
    
        if (forecastsDivHTML) {
            forecastsDivHTML.parentElement.removeChild(forecastsDivHTML);
        }
    
        if (forecastInfoDivHTML) {
            forecastInfoDivHTML.parentElement.removeChild(forecastInfoDivHTML);
        }
    


        let forecastDivHTML = document.getElementById('forecast');
        forecastDivHTML.style.display = 'block';
        let currentDivHTML = document.getElementById('current');
        let upcomingDivHTML = document.getElementById('upcoming');
    
        let locationInput = document.getElementById('location').value;
    
        const BASE_URL = 'http://localhost:3030/jsonstore/forecaster/'
        let locationCode = '';
    
        // console.log(locationInput);


        let symbols = {
            "Sunny" : 	    `&#x2600;`,
            "Partly sunny": `&#x26C5;`,
            "Overcast":		`&#x2601;`,
            "Rain":			`&#x2614;`,
            "Degrees":		`&#176;`,  

        }


        fetch(BASE_URL + 'locations/')
            .then((response) => response.json())
            .then((res => {
                for (const location of res) {
                    if (location.name === locationInput) {
                          locationCode = location.code; 
                          break;
                    }
                }

                // console.log(locationCode)


                fetch(BASE_URL + 'today/' + locationCode)
                    .then((response) => response.json())
                    .then((result) => {

                        // console.log(result)

                        let locationName = result.name;
                        let forecastObject = result.forecast;

                        // console.log(forecastObject);

                        let low = forecastObject.low;
                        let high = forecastObject.high;
                        let condition = forecastObject.condition;

                        let divForecastTodayHTML= document.createElement('div');
                        divForecastTodayHTML.classList.add('forecasts')
                        currentDivHTML.appendChild(divForecastTodayHTML)

                        let  conditionSymbolHTML = document.createElement('span');
                        conditionSymbolHTML.classList.add("condition");
                        conditionSymbolHTML.classList.add("symbol");
                        divForecastTodayHTML.appendChild(conditionSymbolHTML);
                        conditionSymbolHTML.innerHTML = symbols[condition];

                        let conditionHTML = document.createElement('span');
                        conditionHTML.classList.add('condition');
                        divForecastTodayHTML.appendChild(conditionHTML);

                        let forecastDataLocationHTML = document.createElement('span');
                        forecastDataLocationHTML.classList.add('forecast-data');
                        conditionHTML.appendChild(forecastDataLocationHTML);
                        forecastDataLocationHTML.textContent = locationName;

                        let forecastDataTemperaturesHTML = document.createElement('span');
                        forecastDataTemperaturesHTML.classList.add('forecast-data');
                        conditionHTML.appendChild(forecastDataTemperaturesHTML);
                        forecastDataTemperaturesHTML.innerHTML = `${low}&#176;/${high}&#176;`;


                        let forecastDataConditionHTML = document.createElement('span');
                        forecastDataConditionHTML.classList.add('forecast-data');
                        conditionHTML.appendChild(forecastDataConditionHTML);
                        forecastDataConditionHTML.textContent = condition;

                    })
                    .catch((error) => console.error(error.error));
                

                fetch(BASE_URL + 'upcoming/' + locationCode)
                    .then((response) => response.json())
                    .then((result) => {

                        console.log(result)

                        let forecastInfoHTML = document.createElement('div')
                        forecastInfoHTML.classList.add('forecast-info')
                        upcomingDivHTML.appendChild(forecastInfoHTML)
                    
                        let forecastsObjects = result.forecast
                        for (const forecast of forecastsObjects) {

                            console.log(forecast)

                            let low = forecast.low;
                            let high = forecast.high;
                            let condition = forecast.condition;


                            let upcomingSpanHTML = document.createElement('span');
                            upcomingSpanHTML.classList.add('upcoming')
                            forecastInfoHTML.appendChild(upcomingSpanHTML)

                            let symbolHTML = document.createElement('span');
                            symbolHTML.classList.add('symbol');
                            symbolHTML.innerHTML = symbols[forecast.condition]
                            upcomingSpanHTML.appendChild(symbolHTML);

                            let temperaturesHTML = document.createElement('span');
                            temperaturesHTML.classList.add('forecast-data');
                            temperaturesHTML.innerHTML = `${low}&#176;/${high}&#176;`
                            upcomingSpanHTML.appendChild(temperaturesHTML);


                            let conditionHTML = document.createElement('span');
                            conditionHTML.classList.add('forecast-data');
                            conditionHTML.innerHTML = condition;
                            upcomingSpanHTML.appendChild(conditionHTML);

                        }
                    })

                    .catch((error) => console.error(error.error))
                
            }))
            .catch((error) => console.error(error.error))
    }

}

attachEvents();