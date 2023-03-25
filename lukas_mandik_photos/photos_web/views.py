#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Photo, Category, Product
from django.db.models import Q

def hello_world(request):
    return HttpResponse("Hello world!")


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



