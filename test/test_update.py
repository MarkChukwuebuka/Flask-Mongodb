import json


def test_update_audio(app, client):
    data = {
    "name":"rush",
    "duration":500,

    "uploaded_time":"Fri, 26 Mar 2021 16:58:16 GMT"}

    response = client.put('/1/22/', headers={"Content-Type": "application/json"}, data=data)

    assert 200 == response.status_code

