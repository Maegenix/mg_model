import json
from bson.objectid import ObjectId


class Serializer:
    def __init__(self, *models):
        self.models = models

    def serialize(self, doc, **kwargs):
        unwrapped = {}
        nested_dict = {}
        unwrapped["model_type"] = doc.__class__.__name__
        for k in dict(doc._fields).keys():
            try:
                if isinstance(doc[k], (*self.models,)):
                    unwrapped[k] = self.serialize(doc[k])
                elif isinstance(doc[k], ObjectId):
                    unwrapped[k] = doc[k].__str__()
                elif isinstance(doc[k], dict):
                    for p, l in doc[k].items():
                        nested_dict[p] = self.serialize(l)
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
