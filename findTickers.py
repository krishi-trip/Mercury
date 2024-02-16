import loginInfo as info
import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
  host=info.hostname,
  user=info.username,
  password=info.password,
  database="company",
)

mycursor = mydb.cursor()

pd.set_option('expand_frame_repr', False)
pd.set_option("display.max_rows", None, "display.max_columns", None)

payload=pd.read_html('https://en.wikipedia.org/wiki/Nasdaq-100')
df = payload[4]
for i in range(len(df)):
    ticker = df.loc[i, 'Ticker']

    sql = "INSERT INTO ticker (tName) VALUES (%s)"
    val = [ticker]
    mycursor.execute(sql, val)

mydb.commit()
