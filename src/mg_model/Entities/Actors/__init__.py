from mongoengine import FloatField
from .. import InstancedEntity


class Actor(InstancedEntity):
    # Velocity of Actor
    v_x = FloatField(default=0.0)
    v_y = FloatField(default=0.0)
    v_z = FloatField(default=0.0)
    meta = {"allow_inheritance": True}


class Player(Actor):
    meta = {"allow_inheritance": True}
    health = 100
