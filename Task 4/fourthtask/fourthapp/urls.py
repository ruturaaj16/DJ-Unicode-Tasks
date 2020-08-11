from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('result/', views.result, name='result'),
    path('top3/', views.top3, name="top3"),
]