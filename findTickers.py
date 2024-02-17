import pandas as pd
import csv

headers = ['TickerName']
companies = []

pd.set_option('expand_frame_repr', False)
pd.set_option("display.max_rows", None, "display.max_columns", None)

payload=pd.read_html('https://en.wikipedia.org/wiki/Nasdaq-100')
df = payload[4]

for i in range(100):
    ticker = df.loc[i, 'Ticker']
    companies.append([ticker])

with open('data/tickerNames.csv', 'w') as f:
     
    # using csv.writer method from CSV package
    write = csv.writer(f)
     
    write.writerow(headers)
    write.writerows(companies)
