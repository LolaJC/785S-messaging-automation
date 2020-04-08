from flask import Flask, request
from messaging import send_message
app = Flask(__name__)

@app.route('/send', methods=['GET'])
def send():
    number = request.args.get('number')
    message = request.args.get('message')
    return send_message(number, message)