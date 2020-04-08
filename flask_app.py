""" Basic Flask app to send a message using an url """
from flask import Flask, request
from messaging import send_message
app = Flask(__name__)

@app.route('/send', methods=['GET'])
def send():
    """
    Sends a message to a given phone number.
    
    Returns a result message indicating if the 
    message was properly sent.
    """
    # Get the number and the message from the url
    number = request.args.get('number')
    message = request.args.get('message')
    # Send the message and return the result message
    return send_message(number, message)

if __name__ == "__main__":
    app.run()