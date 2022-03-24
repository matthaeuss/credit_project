from django.shortcuts import render, get_object_or_404, redirect
from .models import Film
from .forms import FilmForm


def all_movies(request):
    all = Film.objects.all()
    return render(request, 'films.html', {'films': all})


def new_movie(request):
    form = FilmForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(all_movies)

    return render(request, 'film_form.html', {'form': form})


def edit_movie(request, id):
    film = get_object_or_404(Film, pk=id)
    form = FilmForm(request.POST or None, request.FILES or None,
                    instance=film)

    if form.is_valid():
        form.save()
        return redirect(all_movies)

    return render(request, 'film_form.html', {'form': form})


def delete_movie(request, id):
    film = get_object_or_404(Film, pk=id)

    if request.method == "POST":
        film.delete()
        return redirect(all_movies)

    return render(request, 'confirm.html', {'film': film})
