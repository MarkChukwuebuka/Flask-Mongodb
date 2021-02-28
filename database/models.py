from .db import db
import datetime
import pytz

class MyParticipantsField(db.ListField):


    def validate(self, x):
        super(MyParticipantsField, self).validate(x)
        x = list(x)
        for i in x:
            if len(i) > 100:
                self.error("Participant can't contain more than 100 characters")

  
utc=pytz.UTC

class MyDateTimeField(db.DateTimeField):

    def validate(self, value):
        super(MyDateTimeField, self).validate(value)
        if type(value) == str:
            if datetime.datetime.strptime(value, "%d-%m-%Y %H:%M:%S") < datetime.datetime.utcnow():
                self.error("Your DateTime cannot be in the past")
        else:
             if value < datetime.datetime.now(value.tzinfo):
                self.error("Your DateTime cannot be in the past")



audiotype = (('1', 'Song'),
        ('2', 'Podcast'),
        ('3', 'Audiobook'))

class Song(db.Document):


    Id = db.IntField(required=True, unique=True)
    name = db.StringField(required = True, max_length=100)
    duration = db.IntField(required = True, min_value = 1)
    uploaded_time = MyDateTimeField(required=True)
    audiotype = db.StringField(max_length=10, choices=audiotype, required=True)


class Podcast(db.Document):

    Id = db.IntField(required = True, unique=True)
    name = db.StringField(required = True, max_length=100)
    duration = db.IntField(required = True, min_value = 1)
    uploaded_time = MyDateTimeField(required = True)
    host = db.StringField(required = True, max_length=100)
    participants = MyParticipantsField()
    audiotype = db.StringField(max_length=10, choices=audiotype, required = True)


class AudioBook(db.Document):

    Id = db.IntField(required = True, unique=True)
    title = db.StringField(required = True, max_length=100)
    author = db.StringField(required = True, max_length=100)
    narrator = db.StringField(required = True, max_length=100)
    duration = db.IntField(required = True, min_value = 1)
    uploaded_time = MyDateTimeField(required=True)
    audiotype = db.StringField(max_length=10, choices=audiotype, required = True)