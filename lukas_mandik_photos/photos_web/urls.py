from django.urls import path

from . import views

urlpatterns = [
    path('hello_world', views.hello_world, name='hello_world'),
    path('', views.home, name='home'),
    path('gallery', views.gallery, name='gallery'),
    path('photo/<str:pk>/', views.view_photo, name='photo'),
]