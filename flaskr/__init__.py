import os
import json

from flask import Flask
from . import functions


apiKey = os.environ.get('ALPHAVANTAGE_API_KEY')

test_config = None

# create and configure the app
app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
)

if test_config is None:
    # load the instance config, if it exists, when not testing
    app.config.from_pyfile('config.py', silent=True)
else:
    # load the test config if passed in
    app.config.from_mapping(test_config)

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

# a simple page that says hello
@app.route('/', methods=['GET'])
def index():
    currentTime = functions.printTimes()
    times = json.dumps(currentTime)
    return times

if __name__ == '__main__':
    app.run(host="0.0.0.0", poort=5000, debug=True)
