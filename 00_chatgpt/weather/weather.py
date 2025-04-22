import os
from openai import OpenAI
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--city', required=True, help='City name')
args = parser.parse_args()


# Read API key from file
with open('api.key', 'r') as file:
    api_key = file.read().strip()

# Read prompt from file
with open('prompt', 'r') as file:
    prompt_template = file.read().strip()

prompt = prompt_template.replace('<city>', args.city)

# Initialize OpenAI client with the API key
client = OpenAI(api_key=api_key)

# Request chat completion
response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="gpt-3.5-turbo",
    max_tokens=1000,

    #High Temperature + High Top-p: Produces highly varied and creative responses.
    #Low Temperature + Low Top-p: Produces more focused and predictable responses.
    #High Temperature + Low Top-p: Balances creativity with some level of determinism.
    #Low Temperature + High Top-p: Mostly deterministic but with some diversity.
    temperature=0.2,  # Adjust temperature for creativity
    top_p=0.2  # Adjust top_p for response variability
)

# Print the completion
#print("Payload Response:")
#print(response)
print("ChatGPT Response:")
print(response.choices[0].message.content)
print("\n\n")
print(f"Completion Tokens: {response.usage.completion_tokens}")
print(f"Prompt Tokens: {response.usage.prompt_tokens}")
print(f"Total Tokens: {response.usage.total_tokens}")
