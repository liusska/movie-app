from django import forms
from movie_app.movies.models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = ('user', )


class CreateMovieForm(MovieForm):
    pass


class EditMovieForm(MovieForm):
    pass
