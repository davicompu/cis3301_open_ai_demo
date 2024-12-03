from ollama import Client
import pandas as pd

ai_client = Client()
ai_model = 'llama3.1'
temperature = 0.7

def get_ai_response(text_prompt,system="",temperature=0.7):
    system = f'{system}'
    prompt = f"""{text_prompt}"""
    
    response = ai_client.generate(model=ai_model, prompt=prompt,system=system, options={'temperature':temperature})
    return response['response']


response = get_ai_response("Tell me a joke")
print(response)