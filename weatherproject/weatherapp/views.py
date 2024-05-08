from django.shortcuts import render
import json
import requests
from weatherapp.forms import WeatherForm

# Create your views here.
def home(request):
    submitted = False
    if request.method == 'POST':
        form = WeatherForm(request.POST)
        if form.is_valid():
            submitted = True
            city_name =form.cleaned_data['city']
    else:
        city_name = 'hyderabad'
    api_key = "2606cc6938cad4cc3d018186976acb5b"
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
    data = requests.get(url).json()
    print(data)

        

    city = data['name']
    country = data['sys']['country']
    temperature = round(data['main']['temp']-273,2)
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']


    form = WeatherForm()

    return render(request,'weatherapp/index.html',{'form':form,'submitted':submitted,'city':city,'country':country,'temperature':temperature,'pressure':pressure,'humidity':humidity
})