from django import forms
from .models import Photo


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from allauth.account.forms import SignupForm


class MyCustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user



# class UserCreationWithEmailForm(UserCreationForm):
#     email = forms.EmailField(required=True, help_text="")
#     first_name = forms.CharField(required=True, max_length=30, label='First Name')
#     last_name = forms.CharField(required=True, max_length=30, label='Last Name')
#
#     class Meta:
#         model = User
#         fields = ("username", "first_name", "last_name", "email", "password1", "password2")



class LikePhotoForm(forms.Form):
    photo_id = forms.ModelChoiceField(queryset=Photo.objects.all(), widget=forms.HiddenInput())


