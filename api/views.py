from rest_framework import generics
from rest_framework import mixins
from rest_framework_bulk.mixins import BulkUpdateModelMixin

from api.serializers import SwagSerializer
from api.models import Swag


class SwagEndpoint(mixins.RetrieveModelMixin, mixins.ListModelMixin, BulkUpdateModelMixin, generics.GenericAPIView):
    """
    ---
    GET:
        consumes:
            - application/vnd.api+json
        produces:
            - application/vnd.api+json
    """

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.bulk_update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_bulk_update(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_queryset(self):
        return Swag.objects.all()

    def get_serializer_class(self):
        return SwagSerializer
