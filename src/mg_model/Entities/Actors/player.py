from mongoengine import FloatField
from . import Actor


class Player(Actor):
    meta = {"allow_inheritance": True}
    health = FloatField(default=100.0)
