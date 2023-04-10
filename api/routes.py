from flask import jsonify, render_template
from api import app

@app.route('/report')
def report():
    # Render the base.html template, which includes the content of report.html
    return render_template('report.html')
