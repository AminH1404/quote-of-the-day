from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

quotes = [
    "Do not watch the clock. Do what it does. Keep going.",
    "Believe you can and you're halfway there.",
    "The only way to do great work is to love what you do.",
    "You miss 100% of the shots you don't take.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts."
]

@app.route('/api/quote', methods=['GET'])
def get_quote():
    return jsonify({"quote": random.choice(quotes)})

if __name__ == '__main__':
    app.run(debug=True)
