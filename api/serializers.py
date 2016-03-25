from rest_framework_json_api import serializers

from api.models import Swag


class SwagSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Swag
        fields = ('id', 'name', 'is_dj')
