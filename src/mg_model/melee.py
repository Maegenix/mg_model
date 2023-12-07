from mongoengine import Document, StringField, ListField
import uuid


class Melee(Document):
    name = StringField(max_length=100)
    reference = StringField(default=str(f"Melee/{uuid.uuid4()}"), editable=False)
    combos = ListField(StringField())
