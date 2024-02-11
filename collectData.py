import mysql.connector
import loginInfo as info

mydb = mysql.connector.connect(
  host=info.hostname,
  user=info.username,
  password=info.password,
  database="company"
)

mycursor = mydb.cursor()

# mycursor.execute("USE company")

sql = "INSERT INTO article (id, cName, message) VALUES (%s, %s, %s)"
val = (1, "Amazon", "This is a message")
mycursor.execute(sql, val)

mydb.commit()

mycursor.execute("SELECT * FROM article")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
