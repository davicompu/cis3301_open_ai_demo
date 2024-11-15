from openai import OpenAI
import json

credentials = json.loads(open('credentials.json').read())

client = OpenAI(
    api_key=credentials['api_secret_key']
)

completion = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)