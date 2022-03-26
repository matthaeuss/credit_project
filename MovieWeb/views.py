from django.shortcuts import render, get_object_or_404, redirect
from .models import Film, AdditionalInfo
from .forms import FilmForm, AdditionalInfoForm
from django.contrib.auth.decorators import login_required


def all_movies(request):
    all = Film.objects.all()
    return render(request, 'films.html', {'films': all})


@login_required()
def new_movie(request):
    form_film = FilmForm(request.POST or None, request.FILES or None)
    form_additional = AdditionalInfoForm(request.POST or None)

    if all((form_film.is_valid(), form_additional.is_valid())):
        film = form_film.save(commit=False)
        additional = form_additional.save()
        film.additional = additional
        film.save()
        return redirect(all_movies)

    return render(request, 'film_form.html', {'form': form_film, 'form_additional': form_additional, 'nowy': True})


@login_required()
def edit_movie(request, id):
    film = get_object_or_404(Film, pk=id)

    try:
        additional = AdditionalInfo.objects.get(film=film.id)
    except AdditionalInfo.DoesNotExist:
        additional = None

    form_film = FilmForm(request.POST or None, request.FILES or None,
                    instance=film)
    form_additional = AdditionalInfoForm(request.POST or None,
                    instance=additional)

    if all((form_film.is_valid(), form_additional.is_valid())):
        film = form_film.save(commit=False)
        additional = form_additional.save()
        film.additional = additional
        film.save()
        return redirect(all_movies)

    return render(request, 'film_form.html', {'form': form_film,
    'form_additional': form_additional, 'nowy': False})


@login_required()
def delete_movie(request, id):
    film = get_object_or_404(Film, pk=id)

    if request.method == "POST":
        film.delete()
        return redirect(all_movies)

    return render(request, 'confirm.html', {'film': film})
