import yaml
import openai

import requests

URL = "https://api.openai.com/v1/chat/completions"

# Create a yaml fiel with your openai ssh key
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

ssh_key = config['personal_info']['openai_ssh']

openai.api_key = ssh_key

response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Correct this to standard English:\n\nShe no went to the market.",
    temperature=0,
    max_tokens=60,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
)

print(response.get("choices"))
