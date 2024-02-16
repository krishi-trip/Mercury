# Setup for database
import mysql.connector
import loginInfo as info

mydb = mysql.connector.connect(
  host=info.hostname,
  user=info.username,
  password=info.password,
)

mycursor = mydb.cursor()

mycursor.execute("DROP DATABASE IF EXISTS company")
mycursor.execute("CREATE DATABASE IF NOT EXISTS company")
mycursor.execute("USE company")

mycursor.execute("DROP TABLE IF EXISTS article")
mycursor.execute("CREATE TABLE article (id decimal(9, 0) NOT NULL, cName char(20) DEFAULT NULL, message char(100) NOT NULL, PRIMARY KEY (id), KEY message (message)) ENGINE=InnoDB")

mycursor.execute("DROP TABLE IF EXISTS ticker")
mycursor.execute("CREATE TABLE ticker (tName char(6), PRIMARY KEY (tName)) ENGINE=InnoDB")

mycursor.execute("DROP TABLE IF EXISTS priceData")
mycursor.execute("CREATE TABLE priceData (tName char(6), close_date date, price decimal(9, 2), PRIMARY KEY (tName, close_date), FOREIGN KEY (tName) REFERENCES ticker(tName)) ENGINE=InnoDB")
