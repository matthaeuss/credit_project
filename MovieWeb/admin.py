from django.contrib import admin
from .models import Movie, Category, Profile, Poster, Comment, MovieFavorites


# admin.site.register(Film)


@admin.register(Movie)
class FilmAdmin(admin.ModelAdmin):
    list_display = ["title", "imdb_rating", "year"]
    list_filter = ("year", "imdb_rating")
    search_fields = ("title", "description")


admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Poster)
admin.site.register(Comment)
admin.site.register(MovieFavorites)
