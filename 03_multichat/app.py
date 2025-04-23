from flask import Flask, request, jsonify, render_template
from openai import OpenAI
import os

app = Flask(__name__)

# Initialize OpenAI client with the API key
with open('api.key', 'r') as f:
    api_key = f.read().strip()

client = OpenAI(api_key=api_key)

# Serve the index.html file at the root URL using render_template
@app.route('/')
def index():
    return render_template('index.html')

# Analyze the numbers and ask OpenAI
@app.route('/analyze', methods=['POST'])
def analyze():
    nums = request.json['nums']
    prompt = (
    f"Analyze the numbers {nums[0]}, {nums[1]}, and {nums[2]}. "
    f"List their properties (e.g., prime, even, palindrome), then determine if they share any one property. "
    f"Also find something they have factually in common."
    f"If not, say 'They have no notable property in common.' Be factually accurate and logical."
)
    # prompt = f"Given these three numbers: {nums[0]}, {nums[1]}, {nums[2]}, what is one thing interesting and peculiar they all have in common? Think step by step and make sure the answer is factually accurate."

    res = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="gpt-3.5-turbo",
        max_tokens=100,
        temperature=0.5
    )

    return jsonify({"result": res.choices[0].message.content.strip()})

if __name__ == '__main__':
    app.run(debug=True)
