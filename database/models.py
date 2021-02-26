from .db import db
import datetime



# def val_list(x):
#     for i in x:
#         if len(i) > 100:
#             raise ValidationError("Participant can't contain more than 100 characters")


class MyDateTimeField(db.DateTimeField):

    def validate(self, value):
        super(MyDateTimeField, self).validate(value)
        if datetime.datetime.strptime(value, "%a, %d %b %Y %H:%M:%S %Z") < datetime.datetime.now():
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

    id = db.IntField(required = True, unique=True)
    name = db.StringField(required = True, max_length=100)
    duration = db.IntField(required = True, min_value = 1)
    uploaded_time = MyDateTimeField(required = True)
    host = db.StringField(required = True, max_length=100)
    participants = db.ListField(db.StringField())
    audiotype = db.StringField(max_length=10, choices=audiotype, required = True)


class AudioBook(db.Document):

    id = db.IntField(required = True, unique=True)
    title = db.StringField(required = True, max_length=100)
    author = db.StringField(required = True, max_length=100)
    narrator = db.StringField(required = True, max_length=100)
    duration = db.IntField(required = True, min_value = 1)
    uploaded_time = MyDateTimeField(required=True)
    audiotype = db.StringField(max_length=10, choices=audiotype, required = True)