import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

# Create your views here.
def index(request):
    # url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&APPID=da8bd5a8c02e54d118244384e69a5f07'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=da8bd5a8c02e54d118244384e69a5f07'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:
        r = requests.get(url.format(city)).json()
        city_weather = {
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }
        weather_data.append(city_weather)

    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'template.html', context)