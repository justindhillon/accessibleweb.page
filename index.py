import flask
import requests
import dotenv
from flask import request

app = flask.Flask(__name__)

def accessibility_settings(url):
    response = requests.get(url)
    response.encoding = response.apparent_encoding
    with open('templates/button.html', 'r') as file:
        button = file.read()
    
    return response.text + button

@app.route('/', methods=['GET', 'POST'])
def main_page(): 
    return flask.render_template('index.html')

@app.route('/', defaults={'path': ''})
@app.route('/<path>')
def redirect_to_API_HOST(path):
    # Redirects if url is a webpage
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
    
    res = requests.request(  # ref. https://stackoverflow.com/a/36601467/248616
        method          = request.method,
        url             = request.url.replace(request.host_url, f'{API_HOST}/'),
        headers         = {k:v for k,v in request.headers if k.lower() != 'host'}, # exclude 'host' header
        data            = request.get_data(),
        cookies         = request.cookies,
        allow_redirects = False,
    )

    #region exlcude some keys in :res response
    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']  #NOTE we here exclude all "hop-by-hop headers" defined by RFC 2616 section 13.5.1 ref. https://www.rfc-editor.org/rfc/rfc2616#section-13.5.1
    headers          = [
        (k,v) for k,v in res.raw.headers.items()
        if k.lower() not in excluded_headers
    ]
    #endregion exlcude some keys in :res response

    response = Response(res.content, res.status_code, headers)
    return response

app.run()
