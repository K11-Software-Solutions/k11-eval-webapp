def test_login(client):
    r = client.post('/login', data={'email': 'a@b.com', 'password': 'pass'})
    assert r.status_code in (200, 302)
