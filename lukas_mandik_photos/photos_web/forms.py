from django import forms
from .models import Photo


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserCreationWithEmailForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="")
    first_name = forms.CharField(required=True, max_length=30, label='First Name')
    last_name = forms.CharField(required=True, max_length=30, label='Last Name')

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")



class LikePhotoForm(forms.Form):
    photo_id = forms.ModelChoiceField(queryset=Photo.objects.all(), widget=forms.HiddenInput())


from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.TextInput(attrs={'autofocus': True}),
        max_length=254,
        required=True,
    )