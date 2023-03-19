
from django.http import HttpResponse

from django.shortcuts import render


# Create your views here.

from .models import Photo



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



