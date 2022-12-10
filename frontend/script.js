'use strict';
import Map from "./service/integration.js";

const brusselCoord = [50.901401519800004,
                      4.48443984985]
let map = null;
let opponent = null;

document.addEventListener("selectCity", function(e) {
    let airport = e.detail;
    document.getElementById('airport-name').innerHTML = airport.city;
    document.getElementById('airport-conditions').innerHTML = airport.weather;
    document.getElementById('next-destination-distance').innerHTML = airport.distance;
});


const apiUrl ='http://127.0.0.1:5000/';
const startLoc = 'EBBR';
const countries_visited = [];
let days_until_election = 7;

// icons

const blueIcon = L.divIcon({className: 'blue-icon'});
const greenIcon = L.divIcon({className: 'green-icon'});

// form for player name
document.querySelector('#player-form').addEventListener('submit', function (evt){
   evt.preventDefault();
   const playerName = document.querySelector('#player-input').value;
   document.getElementById("player-name").innerHTML=playerName;
   document.querySelector('#player-modal').classList.add('hide');
   gameSetup(`${apiUrl}newgame?player=${playerName}&loc=${startLoc}`);
});


// function to show weather at selected airport
function showWeather() {
    document.querySelector('airport-name').innerHTML = `Weather at ${airport.name};`
    document.querySelector('airport-icon').src = airport.weather.icon;
    document.querySelector('airport-conditions').innerHTML = getWeather();
}

// function to check if game is over

function checkGameOver () {
    for (let i=7; 0<i<7; i--) {
        if (days_until_election = 0) {
        alert(`Game Over.${countries_visited.length} goals reached.`);
        return false;
    }}

    return true;
}

// function to set up game
// this is the main function that creates the game and calls the other functions

async function gameSetUp() {
    try {
        const response = await fetch('http://127.0.0.1:5000/info-update/EHAM');
        const data = await response.json();
        let airports = data.airport;
        opponent = data.opponent;
        let votes = data.opponent.votes;
        console.log(votes)
        map = new Map(airports, brusselCoord);

    } catch (error){
        console.log(error.message);
    } finally {
        console.log('Ends.');
    }
}



async function confirmFlight (destination) {
    try {
        let url = 'http://127.0.0.1:5000/info-update/' + destination;
;
        const response = await fetch(url);
        const data = await response.json();
        let airports = data.airport;
        let opponent = data.opponent;
        let opponent_co2 = opponent.co2;
        let opponent_votes = opponent.votes;
        let player = data.player;
        let player_co2 = player.co2;
        let player_votes = player.votes;
        map.refreshAirportList(airports);
        document.getElementById('player-co2').innerHTML = player_co2;
        document.getElementById('player-votes').innerHTML = player_votes;
        document.getElementById('opponent-co2').innerHTML = opponent_co2;
        document.getElementById('opponent-votes').innerHTML = opponent_votes
        checkGameOver()
    } catch (e) {

    }
}

gameSetUp()


/*
async function gameSetup(url) {
    try {
        document.querySelector('.days-left').classList.add('hide');
        airportMarkers.clearLayers();
        const nameUpdate = await nameUpdate(url);
        updateStatus(nameUpdate.player1.name);
        if(!checkGameOver(nameUpdate.status.days_until_election)) return;

        for (let airport of infoUpdate.airports) {
            const marker = L.marker([airport.latitude, airport.longitude]).addTo(map);
            airportMarkers.addLayer(marker);
            if (airport in airports) {
                map.flyTo([airport.latitude, airport.longitude], 10);
                showWeather(airport);
                marker.bindPopup(`You are here:<b>${airport.name}</b>`);
                marker.openPopup();
                marker.setIcon(greenIcon);
            } else {
                marker.setIcon(blueIcon);
                const popupContent = document.createElement('div');
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


 */




/*
// event listener to hide goal splash
document.querySelector('.goal').addEventListener('click', function (evt){
    evt.currentTarget.classList.add('hide');
})

 */