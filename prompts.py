
def get_analyze_news_prompt(ticker, article):
    prompt = "Please summarize the following noisy but possible news data extracted from web page HTML, and extract keywords of the news. The news text can be very noisy due to it is HTML extraction. Give formatted answer such as Summary: ..., Keywords: ... The news is supposed to be for {symbol} stock. You may put \'N/A\' if the noisy text does not have relevant information to extract. \n News: {news}".format(symbol=ticker, news=article)
    return prompt

def get_company_summary_prompt(ticker):
    prompt = "Generate a short description for stock \"{companyName}\". Also list general positive and negative factors that might impact the stock price; be brief and use keywords. Consider diverse general factors, such as macro economic situation (e.g. inflation, CPI growth), business factors (e.g. sales, investment, products), technology factors (e.g. innovation), and others. Use format Description: ..., Positive Factors: ..., Negative factors: ...".format(companyName=ticker)
    return prompt

def get_forcasting_prompt():
    prompt = '''
Instruction: Forecast next week stock return (price change) for symbol, given the company profile, historical weekly news summary, keywords, and stock returns, and optionally the examples from other stocks of a similar company. The trend is represented by bins "D5+", "D5", "D4", "D3", "D2", "D1", "U1", "U2", "U3", "U4", "U5", "U5+", where "D5+" means price dropping more than 5%, D5 means price dropping between 4% and 5%, "D4" means price dropping between 3% and 4%, "U5+" means price rising more than 5%, "U5" means price rising between 4% and 5%, "D4" means price rising between 3% and 4%, etc. 
Company Profile: {company_profile}
Recent News: News are ordered from oldest news to latest newsself.
====8 Weeks ago==== 
{meta_news_summary_company}
{meta_news_summary_macro} ... 
====7 weeks ago==== 
... 
====Last week==== 
... 
Forecasting Examples: {few_shot_learning_examples_from_similar_stocks}

Now predict what could be the next week’s Summary, Keywords, and forecast the Stock Return. The predicted Summary/Keywords should explain the stock return forecasting. You should predict what could happen next week. Do not just summarize the history. The next week stock return need not be the same as the previous week. Use format Summary: ..., Keywords: ..., Stock Return: ...
'''
    return prompt
# print(get_company_summary_prompt('Apple'))
