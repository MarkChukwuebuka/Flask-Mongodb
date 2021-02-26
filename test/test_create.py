import json



def test_create_audio(app, client):
    del app
    data = {"Id":102,
    "name":"rush",
    "duration":365,
    "audiotype":"2",
    "uploaded_time":"Fri, 26 Mar 2021 17:58:16 GMT",
    "host":"Mark",
    "participants": ["ark", "Joan"]}


    response = client.post('/', headers={"Content-Type": "application/json"}, data=data)

    assert 200 == response.status_code


