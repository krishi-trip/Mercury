import torch
import prompts
import pandas as pd
from transformers import LlamaTokenizer, LlamaForCausalLM, Trainer, TrainingArguments

model_path = 'openlm-research/open_llama_13b'

DEVICE = torch.device("mps" if torch.backends.mps.is_available() else "cpu") # This always results in MPS

tokenizer = LlamaTokenizer.from_pretrained(model_path)
model = LlamaForCausalLM.from_pretrained(
    model_path, torch_dtype=torch.float16, device_map=DEVICE,
)

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

# Additional examples for instruction-based fine-tuning
additional_examples = [
    {"instruction": "Multiply two numbers", "code": "2 * 3", "output": "6"},
    {"instruction": "Define a list of numbers", "code": "numbers = [1, 2, 3, 4, 5]", "output": "(No specific output provided for this example)"},
    # Add more examples as needed
]

# Combine the initial prompt and additional examples
combined_prompt = instruction_prompt + '\n'.join([f'Instruction: {example["instruction"]}\nCode: {example["code"]}\nOutput: {example["output"]}\n' for example in additional_examples])

# Fine-tune the model
training_args = TrainingArguments(
    per_device_train_batch_size=4,
    num_train_epochs=3,
    logging_dir='./logs',
    overwrite_output_dir=True,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=combined_prompt,
    tokenizer=tokenizer,
)

trainer.train()

prompt = 'Q: What is the largest animal?\nA:'
# prompt = prompts.get_forcasting_prompt(company, createSummary(company, week))

input_ids = tokenizer(prompt, return_tensors="pt").input_ids

generation_output = model.generate(input_ids=input_ids, max_new_tokens=32)
print(tokenizer.decode(generation_output[0]))

