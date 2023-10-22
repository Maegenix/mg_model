from mongoengine import Document, MapField, StringField
from bson.objectid import ObjectId
import uuid


# def to_json(doc, **kwargs):
#     unwrapped = {}
#     nested_dict = {}
#     unwrapped["model_type"] = doc.__class__.__name__
#     for k in dict(doc._fields).keys():
#         try:
#             if isinstance(doc[k], (InstancedEntity, Entity, User, Actor, Player)):
#                 unwrapped[k] = to_json(doc[k])
#             elif isinstance(doc[k], ObjectId):
#                 unwrapped[k] = doc[k].__str__()
#             elif isinstance(doc[k], dict):
#                 for p, l in doc[k].items():
#                     nested_dict[p] = to_json(l)
#                 unwrapped[k] = nested_dict
#             else:
#                 unwrapped[k] = doc[k]
#             # Add Arbitrary values to model packet data
#             for r, v in kwargs.items():
#                 if k == r:
#                     merged = dict()
#                     merged.update(unwrapped[k])
#                     merged.update(v)
#                     unwrapped[k] = merged
#         except Exception as e:
#             print("\n", e)
#     return json.dumps(unwrapped) if not dict else unwrapped


class Island(Document):
    entities = MapField(field=StringField(max_length=100))
    id = StringField(primary_key=True, default=str(uuid.uuid4()), editable=False)
    name = StringField(max_length=100)
