import openai
import random
import datetime
from flask import Flask, request, jsonify
import os

# Initialize Flask app
app = Flask(__name__)

# Set your OpenAI API key here
openai.api_key = "sk-proj-xxxxxxxx"

# Simple rule-based text generator fallback (Padke Boss Style)
def basic_text_generation(prompt):
    responses = {
        "hello": "Hello there! I'm Padke Boss, how can I help you today?",
        "who are you": "I'm Padke Boss, your AI assistant for crypto, astronomy, and cybersecurity!",
        "bye": "Goodbye, Boss! Stay safe online and always stay one step ahead!"
    }
    for key in responses:
        if key in prompt.lower():
            return responses[key]
    return "I'm not sure how to respond to that yet, Boss. Try asking about crypto, astronomy, or hacking."

# PBC Price Prediction (random value) with Boss Meme-style Response
def get_pbc_prediction():
    price = round(random.uniform(0.01, 100), 2)
    response = {
        "coin": "Padke Boss Coin (PBC)",
        "prediction": price,
        "timestamp": datetime.datetime.now().isoformat(),
        "response": f"Missed BTC? Don't miss this, Boss! The current price of Padke Boss Coin (PBC) is ${price}."
    }
    return response

# Example of a random crypto price prediction
def get_crypto_prediction():
    price = round(random.uniform(20000, 80000), 2)
    return {
        "coin": "Bitcoin",
        "prediction": price,
        "timestamp": datetime.datetime.now().isoformat(),
        "response": f"Don't miss out, Boss! Bitcoin's price is currently ${price}. Time to make moves!"
    }

# Astronomy data (randomized)
def get_astronomical_data():
    now = datetime.datetime.now()
    return {
        "sun_position": f"{random.uniform(-90, 90):.2f}°",
        "moon_phase": random.choice(["New Moon", "Full Moon", "Waxing Crescent", "Waning Gibbous"]),
        "timestamp": now.isoformat()
    }

# Cybersecurity tips
def get_cybersecurity_tips():
    tips = [
        "Use a strong, unique password for every service.",
        "Enable 2FA whenever possible.",
        "Avoid clicking suspicious links.",
        "Keep your software and OS updated.",
        "Back up your important data regularly."
    ]
    return random.choice(tips)

# ChatGPT API Call for Natural Conversation
def chatgpt_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use the latest available model
        prompt=prompt,
        temperature=0.7,
        max_tokens=150
    )
    return response.choices[0].text.strip()

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")

    # If it's related to PBC or crypto or astro or hack, use Padke Boss's style
    if "pbc" in user_input.lower():
        return jsonify(get_pbc_prediction())
    elif "crypto" in user_input.lower():
        return jsonify(get_crypto_prediction())
    elif "astro" in user_input.lower():
        return jsonify(get_astronomical_data())
    elif "hack" in user_input.lower():
        return jsonify({"tip": get_cybersecurity_tips()})
    else:
        # Use ChatGPT for generic conversation
        response = chatgpt_response(user_input)
        return jsonify({"response": response})

@app.route("/status", methods=["GET"])
def status():
    return jsonify({"status": "Padke Boss is online."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True, use_reloader=False)
