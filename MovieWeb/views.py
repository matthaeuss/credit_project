from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Category
from .forms import FilmForm, CommentForm
from django.contrib.auth.decorators import login_required


def all_movies(request):
    all = Movie.objects.all()
    return render(request, 'films.html', {'films': all})


@login_required()
def new_movie(request):
    form_film = FilmForm(request.POST or None, request.FILES or None)

    if form_film.is_valid():
        form_film.save()
        return redirect(all_movies)

    ctx = {'form': form_film}

    return render(request, 'film_form.html', ctx)


@login_required()
def comment_movie(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    user = request.user
    comment_form = CommentForm(request.POST or None)

    if request.method == "POST":
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = user
            comment.save()
            return redirect(all_movies)

    ctx = {
        "title": movie.title,
        "form": comment_form

    }
    return render(request, 'comment_movie.html', ctx)

# @login_required()
# def edit_movie(request, id):
#     film = get_object_or_404(Movie, pk=id)
#     oceny = Rating.objects.filter(film=film)
#
#     try:
#         additional = Category.objects.get(film=film.id)
#     except Category.DoesNotExist:
#         additional = None
#
#     form_film = FilmForm(request.POST or None, request.FILES or None,
#                     instance=film)
#     form_additional = AdditionalInfoForm(request.POST or None,
#                                          instance=additional)
#     form_rating = RatingForm(request.POST or None)

# if request.method == 'POST':
#     if 'stars' in request.POST:
#         ocena = form_rating.save(commit=False)
#         ocena.film = film
#         ocena.save()
#
# if all((form_film.is_valid(), form_additional.is_valid())):
#     film = form_film.save(commit=False)
#     additional = form_additional.save()
#     film.additional = additional
#     film.save()
#     return redirect(all_movies)
#
# return render(request, 'film_form.html', {'form': form_film,
# 'form_additional': form_additional, 'rating': oceny, 'form_rating': form_rating, 'nowy': False})


@login_required()
def delete_movie(request, id):
    film = get_object_or_404(Movie, pk=id)

    if request.method == "POST":
        film.delete()
        return redirect(all_movies)

    return render(request, 'confirm.html', {'film': film})
