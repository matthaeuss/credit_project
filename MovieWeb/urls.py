from django.urls import path
from MovieWeb.views import all_movies, new_movie, delete_movie, comment_movie, edit_profile, add_poster, show_posters, \
    edit_movie, add_movie_to_favorites, show_favorites, delete_movie_from_favorites, \
    accept_movie_by_admin, accept_movie_object

urlpatterns = [
    path('all/', all_movies, name="all_movies"),
    path('new/', new_movie, name="new_movie"),
    path('delete/<int:id>/', delete_movie, name="delete_movie"),
    path('comment/<int:movie_id>/', comment_movie, name="comment_movie"),
    path('profile/', edit_profile, name="edit_profile"),
    path('add_poster/<int:movie_id>/', add_poster, name="add_poster"),
    path('show_posters/<int:movie_id>/', show_posters, name="show_posters"),
    path('edit_movie/<int:movie_id>/', edit_movie, name="edit_movie"),
    path('add_movie_to_favorites/<int:movie_id>/', add_movie_to_favorites, name="add_movie_to_favorites"),
    path('show_favorites/', show_favorites, name="show_favorites"),
    path('accept_movie_by_admin/', accept_movie_by_admin, name="accept_movie_by_admin"),
    path('delete_movie_from_favorites/<int:movie_favorite_id>/', delete_movie_from_favorites,
         name="delete_movie_from_favorites"),
    path('accept_movie_object/<int:movie_id>/', accept_movie_object, name="accept_movie_object"),
]
