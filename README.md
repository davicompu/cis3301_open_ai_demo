## OpenAI Demo - CIS 3301

This is a tutorial on how to install the neccesary dependencies for connecting with the OpenAI API. To start we need to install the openai python library; read more about it in the following link: [Open AI Introduction Documentation](https://platform.openai.com/docs/api-reference/introduction).

1. To install the openai python library, run the following command.

`python3 -m pip install openai`

2. Create a python script that will connect to the OpenAI API with your credentials.

`from openai import OpenAI\n`
`client = OpenAI(`
`  api_key = "ENTER YOUR API KEY"`
`)`

3. Read more about the chat completition feature from OpenAI: [https://platform.openai.com/docs/api-reference/chat/create](https://platform.openai.com/docs/api-reference/chat/create).

4. An example we can obtain from it is the following:

`completion = client.chat.completions.create(`
` model="gpt-4o",`
`  messages=[`
`    {"role": "system", "content": "You are a helpful assistant."},`
`    {"role": "user", "content": "Hello!"}`
`  ]`
`)`


