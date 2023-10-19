from rest_framework_mongoengine.serializers import DocumentSerializer
from mg_model.user import User


class TokenSerializer(DocumentSerializer):
    class Meta:
        model = User
        depth = 2
