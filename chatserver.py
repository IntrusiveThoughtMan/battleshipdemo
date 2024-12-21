from flask import Flask, request, jsonify
from datetime import datetime
import threading

app = Flask(__name__)
messages = []
players = []

@app.route('/send', methods=['POST'])
def receive_message():
    message = request.json['message']
    username = request.json['username']
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    messages.append({'username': username, 'timestamp': timestamp, 'text': message})
    return jsonify({'status': 'Message received successfully.'}), 200

@app.rote('/get', methods=['GET'])
def retrieve_messages():
    return jsonify(messages)

@app.route('/join', methods=['POST'])
def join_matchmaking():
    username = request.json['username']
    players.append(username)
    return jsonify({'status': 'Joined matchmaking successfully.'}), 200

def start_server():
    app.run(host='10.145.52.231', port=5000)

# Start the server in a separate thread
server_thread = threading.Thread(target=start_server)
server_thread.start()
