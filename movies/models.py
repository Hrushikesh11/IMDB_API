from django.db import models
from rest_framework import serializers


class movies(models.Model):
    popularity = models.FloatField()
    director = models.CharField(max_length=100)
    genres = models.CharField(max_length=100)
    imdb_score = models.FloatField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name