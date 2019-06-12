from flask import Flask
import pytz
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! CST'

@app.route('/time')
def get_time():
    pst = pytz.timezone('US/Pacific')
    now = datetime.now(tz=pst)
    return now.strftime('%y-%m-%d %H:%M:%S PST')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')