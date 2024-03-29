#!/usr/bin/.env python
# -*- coding: utf-8 -*-

import random
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Photo, Category, Product
from django.db.models import Q, Count
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.backends import ModelBackend



def user_logout(request):
    logout(request)
    return redirect('/')


def hello_world(request):
    return HttpResponse("Hello world!")


def home(request):
    photos = Photo.objects.filter(image_name="_DSC9014.JPG")
    top_likes_photos = Photo.objects.annotate(like_count=Count('likes')).order_by('-likes')[:3]

    # if photos:
    #     random_ids = random.sample([p.id for p in photos], min(len(photos), 3))
    #     photos = Photo.objects.filter(id__in=random_ids)

    home_photo = Photo.objects.filter(image_name="_DSC5009.jpg").first

    # Vyberie všetky produkty
    all_products = list(Product.objects.all())

    # Premieša zoznam produktov
    random.shuffle(all_products)

    # Vyberie prvých tri produkty z premiešaného zoznamu
    random_products = all_products[:3]

    context = {'photos': photos,
               'home_photo': home_photo,
               'top_likes_photos': top_likes_photos,
               'random_products': random_products,}
    return render(request, 'home.html', context)


# def gallery(request):
#     category_name = request.GET.get('category', '')
#     categories = Category.objects.all()
#
#     if category_name:
#         photos = Photo.objects.filter(category__name=category_name).order_by('-id')
#     else:
#         photos = Photo.objects.all().order_by('-id')
#
#     context = {
#         'categories': categories,
#         'photos': photos,
#         'selected_category': category_name,
#     }
#     return render(request, 'photos/gallery.html', context)


from .forms import LikePhotoForm

def gallery(request):
    category_name = request.GET.get('category', '')
    categories = Category.objects.all()

    if category_name:
        photos = Photo.objects.filter(category__name=category_name).order_by('-id')
    else:
        photos = Photo.objects.all().order_by('-id')

    # if request.method == 'POST':
    #     form = LikePhotoForm(request.POST)
    #     if form.is_valid() and request.user.is_authenticated:
    #         photo = form.cleaned_data.get('photo_id')
    #         if request.user in photo.user_likes.all():
    #             photo.user_likes.remove(request.user)
    #             photo.likes -= 1
    #         else:
    #             photo.user_likes.add(request.user)
    #             photo.likes += 1
    #         photo.save()
    #         return redirect('/gallery', category=category_name)

    # form = LikePhotoForm()
    context = {
        'categories': categories,
        'photos': photos,
        'selected_category': category_name,
        # 'like_photo_form': form,
    }
    return render(request, 'photos/gallery.html', context)



def index_store(request):
    # Vyberie všetky produkty
    all_products = list(Product.objects.all())

    # Premieša zoznam produktov
    random.shuffle(all_products)

    # Vyberie prvých tri produkty z premiešaného zoznamu
    random_products = all_products[:3]

    context = {
        'random_products': random_products,
    }

    return render(request, 'store/index.html', context)


def all_products(request):
    category_name = request.GET.get('category', '')
    categories = Category.objects.all()

    if category_name:
        products = Product.objects.filter(is_active=True, category__name=category_name).order_by('-id')
    else:
        products = Product.objects.filter(is_active=True).order_by('-id')

    context = {
        'categories': categories,
        'products': products,
        'selected_category': category_name,
    }
    return render(request, 'store/products_gallery.html', context)


def view_photo(request, photo_slug):
    photo = get_object_or_404(Photo, slug=photo_slug)
    previous_photo = Photo.objects.filter(id__lt=photo.id).order_by('-id').first()
    next_photo = Photo.objects.filter(id__gt=photo.id).order_by('id').first()

    if request.method == 'POST':
        photo.likes.add(request.user)
        photo.save()

    context = {
        'photo': photo,
        'previous_photo': previous_photo,
        'next_photo': next_photo,
    }
    return render(request, 'photos/photo.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/detail.html', {'product': product})


def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category, is_active=True)
    categories = Category.objects.all()
    context = {
        'category': category,
        'products': products,
        'categories': categories,
        'selected_category': category,
    }
    return render(request, 'store/products_gallery.html', context)



from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Photo


def like_photo(request):
    photo_id = request.POST.get('photo_id')
    photo = get_object_or_404(Photo, id=photo_id)

    # Check if user is authenticated
    if request.user.is_authenticated:
        if request.user in photo.user_likes.all():
            # Remove user from user_likes and decrement likes
            photo.user_likes.remove(request.user)
            photo.likes -= 1
            liked = False
        else:
            # Add user to user_likes and increment likes
            photo.user_likes.add(request.user)
            photo.likes += 1
            liked = True

        photo.save()

        return JsonResponse({'likes': photo.likes, 'liked': liked})

    # If user is not authenticated, use cookies
    else:
        liked_photos = request.COOKIES.get('liked_photos')
        if liked_photos:
            liked_photos = liked_photos.split(',')
        else:
            liked_photos = []

        if photo_id not in liked_photos:
            # Add photo_id to liked_photos
            liked_photos.append(photo_id)
            # Increment likes
            photo.likes += 1
            photo.save()

            # Set cookie
            response = JsonResponse({'likes': photo.likes, 'liked': True})
            response.set_cookie('liked_photos', ','.join(liked_photos))

        else:
            # Remove photo_id from liked_photos
            liked_photos.remove(photo_id)
            # Decrement likes
            photo.likes -= 1
            photo.save()

            # Set cookie
            response = JsonResponse({'likes': photo.likes, 'liked': False})
            response.set_cookie('liked_photos', ','.join(liked_photos), max_age=31536000)

        return response
