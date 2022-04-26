from django.urls import path
from .views import MovieGalleryView, create_movie, details_movie, edit_movie, delete_movie, rate_movie, search_movie

urlpatterns = [
    path('gallery/', MovieGalleryView.as_view(), name='movies gallery'),
    path('create/', create_movie, name='create movie'),
    path('delete/<int:pk>', delete_movie, name='delete movie'),
    path('edit/<int:pk>', edit_movie, name='edit movie'),
    path('details/<int:pk>', details_movie, name='details movie'),
    path('rate/<int:pk>', rate_movie, name='rate movie'),
    path('search/', search_movie, name='search movie'),
]