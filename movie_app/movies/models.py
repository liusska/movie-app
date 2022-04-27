from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator

UserModel = get_user_model()


class Movie(models.Model):
    MOVIE_TITLE_MIN_LENGTH = 2
    MOVIE_TITLE_MAX_LENGTH = 50

    ACTORS_MIN_LENGTH = 5
    ACTORS_MAX_LENGTH = 1000

    CATEGORY_CHOICE_BIOGRAPHY = 'Biography'
    CATEGORY_CHOICE_DOCUMENTARY = 'Documentary'
    CATEGORY_CHOICE_FANTASY = 'Fantasy'
    CATEGORY_CHOICE_COMEDY = 'Comedy'
    CATEGORY_CHOICE_MUSICAL = 'Musical'
    CATEGORY_CHOICE_THRILLER = 'Thriller'
    CATEGORY_CHOICE_MYSTERY = 'Mystery'
    CATEGORY_CHOICE_ROMANCE = 'Romance'
    CATEGORY_CHOICE_DRAMA = 'Drama'
    CATEGORY_CHOICE_CRIME = 'Crime'
    CATEGORY_CHOICE_HORROR = 'Horror'
    CATEGORY_CHOICE_FAMILY = 'Family'
    CATEGORY_CHOICE_ANIMATION = 'Animation'

    CATEGORIES = [(x, x) for x in (
        CATEGORY_CHOICE_BIOGRAPHY,
        CATEGORY_CHOICE_DOCUMENTARY,
        CATEGORY_CHOICE_FANTASY,
        CATEGORY_CHOICE_MUSICAL,
        CATEGORY_CHOICE_COMEDY,
        CATEGORY_CHOICE_THRILLER,
        CATEGORY_CHOICE_MYSTERY,
        CATEGORY_CHOICE_ROMANCE,
        CATEGORY_CHOICE_DRAMA,
        CATEGORY_CHOICE_CRIME,
        CATEGORY_CHOICE_HORROR,
        CATEGORY_CHOICE_FAMILY,
        CATEGORY_CHOICE_ANIMATION,
    )]

    category = models.CharField(
        max_length=20,
        choices=CATEGORIES,
        null=False,
        blank=False,
    )

    movie_title = models.CharField(
        max_length=MOVIE_TITLE_MAX_LENGTH,
        validators=(
            MinLengthValidator(MOVIE_TITLE_MIN_LENGTH),
        ),
        blank=False,
        null=False,
    )

    actors = models.CharField(
        max_length=ACTORS_MAX_LENGTH,
        validators=(
            MinLengthValidator(MOVIE_TITLE_MIN_LENGTH),
        ),
        blank=False,
        null=False,
    )

    year = models.PositiveIntegerField(
        null=False,
        blank=False
    )

    image = models.URLField(
        blank=False,
        null=False,
    )

    trailer = models.URLField(
        null=False,
        blank=False,
    )

    publication_date = models.DateTimeField(
        auto_now_add=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    @property
    def get_average_rating(self):
        if self.rating_set.count() == 0:
            rating_count = 1
        else:
            rating_count = self.rating_set.count()
        return sum(e.rate for e in self.rating_set.all()) / rating_count

    def __str__(self):
        return f'{self.movie_title} ({self.year})'


class Rating(models.Model):
    RATE_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    rate = models.PositiveIntegerField(
        default=0,
        choices=RATE_CHOICES,
    )

    def __str__(self):
        return f'{self.movie} - {self.user} Rate: {self.rate}'