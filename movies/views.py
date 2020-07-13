from .serializers import MovieSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from .models import movies


class MovieList(generics.ListCreateAPIView):
    queryset = movies.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MoviesDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = movies.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
