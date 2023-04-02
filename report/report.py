from data.database import Database
from datetime import datetime, timedelta
from flask import Flask, render_template
from pytz import timezone

app = Flask(__name__)

@app.route('/')
def generate_report():
    # Connect to database and fetch data
    db = Database(dbname='mydatabase', user='myusername', password='mypassword', host='localhost', port=5432)
    data = db.query('SELECT * FROM store_status')

    # Calculate uptime and downtime for each store
    uptime = {}
    downtime = {}
    for row in data:
        store_id = row['store_id']
        status = row['status']
        timestamp = row['timestamp']

        # Check if store is open during the timestamp
        store_hours = db.query(f"SELECT * FROM store_hours WHERE store_id = '{store_id}'")[0]
        timezone_name = db.query(f"SELECT * FROM store_timezone WHERE store_id = '{store_id}'")[0]['timezone']
        timezone_obj = timezone(timezone_name)
        opening_time = datetime.strptime(store_hours['opening_time'], '%H:%M:%S').time()
        closing_time = datetime.strptime(store_hours['closing_time'], '%H:%M:%S').time()
        local_timestamp = timezone_obj.localize(timestamp)
        local_opening_time = timezone_obj.localize(datetime.combine(local_timestamp.date(), opening_time))
        local_closing_time = timezone_obj.localize(datetime.combine(local_timestamp.date(), closing_time))
        if local_timestamp >= local_opening_time and local_timestamp <= local_closing_time:
            # Store is open
            if store_id not in uptime:
                uptime[store_id] = timedelta(0)
            uptime[store_id] += timedelta(minutes=5) # Assuming polls are done every 5 minutes
        else:
            # Store is closed
            if store_id not in downtime:
                downtime[store_id] = timedelta(0)
            downtime[store_id] += timedelta(minutes=5) # Assuming polls are done every 5 minutes

    # Generate report using Flask's built-in template rendering engine
    eastern = timezone('US/Eastern')
    current_time = datetime.now(tz=eastern)
    return render_template('report.html', current_time=current_time, uptime=uptime, downtime=downtime)

if __name__ == '__main__':
    app.run()
