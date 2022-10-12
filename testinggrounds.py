# imports
from modules import menu, functions
from geopy import distance
from unittest import result
import mysql.connector
import random

# connection to databases
# use your user and password, host can be localhost or 127.0.0.0
connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user="root",
    password="12332167",
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
    print("List of airports:")
    for x in result:
        print("Country:", x[2], " ", "Id:", x[0], " ", "Municipality:", x[1])

def getCountryCode(icao):
    sql = "SELECT iso_country from airport where ident ='" + icao + "'"
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    country = cursor.fetchall()
    for y in country:
        z = (y[0])
    return z

icao = "EKBI"
x=getCountryCode(icao)
print(x)