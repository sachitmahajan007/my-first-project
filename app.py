from flask import Flask, request, jsonify
from groq import Groq
import os
from dotenv import load_dotenv 

load_dotenv()
app = Flask(__name__)
client = Groq(api_key=os.getenv("your-groq-key-here")) 

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to Sachit's AI API",
        "status": "running", 
        "endpoints": {
            "POST /ask": "Ask the AI anything"
        }
    })

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    
    if not data or 'message' not in data:
        return jsonify({"error": "Please send a message"}), 400
    
    user_message = data['message']
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a helpful assistant named Sachit's AI. Be concise and clear."},
            {"role": "user", "content": user_message}
        ]
    )
    
    reply = response.choices[0].message.content
    
    return jsonify({
        "reply": reply,
        "status": "success"
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
   
