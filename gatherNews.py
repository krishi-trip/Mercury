# API KEY: https://developers.google.com/custom-search/v1/overview
# SEARCH ENGINE CONSOLE: https://programmablesearchengine.google.com/controlpanel/all
# CUSTOME SEARCH API: https://developers.google.com/custom-search/v1/site_restricted_api

import datetime
import pandas as pd
import csv
from googleapiclient.discovery import build
import loginInfo as info
from tqdm import tqdm

# Google Custom Search Engine (CSE) API key
API_KEY = info.google_api_key

# Define the CSE ID for news search
CSE_ID = '103bcbd9dec5e45e1'

# Function to retrieve top news stories for a given query
def get_top_news(api_key, cse_id, query):
    service = build('customsearch', 'v1', developerKey=api_key)
    res = service.cse().list(q=query, cx=cse_id, num=5).execute()
    return res.get('items', [])

data = pd.read_csv("data/tickerNames.csv")

# List of NASDAQ-100 stocks
nasdaq_100_stocks = data['TickerName'].tolist()[:2]
pbar = tqdm(nasdaq_100_stocks)

headers = ['TickerName', 'Week', 'Index', 'NewsTitle', 'NewsLink']
values = []

# Define start and end dates
start_date = datetime.date(2018, 1, 1)
end_date = datetime.date(2018, 2, 20)
# end_date = datetime.date(2018, 12, 31)
#end_date = datetime.date(2023, 12, 31)

# Iterate over weeks from start_date to end_date
current_date = start_date
while current_date <= end_date:
    # Print current week's date range
    end_date = current_date + datetime.timedelta(days=6)
    week = "From {currDate} to {endDate}".format(currDate=current_date, endDate=end_date)
    
    # Iterate over each stock
    for stock in pbar:
        # Construct query for the stock's top news
        query = f"{stock} stock news"
        
        # Retrieve top news stories for the query
        top_news = get_top_news(API_KEY, CSE_ID, query)
        
        # Print the top news stories for the stock
        for idx, news in enumerate(top_news, 1):
            row = [stock, week, idx, news['title'], news['link']]
            values.append(row)
    
    # Move to the next week
    current_date += datetime.timedelta(days=7)

with open('data/newsData.csv', 'w') as f:
     
    # using csv.writer method from CSV package
    write = csv.writer(f)
     
    write.writerow(headers)
    write.writerows(values)

print("Completed")
