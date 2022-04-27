from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .models import Movie
from .forms import CreateMovieForm, EditMovieForm, RateMovieForm


class MovieGalleryView(ListView):
    model = Movie
    template_name = 'movies/movies_galley.html'
    context_object_name = 'movies'

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', '-publication_date')
        return ordering

@login_required
def details_movie(request, pk):
    """
    This FBV sent to the template all information about selected movie and his creator.
    """

    # get the movie by given pk
    movie = Movie.objects.get(pk=pk)

    # get the characters after '=' sign from trailer url
    trailer_id = movie.trailer.split('/')[-1].split('=')[-1]

    is_owner = movie.user == request.user

    # check if current user already rated the current movie
    is_rated_by_user = movie.rating_set.filter(user_id=request.user.id).exists()

    context = {
        'movie': movie,
        'trailer_id': trailer_id,
        'is_owner': is_owner,
        'is_rated_by_user': is_rated_by_user,
        'form': RateMovieForm(
            initial={
                'movie_pk': pk,
            }
        ),
        'avg_rating': f'{movie.get_average_rating:.1f} / 5.0',
        'rating_count': movie.rating_set.count(),
    }
    return render(request, 'movies/details_movie.html', context)


@login_required
def rate_movie(request, pk):
    """
    This FBV add user to the current rating
    """
    form = RateMovieForm(request.POST)

    if form.is_valid():
        rating = form.save(commit=False)
        rating.user = request.user
        rating.save()

    return redirect('details movie', pk)


@login_required
def create_movie(request):
    """
    This FBV create new movie.
    """
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


@login_required
def edit_movie(request, pk):
    """
    This FBV edit the current movie, only if the current user is owner of the movie.
    """
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


@login_required
def delete_movie(request, pk):
    """
    This FBV delete the current movie, only if the current user is owner of the movie.
    """
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movies gallery')

    context = {
        'movie': movie,
    }
    return render(request, 'movies/delete_movie.html', context)


def search_movie(request):
    """
    Get the value from the searched fields, if the method is POST and return the results or message.
    The searched fields are :
        - movie title
        - movie category
        - movie actors
    If the method is GET just show list ot all movies.
    """
    movies = Movie.objects.all()

    if request.method == 'POST':
        title_value = request.POST['title']
        category_value = request.POST['category']
        actors_value = request.POST['actors']

        movies_with_searched_title = Movie.objects.filter(movie_title__icontains=title_value)
        movies_with_searched_category = Movie.objects.filter(category__icontains=category_value)
        movies_with_searched_actors = Movie.objects.filter(actors__icontains=actors_value)

        movies = list(movies_with_searched_title & movies_with_searched_category & movies_with_searched_actors)

    context = {
        'movies': movies,
    }
    return render(request, 'movies/search.html', context)





