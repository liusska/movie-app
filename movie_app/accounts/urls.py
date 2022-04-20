from django.urls import path
from movie_app.accounts.views import UserRegisterView, UserLoginView, logout_user, profile_details

urlpatterns = [
    path('profile/', profile_details, name='profile'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]