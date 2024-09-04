function getInfo() {
    let stopId = document.getElementById('stopId').value;
    let stopNameHTML  = document.getElementById('stopName');
    let busesHTML = document.getElementById('buses');
    busesHTML.innerHTML = '';
    stopNameHTML.textContent = '';

    fetch(`http://localhost:3030/jsonstore/bus/businfo/${stopId} `)
        .then((response => response.json()))
        .then((stop) => {
            let stopName = stop.name;
            stopNameHTML = stopName

            for (const [busId, time] of Object.entries(stop.buses)) {
                let newLi = document.createElement('li');
                newLi.textContent = `Bus ${busId} arrives in ${time} minutes`;
                busesHTML.appendChild(newLi)
            }           
        })
        .catch((error) => {
            stopNameHTML.textContent = "Error";
        })
}