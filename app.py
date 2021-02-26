from flask import Flask, jsonify, request, Response
from database.models import Song, Podcast, AudioBook
from database.db import initialize_db
import json


app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host' : 'mongodb://localhost/web_api'
}


@app.route('/', methods=['POST'])
def create():
    body = request.get_json(force=True)
    if body['audiotype'] == '1':
        audio = Song(**body).save()
    elif body['audiotype'] == '2':
        audio = Podcast(**body).save()
    else:
        audio = AudioBook(**body).save()
    
    id = audio.uploaded_time
    
    return {'success' : '200 Ok'}
    # return id


@app.route('/<audiotype>/')
def get_audio_type(audiotype):
    if audiotype == "1":
        audio = Song.objects().to_json()
    elif audiotype == "2":
        audio = Podcast.objects().to_json()
    elif audiotype  == "3":
        audio = AudioBook.objects().to_json()
    else:
        audio = "Invalid Audio Type"

    return {'success': '200 Ok'}
    


@app.route('/<audiotype>/<id>/')
def get_audio(audiotype, id):
    if audiotype == "1":
        audio = Song.objects.get(Id=id).to_json()
    elif audiotype == "2":
        audio = Podcast.objects.get(Id=id).to_json()
    elif audiotype  == "3":
        audio = AudioBook.objects.get(Id=id).to_json()
    else:
        audio = "Invalid Audio Type"
    
    # return Response(mimetype="application/json", status=200)
    return {'success' : '200 Ok'}


    
@app.route('/<audiotype>/<id>/', methods=['PUT'])
def update_audio(audiotype, id):
    body = request.get_json()

    if audiotype == "1":
        audio = Song.objects.get(Id=id).update(**body)
    elif audiotype == "2":
        audio = Podcast.objects.get(Id=id).update(**body)
    elif audiotype  == "3":
        audio = AudioBook.objects.get(Id=id).update(**body)
    else:
        audio = "Invalid Audio Type"
    
    
    return {'success' : '200 Ok'}


@app.route('/<audiotype>/<id>/', methods=['DELETE'])
def delete_audio(audiotype, id):
    
    if audiotype == "1":
        audio = Song.objects.get(id=id).delete()
    elif audiotype == "2":
        audio = Podcast.objects.get(Id=id).delete()
    elif audiotype  == "3":
        audio = AudioBook.objects.get(Id=id).delete()
    else:
        audio = "Invalid Audio Type"
    
    return {'success' : '200 Ok'}

    


initialize_db(app)

app.run(debug=True)
