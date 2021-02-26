import json


def test_get_audiotype(app, client):
    del app
    response = client.get('/1/')
    assert response.status_code == 200


def test_get_audio(app, client):
    del app
    response = client.get('/1/1')
    assert response.status_code == 200