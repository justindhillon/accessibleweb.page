import flask
import requests
from flask import request

app = flask.Flask(__name__)

def add_accessibility_settings(html):
    with open('templates/button.html', 'r') as file:
        settings_html = file.read()
    html_with_settings = html + settings_html
    return html_with_settings

def accessibility_settings(url):
    response = requests.get(url)
    response.encoding = response.apparent_encoding
    with_accessibility_settings = add_accessibility_settings(response.text)
    return with_accessibility_settings

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
