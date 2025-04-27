from flask import Flask, request, jsonify, render_template, session
from openai import OpenAI
import os
import csv
import json

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Add a secret key for sessions
app.config['SESSION_TYPE'] = 'filesystem'  # Use filesystem session for better persistence

# Initialize OpenAI client with the API key
with open('api.key', 'r') as f:
    api_key = f.read().strip()

client = OpenAI(api_key=api_key)

# Load products from CSV
def load_products():
    products = []
    try:
        with open('products.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['status'] == 'active':
                    products.append(row)
    except Exception as e:
        print(f"Error loading products: {e}")
    return products

# Select the most relevant product based on the conversation
def get_relevant_product(conversation_history, all_products):
    # Create a condensed version of the conversation
    condensed_convo = []
    for msg in conversation_history:
        if msg["role"] != "system":  # Skip system messages
            condensed_convo.append(f"{msg['role']}: {msg['content']}")
    
    conversation_text = "\n".join(condensed_convo)
    
    # Create a simplified product list for the AI to choose from
    simple_products = []
    for product in all_products:
        simple_products.append({
            "id": product["id"],
            "productname": product["productname"],
            "description": product["description"],
            "category": product["category"],
            "cost": product["cost"]
        })
    
    # Create a prompt for product selection
    prompt = f"""Based on the following conversation, select the most relevant product to recommend to the user.
The product should address their needs, concerns, or align with the spiritual guidance they're receiving.

Conversation:
{conversation_text}

Available Products (in JSON format):
{json.dumps(simple_products, indent=2)}

Return only the ID of the most appropriate product as a number.
If you're unsure or there's no clear match between the conversation and any product, respond with "NONE"."""
    
    try:
        res = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="gpt-3.5-turbo",
            max_tokens=10,
            temperature=0.2
        )
        
        # Try to extract a product ID
        response_text = res.choices[0].message.content.strip().upper()
        if response_text == "NONE":
            return None
            
        try:
            product_id = int(response_text.replace(".", "").strip())
            # Find the product with this ID
            for product in all_products:
                if int(product["id"]) == product_id:
                    return product
        except:
            return None  # If we can't parse the ID, don't suggest a product
    
    except Exception as e:
        print(f"Error in product selection: {e}")
    
    # Don't fall back to random selection - return None if no clear match
    return None

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
    
    # Add the new message to conversation history before looking for a product
    conversation_with_response = messages.copy()
    conversation_with_response.append({"role": "assistant", "content": assistant_response})
    
    # Always try to suggest a product (no random chance)
    products = load_products()
    if products:
        # Get a relevant product based on the conversation
        product = get_relevant_product(conversation_with_response, products)
        if product:  # Only suggest if a relevant product was found
            product_suggestion = f"\n\nBy the way, I sense your energy would harmonize beautifully with our {product['productname']}. For just ${product['cost']}, you can {product['description']} This sacred offering will elevate your journey. [SKU: {product['sku']}]"
            assistant_response += product_suggestion
    
    # Add assistant's response to messages (without the product suggestion)
    messages.append({"role": "assistant", "content": assistant_response.split("\n\nBy the way")[0]})
    
    # Store updated conversation history in session
    session['conversation_history'] = messages
    session.modified = True  # Mark the session as modified to ensure it's saved
    
    return jsonify({"result": assistant_response})

if __name__ == '__main__':
    app.run(debug=True)
