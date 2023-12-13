from mongoengine import Document, MapField, StringField
import uuid


class Island(Document):
    default = str(uuid.uuid4())
    entities = MapField(field=StringField(max_length=100))
    id = StringField(primary_key=True, default=default, editable=False)
    reference = StringField(primary_key=True, default=f"Island/{default}", editable=False)
    name = StringField(max_length=100)
