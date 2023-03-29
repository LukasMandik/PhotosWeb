from django import forms
from .models import Photo


class LikePhotoForm(forms.Form):
    photo_id = forms.ModelChoiceField(queryset=Photo.objects.all(), widget=forms.HiddenInput())
