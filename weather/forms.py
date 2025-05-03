from django import forms
from .models import WeatherSearch, FavoriteLocation

class WeatherSearchForm(forms.ModelForm):
    city = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter city name',
            'aria-label': 'City',
        })
    )

    class Meta:
        model = WeatherSearch
        fields = ['city']

class FavoriteLocationForm(forms.ModelForm):
    class Meta:
        model = FavoriteLocation
        fields = ['city', 'country']
        widgets = {
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter city name',
            }),
            'country': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter country (optional)',
            }),
        }