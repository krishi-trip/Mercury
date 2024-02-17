import yfinance as yf
import pandas as pd
import csv

data = pd.read_csv("data/tickerNames.csv")
# tickers = data['TickerName'].tolist()
tickers = data['TickerName'].tolist()[:3]

headers = ['Ticker', 'Date', 'Close', 'Bin']
values = []

for ticker in tickers:
    stock = yf.Ticker(ticker[0])

    hist = stock.history(interval="1wk", period="1y")
    important = hist.loc[:, "Close"]
    important = important.reset_index()
    important['Date'] = pd.to_datetime(important['Date']).dt.date

    for i in range(important.shape[0]):
        val = [ticker, important.at[i, 'Date'], important.at[i, 'Close'], 0]
        values.append(val)

with open('data/stockData.csv', 'w') as f:
    write = csv.writer(f)
     
    write.writerow(headers)
    write.writerows(values)
