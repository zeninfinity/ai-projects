import openai
from modules.tsrequirements import get_required_fields

TS_FILE = "prompt.ts"

# Call this once with your actual key
openai.api_key = "your-api-key"

def ask_gpt_for_field(field_name):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are collecting trip information."},
            {"role": "user", "content": f"What is the value for: {field_name}?"}
        ]
    )
    return response.choices[0].message['content'].strip()

def main():
    fields = get_required_fields(TS_FILE)
    result = {}

    for field in fields:
        value = ask_gpt_for_field(field)
        result[field] = value

    print("const trip: Trip = {")
    for k, v in result.items():
        if v.lower() in ["true", "false"]:
            print(f'  {k}: {v},')
        elif v.startswith("[") and v.endswith("]"):
            print(f'  {k}: {v},')
        elif v == "null":
            print(f'  {k}: null,')
        else:
            print(f'  {k}: "{v}",')
    print("};")

if __name__ == "__main__":
    main()
