from flask import Flask, request, jsonify

app = Flask(__name__)

# Store the received messages
received_messages = []

@app.route('/api/messages', methods=['POST'])
def receive_message():
    data = request.json
    message = data.get('message', '')
    print(f"Received message: {message}")
    received_messages.append(message)
    return jsonify({"status": "Message received!"})

@app.route('/api/send', methods=['GET'])
def send_message():
    if received_messages:
        message_to_send = received_messages.pop(0)
        print(f"Sending message: {message_to_send}")
        return jsonify({"message": message_to_send})
    else:
        return jsonify({"message": "No messages to send."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2340)
