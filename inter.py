import os
from dotenv import load_dotenv
import openai
import json
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

Prompt=input("Enter your prompt: ").strip().replace("n/","")
response = openai.Completion.create(
  model="text-davinci-003",
  prompt=Prompt,
  temperature=1,
  max_tokens=2306,
  top_p=1,
  frequency_penalty=2,
  presence_penalty=2
)
response_str = json.dumps(response)
response_dict = json.loads(response_str)
output = response_dict['choices'][0]['text']
print(output)