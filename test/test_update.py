import json


def test_update_audio(app, client):
    data = {
    "name":"rush",
    "duration":365,
    "audiotype":"2",
    "uploaded_time":"Fri, 26 Mar 2021 16:58:16 GMT",
    "host":"Mark",
    "participants": ["ark", "Joan"]}

    response = client.put('/1/44/', headers={"Content-Type": "application/json"}, data=data)

    self.assertEqual(200, response.status_code)

