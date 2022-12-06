'use strict';
/* 1. show map using Leaflet library. (L comes from the Leaflet library) */
const map = L.map('map', {tap: false});
L.tileLayer('https://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
  maxZoom: 20,
  subdomains: ['mt0', 'mt1', 'mt2', 'mt3'],
}).addTo(map);
map.setView([60, 24], 7);

// global variables

const apiUrl ='http://127.0.0.1:5000/';
const startLoc = 'EBBR';
const countries_visited = [];
const airportMarkers = L.featureGroup().addTo(map);

// icons

const blueIcon = L.divIcon({className: 'blue-icon'});
const greenIcon = L.divIcon({className: 'green-icon'});


// form for player name
document.querySelector('#player-form').addEventListener('submit', function (evt){
    evt.preventDefault();
    const playerName = document.querySelector('#player-input').value;
    document.querySelector('#player-modal').classList.add('hide');
    gameSetup(`${apiUrl}newgame?player=${playerName}&loc=${startLoc}`);
});


// function to update game status

function updateStatus(status) {
    document.querySelector('#player-name').innerHTML = `Player: ${status.name}`;
    document.querySelector('#consumed').innerHTML = status.co2.consumed;
    document.querySelector('#number_of_place_visited').innerHTML = status.countries_visited;

}

// function to show weather at selected airport
function showWeather() {
    document.querySelector('airport-name').innerHTML = `Weather at ${airport.name};`
    document.querySelector('airport-temp').innerHTML = `${airport.tempt}°C;`
    document.querySelector('airport-icon').src = airport.weather.icon;
    document.querySelector('airport-conditions').innerHTML = airport_weather.description;
}

// function to check if game is over

function checkGameOver (visited_countries) {
    if (visited_countries >=4) {
        alert(`Game Over.${countries_visited.length} goals reached.`);
        return false;
    }
    return true;
}

// function to set up game
// this is the main function that creates the game and calls the other functions
async function gameSetup(url) {
    try {
        document.querySelector('.goal').classList.add('hide');
        airportMarkers.clearLayers();
        const gameData = await getData(url);
        console.log(gameData);
        updateStatus(gameData.status);
        if(!checkGameOver(gameData.status.countries_visited)) return;

        for (let airport of gameData.location) {
            const marker = L.marker([airport.latitude, airport.longitude]).addTo(map);
            airportMarkers.addLayer(marker);
            if (airport.active) {
                map.flyTo([airport.latitude, airport.longitude], 10);
                showWeather(airport);
                marker.bindPopup(`You are here:<b>${airport.name}</b>`);
                marker.openPopup();
                marker.setIcon(greenIcon);
            } else {
                marker.setIcon(blueIcon);
                const popupContent = document.createElement('div');
                const h4 = document.createElement('h4');
                h4.innerHTML = airport.name;
                popupContent.append(h4);
                const goButton = document.createElement('button');
                goButton.classList.add('button');
                goButton.innerHTML = 'Fly here';
                popupContent.append(goButton);
                const p = document.createElement('P');
                p.innerHTML = `Distance ${airport.distance} km`;
                popupContent.append(p);
                marker.bindPopup(popupContent);
                goButton.addEventListener('click', function () {
//                    gameSetup(`${apiUrl}?game=`);
                })
            }
        }

    } catch (error) {
        console.log(error);
    }
}

// event listener to hide goal splash
document.querySelector('.goal').addEventListener('click', function (evt){
    evt.currentTarget.classList.add('hide');
})