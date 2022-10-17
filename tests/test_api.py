def test_users(client):
    req = client.get(f"/latest/users/")
    assert req.content == []
