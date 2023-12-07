from mongoengine import FloatField, ListField
from ...Entities import InstancedEntity


class Actor(InstancedEntity):
    # Velocity of Actor
    velocity = ListField(FloatField(), default=[0.0, 0.0, 0.0])
    meta = {"allow_inheritance": True}
