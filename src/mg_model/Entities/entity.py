from mongoengine import Document, StringField, ListField
import uuid


class Entity(Document):
    name = StringField(max_length=100)
    id = StringField(primary_key=True, default=str(uuid.uuid4()), editable=False)
    position = ListField(FloatField(), default=[0.0, 0.0, 0.0])
    meta = {"allow_inheritance": True}
