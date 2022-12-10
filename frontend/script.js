'use strict';
import Map from "./service/integration.js";

const brusselCoord = [50.901401519800004,
                      4.48443984985]
let map = null;
let opponent = null;
let selectedNextDestination = null;
let playerCO2Budget = 1000000;
let opponentCO2Budget = 1000000;
let playerVotes = 0;
let opponentVotes = 0;
let playerName = ''

document.addEventListener("selectCity", function(e) {
    selectedNextDestination = e.detail;
    document.getElementById('airport-name').innerHTML = selectedNextDestination.city;
    document.getElementById('airport-conditions').innerHTML = selectedNextDestination.weather;
    document.getElementById('next-destination-distance').innerHTML = selectedNextDestination.distance;
});

let days_until_election = 7;


// form for player name
document.querySelector('#player-form').addEventListener('submit', function (evt){
   evt.preventDefault();
   playerName = document.querySelector('#player-input').value;
   document.getElementById("player-name").innerHTML=playerName;
   document.querySelector('#player-modal').classList.add('hide');
});


// function to show weather at selected airport
function showWeather() {
    document.querySelector('airport-name').innerHTML = `Weather at ${airport.name};`
    document.querySelector('airport-icon').src = airport.weather.icon;
    document.querySelector('airport-conditions').innerHTML = getWeather();
}

// function to check if game is over

function checkGameOver () {
    let daysLeft = document.getElementById('days-left');
    daysLeft.innerHTML = days_until_election.toString() + ' days';
    if(days_until_election === 0) {
        confirmButton = document.getElementById('confirm-flight');
        confirmButton.innerHTML = 'Play again';
        alert(`Game ended. The winner is ${playerVotes > opponentVotes ? 'the player ' + playerName : 'the AI.'}` )
    }
}

// function to set up game
// this is the main function that creates the game and calls the other functions

async function resetGame() {
    location.reload();
}
async function gameSetUp() {
    try {
        const response = await fetch('http://127.0.0.1:5000/info-update/EBBR');
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

let confirmButton = document.getElementById('confirm-flight')
confirmButton.addEventListener('click', await confirmFlight, false)


async function confirmFlight (e) {
    e.preventDefault();
    if(days_until_election > 0) {
        days_until_election = days_until_election - 1;
        try {
            let url = 'http://127.0.0.1:5000/info-update/' + selectedNextDestination.icao;
            const response = await fetch(url);
            const data = await response.json();
            console.log(data)
            let airports = data.airport;
            map.flyTo(selectedNextDestination, airports);
            let opponent = data.opponent;
            let opponent_co2 = opponent.co2;
            opponentVotes += opponent.votes;
            let player = data.player;
            let player_co2 = player.co2;
            playerVotes += player.votes;
            playerCO2Budget += player_co2
            opponentCO2Budget += opponent_co2
            document.getElementById('player-co2').innerHTML = playerCO2Budget;
            document.getElementById('player-votes').innerHTML = playerVotes + ' votes';
            document.getElementById('opponent-co2').innerHTML = opponentCO2Budget;
            document.getElementById('opponent-votes').innerHTML = opponentVotes + ' votes'
            checkGameOver()
        } catch (e) {

        }
    } else {
        resetGame()
    }
}

gameSetUp()
