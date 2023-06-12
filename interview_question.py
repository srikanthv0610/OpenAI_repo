import yaml
import openai

# Create a yaml fiel with your openai ssh key
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

ssh_key = config['personal_info']['openai_ssh']

openai.api_key = ssh_key

response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Create a list of 8 questions for my interview with a Machine learning engineer:",
    temperature=0.5,
    max_tokens=150,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
)

print(response.get("choices"))
