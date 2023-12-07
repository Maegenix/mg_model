from mongoengine import (
    FloatField,
    ReferenceField,
    StringField,
    CASCADE,
    IntField,
    MapField,
    BooleanField,
)
from . import Actor
import uuid
from ...user import User


class Player(Actor):
    meta = {"allow_inheritance": True}
    health = MapField(
        alive=BooleanField(default=True),
        current=FloatField(default=100),
        Capacity=IntField(default=100),
        required=True,
    )
    speed = IntField(default=1, required=True)
    strength = IntField(default=1, required=True)
    level = IntField(default=1, required=True)
    experience = FloatField(default=0.0, required=True)
    user = ReferenceField(User, reverse_delete_rule=CASCADE, required=True)
    reference = StringField(default=f"Player/{uuid.uuid4()}", required=True)
    resource = StringField(default="Player", required=True)
    melee = StringField(default="Melee/default", required=True)
