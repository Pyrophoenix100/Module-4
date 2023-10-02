from requests import get
loc = get('https://ipapi.co/json/')
res = loc.json()
if (res['error']):
    print("The API has Rate Limited")
else:
    print ("Your IP is: " + loc.json()['ip'])