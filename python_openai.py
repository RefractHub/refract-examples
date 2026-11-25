# pip install openai
# Set your key first:  export REFRACT_API_KEY=rf_...   (Windows PowerShell: $env:REFRACT_API_KEY = "rf_...")
import os
from openai import OpenAI

client = OpenAI(base_url="https://refracthub.com/v1", api_key=os.environ["REFRACT_API_KEY"])

# a normal reply
reply = client.chat.completions.create(
    model="gpt-6.2-sol",
    messages=[{"role": "user", "content": "Explain recursion in one sentence."}],
)
print(reply.choices[0].message.content)

# the same, streamed word by word, with a different model: only the name changes
stream = client.chat.completions.create(
    model="claude-sonnet-5-5",
    messages=[{"role": "user", "content": "Count from 1 to 5."}],
    stream=True,
)
for chunk in stream:
    if chunk.choices and chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
print()
