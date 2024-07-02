from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('zakazy/god/', views.year, name='year'),
    path('zakazy/mesyac/', views.month, name='month'),
    path('zakazy/nedelya/', views.day, name='day'),
]