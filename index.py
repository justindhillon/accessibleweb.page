import flask
import requests
import urllib.parse
from flask import request
import re

app = flask.Flask(__name__)

def gethtml(html, url):
    print(html);
    split_url = urllib.parse.urlsplit(url)
    html = html.replace('src="/', 'src="https://www.' + split_url.netloc + "/")
    html = html.replace("src='/", "src='https://www." + split_url.netloc + "/")
    html = html.replace('herf="/', 'herf="https://www.' + split_url.netloc + "/")
    html = html.replace("herf='/", "herf='https://www." + split_url.netloc + "/")
    html = html.replace("url(/", "url(https://www." + split_url.netloc + "/")
    html = html.replace('u="/', 'u="https://www.' + split_url.netloc + "/")
    html = html.replace("u='/", "u='https://www." + split_url.netloc + "/")
    return html

def accessibility_settings(url):
    response = requests.get(url)
    response.encoding = response.apparent_encoding
    with open('templates/button.html', 'r') as file:
        button = file.read()
    
    return gethtml(response.text, url) + button

@app.route('/', methods=['GET', 'POST'])
def main_page(): 
    return flask.render_template('index.html')

# Code from https://github.com/wasi-master/13ft
@app.route("/", defaults={"path": ""})
@app.route('/<path:path>', methods=["GET"])
def get_article(path):
    full_url = request.url
    parts = full_url.split('/',4)
    if len(parts) >= 5:
        actual_url = 'https://' + parts[4].lstrip('/')
        try:
            return accessibility_settings(actual_url)
        except requests.exceptions.RequestException as e:
            return str(e), 400
        except e:
            raise e
    else:
        return "Invalid URL", 400

app.run()
