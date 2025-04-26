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
@app.route('/coach', methods=['POST'])
def coach():
    user_input = request.json['user_input']
    prompt = open("prompt.persona", "r").read().replace('{user_input}', request.json['user_input'])

    res = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        #model="gpt-4-turbo",
        model="gpt-3.5-turbo",
        max_tokens=150,
        temperature=0.8
    )

    return jsonify({"result": res.choices[0].message.content.strip()})

if __name__ == '__main__':
    app.run(debug=True)
