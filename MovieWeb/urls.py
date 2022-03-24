from django.urls import path
from MovieWeb.views import all_movies, new_movie, edit_movie, delete_movie

urlpatterns = [
    path('all/', all_movies, name="all_movies"),
    path('new/', new_movie, name="new_movie"),
    path('edit/<int:id>/', edit_movie, name="edit_movie"),
    path('delete/<int:id>/', delete_movie, name="delete_movie"),
]
