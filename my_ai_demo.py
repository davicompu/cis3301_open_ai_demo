
from openai import OpenAI
import json

credentials = json.loads(open('credential.json').read())
# print(credentials['api_key'])

client = OpenAI(api_key=credentials['api_key'])

my_joke_prompt = input("Enter a joke prompt: ")

my_message_prompts = [{'role':'system','content':'You are a stand up comedian, and your audience are non Python programmers'},
                        {'role':'user','content':my_joke_prompt}
                        ]

completion = client.chat.completions.create(
    model='gpt-4o-mini',
    messages= my_message_prompts
)

print(completion.choices[0].message.content)
