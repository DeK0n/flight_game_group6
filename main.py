# IMPORTS
from modules import menu, functions
from geopy import distance
import mysql.connector
from flask import Flask, request
from flask_cors import CORS         # this is needed if you want JavaScript access
import math
import json
import random

# CONNECTION TO DATABASE - !!! use your user and password, host can be localhost or 127.0.0.0

connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',  # correct database - add table with final scores.
    user="root",
    password="12332167",
    autocommit=True
)


# VARIABLES

playerId = functions.playerIdGen()  # applying unique id for player from generator
playerName = " "
playerCredits = 10000  # starting balance of CO2
playerVisited = 1
# Set of countries codes to prevent double counting, correlating with starting position
playerVisitedSet = {"BE"}
playerPosition = "EBBR"  # Starting position
playerGoal = 5  # countries to visit ! change

weatherPenalty = 200  # in credits cr
weatherCheck = 50  # in credits cr


# FLASK ->

app = Flask(__name__)


@app.route('/airport/<icao>')  # check airport by ICAO
def airport_check(icao):
    sql = "SELECT name, municipality from airport where ident ='" + icao + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    response1 = cursor.fetchall()
    for i in response1:
        name = i[0]
        location = i[1]
    response = '{"ICAO":"'+icao+'", "Name":"' + \
        name+'", "Location":"'+location+'"}'
    return response


@app.route('/get_info')  # info (information about available destinations)
def getInfo():
    # currently large airports in Europe
    sql = "SELECT ident,municipality,iso_country from airport where continent ='EU' and type = 'large_airport' "
    cursor = connection.cursor()
    cursor.execute(sql)
    response = cursor.fetchall()
    #response = sql.dumps(cursor.fetchall())
    return response


# status (printing information about current balance, position,visited countries)
@app.route('/get_status')
def getStatus():
    response = '{"co2":"'+str(playerCredits)+'", ""visitedNumber:"' + str(playerVisited)+'", "visitedList":"' + \
        str(playerVisitedSet)+'", "position":"' + \
        str(playerPosition)+'"}'  # modify format to json
    return response


@app.route('/get_position/<ICAO>')  # position (select position from database)
def getPosition(icao):
    sql = "SELECT latitude_deg, longitude_deg from airport where ident ='" + icao + "'"
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    response = cursor.fetchall()
    return response


@app.route('/get_countrycode/<ICAO>')  # country code (select from airport database)
def getCountryCode(icao):
    sql = "SELECT iso_country from airport where ident ='" + icao + "'"
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    country = cursor.fetchall()
    for y in country:
        countrycode = (y[0])
        return countrycode


@app.route('/get_distance/<icao1>%<icao2>') # distance (calculating distance between points)
def getDistance(icao1, icao2):
    a = getPosition(icao1)[0]
    b = getPosition(icao2)[0]
    response = round((distance.distance(a, b).km), 0)  # distance in km rounded
    return response


@app.route('/random') # random function set to 80%
def randomGenerator80():
    import random
    x = random.randint(0, 100)
    if x <= 80:
        response = "True"  # in string form, change to needed form
    else:
        response = "False"
    return response


# flask finish statement, all requests are above
if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
#  <- FLASK

# FUNCTIONS FROM old version - some still in use

# info (information about available destinations)


def getInfo():
    sql = "SELECT ident,municipality,iso_country from airport where continent ='EU' and type = 'large_airport' "
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print("List of airports:")
    for x in result:
        print("Country:", x[2], " ", "Id:", x[0], " ", "Municipality:", x[1])

# status (printing information about current balance, position,visited countries)


def getStatus():
    print("Your curent status:")
    print("Credits: "+str(playerCredits))
    print("Visited countries: "+str(playerVisited)+" : "+str(playerVisitedSet))
    print("Current position: "+str(playerPosition))

# position (select position from database)


def getPosition(icao):
    sql = "SELECT latitude_deg, longitude_deg from airport where ident ='" + icao + "'"
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    return cursor.fetchall()

# country code (select from airport database)


def getCountryCode(icao):
    sql = "SELECT iso_country from airport where ident ='" + icao + "'"
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    country = cursor.fetchall()
    for y in country:
        countrycode = (y[0])
        return countrycode

# distance (calculating distance between points)


def getDistance(playerPosition, playerDestination):
    icao = playerPosition
    a = getPosition(icao)[0]
    icao = playerDestination
    b = getPosition(icao)[0]
    #print(a, b)
    return round((distance.distance(a, b).km), 0)  # distance in km rounded


# random weather function


def weather():
    import random
    x = random.randint(0, 100)
    # current chance of bad weather is set to 20%
    if x <= 80:
        landing = True
    else:
        landing = False
    return landing
