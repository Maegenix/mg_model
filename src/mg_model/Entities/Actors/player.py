from mongoengine import FloatField, ReferenceField, CASCADE, IntField
from . import Actor
from ...user import User


class Player(Actor):
    meta = {"allow_inheritance": True}
    health = FloatField(default=100.0)
    level = IntField(default=1)
    experience = FloatField(default=0.0)
    user = ReferenceField(User, reverse_delete_rule=CASCADE)
