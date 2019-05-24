from __future__ import unicode_literals

import uuid
from django.db import models


class Continent(models.Model):
    name = models.CharField(max_length=60)
    latitude_center = models.FloatField()
    longitude_center = models.FloatField()

    def __str__(self):
        return self.name

    def to_json(self):
        continent_info = {
            "id": self.id,
            "name": self.name,
            "latitude_center": self.latitude_center,
            "longitude_center": self.longitude_center
        }
        return continent_info

class Country(models.Model):
    name = models.CharField(max_length=60)
    latitude_center = models.FloatField()
    longitude_center = models.FloatField()
    continent = models.ForeignKey('Continent', on_delete=models.CASCADE)
    basic_info = models.TextField()

    def __str__(self):
        return self.name

    def to_json(self):
        country_info = {
            "id": self.id,
            "name": self.name,
            "continent_id": self.continent.id,
            "latitude_center": self.latitude_center,
            "longitude_center": self.longitude_center,
            "basic_info": self.basic_info
        }
        return country_info

class City(models.Model):
    name = models.CharField(max_length=60)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    latitude_center = models.FloatField()
    longitude_center = models.FloatField()
    basic_info = models.TextField()

    def __str__(self):
        return self.name

    def to_json(self):
        city_info = {
            "id": self.id,
            "name": self.name,
            "country_id": self.country.id,
            "latitude_center": self.latitude_center,
            "longitude_center": self.longitude_center,
            "basic_info": self.basic_info
        }
        return city_info

