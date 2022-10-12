# imports
from modules import menu, functions
from geopy import distance
from unittest import result
import mysql.connector

#connection to database login-password input
dbUser = input("Input local server user: ") #"root"
dbPw = input("Input local server password: ") #your password

#connection to databases
# use your user and password, host can be localhost or 127.0.0.0
connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user= dbUser,
    password= dbPw,
    autocommit=True
)

menu.greetings()
menu.commands()

playerCredits = 10000
playerName = input("Enter your name:")
# print('Use "fly" command to set starting point.')
functions.action()

# distance
# def getInfoBy(icao):
#     sql = "SELECT latitude_deg, longitude_deg from airport where ident ='" + icao + "'"
#     # print(sql)
#     cursor = connection.cursor()
#     cursor.execute(sql)
#     result = cursor.fetchall()
#     return result
# icao = input("Enter 1st ICAO: ")
# a = getInfoBy(icao)[0]
# icao = input("Enter 2nd ICAO: ")
# b = getInfoBy(icao)[0]
# print(a, b)
# print(f"The distance between is {distance.distance(a, b).km:.2f} km")


