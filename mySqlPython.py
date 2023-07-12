
import mysql.connector

mydb = mysql.connector.conect(
    host = "localhost",
    username = "root",
    password = ""
)
  
mycursor = mydb.cursor()

mycursor.executive("create database customers")
print("Table Created")