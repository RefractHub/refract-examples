# pip install anthropic
# Refract also speaks the Anthropic Messages API. Note the base URL has no /v1: the SDK adds it.
import os
import anthropic

client = anthropic.Anthropic(base_url="https://refracthub.com", api_key=os.environ["REFRACT_API_KEY"])

message = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=500,
    messages=[{"role": "user", "content": "What's a good first project for learning Rust?"}],
)
print(message.content[0].text)
