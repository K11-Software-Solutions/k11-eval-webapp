def test_profile_requires_login(client):
    r = client.get('/profile')
    assert r.status_code == 302  # redirect to login
