import flask
import requests
app = flask.Flask(__name__)
@app.route('/api/loc')
def main(path):
    loc = requests.get('https://ipapi.co/json/')
    res = loc.json()
    if ('error' in res):
        out = "The API has Rate Limited you"
    else:
        out = "Your location is " + res['city'] + ", " + res['region'] + " " + res['country']
    return out
if __name__ == '__main__':
    app.run(debug=True, port=8002)