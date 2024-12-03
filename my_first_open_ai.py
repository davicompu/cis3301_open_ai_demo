from openai import OpenAI
import json

credentials = json.loads(open('credential.json').read())

client = OpenAI(
    api_key=credentials['api_key']
)

completion = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Do you think you could beat the Turing test?"}
  ]
)

print(completion.choices[0].message.content)