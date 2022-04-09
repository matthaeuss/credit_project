from django.test import TestCase
from django.urls import resolve, reverse

from MovieWeb.models import Movie
from MovieWeb.views import all_movies, new_movie, delete_movie, comment_movie, edit_profile, add_poster, show_posters, \
    add_movie_to_favorites, edit_movie, show_favorites, accept_movie_by_admin, delete_movie_from_favorites, \
    accept_movie_object


class CreateMovieAsNotAcceptedTestCase(TestCase):

    def setUp(self):
        Movie.objects.create(title="Avatar")

    def test_new_movie_object_is_not_accepted(self):
        movie = Movie.objects.get(title="Avatar")
        self.assertEqual(movie.is_accepted, False)


class UrlTestCase(TestCase):

    def setUp(self):
        self.movie = Movie.objects.create(title="Avatar")

    def test_url_home_url(self):
        url = resolve(reverse('all_movies'))
        assert url.func == all_movies

    def test_new_movie_url(self):
        url = resolve(reverse('new_movie'))
        assert url.func == new_movie

    def test_delete_movie_url(self):
        url = resolve(reverse('delete_movie', args=[self.movie.id]))
        assert url.func == delete_movie

    def test_add_comment_url(self):
        url = resolve(reverse('comment_movie', args=[self.movie.id]))
        assert url.func == comment_movie

    def test_edit_profile_url(self):
        url = resolve(reverse('edit_profile'))
        assert url.func == edit_profile

    def test_show_posters_url(self):
        url = resolve(reverse('show_posters', args=[self.movie.id]))
        assert url.func == show_posters

    def test_add_movie_to_favorites_url(self):
        url = resolve(reverse('add_movie_to_favorites', args=[self.movie.id]))
        assert url.func == add_movie_to_favorites

    def test_add_poster_url(self):
        url = resolve(reverse('add_poster', args=[self.movie.id]))
        assert url.func == add_poster

    def test_show_favorites_url(self):
        url = resolve(reverse('show_favorites'))
        assert url.func == show_favorites

    def test_delete_movie_from_favorites_url(self):
        url = resolve(reverse('delete_movie_from_favorites', args=[self.movie.id]))
        assert url.func == delete_movie_from_favorites

    def test_accept_movie_object_url(self):
        url = resolve(reverse('accept_movie_object', args=[self.movie.id]))
        assert url.func == accept_movie_object

    def test_edit_movie_url(self):
        url = resolve(reverse('edit_movie', args=[self.movie.id]))
        assert url.func == edit_movie

    def test_url_accept_movie_by_admin_url(self):
        url = resolve(reverse('accept_movie_by_admin'))
        assert url.func == accept_movie_by_admin

