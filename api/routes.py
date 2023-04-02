from flask import jsonify, render_template
from api import app

@app.route('/')
def index():
    # Render the base.html template, which includes the content of report.html
    return render_template('base.html')
