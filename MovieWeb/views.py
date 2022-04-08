from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Poster, MovieFavorites
from .forms import FilmForm, CommentForm, ProfileForm, PosterForm, MovieFavoritesForm
from django.contrib.auth.decorators import login_required


def all_movies(request):
    all_movies = Movie.objects.filter(is_accepted=True)
    favorites_ids = MovieFavorites.objects.filter(user=request.user).values_list("movie__id", flat=True)
    ctx = {
        'films': all_movies,
        "favorites_ids": favorites_ids
           }
    return render(request, 'films.html', ctx)


@login_required()
def new_movie(request):
    form_film = FilmForm(request.POST or None, request.FILES or None)

    if form_film.is_valid():
        form_film.save()
        return redirect(all_movies)

    ctx = {'form': form_film}

    return render(request, 'film_form.html', ctx)


@login_required()
def edit_movie(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    film_form = FilmForm(instance=movie)

    if request.method == "POST":
        film_form = FilmForm(request.POST, request.FILES, instance=movie)
        if film_form.is_valid():
            film_form.save()
            return redirect(all_movies)

    ctx = {
        "movie": movie,
        "form": film_form,
        "on_edition": True
    }
    return render(request, 'film_form.html', ctx)


@login_required()
def comment_movie(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    comment_form = CommentForm(request.POST or None)

    if request.method == "POST":
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect(all_movies)

    ctx = {
        "title": movie.title,
        "form": comment_form

    }
    return render(request, 'comment_movie.html', ctx)


@login_required()
def edit_profile(request):
    user = request.user
    profile_form = ProfileForm(request.POST or None, request.FILES, instance=user.profile)

    if request.method == "POST":
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect(all_movies)

    ctx = {
        "user": user,
        "form": profile_form
    }
    return render(request, 'edit_profile.html', ctx)


@login_required()
def add_poster(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    poster_form = PosterForm(request.POST or None, request.FILES)

    if request.method == "POST":
        if poster_form.is_valid():
            poster = poster_form.save(commit=False)
            poster.movie = movie
            poster.save()
            return redirect(all_movies)

    ctx = {
        "movie": movie,
        "form": poster_form
    }

    return render(request, 'add_poster.html', ctx)


@login_required()
def show_posters(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    movie_posters = Poster.objects.filter(movie=movie)
    return render(request, 'movie_posters.html', {'posters': movie_posters})


@login_required()
def delete_movie(request, id):
    film = get_object_or_404(Movie, pk=id)

    if request.method == "POST":
        film.delete()
        return redirect(all_movies)

    return render(request, 'confirm.html', {'film': film})


@login_required()
def add_movie_to_favorites(request, movie_id):
    user = request.user
    movie = Movie.objects.get(id=movie_id)
    rating_form = MovieFavoritesForm(request.POST or None)

    if request.method == "POST":
        if rating_form.is_valid():
            favorite = rating_form.save(commit=False)
            favorite.user = user
            favorite.movie = movie
            favorite.save()
            return redirect(all_movies)

    ctx = {
        "movie": movie,
        "form": rating_form
    }

    return render(request, 'add_to_favorites.html', ctx)


@login_required()
def show_favorites(request):
    my_favorites = MovieFavorites.objects.filter(user=request.user)

    ctx = {
        'favorites': my_favorites
           }
    return render(request, 'my_favorites.html', ctx)


@login_required()
def delete_movie_from_favorites(request, movie_favorite_id):
    favorite = MovieFavorites.objects.get(id=movie_favorite_id)

    if request.method == "POST":
        favorite.delete()
        return redirect(all_movies)

    return render(request, 'favorite_delete.html', {'favorite': favorite})


@login_required()
def accept_movie_by_admin(request):
    not_accepted_movies = Movie.objects.filter(is_accepted=False)
    if request.method == "POST":
        if "accept_all" in request.POST:
            not_accepted_movies.update(is_accepted=True)

    ctx = {
        'not_accepted_movies': not_accepted_movies
           }
    return render(request, 'accept_movie_by_admin.html', ctx)


@login_required()
def accept_movie_object(request, movie_id):
    movie = Movie.objects.get(id=movie_id)

    if request.method == "POST":
        movie.is_accepted = True
        movie.save()
        return redirect(accept_movie_by_admin)

    return render(request, 'accept_movie_object.html', {'movie': movie})