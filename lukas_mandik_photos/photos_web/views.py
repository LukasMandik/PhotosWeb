from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
from .models import Photo, MetaPhoto
from PIL import Image
from PIL.ExifTags import TAGS
from django.shortcuts import render

from PIL import Image
# Create your views here.


def hello_world(request):
    return HttpResponse("Hello world!")


def home(request):
    photos = Photo.objects.all()
    context = {'photos': photos}
    return render(request, 'home.html', context)


def gallery(request):
    photos = Photo.objects.all()
    context = {'photos': photos}
    return render(request, 'gallery.html', context)
