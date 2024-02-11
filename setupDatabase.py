# Setup for database
import mysql.connector
import loginInfo as info

mydb = mysql.connector.connect(
  host=info.hostname,
  user=info.username,
  password=info.password,
)

mycursor = mydb.cursor()

# mycursor.execute("USE company")

# sql = "INSERT INTO article (id, cName, message) VALUES (%s, %s, %s)"
# val = (1, "Amazon", "This is a message")
mycursor.execute("DROP DATABASE IF EXISTS company")
mycursor.execute("CREATE DATABASE IF NOT EXISTS company")
mycursor.execute("USE company")

mycursor.execute("DROP TABLE IF EXISTS article")
mycursor.execute("CREATE TABLE article (id decimal(9, 0) NOT NULL, cName char(20) DEFAULT NULL, message char(100) NOT NULL, PRIMARY KEY (id), KEY message (message)) ENGINE=InnoDB")
