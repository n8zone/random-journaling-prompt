from flask import Flask, jsonify
import random
import os

app = Flask(__name__)

with open("journal_prompts.txt", "r") as f:
    prompts = f.readlines()

@app.route('/')
def index():
    return "Welcome!"

@app.route('/random_prompt', methods=['GET'])
def get_random_prompt():
    return jsonify({"prompt": random.choice(prompts).strip()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))