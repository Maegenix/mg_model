import binascii
import os
import json
from bson.objectid import ObjectId
import uuid
from mongoengine import Document, fields, CASCADE
from django.utils import timezone
from .user import User


def serialize(doc, **kwargs):
    unwrapped = {}
    nested_dict = {}
    unwrapped["model_type"] = doc.__class__.__name__
    for k in dict(doc._fields).keys():
        try:
            if isinstance(doc[k], (User,)):
                unwrapped[k] = serialize(doc[k])
            elif isinstance(doc[k], ObjectId):
                unwrapped[k] = doc[k].__str__()
            elif isinstance(doc[k], dict):
                for p, l in doc[k].items():
                    nested_dict[p] = serialize(l)
                unwrapped[k] = nested_dict
            else:
                unwrapped[k] = doc[k]
            # Add Arbitrary values to model packet data
            for r, v in kwargs.items():
                if k == r:
                    merged = dict()
                    merged.update(unwrapped[k])
                    merged.update(v)
                    unwrapped[k] = merged
        except Exception as e:
            print("\n", e)
    return json.dumps(unwrapped) if not dict else unwrapped


class Token(Document):
    # TODO - Add time to live on key https://docs.mongoengine.org/guide/defining-documents.html#time-to-live-ttl-indexes
    key = fields.StringField(required=True)
    user = fields.ReferenceField(User)
    reference = fields.StringField(default=f"Token/{uuid.uuid4()}")
    resource = fields.String(default="Token")
    created = fields.DateTimeField(default=timezone.now)
    to_json = serialize

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super(Token, self).save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key
