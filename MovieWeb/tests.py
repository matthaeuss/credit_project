
from django.test import TestCase

from MovieWeb.models import Movie


class CreateMovieAsNotAcceptedTestCase(TestCase):

    def new_movie_object_is_not_accepted(self):
        movie = Movie.objects.create(title="Avatar")
        movie.save()
        self.assertEqual(movie.is_accepted, False)