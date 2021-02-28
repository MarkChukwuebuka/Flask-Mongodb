import json


def test_update_audio(app, client):
    # del app
    data = {
        "Id":47,
    "name":"rush",
    "duration": 500,
    "audiotype":"1",

    "uploaded_time":"28-02-2021 16:58:16"}

    response = client.put('/1/47/', headers={"Content-Type": "application/json"}, data=data)

    assert 400 == response.status_code

