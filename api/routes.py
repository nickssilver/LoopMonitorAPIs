from api import app
from flask import jsonify

@app.route('/')
def index():
    return jsonify({'message': 'Hello, there'})
