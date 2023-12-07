from mongoengine import StringField, FloatField
from . import Entity


class InstancedEntity(Entity):
    # Position of Entity
    x = FloatField(default=0.0)
    y = FloatField(default=0.0)
    z = FloatField(default=0.0)
    # Position of Entity
    map_id = StringField(default="0cbf86a9-adc8-4aed-bbed-e8ce9a38df79", max_length=100)
    meta = {"allow_inheritance": True}
