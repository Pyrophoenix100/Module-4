import requests
def test_call():
    assert "Your IP is:" in requests.get("http://module-4-silk.vercel.app/api").text