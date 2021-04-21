from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
  return '<h1><center>This is a Demo Flask Application</center></h1>'

FLASK_PORT = os.getenv('FLASK_PORT',5000)

app.run(host='0.0.0.0', port=int(FLASK_PORT))
