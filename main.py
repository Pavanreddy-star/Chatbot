from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse
from twilio_handler import send_whatsapp_message
from dialogflow import get_dialogflow_response

app = Flask(__name__)

@app.route('/')
def home():
    return "WhatsApp Chatbot is running!"

@app.route('/webhook/whatsapp', methods=['POST'])
def whatsapp_webhook():
    # Get the incoming message from WhatsApp
    incoming_msg = request.values.get('Body', '').strip()  # Message sent by the user
    sender = request.values.get('From', '')  # Phone number of the user sending the message
    
    # Log the incoming message and sender's number (for debugging)
    print(f"Message from {sender}: {incoming_msg}")
    
    # Process the message with Dialogflow and get the response
    response_text = get_dialogflow_response(incoming_msg)
    
    # Send the response back to the user on WhatsApp
    resp = MessagingResponse()
    resp.message(response_text)
    
    return str(resp)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
