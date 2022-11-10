from flask import Flask, render_template
from PIL import Image
import numpy as np
import random

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("pillow_start.html")

@app.route("/img")
def img():

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
