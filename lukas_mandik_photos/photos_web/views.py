from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
from .models import Photo
# Create your views here.


def hello_world(request):
    return HttpResponse("Hello world!")


def home(request):
    return render(request, 'home.html')


def gallery(request):
    photos = Photo.objects.all()
    context = {'photos': photos}
    return render(request, 'gallery.html', context)
