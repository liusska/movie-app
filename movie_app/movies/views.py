from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Movie
from .forms import CreateMovieForm


class MovieGalleryView(ListView):
    model = Movie
    template_name = 'movies/movies_galley.html'
    context_object_name = 'movies'
    paginate_by = 5

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', '-publication_date')
        return ordering


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
