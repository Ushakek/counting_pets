import time
import uuid

from django.db import models
from rest_framework import fields


class AllPets(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    name = models.CharField(max_length=100)
    age = models.FloatField(default=0)
    type = models.CharField(max_length=50)
    photos = models.ImageField(null=True, upload_to=f'images_{uuid.uuid4()}')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
