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

@app.route("/", defaults={"path": ""})
@app.route('/<path:path>', methods=["GET"])
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

        print("https://www.google.com/" + parts[3] + "/" + parts[4])
        response = requests.get("https://www.google.com/" + parts[3] + "/" + parts[4])
        return response.content
    
    return "Invalid URL"

if __name__ == "__main__":
    app.run()
