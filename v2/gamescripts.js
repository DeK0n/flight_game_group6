"use strict";
const playerName = prompt("Enter your name:");
let airportsList;
let playerInfo;
let opponentInfo;
let destinationIcao = "EBBR"; // change to be chosen by player
let jsonData;
const markerList = [];
let marker;
let daysCounter = 7;
// map---->
var map = L.map("map", {
  center: [52, 12],
  zoom: 4,
  zoomControl: false,
  dragging: false,
});

L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
  maxZoom: 4,
  minZoom: 4,

  // attribution:
  //   '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
}).addTo(map);

function initializeMarks() {
  console.log(airportsList);
  for (let i = 0; i < airportsList.length; i++) {
    marker = L.marker([
      +airportsList[i].latitude,
      +airportsList[i].longitude,
    ]).addTo(map);
    // marker.bindPopup(`${airportsList[i].city}`); //.openOn(map)
    marker.on("click", (e) => {
      destinationIcao = airportsList[i].icao;
      destinationText.innerText = airportsList[i].city;
      document.getElementById("weather-destination").innerText =
        airportsList[i].weather;
    });
    markerList.push(marker);
  }
}
// <----map

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
    document.querySelector(
      "#player-name"
    ).innerHTML = `${playerInfo.name}'s votes`;
    document.querySelector("#player-votes").innerHTML = playerInfo.votes;
    document.querySelector("#player-co2").innerHTML = playerInfo.co2;
    document.getElementById("player-position").innerHTML =
      playerInfo.positionCity;
  }
  opponentInfo = await getOpponent();
  if (opponentInfo) {
    document.querySelector(
      "#opponent-name"
    ).innerHTML = `${opponentInfo.name}'s votes`;
    document.querySelector("#opponent-votes").innerHTML = opponentInfo.votes;
  }
  airportsList = await getAirports();
  if (airportsList) {
    initializeMarks();
    console.log(marker);
  }
   document.getElementById("main-container").classList.remove("opacity-zero");
}
async function gameTurn() {
  //modifications on each press of main button

  await modifyOneTurn(destinationIcao);
  if (modifyOneTurn) {
    playerInfo = await getPlayer();
    if (playerInfo) {
      document.querySelector(
        "#player-name"
      ).innerHTML = `${playerInfo.name}'s votes`;
      document.querySelector("#player-votes").innerHTML = playerInfo.votes;
      document.querySelector("#player-co2").innerHTML = playerInfo.co2;
      document.getElementById("player-position").innerHTML =
        playerInfo.positionCity;
    }
    opponentInfo = await getOpponent();
    if (opponentInfo) {
      document.querySelector(
        "#opponent-name"
      ).innerHTML = `${opponentInfo.name}'s votes`;
      document.querySelector("#opponent-votes").innerHTML = opponentInfo.votes;
    }
    airportsList = await getAirports();
  }
  destinationText.innerText = "- - -";
  document.getElementById("weather-destination").innerText = "- - -";
  daysCounter = daysCounter - 1;
  document.getElementById("days-counter").innerHTML = `${daysCounter} days`;

  if (daysCounter == 1) {
    document.getElementById("game-button").innerHTML =
      "Confirm last flight and go to elections";
    document.getElementById("days-counter").innerHTML = `${daysCounter} day`;
  }
  if (daysCounter == 0) {
    document.getElementById("final-board").classList.remove("hidden");
  }
}

// game
gameStart();
const destinationText = document.getElementById("player-destination");
destinationText.innerText = "- - -";
document.getElementById("days-counter").innerHTML = `${daysCounter} days`;
