import api.index as api
a = api.handler()
def test_call():
    assert "Your IP is:" in a.do_GET()