from mongoengine import Document, StringField
import uuid


class Entity(Document):
    name = StringField(max_length=100)
    id = StringField(primary_key=True, default=str(uuid.uuid4()), editable=False)
    meta = {"allow_inheritance": True}
