import flask
import requests
app = flask.Flask(__name__)
@app.route('/api/', defaults={'path': ''})
@app.route('/api/<path:path>')
def main(path):
    if (path == "ip"):
        loc = requests.get('https://ipapi.co/json/')
        res = loc.json()
        if ('error' in res):
            out = "The API has Rate Limited you"
        else:
            out = "Your IP is: " + loc.json()['ip']
        return out
    elif (path == "loc"):
        loc = requests.get('https://ipapi.co/json/')
        res = loc.json()
        if ('error' in res):
            out = "The API has Rate Limited you"
        else:
            out = "Your location is " + res['city'] + ", " + res['region'] + " " + res['country']
        return out
    else:
        return path + " was not found on the server."
if __name__ == '__main__':
    app.run(debug=True, port=8002)