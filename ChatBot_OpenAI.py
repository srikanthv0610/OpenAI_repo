import yaml
import openai

# Create a yaml fiel with your openai ssh key
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

ssh_key = config['personal_info']['openai_ssh']

openai.api_key = ssh_key

messages = [
    {"role": "system", "content": "You are a kind helpful assistant."},
]

while True:
    message = input("User : ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )

    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})
