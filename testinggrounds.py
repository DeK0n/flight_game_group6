# imports
from modules import menu, functions
from geopy import distance
from unittest import result
import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user= "root",
    password= "12332167",
    autocommit=True
)