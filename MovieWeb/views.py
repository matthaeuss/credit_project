from django.shortcuts import render, get_object_or_404, redirect
from .models import Film
from .forms import FilmForm
from django.contrib.auth.decorators import login_required


def all_movies(request):
    all = Film.objects.all()
    return render(request, 'films.html', {'films': all})


@login_required()
def new_movie(request):
    form = FilmForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(all_movies)

    return render(request, 'film_form.html', {'form': form})


@login_required()
def edit_movie(request, id):
    film = get_object_or_404(Film, pk=id)
    form = FilmForm(request.POST or None, request.FILES or None,
                    instance=film)

    if form.is_valid():
        form.save()
        return redirect(all_movies)

    return render(request, 'film_form.html', {'form': form})


@login_required()
def delete_movie(request, id):
    film = get_object_or_404(Film, pk=id)

    if request.method == "POST":
        film.delete()
        return redirect(all_movies)

    return render(request, 'confirm.html', {'film': film})
