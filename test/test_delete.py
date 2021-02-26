import json

def test_delete_audio(app, client):
        
    response = client.delete('/3/2/')
    assert response.status_code == 204