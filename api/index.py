import flask
import requests
app = flask.Flask(__name__)
EOL = "<br>"
@app.route('/api')
def help():
    out = "DEVNET API v0.0.1" + EOL
    out += "/api/ip -- Get your public ip" + EOL
    out += "/api/loc -- Get your IP geolocation" + EOL
    return out