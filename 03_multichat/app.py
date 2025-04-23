from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

with open('api.key', 'r') as f:
    api_key = f.read().strip()

client = OpenAI(api_key=api_key)

@app.route('/analyze', methods=['POST'])
def analyze():
    nums = request.json['nums']
    prompt = f"Given these three numbers: {nums[0]}, {nums[1]}, {nums[2]}, what is one thing they all have in common?"
    
    res = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="gpt-3.5-turbo",
        max_tokens=100,
        temperature=0.5
    )
    
    return jsonify({"result": res.choices[0].message.content.strip()})

if __name__ == '__main__':
    app.run(debug=True)
