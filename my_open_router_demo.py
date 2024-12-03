from openai import OpenAI
import json

credentials = json.loads(open('credential.json').read())


client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=credentials['openrouter'],
)

completion = client.chat.completions.create(
  model="meta-llama/llama-3.2-3b-instruct:free",
  messages=[
    {
      "role": "user",
      "content": "Tell me a joke"
    }
  ]
)
print(completion.choices[0].message.content)