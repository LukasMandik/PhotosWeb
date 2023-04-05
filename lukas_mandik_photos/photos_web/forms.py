from django import forms
from .models import Photo


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserCreationWithEmailForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. Enter a valid email address.")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")




class LikePhotoForm(forms.Form):
    photo_id = forms.ModelChoiceField(queryset=Photo.objects.all(), widget=forms.HiddenInput())
