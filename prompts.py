
def get_analyze_news_prompt(ticker, article):
    prompt = "Please summarize the following noisy but possible news data extracted from web page HTML, and extract keywords of the news. The news text can be very noisy due to it is HTML extraction. Give formatted answer such as Summary: ..., Keywords: ... The news is supposed to be for {symbol} stock. You may put \'N/A\' if the noisy text does not have relevant information to extract. \n News: {news}".format(symbol=ticker, news=article)
    return prompt

def get_company_summary_prompt(ticker):
    prompt = "Generate a short description for stock \"{companyName}\". Also list general positive and negative factors that might impact the stock price; be brief and use keywords. Consider diverse general factors, such as macro economic situation (e.g. inflation, CPI growth), business factors (e.g. sales, investment, products), technology factors (e.g. innovation), and others. Use format Description: ..., Positive Factors: ..., Negative factors: ...".format(companyName=ticker)
    return prompt

# print(get_company_summary_prompt('Apple'))
