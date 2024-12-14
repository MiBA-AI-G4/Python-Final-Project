"""Web service that accepts a text and returns its language code."""

from flask import Flask
from flask import request
import langdetect as ld
import os

app = Flask(__name__)


@app.route("/")
def hello_world():
    """Returns a description of the web service."""
    return "Hello!! This is an app to detect the language of a document"


@app.route("/detect", methods=['GET'])
def detect():
    """Identifies the language of the text."""
    query = request.args.get('text')
    language = ld.detect(query)
    return language

@app.route("/instance", methods=['GET'])
def instance():
    """Returns the first directory entry in /var/lib/cloud/instances/."""
    dirs = os.listdir('/var/lib/cloud/instances/')
    return dirs[0]  # Return the first directory in the list


if __name__ == "__main__":
    app.run()

