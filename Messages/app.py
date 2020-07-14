from flask import Flask
import json

app = Flask(__name__)

@app.route('/messages')
def messages():
    message = {'message': 'Mensajes para usuarios',}
    return json.dumps(message)

@app.route('/messages/<id>')
def messages_id(id):
    message = {'message': 'Estado del usuario', 'status': 'authorized', 'user': id}
    return json.dumps(message)

if __name__ == "__main__":
    app.run(port=5002)