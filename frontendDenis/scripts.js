"use strict";
const playerName = prompt("Enter your name:");
let airportsList;
let playerInfo;
let opponentInfo;
let destination = "ESSA"; // change to chosen by player
async function changeName() {
  try {
    const response = await fetch(
      `http://127.0.0.1:5000/name-update/${playerName}`
    );
    const jsonData = await response.json();
    console.log("data", jsonData);
  } catch (error) {
    console.log(error.message);
  }
  return jsonData;
}
async function getOpponent() {
  try {
    const response = await fetch(
      'http://127.0.0.1:5000/opponent-update'
    );
    const jsonData = await response.json();
    console.log("data", jsonData);
  } catch (error) {
    console.log(error.message);
  }
  return jsonData;
}
async function getAirports() {
  try {
    const response = await fetch(
      'http://127.0.0.1:5000/airports-update'
    );
    const jsonData = await response.json();
    console.log("data", jsonData);
  } catch (error) {
    console.log(error.message);
  }
  return jsonData;
}
async function getPlayer() {
  try {
    const response = await fetch(
      'http://127.0.0.1:5000/player-update'
    );
    const jsonData = await response.json();
    console.log("data", jsonData);
  } catch (error) {
    console.log(error.message);
  }
  return jsonData;
}
async function modifyOneTurn(destinationIcao) {
  try {
    const response = await fetch(
      `http://127.0.0.1:5000/modify-players/${destinationIcao}`
    );
    const jsonData = await response.json();
    console.log("data", jsonData);
  } catch (error) {
    console.log(error.message);
  }
  return jsonData;
}

function gameStart() {
  //first request to change name and get starting info
  playerInfo = changeName();
  opponentInfo = getOpponent();
  airportsList = getAirports();
}
function gameTurn(){
  //modifications on each press of main button
  modifyOneTurn(destination)
  playerInfo = getPlayer();
  opponentInfo = getOpponent();
  airportsList = getAirports();
}

gameStart();
console.log(playerInfo)
gameTurn();
console.log(playerInfo)
// async function changeName() {
//   console.log("asynchronous download begins");
//   try {
//     const response = await fetch(`http://127.0.0.1:5000/name-update/${playerName}`);
//     const jsonData = await response.json();
//     console.log("data", jsonData);
//   } catch (error) {
//     console.log(error.message);
//   } finally {
//     console.log("asynchronous load complete");
//   }
//   return jsonData
// }
