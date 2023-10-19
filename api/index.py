import flask
import requests
app = flask.Flask(__name__)
@app.route("/get/ip")
def getIP():
    loc = requests.get('https://ipapi.co/json/')
    res = loc.json()
    if ('error' in res):
        out = "The API has Rate Limited"
    else:
        out = "Your IP is: " + loc.json()['ip']
    return out