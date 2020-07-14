from flask import Flask, request
from db_utils import add_message
import json

mensajes = [
    {
        'message': 'hello',
        'status': 'OK',
        'user': 'admin'
    },
    {
        'message': 'Who is it?',
        'status': 'NOT OK',
        'user': 'user1'
    },
    {
        'message': 'Hi!',
        'status': 'OK',
        'user': 'user2'
    },
    {
        'message': 'Ein Fremder',
        'status': 'NOT OK',
        'user': 'user3'
    }
]

app = Flask(__name__)

@app.route('/messages')
def messages():
    return json.dumps(mensajes)

@app.route('/messages/<int:id>')
def messages_id(id):
    return json.dumps(mensajes[id])

@app.route('/messages/add', methods=['GET', 'POST'])
def message_add():
    document_id = add_message(request.json)
    response = {'document_id' : str(document_id)}
    return response
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002, debug=True)