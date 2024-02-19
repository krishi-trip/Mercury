import prompts
import google.generativeai as model
import loginInfo as info
import pandas as pd

model.configure(api_key=info.model_api_key)

defaults = {
  'model': 'models/text-bison-001',
  'temperature': 0.7,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
  'max_output_tokens': 1024,
  'stop_sequences': [],
  'safety_settings': [{"category":"HARM_CATEGORY_DEROGATORY","threshold":"BLOCK_LOW_AND_ABOVE"},{"category":"HARM_CATEGORY_TOXICITY","threshold":"BLOCK_LOW_AND_ABOVE"},{"category":"HARM_CATEGORY_VIOLENCE","threshold":"BLOCK_MEDIUM_AND_ABOVE"},{"category":"HARM_CATEGORY_SEXUAL","threshold":"BLOCK_MEDIUM_AND_ABOVE"},{"category":"HARM_CATEGORY_MEDICAL","threshold":"BLOCK_MEDIUM_AND_ABOVE"},{"category":"HARM_CATEGORY_DANGEROUS","threshold":"BLOCK_MEDIUM_AND_ABOVE"}],
}

#Import the data from the csv
news_data = pd.read_csv("data/newsData.csv")
stock_data = pd.read_csv("data/stockData.csv")

def createSummary(company, week):
    summary = ""
    for i in range(4):
        index = news_data.loc[week]
        news_summary = prompts.get_analyze_news_prompt(company, news_data.at[index, 'Content'])
        macro_summary = stock_data.at[week, 'Bin']
        summary += "===={idx} Weeks ago====".format(idx=i)
        summary += news_summary
        summary += macro_summary

# Inputs
company = 'ADP'
week = '2018-01-01'

input = prompts.get_forcasting_prompt(company, createSummary(company, week))
prompt = f"""input: {input}
output:"""

response = model.generate_text(
  **defaults,
  prompt=prompt
)

print(response.result)
