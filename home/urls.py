from django.urls import path
from .views import*

urlpatterns = [
    path('', wheather, name='wheather'),
]
