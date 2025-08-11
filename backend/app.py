import os
import requests
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

# --- AI Integration ---
# It's recommended to store your API key in an environment variable for security.
# For example: export OPENAI_API_KEY='your_key_here'
API_KEY = os.environ.get("OPENAI_API_KEY", "DEFAULT_API_KEY_FOR_TESTING")
API_URL = "https://api.openai.com/v1/chat/completions" # Example for OpenAI

def get_ai_response(user_message):
    """
    This function gets a response from an AI model.
    Currently, it uses a mock response for demonstration.
    To use a real AI, replace the mock logic with a real API call.
    """

    # --- Mock AI Response Logic (for demonstration) ---
    if "gold" in user_message.lower():
        return "Trading gold can be a good way to diversify your portfolio. It's often seen as a 'safe haven' asset during times of economic uncertainty. Would you like to know about fundamental or technical analysis for gold?"
    elif "forex" in user_message.lower():
        return "Forex (Foreign Exchange) is the market for trading currencies. It's the largest financial market in the world. Key concepts include pips, lots, and leverage. What specific topic are you interested in?"
    elif "data analysis" in user_message.lower():
        return "Data analysis in trading involves using historical data to find patterns and predict future market movements. Common tools include moving averages, RSI, and MACD. Which indicator would you like to learn about first?"
    else:
        return "I can teach you about data analysis, gold trading, and Forex. Please ask me a question about one of these topics!"

    # --- Real AI API Call Logic (Example for OpenAI) ---
    # headers = {
    #     "Authorization": f"Bearer {API_KEY}",
    #     "Content-Type": "application/json"
    # }
    # data = {
    #     "model": "gpt-3.5-turbo", # Or any other model
    #     "messages": [
    #         {"role": "system", "content": "You are a helpful assistant specialized in teaching about gold trading, forex, and data analysis."},
    #         {"role": "user", "content": user_message}
    #     ]
    # }
    #
    # try:
    #     response = requests.post(API_URL, headers=headers, json=data)
    #     response.raise_for_status() # Raise an exception for bad status codes
    #     return response.json()["choices"][0]["message"]["content"]
    # except requests.exceptions.RequestException as e:
    #     print(f"Error calling AI API: {e}")
    #     return "Sorry, I'm having trouble connecting to the AI service right now."


# --- Flask App ---
app = Flask(__name__, static_folder='../frontend')
CORS(app)

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get('message')

    if not message:
        return jsonify({"response": "Please provide a message."}), 400

    ai_response = get_ai_response(message)
    return jsonify({'response': ai_response})

if __name__ == '__main__':
    # Make sure to set the FLASK_APP and FLASK_ENV environment variables
    # export FLASK_APP=app.py
    # export FLASK_ENV=development
    app.run(debug=True, port=5000)
