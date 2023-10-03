from requests import get
from http.server import BaseHTTPRequestHandler
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        loc = get('https://ipapi.co/json/')
        res = loc.json()
        if ('error' in res):
            out = "The API has Rate Limited"
        else:
            out = "Your IP is: " + loc.json()['ip']
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(out.encode('utf-8'))
        return