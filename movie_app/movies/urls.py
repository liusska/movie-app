from django.urls import path
from .views import MovieGalleryView, create_movie

urlpatterns = [
    path('gallery/', MovieGalleryView.as_view(), name='movies gallery'),
    path('create/', create_movie, name='create movie'),
]