
from django.http import HttpResponse

from django.shortcuts import render


# Create your views here.

from .models import Photo, Category


def hello_world(request):
    return HttpResponse("Hello world!")


import random
from random import sample

def home(request):
    photos = Photo.objects.all()
    if photos:

        random_ids = random.sample([p.id for p in photos], min(len(photos), 3))
        photos = Photo.objects.filter(id__in=random_ids)
    context = {'photos': photos}
    return render(request, 'home.html', context)


def gallery(request):
    category_name = request.GET.get('category', '')
    categories = Category.objects.all()

    if category_name:
        photos = Photo.objects.filter(category__name=category_name).order_by('-id')
    else:
        photos = Photo.objects.all().order_by('-id')

    context = {
        'categories': categories,
        'photos': photos,
        'selected_category': category_name,
    }
    return render(request, 'photos/gallery.html', context)


def view_photo(request, pk):
    photo = Photo.objects.get(id=pk)
    context = {'photo': photo}
    return render(request, 'photos/photo.html', context)




