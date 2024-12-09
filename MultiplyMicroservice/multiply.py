from flask import Flask, request, jsonify
import os

app = Flask(__name__)
PORT = os.getenv('PORT', 8080)

@app.route('/', methods=['GET'])
def home():
    return jsonify({'response': 'Multiply two numbers by passing them in the URL e.g. http://localhost:8080/10/20'}), 200

@app.route('/<int:number1>/<int:number2>', methods=['GET'])
def multiply(number1, number2):
    return jsonify({'response': number1 * number2}), 200

if __name__ == '__main__':
    app.run(port=PORT)