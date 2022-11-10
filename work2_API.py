from flask import Flask, render_template, request
import json
import requests

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/post", methods=["POST"])
def post():
    choice = request.form["animal"]
    if choice == "cat":
        r = requests.get("https://api.thecatapi.com/v1/images/search")
        partner = json.loads(r.text)[0]["url"]
    elif choice == "dog":
        r = requests.get("https://dog.ceo/api/breeds/image/random")
        partner = json.loads(r.text)["message"]
    else:
        r = requests.get("https://randomfox.ca/floof")
        partner = json.loads(r.text)["image"]
    return render_template("post.html", partner=partner)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
