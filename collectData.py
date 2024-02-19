from os import close
import yfinance as yf
import pandas as pd
import csv
from tqdm import tqdm
import warnings

warnings.simplefilter(action="ignore", category=FutureWarning)

def calculateBin(prevClose, currClose):
    percent_change = 100 * (currClose - prevClose) / prevClose
    ret = ""
    if percent_change < 0:
        ret = ret + "D"
    else:
        ret = ret + "U"

    if abs(percent_change) > 5:
        ret = ret + "5+"
    elif abs(percent_change) > 4:
        ret = ret + "5"
    elif abs(percent_change) > 3:
        ret = ret + "4"
    elif abs(percent_change) > 2:
        ret = ret + "3"
    elif abs(percent_change) > 1:
        ret = ret + "2"
    else:
        ret = ret + "1"
    return ret

data = pd.read_csv("data/tickerNames.csv")
# tickers = data['TickerName'].tolist()
pbar = tqdm(data['TickerName'].tolist()[:10])

headers = ['Ticker', 'Date', 'Close', 'Bin']
values = []

for ticker in pbar:
    stock = yf.Ticker(ticker[0])

    hist = stock.history(start="2018-01-01", interval="1wk", period="1y")
    important = hist.loc[:, "Close"]
    important = important.reset_index()
    important['Date'] = pd.to_datetime(important['Date']).dt.date

    for i in range(important.shape[0]):
        closePrice = important.at[i, 'Close']
        bin = "NA" 
        if i > 0:
            prevPrice = important.at[i - 1, 'Close']
            bin = calculateBin(prevPrice, closePrice)
        val = [ticker, str(important.at[i, 'Date']), closePrice, bin]
        values.append(val)

with open('data/stockData.csv', 'w') as f:
    write = csv.writer(f)
     
    write.writerow(headers)
    write.writerows(values)

print("Completed")
