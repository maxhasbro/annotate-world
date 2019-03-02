from __future__ import unicode_literals

import uuid
from django.db import models


class Continent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    lat_center = models.CharField(max_length=200)
    long_center = models.TextField()

    def __str__(self):
        return self.name

class Country(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    lat_center = models.CharField(max_length=200)
    country = models.ForeignKey('Continent', on_delete=models.CASCADE)
    long_center = models.TextField()
    basic_info = models.TextField()

    def __str__(self):
        return self.name

class City(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    lat_center = models.CharField(max_length=200)
    long_center = models.TextField()
    basic_info = models.TextField()

    def __str__(self):
        return self.name