from mongoengine import FloatField, ReferenceField, StringField, CASCADE, IntField
from . import Actor
from ...melee import Melee
import uuid
from ...user import User


class Player(Actor):
    meta = {"allow_inheritance": True}
    health = FloatField(default=100.0)
    level = IntField(default=1)
    experience = FloatField(default=0.0)
    user = ReferenceField(User, reverse_delete_rule=CASCADE, required=True)
    reference = StringField(default=f"Player/{uuid.uuid4()}")
    resource = StringField(default="Player")
    melee = StringField(default="Melee/default")
