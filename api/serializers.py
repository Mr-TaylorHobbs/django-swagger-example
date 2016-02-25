from rest_framework import serializers

from api.models import Swag

class SwagSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Swag
        fields = ('id', 'name', 'is_dj')

