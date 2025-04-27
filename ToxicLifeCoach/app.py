from flask import Flask, request, jsonify, render_template, session
from openai import OpenAI
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Add a secret key for sessions
app.config['SESSION_TYPE'] = 'filesystem'  # Use filesystem session for better persistence

# Initialize OpenAI client with the API key
with open('api.key', 'r') as f:
    api_key = f.read().strip()

client = OpenAI(api_key=api_key)

# Serve the index.html file at the root URL using render_template
@app.route('/')
def index():
    # Clear conversation history when user loads the page
    session['conversation_history'] = []
    return render_template('index.html')

# Analyze the numbers and ask OpenAI
@app.route('/coach', methods=['POST'])
def coach():
    user_input = request.json['user_input']
    
    # Get conversation history or initialize if it doesn't exist
    conversation_history = session.get('conversation_history', [])
    
    # Create a modified system prompt that explicitly instructs to remember previous context
    base_system_prompt = open("prompt.persona", "r").read().split("User Input:")[0].strip()
    enhanced_system_prompt = base_system_prompt + "\n\nIMPORTANT: You must remember and reference information from previous messages in the conversation. If asked about preferences, likes, dislikes, or any personal information shared earlier, refer back to that information in your response."
    
    # Prepare messages array starting with the system message
    if not conversation_history:
        # First message in conversation - initialize with system message
        messages = [{"role": "system", "content": enhanced_system_prompt}]
    else:
        # For existing conversations, update the system message
        if conversation_history[0]["role"] == "system":
            conversation_history[0]["content"] = enhanced_system_prompt
            messages = conversation_history
        else:
            messages = [{"role": "system", "content": enhanced_system_prompt}] + conversation_history
    
    # Add the new user message
    messages.append({"role": "user", "content": user_input})
    
    # For debugging
    print("Sending to OpenAI:", messages)
    
    res = client.chat.completions.create(
        messages=messages,
        #model="gpt-4-turbo",
        model="gpt-3.5-turbo",
        max_tokens=250,  # Increased max tokens for more detailed responses
        temperature=0.7   # Slightly lower temperature for more consistent responses
    )
    
    # Get the response
    assistant_response = res.choices[0].message.content.strip()
    
    # Add assistant's response to messages
    messages.append({"role": "assistant", "content": assistant_response})
    
    # Store updated conversation history in session
    session['conversation_history'] = messages
    session.modified = True  # Mark the session as modified to ensure it's saved
    
    return jsonify({"result": assistant_response})

if __name__ == '__main__':
    app.run(debug=True)
