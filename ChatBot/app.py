# Import Modules
from flask import Flask, render_template, request, jsonify
import google.generativeai as gen_ai
import config

# Initialize Flask app
app = Flask(__name__)

# Configure Google Gemini-Pro AI model
gen_ai.configure(api_key=config.api_key)
model = gen_ai.GenerativeModel('gemini-pro')

# Initialize chat session
chat_session = model.start_chat(history=[])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_prompt = request.form['user_input']
    
    # Send user's message to Gemini-Pro and get the response
    gemini_response = chat_session.send_message(user_prompt)
    
    # Store the chat history in a list to pass to the frontend
    chat_history = [
        {"role": "assistant" if msg.role == "model" else msg.role, 
         "text": msg.parts[0].text} 
        for msg in chat_session.history
    ]
    
    return jsonify(chat_history)

# Main Part
if __name__ == '__main__':
    app.run(debug=True)