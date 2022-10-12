# imports
from modules import menu, functions
from geopy import distance
from unittest import result
import mysql.connector

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

#  FUNCTIONS
# info


def getInfo():
    sql = "SELECT ident,municipality,iso_country from airport where continent ='EU' and type = 'large_airport' "
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for x in result:
        print("Country:", x[2], " ", "Id:", x[0], " ", "Municipality:", x[1])

# distance


def getInfoBy(icao):
    sql = "SELECT latitude_deg, longitude_deg from airport where ident ='" + icao + "'"
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


icao = input("Enter 1st ICAO: ")
a = getInfoBy(icao)[0]
icao = input("Enter 2nd ICAO: ")
b = getInfoBy(icao)[0]
print(a, b)
print(f"The distance between is {distance.distance(a, b).km:.2f} km")

# variables for current game session
playerCredits = 10000
playerName = input("Enter your name:")
playerVisited = 1
playerPosition = ""

# Actual game starts
menu.greetings()
menu.commands()

if playerVisited != 15:
    command = ""
    while command != "exit":
        command = input("Enter command: ")
        if command == "fly":
            print("Enter destination code: ")

        elif command == "check":
            print("check")
        elif command == "info":
            print("List of airports:")
            getInfo()
        elif command == "status":
            print("Your curent status:")

        elif command == "commands":
            print("commands")
        elif command == "exit":
            command = "exit"
            print("Game stopped")
        else:
            print("Wrong command")
else:
    print("The game is over. Your final status is:")
    # print(playerStatus)
