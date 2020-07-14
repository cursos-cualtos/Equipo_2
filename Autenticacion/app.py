from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def index():
    message = {'message': 'Welcome to the app!'}
    return json.dumps(message)

@app.route('/auth/<user>')
def index(user):
    data = ["admin", "user1", "user2", "user3"]

    if user in data:
        message = {'status':'authorized'}
    else:
        message = {'status':'unauthorized'}

    return json.dumps(message)

@app.route('/greeting/<string:name>')
def gretting_by_name(name):
    message = {'message': 'Hello ' + name}
    return json.dumps(message)

@app.route('/add', methods=['GET', 'POST'])
def add():
    return ''

if __name__ == "__main__":
    app.run(port=5001)