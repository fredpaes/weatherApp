import requests
from django.shortcuts import render

# Create your views here.
def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&APPID=da8bd5a8c02e54d118244384e69a5f07'
    city = 'Las Vegas'

    r = requests.get(url.format(city))
    print(r.text)
    return render(request, 'template.html')