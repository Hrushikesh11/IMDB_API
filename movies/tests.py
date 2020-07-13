from django.test import TestCase
from django.contrib.auth.models import User
from .models import movies


class MoviesTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(username='testuser1', password='abc123')
        testuser1.save()

        test_post = movies.objects.create(director=testuser1, name='Star Wars', imdb_score=9.9, popularity=7.7, genres="action")
        test_post.save()

    def test_movie_content(self):
        movie = movies.objects.get(id=1)

        director = f'{movies.director}'
        imdb_score = f'{movies.imdb_score}'
        name = f'{movies.name}'
        genres = f'{movies.genres}'
        popularity = f'{movies.popularity}'
        self.assertEqual(director, 'Christopher Nolan')
        self.assertEqual(imdb_score, 'Imdb Score')
        self.assertEqual(name, 'Name')
        self.assertEqual(genres, 'Genres')
        self.assertEqual(popularity, 'Popularity')

