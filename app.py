from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

greetings = {
    "English": "Hello World",
    "French": "Bonjour le monde",
    "Hindi": "Namastey sansar"
}

@app.route('/hello', methods=['GET'])
def hello_world():
    language = request.args.get('language', 'English')
    message = greetings.get(language, 'Please select a language.')
    return message

@app.route('/')
def home():
    return "Homepage"


if __name__ == '__main__':
    app.run(debug=True)
