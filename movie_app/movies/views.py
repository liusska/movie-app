from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Movie
from .forms import CreateMovieForm, EditMovieForm


class MovieGalleryView(ListView):
    model = Movie
    template_name = 'movies/movies_galley.html'
    context_object_name = 'movies'

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', '-publication_date')
        return ordering


def details_movie(request, pk):
    movie = Movie.objects.get(pk=pk)
    trailer_id = movie.trailer.split('/')[-1].split('=')[-1]
    is_owner = movie.user == request.user
    context = {
        'movie': movie,
        'trailer_id': trailer_id,
        'is_owner': is_owner,
    }
    return render(request, 'movies/details_movie.html', context)


def create_movie(request):
    if request.method == 'POST':
        form = CreateMovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('movies gallery')

    form = CreateMovieForm()
    context = {
        'form': form
    }

    return render(request, 'movies/create_movie.html', context)


def edit_movie(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditMovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('details movie', movie.pk)

    form = EditMovieForm(instance=movie)
    context = {
        'form': form,
        'movie': movie,
    }

    return render(request, 'movies/edit_movie.html', context)


def delete_movie(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movies gallery')

    context = {
        'movie': movie,
    }
    return render(request, 'movies/delete_movie.html', context)