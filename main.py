import flask
import requests

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

@app.route('/robots.txt')
@app.route('/sitemap.xml')
def static_from_root():
    return flask.send_from_directory(app.static_folder, flask.request.path[1:])

@app.route('/favicon.ico')
def favicon():
    return flask.send_from_directory(app.static_folder, 'favicon.ico')

@app.route("/", defaults={"path": ""})
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def redirect(path):
    # Redirects if url is a webpage
    full_url = flask.request.url
    parts = full_url.split('/',4)
    if len(parts) >= 5:
        if parts[3] == "http:" or parts[3] == "https:":
            actual_url = 'https://' + parts[4].lstrip('/')
            try:
                return accessibility_settings(actual_url)
            except requests.exceptions.RequestException as e:
                return str(e), 400
            except e:
                raise e

        target_url = flask.request.headers.get('Referer')[27:] + "/" + parts[3] + "/" + parts[4]

        try:
            if flask.request.method == 'GET':
                response = requests.get(target_url)
            elif flask.request.method == 'POST':
                response = requests.post(target_url, data=flask.request.get_data())
            elif flask.request.method == 'PUT':
                response = requests.put(target_url, data=flask.request.get_data())
            elif flask.request.method == 'DELETE':
                response = requests.delete(target_url)
            else:
                return 'Error: Unsupported HTTP method.'

            return response.content
        
        except requests.exceptions.RequestException as e:
            return f'Error: {e}'
    
    return "Invalid URL"

if __name__ == "__main__":
    app.run()
