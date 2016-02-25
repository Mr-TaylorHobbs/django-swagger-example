from django.db import models

class Swag(models.Model):
    name = models.CharField(max_length=50)
    is_dj = models.BooleanField(default=False)
