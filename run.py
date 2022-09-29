from flask import Flask
from datetime import datetime
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def current_time_GMT():
    CurrTimeGMT = datetime.now().strftime("%H:%M:%S")
    return "World's Current Time in GMT : " + CurrTimeGMT
    
app.run(host='0.0.0.0',
        port=8080,
        debug=True)
