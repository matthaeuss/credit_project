from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50, blank=False, unique=True, null=False)
    description = models.TextField()

    def __str__(self):
        return f"Category {self.name}"


class Movie(models.Model):
    title = models.CharField(max_length=64, blank=False, unique=True)
    description = models.TextField()
    year = models.IntegerField(default=2000)
    country = models.CharField(max_length=100, blank=True, null=True)
    imdb_rating = models.DecimalField(max_digits=4, decimal_places=2,
                                      null=True, blank=True)
    is_accepted = models.BooleanField(default=False)
    image = models.ImageField(upload_to="posters", null=True, blank=True)
    category = models.ManyToManyField(to=Category, related_name="movies")

    def __str__(self):
        return self.title_with_year()

    def title_with_year(self):
        return f"{self.title} ({self.year})"


class Comment(models.Model):
    user = models.ForeignKey(to=User, related_name="comments", on_delete=models.CASCADE)
    movie = models.ForeignKey(to=Movie, related_name="comment", on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment added by {self.user} to movie {self.movie}"


class Poster(models.Model):
    title = models.CharField(max_length=30, blank=False, unique=True, null=False)
    description = models.TextField()
    year = models.IntegerField()
    image = models.ImageField(upload_to="posters", null=True, blank=True)
    movie = models.ForeignKey(to=Movie, related_name="poster", on_delete=models.CASCADE)


class Profile(models.Model):
    avatar = models.ImageField(upload_to="avatars", null=True, blank=True)
    age = models.IntegerField()
    user = models.OneToOneField(to=User, related_name="profile", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}'s profile"


class MovieFavorites(models.Model):
    RATINGS = [
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]

    movie = models.ForeignKey(to=Movie, related_name="favorites", on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, related_name="favorites", on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATINGS, max_length=1, default=3)

    unique_together = ("user", "movie")
