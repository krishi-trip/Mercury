# API KEY: https://developers.google.com/custom-search/v1/overview
# SEARCH ENGINE CONSOLE: https://programmablesearchengine.google.com/controlpanel/all
# CUSTOME SEARCH API: https://developers.google.com/custom-search/v1/site_restricted_api

import datetime
from googleapiclient.discovery import build

# Google Custom Search Engine (CSE) API key
API_KEY = 'AIzaSyBuwLuv50KVCdl3M7byw3rBpaqypSaoCxk'

# Define the CSE ID for news search
CSE_ID = '103bcbd9dec5e45e1'

# Function to retrieve top news stories for a given query
def get_top_news(api_key, cse_id, query):
    service = build('customsearch', 'v1', developerKey=api_key)
    res = service.cse().list(q=query, cx=cse_id, num=5).execute()
    return res.get('items', [])

# List of NASDAQ-100 stocks
nasdaq_100_stocks = [
    'AAPL', 'MSFT', 'AMZN', 'GOOGL', 'GOOG', 'FB', 'TSLA', 'NVDA', 'PYPL', 'INTC',
    'CMCSA', 'ADBE', 'NFLX', 'PEP', 'CSCO', 'AVGO', 'TMUS', 'TXN', 'QCOM', 'AMD',
    'COST', 'ABBV', 'BKNG', 'CHTR', 'MDLZ', 'INTU', 'ISRG', 'AMGN', 'GILD', 'LRCX',
    'WBA', 'MU', 'FISV', 'ADP', 'REGN', 'VRTX', 'ATVI', 'ILMN', 'CSX', 'ADI', 'ZM',
    'ADI', 'ADSK', 'MELI', 'KLAC', 'DXCM', 'DOCU', 'LULU', 'EBAY', 'MRNA', 'AEP'
]

# Define start and end dates
start_date = datetime.date(2018, 1, 1)
end_date = datetime.date(2018, 12, 31)
#end_date = datetime.date(2023, 12, 31)

# Iterate over weeks from start_date to end_date
current_date = start_date
while current_date <= end_date:
    # Print current week's date range
    print(f"Week of {current_date} to {current_date + datetime.timedelta(days=6)}")
    
    # Iterate over each stock
    for stock in nasdaq_100_stocks:
        # Construct query for the stock's top news
        query = f"{stock} stock news"
        
        # Retrieve top news stories for the query
        top_news = get_top_news(API_KEY, CSE_ID, query)
        
        # Print the top news stories for the stock
        print(f"{stock}:")
        for idx, news in enumerate(top_news, 1):
            print(f"{idx}. {news['title']} - {news['link']}")
        print()
    
    # Move to the next week
    current_date += datetime.timedelta(days=7)
