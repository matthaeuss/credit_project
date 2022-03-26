from django.forms import ModelForm
from .models import Film, AdditionalInfo, Rating


class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'description', 'premiere', 'year', 'imdb_rating', 'poster']


class AdditionalInfoForm(ModelForm):
    class Meta:
        model = AdditionalInfo
        fields = ['duration', 'genre']


class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = ['stars', 'review']