from django import forms
from movie_app.movies.models import Movie


class CreateMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = ('user', )
