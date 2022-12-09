"use strict";
const playerName = prompt("Enter your name:");
let airportsList;
let playerInfo;
let opponentInfo;
let destinationIcao = "ESSA"; // change to chosen by player
let jsonData;
async function changeName() {
  try {
    const response = await fetch(
      `http://127.0.0.1:5000/name-update/${playerName}`
    );
    jsonData = await response.json();
    console.log("data", jsonData);
  } catch (error) {
    console.log(error.message);
  }
  return jsonData;
}
async function getOpponent() {
  try {
    const response = await fetch("http://127.0.0.1:5000/opponent-update");
    jsonData = await response.json();
    console.log("data", jsonData);
  } catch (error) {
    console.log(error.message);
  }
  return jsonData;
}
async function getAirports() {
  try {
    const response = await fetch("http://127.0.0.1:5000/airports-update");
    jsonData = await response.json();
    console.log("data", jsonData);
  } catch (error) {
    console.log(error.message);
  }
  return jsonData;
}
async function getPlayer() {
  try {
    const response = await fetch("http://127.0.0.1:5000/player-update");
    jsonData = await response.json();
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
    jsonData = await response.json();
    console.log("data", jsonData);
  } catch (error) {
    console.log(error.message);
  }
  return jsonData;
}

async function gameStart() {
  //first request to change name and get starting info
  playerInfo = await changeName();
  if (playerInfo) {
    document.querySelector("#player-name").innerHTML = playerInfo.name;
    document.querySelector("#player-votes").innerHTML = playerInfo.votes;
    document.querySelector("#player-co2").innerHTML = playerInfo.co2;

  }
  opponentInfo = await getOpponent();
  if (playerInfo) {
    document.querySelector("#opponent-name").innerHTML = opponentInfo.name;
    document.querySelector("#opponent-votes").innerHTML = opponentInfo.votes;
    document.querySelector("#opponent-co2").innerHTML = opponentInfo.co2;

  }
  airportsList = await getAirports();
}
function gameTurn() {
  //modifications on each press of main button
  modifyOneTurn(destinationIcao);
  playerInfo = getPlayer();
  opponentInfo = getOpponent();
  airportsList = getAirports();
}

// game
gameStart();
// gameTurn();

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
