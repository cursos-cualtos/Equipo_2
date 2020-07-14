from flask import Flask
import json

mensajes = [
    {
        'message': 'hello',
        'status': 'OK',
        'user': 'someone'
    },
    {
        'message': 'hello',
        'status': 'NOT OK',
        'user': 'someone'
    },
    {
        'message': 'hello',
        'status': 'OK',
        'user': 'someone'
    },
    {
        'message': 'hello',
        'status': 'NOT OK',
        'user': 'someone'
    }
]

app = Flask(__name__)

@app.route('/messages')
def messages():
    return json.dumps(mensajes)

@app.route('/messages/<int:id>')
def messages_id(id):
    return json.dumps(mensajes[id])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002, debug=True)