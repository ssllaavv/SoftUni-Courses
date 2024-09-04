function solve() {
    let infoHTML = document.querySelector('#info > .info') ;
    let departBtn = document.getElementById('depart');
    let arriveBtn = document.getElementById('arrive');

    const BASE_URL = 'http://localhost:3030/jsonstore/bus/schedule/';
    let busId = "depot";
    let nextStop = "";

    departBtn.addEventListener('click', depart);
    arriveBtn.addEventListener('click', arrive)


    function depart() {
        departBtn.disabled = true;
        arriveBtn.disabled = false;
        fetch(BASE_URL + busId)
            .then((response) => response.json())
            .then((result) => {
                busId = result.next;
                nextStop = result.name;
                infoHTML.textContent = `Next stop ${nextStop}`
            })
            .catch((err) => console.error(err.error))
    }

    function arrive() {
        departBtn.disabled = false;
        arriveBtn.disabled = true;

        infoHTML.textContent = `Arriving at ${nextStop}`;
        
    }

    return {
        depart,
        arrive
    };
}

let result = solve();