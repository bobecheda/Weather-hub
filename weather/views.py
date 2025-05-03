from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import WeatherSearch, FavoriteLocation
from .forms import WeatherSearchForm, FavoriteLocationForm
from .api import WeatherAPI, WeatherAPIError

def index(request):
    form = WeatherSearchForm()
    context = {'form': form}
    
    if request.method == 'POST':
        form = WeatherSearchForm(request.POST)
        if form.is_valid():
            try:
                weather_api = WeatherAPI()
                weather_data = weather_api.get_weather_by_city(form.cleaned_data['city'])
                
                if request.user.is_authenticated:
                    # Save the search for logged-in users
                    weather_search = form.save(commit=False)
                    weather_search.user = request.user
                    weather_search.country = weather_data['country']
                    weather_search.temperature = weather_data['temperature']
                    weather_search.humidity = weather_data['humidity']
                    weather_search.wind_speed = weather_data['wind_speed']
                    weather_search.description = weather_data['description']
                    weather_search.icon = weather_data['icon']
                    weather_search.save()
                
                context.update({
                    'weather_data': weather_data,
                    'form': form
                })
            except WeatherAPIError as e:
                messages.error(request, str(e))
    
    return render(request, 'weather/index.html', context)

@login_required
def favorite_locations(request):
    locations = FavoriteLocation.objects.filter(user=request.user)
    form = FavoriteLocationForm()
    
    if request.method == 'POST':
        form = FavoriteLocationForm(request.POST)
        if form.is_valid():
            location = form.save(commit=False)
            location.user = request.user
            location.save()
            messages.success(request, 'Location added to favorites!')
            return redirect('favorite_locations')
    
    context = {
        'locations': locations,
        'form': form
    }
    return render(request, 'weather/favorites.html', context)

@login_required
def delete_favorite(request, location_id):
    location = get_object_or_404(FavoriteLocation, id=location_id, user=request.user)
    location.delete()
    messages.success(request, 'Location removed from favorites!')
    return redirect('favorite_locations')

@login_required
def search_history(request):
    searches = WeatherSearch.objects.filter(user=request.user)
    return render(request, 'weather/history.html', {'searches': searches})