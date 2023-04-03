from django.contrib.auth.views import LoginView
from django.urls import path

from . import views

app_name = 'photos_web'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('hello_world', views.hello_world, name='hello_world'),
    path('', views.home, name='home'),

    path('gallery', views.gallery, name='gallery'),
    path('like_photo/', views.like_photo, name='like_photo'),

    path('store/products_gallery/', views.all_products, name='all_products'),
    path('item/<slug:slug>/', views.product_detail, name='product_detail'),
    path('search/<slug:category_slug>/', views.category_list, name='category_list'),
    path('photo/<slug:photo_slug>/', views.view_photo, name='view_photo'),
]

