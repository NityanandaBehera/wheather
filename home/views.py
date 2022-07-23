import dataclasses
from django.shortcuts import render
import requests


def wheather(request):
    city = request.GET.get('city', "Balasore")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=9357db6e5fb0d06b8234731ec7c6c350"
    data = requests.get(url).json()
    payload = {'city': data['name'],
               'weather': data['weather'][0]['main'],
               'icon': data['weather'][0]['icon'],
               'kelvin_temprature': data['main']['temp'],
               'celcius_temprature': int(data['main']['temp']-273),
               'pressure': data['main']['pressure'],
               'humidity': data['main']['humidity'],
               'description': data['weather'][0]['main'],
               }
    context = {
        'data': payload,
    }
    return render(request, 'home.html', context)
# Create your views here.
