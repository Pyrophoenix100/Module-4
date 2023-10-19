import requests
def test_call():
    assert "Your IP is:" in requests.get("http://127.0.0.1").text