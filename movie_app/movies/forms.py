from django import forms
from movie_app.movies.models import Movie, Rating


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = ('user', )


class CreateMovieForm(MovieForm):
    pass


class EditMovieForm(MovieForm):
    pass


class RateMovieForm(forms.ModelForm):
    movie_pk = forms.IntegerField(
        widget=forms.HiddenInput()
    )

    class Meta:
        model = Rating
        fields = ('rate', 'movie_pk')

    def save(self, commit=True):
        movie_pk = self.cleaned_data['movie_pk']
        movie = Movie.objects.get(pk=movie_pk)
        rating = Rating(
            rate=self.cleaned_data['rate'],
            movie=movie,
        )
        if commit:
            rating.save()

        return rating