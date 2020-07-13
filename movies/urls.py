from django.urls import path
from .views import MovieList, MoviesDetails
from movies import views

urlpatterns = [
           path('', MovieList.as_view(), name='movies_list'),
           path('<int:pk>/', MoviesDetails.as_view(), name='movies_detail'),

           path('users/',views.UserList.as_view()),
           path('users/<int:pk>/',views.UserDetails.as_view()),
]