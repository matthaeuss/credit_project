from django.forms import ModelForm
from .models import Movie, Comment


class FilmForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'year', 'country', 'imdb_rating', 'image', 'category']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["movie", "content"]