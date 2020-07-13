from django.contrib.auth.models import User
from rest_framework import serializers
from .models import movies


class MovieSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = movies
        fields = ('popularity', 'director', 'genres', 'imdb_score', 'name', 'owner')


class UserSerializer(serializers.ModelSerializer):
    movies = serializers.PrimaryKeyRelatedField(many=True,
                                                queryset=movies.objects.all())

    class Meta:
        movies = User
        fields = ('id', 'username', 'movies')
