from django.forms import ModelForm, forms
from .models import Movie, Comment, Profile, Poster, MovieFavorites


class FilmForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'year', 'country', 'imdb_rating', 'image', 'category']

    image = forms.FileField(required=False)


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["movie", "content"]

        
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["avatar", "age"]


class PosterForm(ModelForm):
    class Meta:
        model = Poster
        fields = ["description", "title", "year", "image"]


class MovieFavoritesForm(ModelForm):
    class Meta:
        model = MovieFavorites
        fields = ["rating"]