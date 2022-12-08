# IMPORTS
from geopy import distance
import mysql.connector
from flask import Flask, request
from flask_cors import CORS
import math
import json
import random
import requests

# CONNECTION TO DATABASE - !!! use your user and password, host can be localhost or 127.0.0.0

connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user="root",
    password="12332167",
    autocommit=True
)

# FUNCTIONS

# real weather fetcher !!!!!!!!!!!!!!!!!! add somehow to the game!!!!!!!!!!!!!!!!!!!
# def getTemperature(municipality):
#     cityName = municipality
#     request = "https://api.openweathermap.org/data/2.5/weather?q=" + \
#         cityName + \
#         "&appid={APIkey}&units=metric"  # paste your openweathermap api key where {APIkey} without brackets
#     response = requests.get(request).json()
#     return response["main"]["temp"]


def playerIdGen():  # random id generator
    import random
    x = "id"+str(random.randint(1000, 9999))  # e.g. id7362
    return x


def randomizeWeather():  # random weather condition (sun,clouds,rain)
    x = random.randint(0, 100)
    if x <= 100 and x > 66:
        weather = "sun"
    elif x <= 66 and x > 33:
        weather = "clouds"
    else:
        weather = "rain"
    return weather


def getPosition(icao):  # get position latitude and longitude from icao
    sql = "SELECT latitude_deg, longitude_deg from airport where ident ='" + icao + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    return cursor.fetchall()


def getDistance(icao):  # get distance from icao of player position to selected icao
    a = getPosition(player1.position)[0]
    b = getPosition(icao)[0]
    # print(a, b)
    return round((distance.distance(a, b).km), 0)  # distance in km rounded


def getAirports():  # get list of dictionaries with airports
    airportList = []
    icaoList = ["LOWW", "EBBR", "LBSF", "LDZA", "LKPR", "EKCH", "EETN", "EFHK", "LFPG", "EDDB", "LGAV", "LHBP", "EIDW",
                "LIRF", "EVRA", "EYVI", "ELLX", "LMML", "EHAM", "EPWA", "LPPT", "LROP", "LZIB", "LJLJ", "LEMD", "ESSA", "LCLK"]
    for i in icaoList:
        sql = "SELECT ident, latitude_deg, longitude_deg, iso_country, municipality from airport where ident ='"+i+"'"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        airport = {"icao": result[0][0], "latitude": result[0][1],
                   "longitude": result[0][2], "country": result[0][3], "city": result[0][4], "weather": randomizeWeather(), "distance": getDistance(result[0][0])}
        airportList.append(airport)
    return airportList


def modifyPlayer(player1Destination):  # modifing player data on each game loop
    print("**starting position: "+str(player1.position))

    def getDistance():
        for i in airportList:
            if i["icao"] == player1Destination:
                return (i["distance"])

    def getWeather():
        for i in airportList:
            if i["icao"] == player1Destination:
                return (i["weather"])
    distance = getDistance()
    weather = getWeather()
    print("**travelled distance: "+str(distance))
    print("**co2budget BEFORE: "+str(player1.co2))
    player1.co2 = player1.co2-distance  # subtracting distance from co2 budjet
    print("**co2budget AFTER: "+str(player1.co2))

    if weather == "sun":
        votingCoefficient = 1.25
    elif weather == "clouds":
        votingCoefficient = 1
    elif weather == "rain":
        votingCoefficient = 0.75
    else:
        votingCoefficient = 1  # voting coefficient based on weather

    if player1.co2 < 0:  # co2 coefficient to calc final - add to final calculations !!!!!!!!!!!!!!
        player1.co2Coefficient = 0.9

    player1.votes = player1.votes + \
        round((random.randint(350, 500)*votingCoefficient)
              )  # calculating votes on each step mb add co2coefficient right here? !!!!!

    player1.position = player1Destination  # changing destination to current
    print("**destination reached: "+str(player1.position))
    print("**weather in destination: "+str(weather))
    
def modifyOpponent():  # modify opponent each game loop - make more complicated with flying to different random airports!!!!!
    player2.votes += 425
    x = (random.randint(750, 1350))
    player2.co2 = player2.co2-x


def getPlayer():  # combine player info to send to fromtend
    response = {"name": player1.name, "id": player1.id, "co2": player1.co2,
                "position": player1.position, "c02coefficient": player1.co2Coefficient, "votes": player1.votes}
    return response


def getOpponent():  # compbine opponent info to send to forntend
    response = {"name": player2.name, "id": player2.id, "co2": player2.co2,
                "position": player2.position, "c02coefficient": player2.co2Coefficient, "votes": player2.votes}
    return response


# Game

class Player:
    def __init__(self, name, co2, position, co2Coefficient=1, votes=0) -> None:
        self.name = name
        self.id = id
        self.co2 = co2
        self.position = position
        self.co2Coefficient = co2Coefficient
        self.votes = votes
        self.id = playerIdGen()


# this name is showed on screen before player have entered name
getName = "Enter your name"
player1 = Player(getName, 15000, "EBBR")
player2 = Player("Opponent", 15000, "EBBR")

airportList = getAirports()

# FLASK -------------------------------------->

app = Flask(__name__)


@ app.route('/name-update/<name>')  # for changing name
def nameUpdate(name):
    player1.name = name
    a = getPlayer()
    b = getOpponent()
    c = airportList
    print(player1.position)
    response = "'"+str(a)+", " + str(b)+", " + str(c)+"'"
    return response


# each game loop updating based on player selected destination
@ app.route('/info-update/<player1Destination>')
def infoUpdate(player1Destination):
    modifyPlayer(player1Destination)
    modifyOpponent()
    a = getPlayer()  # player info
    b = getOpponent()  # opponent info
    c = airportList  # airports data
    response = "'"+str(a)+", " + str(b)+", " + str(c)+"'"
    return response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)

#  <-------------------------------------- FLASK
