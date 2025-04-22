import os
from openai import OpenAI
import argparse
import psycopg2
from modules.openai2json import parse_openai_response, format_for_psql

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
print("ChatGPT Response:")
print(response.choices[0].message.content)
print("\n\n")

# Checks
parsed_data = parse_openai_response(response.choices[0].message.content)
psql_data = format_for_psql(parsed_data)

if psql_data:
    print("Data ready for PostgreSQL insertion:", psql_data)
else:
    print("Error processing OpenAI response.")

# Insert into DB
conn = psycopg2.connect(dbname="weather", user="z")
cur = conn.cursor()
cur.execute("""
    INSERT INTO city_weather (name, country, lat, lon, temperature_c, condition)
    VALUES (%s, %s, %s, %s, %s, %s)
""", psql_data)
conn.commit()
cur.close()
conn.close()


print(f"Completion Tokens: {response.usage.completion_tokens}")
print(f"Prompt Tokens: {response.usage.prompt_tokens}")
print(f"Total Tokens: {response.usage.total_tokens}")
