from flask import Flask, render_template
import img

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("pillow_start.html")


@app.route("/img")
def image():
    img.color()
    return render_template("img.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
