from django.urls import path, include
from . import views

app_name = 'cvcam'

urlpatterns = [
    path('feed/', views.feed, name='feed'),
    path('', views.index, name='index'),
    path('photo/', views.photo, name='photo')
]