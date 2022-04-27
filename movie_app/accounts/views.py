from django.views.generic import CreateView
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from .forms import RegistrationForm
from movie_app.movies.models import Movie


def profile_details(request):
    """
    This FBV sent to the template the information about current user activity.
    """
    user = User.objects.get(username=request.user)
    movies = Movie.objects.filter(user_id=request.user.id)
    context = {
        'user': user,
        'movies': movies,
        'message': 'Nothing to show! Add you first movie',
    }
    return render(request, 'accounts/profile.html', context)


class UserRegisterView(CreateView):
    """
    This CBV creates new user, with automatic login after successful registration.
    """
    form_class = RegistrationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, *args, **kwargs):
        result = super().form_valid(*args, **kwargs)
        login(self.request, self.object)
        return result


class UserLoginView(LoginView):
    """
    Using built-in LoginView, this CBV responds for login user.
    """
    template_name = 'accounts/login.html'

    def get_success_url(self):
        return reverse_lazy('index')


def logout_user(request):
    logout(request)
    return redirect('index')
