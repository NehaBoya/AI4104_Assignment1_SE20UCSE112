import requests

# Send a message to the server
send_url = "http://167.71.232.99:2340/api/messages"
send_data = {"message": "Hello Neha"}
send_response = requests.post(send_url, json=send_data)
print(send_response.text)

# Receive a message from the server
receive_url = "http://167.71.232.99:2340/api/send"
receive_response = requests.get(receive_url)
receive_data = receive_response.json()

if 'message' in receive_data:
    received_message = receive_data['message']
    print(f"Received message from server: {received_message}")
else:
    print("No message received from the server.")


