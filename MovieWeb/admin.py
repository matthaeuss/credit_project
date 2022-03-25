from django.contrib import admin
from .models import Film, AdditionalInfo, Rating


# admin.site.register(Film)


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ["title", "imdb_rating", "year"]
    list_filter = ("year", "imdb_rating")
    search_fields = ("title", "description")


admin.site.register(AdditionalInfo);
admin.site.register(Rating)
