import json

from django import http
from rest_framework import generics
from rest_framework import mixins

from api.serializers import SwagSerializer
from api.models import Swag

class SwagEndpoint(generics.RetrieveUpdateDestroyAPIView, mixins.CreateModelMixin):

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_queryset(self):
        return Swag.objects.all()

    def get_serializer_class(self):
        return SwagSerializer
