import binascii
import os

from mongoengine import Document, fields, CASCADE
from mongoengine.queryset import queryset_manager
from django.utils import timezone
from mg_model.user import User
from mg_model.Serializers import TokenSerializer


class Token(Document):
    # TODO - Add time to live on key https://docs.mongoengine.org/guide/defining-documents.html#time-to-live-ttl-indexes
    key = fields.StringField(required=True)
    user = fields.ReferenceField(User, reverse_delete_rule=CASCADE)
    created = fields.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super(Token, self).save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key

    @queryset_manager
    def get(self, queryset, user):
        token = queryset.get(user=user)
        return TokenSerializer(token)
