from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class RegistrationForm(UserCreationForm):
    pass
    # class Meta:
    #     model = User
    #     fields = ('username', 'email', 'first_name', 'last_name')

