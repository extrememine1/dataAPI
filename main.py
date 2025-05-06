from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_data():
    return jsonify({'content': 'hello'})

app.run()
