import json

def test_delete_audio(app, client):
    del app
        
    response = client.delete('/1/44/')
    assert response.status_code == 200