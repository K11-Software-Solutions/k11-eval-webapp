def test_status(client):
    r = client.get('/api/status')
    assert r.json == {'ok': True}
