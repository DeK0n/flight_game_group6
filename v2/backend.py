# IMPORTS
from geopy import distance
import mysql.connector
from flask import Flask, request
from flask_cors import CORS
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

# real weather


def getTemperature():
    request = "https://api.openweathermap.org/data/2.5/weather?q=Brussels&appid=a90e3aac59a9af0d4c05758d10e19343&units=metric"
    response = requests.get(request).json()
    x = str(response["weather"][0]["description"]) + \
        " and " + str(response["main"]["temp"])+" C"
    return x


def getCurrencyRate():
    request = "https://www.freeforexapi.com/api/live?pairs=EURUSD"
    response = requests.get(request).json()
    x = response["rates"]["EURUSD"]["rate"]
    return x


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
    player1.co2 = player1.co2-distance  # subtracting distance from co2 budjet
    if weather == "sun":
        votingCoefficient = 1.25
    elif weather == "clouds":
        votingCoefficient = 1
    elif weather == "rain":
        votingCoefficient = 0.75
    else:
        votingCoefficient = 1  # voting coefficient based on weather

    if player1.co2 < 0:
        player1.co2Coefficient = 0.9

    player1.votes = player1.votes + \
        round((random.randint(350, 500)*votingCoefficient*player1.co2Coefficient)
              )

    player1.position = player1Destination  # changing destination to current

    def changeCity():
        for i in airportList:
            if i["icao"] == player1Destination:
                return (i["city"])
    player1.positionCity = changeCity()


def modifyOpponent():  # modify opponent each game loop - make more complicated with flying to different random airports!!!!!
    player2.votes += 425
    x = (random.randint(750, 1350))
    player2.co2 = player2.co2-x


def getPlayer():  # combine player info to send to fromtend
    response = {"name": player1.name, "id": player1.id, "co2": player1.co2,
                "position": player1.position, "positionCity": player1.positionCity, "c02coefficient": player1.co2Coefficient, "votes": player1.votes, "apiInfo": player1.apiInfo}
    return response


def getOpponent():  # compbine opponent info to send to forntend
    response = {"name": player2.name, "id": player2.id, "co2": player2.co2,
                "position": player2.position, "positionCity": player2.positionCity, "c02coefficient": player2.co2Coefficient, "votes": player2.votes, "apiInfo": player2.apiInfo}
    return response


# Game

class Player:
    def __init__(self, name, co2, position, positionCity, co2Coefficient=1, votes=0, apiInfo="") -> None:
        self.name = name
        self.id = id
        self.co2 = co2
        self.position = position
        self.co2Coefficient = co2Coefficient
        self.votes = votes
        self.positionCity = positionCity
        self.apiInfo = apiInfo
        self.id = playerIdGen()


getName = "Enter your name"
player1 = Player(getName, 10000, "EBBR", "Brussels")
player2 = Player("Opponent", 10000, "EBBR", "Brussels")
airportList = getAirports()
realWeather = getTemperature()
realCurrency = getCurrencyRate()
player1.apiInfo = "Real weather Brusseles: "+str(realWeather)
player2.apiInfo = "EUR to USD rate:"+ str(realCurrency)


# FLASK -------------------------------------->

app = Flask(__name__)
CORS(app)


@ app.route('/name-update/<name>')  # for changing name
def nameUpdate(name):
    player1.name = name
    response = getPlayer()
    return response


@ app.route('/player-update')
def playerUpdate():
    response = getPlayer()
    return response


@ app.route('/modify-players/<icao>')
def modifyUpdate(icao):
    modifyPlayer(icao)
    modifyOpponent()
    turncount = '{"+turn":"1"}'
    return turncount


@ app.route('/opponent-update')
def opponentUpdate():
    response = getOpponent()
    return response


@ app.route('/airports-update')
def airportsUpdate():
    response = getAirports()
    return response


@ app.route('/test')
def testing():
    response = '{"teststr":"OK", "testint":999, "testbool":true}'
    print(response)
    return response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)

#  <-------------------------------------- FLASK
