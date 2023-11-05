import os
import openai

'''
If you have an api key saved that ou have made accessible to all your projects, you can
uncomment the first line. Else, add the key or path to the file containing the key in the second line.
'''
#openai.api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = '<insert key or path here>'

'''
Most basic possible setup to perform titular task:
'''
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role":"user", "content":"Compose a haiku about random topic, and tell me what that topic is at the start"}]
)

print(completion.choices[0].message.content)