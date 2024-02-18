from pygooglenews import GoogleNews
import requests
from bs4 import BeautifulSoup
import pandas as pd
import tqdm
import datetime
import csv

#query = 'MSFT top news'
#search = gn.search('MSFT top news', helper = True, from_ = '2022-01-01', to_ = '2022-01-07')
#search = gn.search(query, helper = True, when = None, from_ = '2018-01-01', to_ = '2018-01-07', proxies=None, scraping_bee=None)

# for i in range(0, 1):
#     print(i, search['entries'][i]['title'])
#     print(i, search['entries'][i]['links'][0]['href'])

gn = GoogleNews(lang = 'en', country = 'US')

def get_top_news(query, from_, to_):
    search = gn.search(query, helper = True, when = None, from_ = from_, to_ = to_, proxies=None, scraping_bee=None)
    return search

def extract_article_content(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')
            # Extract the text content
            text_content = soup.get_text()
            return text_content
        else:
            print("Failed to retrieve content. Status code:", response.status_code)
            return None
    except Exception as e:
        print("An error occurred:", str(e))
        return None

#Import the data from the csv
data = pd.read_csv("data/tickerNames.csv")

# List of NASDAQ-100 stocks
nasdaq_100_stocks = data['TickerName'].tolist()[:2]
pbar = tqdm(nasdaq_100_stocks)

headers = ['TickerName', 'Week', 'NewsTitle', 'NewsLink']
values = []

start_date = datetime.date(2018, 1, 1)
end_date = datetime.date(2018, 1, 14)

current_date = start_date

while current_date <= end_date:
    #Print the current week's date range
    week = "From {currDate} to {currEnd}".format(currDate = current_date, currEnd = current_date + datetime.timedelta(days=6))

    for stock in pbar:
        #Construct the query for the stock's top news
        query = f"{stock} stock news"

        #Retrieve the top news stories for the query
        top_news = get_top_news(query, current_date.strftime("%Y-%m-%d"), (current_date + datetime.timedelta(days=6)).strftime("%Y-%m-%d"))

        count = 0
        for entry in top_news['entries']:
            if (count > 5):
                count = 0
                break

            count += 1

            link = entry['links'][0]['href']
            title = entry['title']
            
            row = [stock, week, title, link]
            values.append(row)

            content = extract_article_content(link)

            if content:
                print(content)

        print()

    current_date += datetime.timedelta(days=7)

with open('data/newsData.csv', 'w') as f:
     
    # using csv.writer method from CSV package
    write = csv.writer(f)
     
    write.writerow(headers)
    write.writerows(values)

print("Completed")
