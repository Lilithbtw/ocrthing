from flask import Flask, render_template, request
from flask_dropzone import Dropzone
import os

app = Flask(__name__, template_folder='templates')
port = 8080


@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run("0.0.0.0", port, debug=True)