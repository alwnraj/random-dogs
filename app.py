from flask import Flask, render_template
import requests
import json 

app = Flask(__name__)

def get_meme():
    url = "https://dog.ceo/api/breeds/image/random"
    response = json.loads(requests.request("GET",url).text)
    meme_large = response["message"]
    return meme_large

@app.route("/")
def index():
    meme_large = get_meme()
    return render_template("index.html", meme_large=meme_large)