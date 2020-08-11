from django.urls import path  
from . import views
urlpatterns = [
    path('<int:a>/<int:c>/', views.index, name='index'),
]