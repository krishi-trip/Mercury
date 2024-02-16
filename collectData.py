import loginInfo as info
import mysql.connector
import yfinance as yf
import pandas as pd

mydb = mysql.connector.connect(
  host=info.hostname,
  user=info.username,
  password=info.password,
  database="company",
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM ticker")

tickers = mycursor.fetchall()

for ticker in tickers:
    stock = yf.Ticker(ticker[0])

    hist = stock.history(interval="1d", period="1mo")
    important = hist.loc[:, "Close"]
    important = important.reset_index()
    important['Date'] = pd.to_datetime(important['Date']).dt.date
    # print(important)
    for i in range(important.shape[0]):
        sql = "INSERT INTO priceData (tName, close_date, price) VALUES (%s, %s, %s)"
        val = (ticker[0], important.at[i, 'Date'], important.at[i, 'Close'])
        # print(val)
        try:
            mycursor.execute(sql, val)
        except:
            print("Error for ", val)

mydb.commit()

mycursor.execute("SELECT * FROM article")

myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)
