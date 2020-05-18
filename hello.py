"""Simple python Flask app to demonstrate running on Cloud Foundry"""
from flask import Flask
import os

app = Flask(__name__)

port = int(os.getenv("PORT"))  # CF provides the port thru the PORT environment variable

@app.route('/')  # This is the main route for the web page
def hello():  # The name of this function is arbitrary
    return 'Hello World! I am running on port ' + str(port)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
