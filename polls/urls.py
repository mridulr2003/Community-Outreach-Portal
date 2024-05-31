from django.urls import path

from . import views
app_name= 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('results/', views.ResultsView.as_view(), name='results'),
    path('myerror/', views.myerror, name='myerror'),
    path('tweet/', views.index, name='index'),
]
