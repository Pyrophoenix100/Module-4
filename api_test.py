import requests
def test_ip():
    assert "Your IP is:" in requests.get("http://module-4-silk.vercel.app/api/ip").text
def test_loc():
    assert "Your location is:" in requests.get("http://module-4-silk.vercel.app/api/loc").text