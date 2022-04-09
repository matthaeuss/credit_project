from django.contrib.auth.models import User
from django.forms import ModelForm, forms
from .models import Movie, Comment, Profile, Poster, MovieFavorites
from django.contrib.auth.forms import UserCreationForm
from django import forms


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


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    # def save(self, commit=True):
    #     user = super(MyLoginForm, self).save(commit=False)
    #     user.email = self.cleaned_data['email']
    #     user.username = self.cleaned_data['email']

        # if commit:
        #     user.save()
        #
        # return user
