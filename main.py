# GENERAL ----------------------------------------------------------------------------
# imports

from modules import menu  # ,functions
from geopy import distance
from unittest import result
import mysql.connector
import random

# connection to database login-password input

dbUser = input("Input local server user: ")  # "root"
dbPw = input("Input local server password: ")  # your password

# connection to databases
# use your user and password, host can be localhost or 127.0.0.0

connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user=dbUser,
    password=dbPw,
    autocommit=True
)

# FUNCTIONS --------------------------------------------------------------------------

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


def getDistance():
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

# random player id generator


def playerIdGen():
    import random
    x = "id"+str(random.randint(1000, 9999))  # e.g. id7362
    return x


# VARIABLES for current game session-------------------------------------------------

playerId = playerIdGen()  # applying unique id for player from generator
playerName = " " 
playerCredits = 10000  # starting balance
playerVisited = 1
playerVisitedSet = {"BE"}  # Set of countries codes to prevent double counting
playerPosition = "EBBR"  # later change to random or chosen
weatherPenalty = 200  # in credits cr
weatherCheck = 50  # in credits cr
playerGoal = 5  # countries to visit

# BODY OF THE GAME --------------------------------------------------------------------
menu.footer()
menu.pictureAircraft1()
playerName = input("Enter your name: ")
menu.greetings()

menu.commands()
print("Your starting point is Brusseles, Belgium (EBBR)")

while playerVisited != playerGoal and playerCredits > 0:
    menu.divider()
    command = input("Enter command: ")
    condition = weather()

    if command == "fly":
        # add what happens if wrong code
        # add restriction to travel outside available list
        playerDestination = input("Enter destination code: ")
        playerDestinationCountry = getCountryCode(playerDestination)

        if condition == True:  # if weather
            ticket = getDistance()
            playerCredits = playerCredits-ticket  # paying for flight
            playerPosition = playerDestination  # changing current position

            if playerDestinationCountry not in playerVisitedSet:  # if visited this country
                playerVisited = playerVisited+1  # country counter
                playerVisitedSet.add(playerDestinationCountry)  # visited list
            print("You successfully got to destination point of " +
                  str(playerPosition)+". You've spent "+str(ticket)+" credits.")
        else:
            playerCredits = playerCredits-weatherPenalty
            print("Destination is closed due to weather, you were penaltied " +
                  str(weatherPenalty)+"credits and stayed at "+str(playerPosition)+".")
    elif command == "info":
        getInfo()
    elif command == "status":
        getStatus()
    elif command == "commands":
        menu.commands()
    elif command == "exit":
        print("Game stopped")
        menu.footer()
        break
    else:
        print("Wrong command")

if playerVisited >= playerGoal:
    # add name, id, and score to database
    print("You finished the game. Final status is:")
    getStatus()
    menu.footer
elif playerCredits <= 0:
    print("You ran out of credits. Balance is: "+str(playerCredits))
    menu.footer