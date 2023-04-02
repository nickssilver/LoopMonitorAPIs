from flask import Flask
from routes import *

app = Flask(__name__, template_folder='report/templates')

if __name__ == '__main__':
    app.run(debug=True)
