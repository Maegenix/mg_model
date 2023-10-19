from mongoengine import Document, StringField, DateTimeField, BooleanField, FloatField
import uuid


class Entity(Document):
    name = StringField(max_length=100)
    id = StringField(primary_key=True, default=str(uuid.uuid4()), editable=False)
    meta = {"allow_inheritance": True}


class InstancedEntity(Entity):
    # Position of Entity
    x = FloatField(default=0.0)
    y = FloatField(default=0.0)
    z = FloatField(default=0.0)
    # Position of Entity
    map_id = StringField(default="0cbf86a9-adc8-4aed-bbed-e8ce9a38df79", max_length=100)
    meta = {"allow_inheritance": True}
